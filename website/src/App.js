import React from 'react'
import {
  ChakraProvider,
  Container,
  IconButton,
  Center,
  Text,
  Button
} from '@chakra-ui/react'
import {
  ChevronRightIcon,
  CloseIcon,
  ChevronLeftIcon,
  ArrowLeftIcon,
  ChevronUpIcon,
  ArrowRightIcon,
  ChevronDownIcon
} from '@chakra-ui/icons'

function App(){

  async function sendCommand(command) {

    let response = await fetch(`http://127.0.0.1:8000/${command}`);

    if (response.ok) { // if HTTP-status is 200-299
      // get the response body (the method explained below)
      //let json = await response.json();
    } else {
      alert("HTTP-Error: " + response.status);
    }
  }

  return (
  <ChakraProvider resetCSS>
    <Container backgroundColor="blackAlpha.200" display="block">
      <Text fontSize="xl" fontWeight="bold" textAlign="center">
        Ragna Controllcenter v3
      </Text>
      <Center m={5}>
        <IconButton
          onMouseDown={() => sendCommand("move_left_start")}
          onMouseUp={() => sendCommand("move_left_stop")}
          aria-label="icon"
          icon={<ArrowLeftIcon />}
          size="md"
          ml={2}
          mr={2}
          colorScheme="blackAlpha"
          
        />
        <IconButton
          onMouseDown={() => sendCommand("move_forward_start")}
          onMouseUp={() => sendCommand("move_forward_stop")}
          aria-label="icon"
          icon={<ChevronUpIcon />}
          size="md"
          ml={2}
          mr={2}
          colorScheme="blackAlpha"
        />
        <IconButton 
          onMouseDown={() => sendCommand("move_right")}
          onMouseUp={() => sendCommand("move_right_stop")}
          aria-label="icon"
          icon={<ArrowRightIcon />}
          size="md"
          ml={2}
          mr={2}
          colorScheme="blackAlpha"
        />
      </Center>
      <Center m={5}>
        <IconButton 
          onMouseDown={() => sendCommand("turn_left_start")}
          onMouseUp={() => sendCommand("turn_left_stop")}
          aria-label="icon"
          icon={<ChevronLeftIcon />}
          size="md"
          ml={2}
          mr={2}
          colorScheme="blackAlpha"
        />
        

        <IconButton 
          aria-label="icon"
          icon={<CloseIcon />}
          size="md"
          ml={2}
          mr={2}
          colorScheme="blackAlpha"
        />

        
        <IconButton
          onMouseDown={() => sendCommand("turn_right_start")}
          onMouseUp={() => sendCommand("turn_right_stop")}
          aria-label="icon"
          icon={<ChevronRightIcon />}
          size="md"
          mr={2}
          ml={2}
          colorScheme="blackAlpha"
        />
      </Center>
      <Center m={5}>
        <IconButton
          onMouseDown={() => sendCommand("move_backwards_start")}
          onMouseUp={() => sendCommand("move_backwards_stop")}
          aria-label="icon"
          icon={<ChevronDownIcon />}
          size="md"
          ml={2}
          mr={2}
          colorScheme="blackAlpha"
        />
      </Center>
      <Center m={5}>
        <Button onClick={() => sendCommand("standUp")}
          variant="solid"
          size="md"
          colorScheme="blackAlpha"
          ml={2}
          mr={2}
        >
          stand up
        </Button>
        <Button onClick={() => sendCommand("layDown")}
          variant="solid"
          size="md"
          colorScheme="blackAlpha"
          ml={2}
          mr={2}
        >
          lay down
        </Button>
      </Center>
      <Center m={5}>
        <Button onClick={() => sendCommand("wiggle")}
          variant="solid"
          size="md"
          colorScheme="blackAlpha"
          ml={2}
          mr={2}
        >
          wiggle
        </Button>
        <Button onClick={() => sendCommand("sit")}
          variant="solid"
          size="md"
          colorScheme="blackAlpha"
          ml={2}
          mr={2}
        >
          sit
        </Button>
      </Center>
    </Container>
  </ChakraProvider>
);
}


export default App
