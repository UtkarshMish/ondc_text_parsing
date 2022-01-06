import { Box } from "@chakra-ui/react";
import React, { useState } from "react";
import Products from "./Products";
import SearchView from "./SearchView";

export default function Home() {
	const [products, setProducts] = useState(null);
	const [total, setTotal] = useState(null);
	return (
		<Box
			background={"#151619"}
			minHeight={"100vh"}
			overflowY={"auto"}
			paddingBottom={"10"}>
			<SearchView setProducts={setProducts} setTotal={setTotal} />
			<Products
				products={products}
				setProducts={setProducts}
				total={total}
				setTotal={setTotal}
			/>
		</Box>
	);
}
