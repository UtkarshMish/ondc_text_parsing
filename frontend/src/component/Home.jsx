import { Box } from '@chakra-ui/react';
import React from 'react';
import SearchView from './SearchView';

export default function Home() {
  return (
    <Box background={'#151619'} height={'100vh'}>
      <SearchView />
    </Box>
  );
}
