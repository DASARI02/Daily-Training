import random
def sum(random_numbers):
    
    odd = 0
    even = 0
    for number in random_numbers:
        if number % 2 == 0:
            even += number
        else:
            odd += number
    return even,odd  

def start():
    n = int(input(" random numbers needed?"))
    random_numbers = [random.randint(1, 100) for _ in range(n)]
    even,odd = sum(random_numbers)
    print(f"Even numbers: {even}  Odd numbers: {odd} random number{random_numbers}"
          )
    
start()
