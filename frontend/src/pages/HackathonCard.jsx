import { useEffect, useState } from "react";
import {
  Box,
  Badge,
  Image,
  Flex,
  Text,
  Icon,
  VStack,
  SimpleGrid,
  Link,
  Spinner,
} from "@chakra-ui/react";
import { Globe } from "lucide-react";

export default function HackathonList() {
  const [hackathons, setHackathons] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/hackathons")
      // Adjust URL if necessary
      .then((response) => response.json())
      .then((data) => {
        setHackathons(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching hackathons:", error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <Spinner size="xl" />;
  }

  return (
    <SimpleGrid columns={{ base: 1, md: 2 }} spacing={6} p={4}>
      {hackathons.map((hackathon, index) => (
        <Box
          key={index}
          maxW="md"
          p={4}
          boxShadow="lg"
          borderRadius="lg"
          borderWidth="1px"
          borderColor="gray.200"
          bg="white"
        >
          <Box
            bg="gray.200"
            color="gray.800"
            fontSize="sm"
            fontWeight="semibold"
            textTransform="uppercase"
            px={3}
            py={1}
            borderRadius="full"
            w="max-content"
            mb={2}
          >
            Featured
          </Box>
          <Flex align="center" gap={4}>
            <Image
              src="https://via.placeholder.com/50"
              alt={hackathon["Event Title"]}
              w={14}
              h={14}
              borderRadius="md"
            />
            <VStack align="start" spacing={0}>
              <Flex align="center" color="gray.600" fontSize="sm">
                <Icon as={Globe} w={4} h={4} mr={1} /> Online
              </Flex>
              <Link href={hackathon.href} isExternal>
                <Text fontSize="lg" fontWeight="bold" color="blue.500">
                  {hackathon["Event Title"]}
                </Text>
              </Link>
            </VStack>
          </Flex>
          <Box mt={4}>
            <Flex align="center" gap={2} fontSize="sm" color="gray.700">
              <Badge colorScheme="green">{hackathon["Days Left"]}</Badge>
            </Flex>
            <Flex wrap="wrap" gap={2} mt={3}>
              {hackathon["Span Texts"].map((tag, idx) => (
                <Badge key={idx} variant="outline" colorScheme="blue">
                  {tag}
                </Badge>
              ))}
            </Flex>
          </Box>
        </Box>
      ))}
    </SimpleGrid>
  );
}
