import { Box, Input, Text } from '@chakra-ui/react';
import { BiSearchAlt } from 'react-icons/bi';
import { IconContext } from 'react-icons';
import React from 'react';
import './search.css';

export default function Search() {
  return (
    <>
      <Box
        width={'100vw'}
        height={'100vh'}
        display={'flex'}
        justifyContent={'center'}
        alignItems={'center'}
        background={'gray.400'}
      >
        <Box
          background={'gray.300'}
          boxShadow={'5px 5px 20px #888888'}
          borderRadius={'1%'}
          width={'50rem'}
          height={'30rem'}
          display={'flex'}
          justifyContent={'space-evenly'}
          flexDirection={'column'}
        >
          <Box>
            <Text textAlign={'center'} fontSize={'5xl'}>
              Smart Search
            </Text>
          </Box>
          <IconContext.Provider
            value={{
              color: 'black',
              className: 'global-class-name',
            }}
          >
            <Box
              display={'flex'}
              width={'50%'}
              alignSelf={'center'}
              justifySelf={'center'}
            >
              <BiSearchAlt />
              <Input type={'text'} name="search" background={'gray.400'} />
            </Box>
          </IconContext.Provider>
        </Box>
      </Box>
    </>
  );
}
