from typing import List
import unittest


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        - Loop through numbers from 0 to n
            - Check if i // 3 and 5
            - Check if i // 5
            - Check if i // 3          

        - append the number to the result list
        """
        result = list()

        for i in range(1, n+1):
            r_str = ""
            if (i % 3) == 0:
                r_str += "Fizz"
            if (i % 5) == 0:
                r_str += "Buzz"
            if not r_str:
                r_str = str(i)
            result.append(r_str)

        return result


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_fizzbuzz_15(self):
        self.assertEqual(self.solution.fizzBuzz(15), 
                         ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])

    def test_fizzbuzz_3(self):
        self.assertEqual(self.solution.fizzBuzz(3), ["1","2","Fizz"])

    def test_fizzbuzz_5(self):
        self.assertEqual(self.solution.fizzBuzz(5), ["1","2","Fizz","4","Buzz"])

if __name__ == '__main__':
    unittest.main()
