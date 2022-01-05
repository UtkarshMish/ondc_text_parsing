import { ChakraProvider, theme } from '@chakra-ui/react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react';
import Error from './component/Error';
import Home from './component/Home';

function App() {
  return (
    <ChakraProvider theme={theme}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} exact />
          <Route path="/*" element={<Error />} exact />
        </Routes>
      </BrowserRouter>
    </ChakraProvider>
  );
}

export default App;
