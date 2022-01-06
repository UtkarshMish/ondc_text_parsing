import { Box, Button } from "@chakra-ui/react";
import React from "react";
import { Link } from "react-router-dom";

function generateNum(end = 0, start = 1) {
	if (end > 0 && end < 10_00_000) {
		const arr = [];
		for (let index = start; index < end; index++) {
			arr.push(index);
		}
		return arr;
	} else {
		throw new Error("value should be > 0");
	}
}
export default function PageBox({ total = 0, current = 0 }) {
	const fiveLess = current - 5;
	const isLess = fiveLess > 0;
	const fiveMore = current + 5;
	const isMore = fiveMore > total;
	const screenNumbers =
		total < 10
			? generateNum(total, 2)
			: [
					...new Set([
						1,
						...generateNum(isLess ? current + 1 : 6, isLess ? fiveLess + 1 : 2),
						...generateNum(isMore ? total : current + 5, isMore ? total : current + 1),

						total
					]).values()
			  ];
	return (
		<Box
			width={"100%"}
			textColor={"white"}
			display={"flex"}
			justifyContent={"center"}>
			{screenNumbers.map((value) => (
				<Button
					backgroundColor={current === value ? "darkblue" : "purple.600"}
					key={value}
					colorScheme={"purple"}
					as={Link}
					to={`/${value}`}
					marginInline={"1"}>
					{value}
				</Button>
			))}
		</Box>
	);
}
