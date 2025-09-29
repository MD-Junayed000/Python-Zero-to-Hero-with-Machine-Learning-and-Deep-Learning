def add(a, b):
    return a + b

# Example usage
if __name__ == "__main__":
    result = add(3, 5)
    print(f"The result of adding 3 and 5 is {result}")
    

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True