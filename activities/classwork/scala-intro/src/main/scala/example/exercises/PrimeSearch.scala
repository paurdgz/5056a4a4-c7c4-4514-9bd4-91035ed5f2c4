package example.exercises

object PrimeSearch {
 /**
  * Problem definition: Find all the prime numbers in between two natural numbers.
  *
  * Prime number is defined as a natural number grater than one that cannot be composed by with the multiplication
  * of two smaller natural numbers.
  *
  * Consider:
  *    - Using the option-type safely transform the input values.
  *    - Create your own tests for the isPrime function.
  *    - Return a string separated by commas: 2, 3, 5, 7, 11, 13
  */

  }
  def primesUnder(n: Int): List[Int] = {
    require(n >= 2)

    def rec(i: Int, primes: List[Int]): List[Int] = {
      if (i >= n) primes
      else if (prime(i, primes)) rec(i + 1, i :: primes)
      else rec(i + 1, primes)
    }

    rec(2, List()).reverse
  }

  def prime(num: Int, factors: List[Int]): Boolean = factors.forall(num % _ != 0)
}

