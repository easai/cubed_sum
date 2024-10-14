## cubed_sum

The `cubed_sum` calculates the sum of cubes for a specified range. The naive implementation is just adding cubed numbers. The time complexity is O(n). A more efficient method would involve using the mathematical formula for the sum of cubes, which can compute the result in constant time O(1).

Additinally, the `cubed_sum` can calculates the even and odd sums of cubes.

The definition of the sum of cubes and related formulas, click below:
[The sum of cubes](https://github.com/easai/cubed_sum/blob/main/cubed_sum.ipynb)

### Installation

Clone the repository.

```bash
git clone https://github.com/easai/cubed_sum.git
```

Go to the installed directory, and run `poetry install`.

```bash
poetry install
```

### Test

Run `poetry run pytest` to run the `pytest` file.

```bash
poetry run pytest
```

### Usage Example

Calculate the sum of cubes of all numbers in a range by calling `cubed_sum()` method. The parity is set to both even and odd (`Parity.BOTH`) by default.

```bash
print(cubed_sum(1, 5, parity=Parity.BOTH))  # Sum of cubes of all numbers from 1 to 5
print(cubed_sum(1, 5, parity=Parity.EVEN))  # Sum of cubes of even numbers from 1 to 5
print(cubed_sum(1, 5, parity=Parity.ODD))  # Sum of cubes of odd numbers from 1 to 5
```
