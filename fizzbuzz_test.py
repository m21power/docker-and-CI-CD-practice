import pytest
from fizzbuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"  # Divisible by 3 and 5
    assert fizzbuzz(9) == "Fizz"       # Divisible by 3
    #let's change here and make it fail
    assert fizzbuzz(10) == "Fizz"      # Divisible by 5
    assert fizzbuzz(7) == 7            # Not divisible by 3 or 5

if __name__ == "__main__":
    pytest.main()
