from hashlib import sha256
import time
start_time = time.time()

data = "Hello, world!"
nonce = 0
difficulty = 1


def create_hash(data, nonce):
    # print(f'{data*nonce}')
    return sha256(f'{data*nonce}'.encode()).hexdigest()


# Keep incrementing until the last 4 digits ends with a 0000.. which would
# yield 5 * 54455
while sha256(f'{data*nonce}'.encode()).hexdigest()[:difficulty] != "0" * difficulty:
    nonce += 1
    # print(create_hash(data, nonce))


print("data is %s" % data)
print(f'The solution for nonce = {nonce} and hash is: {create_hash(data, nonce)}')
print("*#$*#$( %s seconds )*#$*#$" % (time.time() - start_time))
