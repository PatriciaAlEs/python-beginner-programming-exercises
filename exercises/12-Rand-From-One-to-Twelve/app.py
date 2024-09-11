import random

def get_randomInt():
	# ✅↓ Write your code here ↓✅
	result = random.randrange(1,13)
	return result

# randint() da un número <= parametro, mientras que randrange da < parametro por la definición de range()

# ❌ ↓ DON'T CHANGE THE CODE BELOW ↓ ❌
print(get_randomInt())
