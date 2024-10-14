## cubed_sum

The `cubed_sum` calculates the cubic sum of numbers within a range. The `parity` argument specifies whether the term is added when it is odd, even, or both. Generate example usages of the function when the parity is set to odd, even, or both. Include cases when the range starts with odd or even numbers.

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
