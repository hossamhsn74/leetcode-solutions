class Solution:
    def isPrime(self, n):
        if n < 2:
            return False

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # product = 1
        # for item in nums:
        #     print(item, self.isPrime(item))
        #     product *= item

        # result = []
        # # get prime factors of numbers
        # for i in nums:
        #     if self.isPrime(i) and product % i == 0:
        #         product //= i
        #         result.append(i)
        #     elif not self.isPrime(i):
        #         # get prime factors of numbers
        #         factors = []
        #         for j in range(2, i):
        #             if i % j == 0:
        #                 factors.append(j)

        #         for x in factors:
        #             if self.isPrime(x) and product % x == 0:
        #                 product //= x
        #                 result.append(x)

        # return len(set(result)) 
        # we will not have to calculate product of all items of array

        # we will get the factors for each number and if prime we will save it to list
        prime_factors = set()
        # get prime factors of numbers
        for i in nums:
            if self.isPrime(i):
                prime_factors.add(i)
            else:
                # get prime factors of numbers
                factors = []
                for j in range(2, i):
                    if i % j == 0:
                        factors.append(j)

                for x in factors:
                    if self.isPrime(x):
                        prime_factors.add(x)

        return len(prime_factors)