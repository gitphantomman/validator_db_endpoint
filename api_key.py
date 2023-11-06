import utils

import random
import string

def generate_api_key(length=20):
    new_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    utils.saveApiKey(new_key)
    return new_key

def verify_api_key(api_key):
    # This is a placeholder for your actual verification logic
    # For example, you might check if the key exists in your database
    # and return True if it does, False otherwise
    return utils.checkApiKey(api_key)
# print(generate_api_key())

# api_key = generate_api_key()
# print(f"api_key generated:{api_key}")

# 0JCUjFiMn85ZnwLQJmay
print(verify_api_key("j2vTEjjn5wx4jt9kNMJs"))


