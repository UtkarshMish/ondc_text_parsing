import axios from "axios";
export async function getProducts(pageNo = 1) {
	try {
		const response = await axios.get("/api/products?page=" + pageNo);
		if (response.data) {
			return [response.data.products, response.data.total];
		}
	} catch (err) {
		console.log("error: ", err);
	}
	return [null, null];
}

export async function searchProduct(searchString = "") {
	try {
		const response = await axios.post("/api/search", { search: searchString });
		if (response.data?.message?.fulfillment) {
			const [{ product }, { total }] = response.data.message.fulfillment;
			return [product, total];
		}
	} catch (err) {
		console.log("error: ", err);
	}

	return null;
}
