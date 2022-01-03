import { Box, ChakraProvider, Text, theme } from "@chakra-ui/react";
import React from "react";

function App() {
	return (
		<ChakraProvider theme={theme}>
			<Box textAlign="center" fontSize="xl">
				<Text>Boiler Plate</Text>
			</Box>
		</ChakraProvider>
	);
}

export default App;
