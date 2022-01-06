import { Box } from "@chakra-ui/react";
import React from "react";
import Products from "./Products";
import SearchView from "./SearchView";

export default function Home() {
	return (
		<Box
			background={"#151619"}
			minHeight={"100vh"}
			overflowY={"auto"}
			paddingBottom={"10"}>
			<SearchView />
			<Products />
		</Box>
	);
}
