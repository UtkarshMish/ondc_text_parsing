import { Box, Image, Input, Text } from "@chakra-ui/react";
import React from "react";
import { useNavigate } from "react-router-dom";
import { useDebounce } from "rooks";
import ondc from "../assets/logo-ondc-bg.png";
import npciLogo from "../assets/npci-logo.png";
import { searchProduct } from "../utils/apiHelpers";
export default function SearchView({ setProducts, setTotal }) {
	const navigate = useNavigate();
	async function searchTerm(e) {
		const value = e.target.value;
		const result = await searchProduct(value);
		if (result && Array.isArray(result) && setProducts) {
			const [data, total] = result;
			setProducts(data);
			setTotal(total);
		}
	}
	const debouncedSearch = useDebounce(searchTerm, 300);
	return (
		<Box
			display={"flex"}
			padding={"1rem"}
			height={"fit-content"}
			justifyContent={"space-between"}
			alignItems={"center"}
			flexWrap={"wrap"}
			position={"relative"}
			borderBottom={"1px solid #3c4043"}>
			<Image
				src={ondc}
				alt="ondc-logo"
				width={"auto"}
				height={"7rem"}
				cursor={"pointer"}
				onClick={() => navigate("/")}
			/>
			<Input
				type={"search"}
				name="search"
				minWidth={"35%"}
				width={"30rem"}
				background={"whiteAlpha.900"}
				borderRadius={"full"}
				marginInline={"5rem"}
				fontSize={"lg"}
				onChange={debouncedSearch}
				placeholder="search for products here ..."
				_placeholder={{ textColor: "gray" }}
			/>
			<Box display={"flex"} margin={2}>
				<Text
					fontSize={"2xl"}
					fontWeight={"bold"}
					fontStyle={"italic"}
					color={"#21317d"}>
					Powered By
				</Text>
				<Image
					src={npciLogo}
					alt="ondc-logo"
					width={"10rem"}
					height={"auto"}
					marginLeft={-1.5}
				/>
			</Box>
		</Box>
	);
}
