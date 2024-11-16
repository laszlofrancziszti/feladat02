# -------------------------------------------------megoldas---------------------------------------------

MOD = 10**9 + 7


def dice_ways(n, memo={}):
    # Ha már számoltuk az n-hez tartozó eredményt, adjuk vissza
    if n in memo:
        return memo[n]

    # Alapeset: n = 0 esetén egyetlen mód van (üres dobássorozat)
    if n == 0:
        return 1

    # Számítás az összes lehetséges dobással
    ways = 0
    for j in range(1, 7):
        if n - j >= 0:
            ways = (ways + dice_ways(n - j, memo)) % MOD

    # Az eredmény eltárolása a memo szótárban
    memo[n] = ways
    return ways


# Példa bemenet
n = int(input().strip())
print(dice_ways(n))

# --------------------------------------------teszt----------------------------------------------
import random

bemenetek = [random.randint(6, 200) for i in range(10)]

for i in range(10):
    print(bemenetek[i], dice_ways(bemenetek[i]))
