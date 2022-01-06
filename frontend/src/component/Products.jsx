import { Badge, Box, Image, Spinner } from "@chakra-ui/react";
import React, { useEffect, useState } from "react";
import { getProducts } from "../utils/apiHelpers";
export default function Products() {
	const [products, setProducts] = useState(null);
	const [total, setTotal] = useState(null);
	const [isLoading, setIsLoading] = useState(true);
	useEffect(() => {
		async function fetchData() {
			const [data, size] = await getProducts();
			setProducts(data);
			setTotal(size);
			setIsLoading(false);
		}
		fetchData();
	}, []);

	if (isLoading) {
		return (
			<Box
				display={"flex"}
				alignItems={"center"}
				justifyContent={"center"}
				marginBlock={20}
				flexDirection={"column"}>
				<Spinner
					thickness="8px"
					speed="0.55s"
					emptyColor="gray.200"
					color="blue.500"
					size={"xl"}
					width={"6rem"}
					height={"6rem"}
				/>
			</Box>
		);
	}
	return (
		<Box
			margin={"2rem"}
			display={"flex"}
			justifyContent={"space-evenly"}
			height={"inherit"}
			flexWrap={"wrap"}>
			{products &&
				products.map((element) => (
					<Box
						maxWidth={"20rem"}
						borderWidth="1px"
						borderRadius="lg"
						overflow="hidden"
						boxShadow={
							"rgba(251, 251, 255, 0.75) 0px 2px 5px -1px,rgba(255, 253, 253, 0.3) 0px 1px 3px -1px"
						}
						minHeight={"27rem"}
						margin={2}>
						<Box display={"flex"} justifyContent={"center"}>
							<Image
								src={element.descriptor.images[0]}
								alt="card-logo"
								objectFit={"contain"}
								maxHeight={"30rem"}
							/>
						</Box>

						<Box
							paddingBlock="6"
							paddingInline={2}
							display={"flex"}
							flexDirection={"column"}>
							<Box
								display="flex"
								alignItems="baseline"
								justifyContent={"space-between"}>
								<Box maxWidth={"70%"}>
									<Badge
										borderRadius="full"
										px="2"
										colorScheme="teal"
										maxWidth={"100%"}
										isTruncated>
										{element.descriptor.name}
									</Badge>
									<Box
										marginBlock={2}
										color="messenger.100"
										fontWeight="bold"
										letterSpacing="wide"
										fontSize="xs"
										textTransform="uppercase"
										ml="2">
										{element.category}
									</Box>
								</Box>
								<Box
									fontSize={"sm"}
									fontWeight={"bold"}
									letterSpacing={"wide"}
									color={"messenger.100"}>
									{element.price.value + " " + element.price.currency}
								</Box>
							</Box>

							<Box
								alignSelf={"flex-end"}
								mt="1"
								fontWeight="semibold"
								as="h4"
								lineHeight="tight"
								color={"messenger.100"}>
								{element.descriptor.short_desc}
							</Box>
						</Box>
					</Box>
				))}
		</Box>
	);
}
