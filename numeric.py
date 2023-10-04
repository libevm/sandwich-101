def get_amount_out(amount_in, reserve_in, reserve_out):
    """
    Referenced from UniswapV2Library.sol
    """
    amount_in_with_fee = amount_in * 997
    numerator = amount_in_with_fee * reserve_out
    denominator = reserve_in * 1000 + amount_in_with_fee
    return numerator / denominator

eth_reserve = 100
usd_reserve = 100_000
user_eth_in = 5
user_usd_min_recv = 3_500 # User min recv 3,500 USD

def binary_search(left, right, tolerance=0.0001):
    eth_to_swap = (right + left) / 2

    # Exceedeed tolerance
    if right - left < tolerance:
        return eth_to_swap

    # Calculate new reserves
    usd_recv = get_amount_out(eth_to_swap, eth_reserve, usd_reserve)
    new_eth_reserve = eth_reserve + eth_to_swap
    new_usd_reserve = usd_reserve - usd_recv
    user_usd_recv = get_amount_out(user_eth_in, new_eth_reserve, new_usd_reserve)

    # If user recv is too little, we swapped too much
    if user_usd_recv < user_usd_min_recv:
        return binary_search(left, eth_to_swap)

    # Can swap more
    return binary_search(eth_to_swap, right)

eth_to_swap = binary_search(0, 100)
print('eth_to_swap', eth_to_swap)