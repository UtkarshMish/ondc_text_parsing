import { Box, Image, Input, Text } from "@chakra-ui/react";
import React from "react";
import ondc from "../assets/logo-ondc-bg.png";
import npciLogo from "../assets/npci-logo.png";
export default function SearchView() {
	return (
		<>
			<Box
				display={"flex"}
				padding={"1rem"}
				height={"fit-content"}
				justifyContent={"flex-start"}
				alignItems={"center"}
				position={"relative"}
				borderBottom={"1px solid #3c4043"}>
				<Image src={ondc} alt="ondc-logo" width={"auto"} height={"7rem"} />
				<Input
					type={"search"}
					name="search"
					width={"30rem"}
					background={"whiteAlpha.900"}
					borderRadius={"full"}
					marginInline={"5rem"}
					fontSize={"lg"}
					placeholder="search for products here ..."
					_placeholder={{ textColor: "gray" }}
				/>
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
		</>
	);
}
