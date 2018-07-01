import time
from random import randint

from max_product import max_product, max_product_fast

arrays = []
for exp in range(1, 8):
    arrays.append([randint(-100, 100) for _ in range(10**exp)])

# Profile max_product
for array in arrays:
    start = time.time()
    mp = max_product(array)
    elapsed = time.time() - start

    print(f'max_product: {elapsed} for array of length {len(array)}')

    start = time.time()
    mp = max_product_fast(array)
    elapsed = time.time() - start

    print(f'max_product_fast: {elapsed} for array of length {len(array)}')

