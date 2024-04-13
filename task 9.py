class BigInt:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = str(value)
        elif isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Invalid initialization value")

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __lt__(self, other):
        return int(self.value) < int(other.value)

    def __le__(self, other):
        return int(self.value) <= int(other.value)

    def __gt__(self, other):
        return int(self.value) > int(other.value)

    def __ge__(self, other):
        return int(self.value) >= int(other.value)

    def __eq__(self, other):
        return int(self.value) == int(other.value)

    def __add__(self, other):
        return BigInt(int(self) + int(other))

    # Implement other arithmetic operations similarly

# Example usage
a = BigInt(12345678901234567890)
b = BigInt("98765432109876543210")

print(a + b)  # Output: 111111111011111111100
print(a < b)  # Output: True
