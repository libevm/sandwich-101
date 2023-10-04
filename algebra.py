"""
We know that
x y   = k
y / x = p

where
k = constant
x = quantity of asset x
y = quantity of asset y
p = price of asset x: asset y

So, to get the amount of X to sell to hit new price new_p

(x + a) (y - b) = k
(y - b) / (x + a) = new_p

(substitute)
new_p(x + a) = (y - b)

new_p(x+a)**2 = k
new_p(x+a)**2 - k = 0
"""

import sympy
import math

def get_amount_out(amount_in, reserve_in, reserve_out):
    """
    Referenced from UniswapV2Library.sol
    """
    amount_in_with_fee = amount_in * 997
    numerator = amount_in_with_fee * reserve_out
    denominator = reserve_in * 1000 + amount_in_with_fee
    return numerator / denominator

p, x, a, k = sympy.symbols("p,x,a,k")
# print(sympy.solve(p*((x+a)**2)-k, a))

eth_reserve = 100
usd_reserve = 100_000
user_eth_in = 5
user_usd_min_recv = 3_500 # User min recv 3,500 USD
user_price = user_usd_min_recv / user_eth_in

# k is constant
k = eth_reserve * usd_reserve
eth_to_swap = math.sqrt(eth_reserve * usd_reserve * user_price)/user_price - eth_reserve

print(eth_to_swap)

# usd_recv = get_amount_out(eth_to_swap, eth_reserve, usd_reserve)
# new_eth_reserve = eth_reserve + eth_to_swap
# new_usd_reserve = usd_reserve - usd_recv
# user_usd_recv = get_amount_out(user_eth_in, new_eth_reserve, new_usd_reserve)
