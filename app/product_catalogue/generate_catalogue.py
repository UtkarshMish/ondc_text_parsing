import csv
from dataclasses import dataclass
from datetime import datetime
from os import listdir
from typing import Dict, List
from uuid import uuid4

from app.database import connect_db
from app.database.Category import Category
from app.database.Country import Country
from app.database.Item import Item
from app.database.meta import Price
from app.database.meta.Descriptor import Descriptor
from pycountry import countries
from pydantic import validate_arguments


@validate_arguments
@dataclass(repr=True, init=True, order=True, frozen=True)
class ProductData:
    category: str
    subcategory: str
    name: str
    current_price: float
    raw_price: float
    currency: str
    discount: float
    likes_count: int
    is_new: bool
    brand: str
    brand_url: str
    cod_country: str
    variation_0_color: str
    variation_1_color: str
    variation_0_thumbnail: str
    variation_0_image: str
    variation_1_thumbnail: str
    variation_1_image: str
    image_url: str
    url: str
    id: int
    model: str


async def generate_catalogue():
    await connect_db()
    if not (await Item.count() > 1):
        catalogue_path = (
            "C:/Users/abish/Desktop/Sandbox/ondc_text_parsing/app/product_catalogue"
        )
        product_files = [
            file for file in listdir(catalogue_path) if file.endswith(".csv")
        ]
        product_datas: List[ProductData] = list()

        country_dict: Dict[str, Country] = dict()
        category_dict: Dict[str, Category] = dict()
        items: List[Item] = list()
        for product in product_files:
            product_datas.extend(
                [
                    ProductData(*data)
                    for index, data in enumerate(
                        csv.reader(
                            open(
                                f"{catalogue_path}/{product}", "r", encoding="utf-8"
                            ).readlines()
                        )
                    )
                    if index != 0
                ]
            )

        generate_product_country(product_datas, category_dict, items, country_dict)

        await save_data_to_db(
            countries=list(country_dict.values()),
            items=items,
            categories=list(category_dict.values()),
        )


def generate_product_country(
    product_datas: List[ProductData],
    category_dict: Dict[str, Category],
    items: List[Item],
    country_dict: dict[str, Country],
):
    for product in product_datas:
        discounted_price = product.current_price * (product.discount / 100)
        price = Price(
            currency=product.currency,
            value=product.current_price,
            estimated_value=product.raw_price,
            minimum_value=discounted_price,
            listed_value=product.current_price,
            maximum_value=product.raw_price,
            offered_value=product.current_price - discounted_price,
            computed_value=product.current_price - discounted_price,
        )
        tags = [
            *product.category.split(" "),
            *product.subcategory.split(" "),
            *product.name.split(" "),
            *product.cod_country.split(","),
        ]
        if not product.category in category_dict:
            category_dict[product.category] = Category(
                id=str(uuid4()),
                time=datetime.now(),
                descriptor=Descriptor(name=product.category),
                tags=[
                    *product.category.split(" "),
                    *product.subcategory.split(" "),
                ],
            )
        items.append(
            Item(
                id=str(uuid4()),
                price=price,
                tags=tags,
                category_id=category_dict[product.category].id,
                descriptor=Descriptor(
                    name=product.name,
                    short_desc=product.model,
                    images=[
                        product.image_url,
                        product.variation_0_image,
                        product.variation_1_image,
                    ],
                ),
                time=datetime.now(),
            )
        )
        generate_countries(country_dict, product)


def generate_countries(country_dict: dict[str, Country], product: ProductData):
    for code in product.cod_country.split(","):
        try:
            code = code.strip()
            if not code in country_dict and len(code) > 1:
                country_dict[code] = Country(
                    name=str(countries.get(alpha_2=code).name), code=code
                )
        except AttributeError:
            print(code)


async def save_data_to_db(
    countries: List[Country], items: List[Item], categories: List[Category]
):
    await Country.insert_many(countries)
    await Item.insert_many(items)
    await Category.insert_many(categories)
