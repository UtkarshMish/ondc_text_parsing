import { ChakraProvider, theme } from "@chakra-ui/react";
import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./component/Home";

function App() {
	return (
		<ChakraProvider theme={theme}>
			<BrowserRouter>
				<Routes>
					<Route path="/" element={<Home />} exact />
					<Route path="/:page" element={<Home />} exact />
				</Routes>
			</BrowserRouter>
		</ChakraProvider>
	);
}

export default App;
