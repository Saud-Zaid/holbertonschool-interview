#!/usr/bin/python3
"""
0-making_change module
Defines a function that determines the fewest number of coins
needed to meet a given amount total.
"""


def _gcd(a, b):
    """Computes the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a


def _bfs_change(coins, total):
    """Finds minimum coins using BFS (coins sorted ascending)."""
    visited = {total}
    queue = [total]
    steps = 0

    while queue:
        steps += 1
        next_queue = []
        for rem in queue:
            for c in coins:
                if c > rem:
                    break
                nxt = rem - c
                if nxt == 0:
                    return steps
                if nxt not in visited:
                    visited.add(nxt)
                    next_queue.append(nxt)
        queue = next_queue

    return -1


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet total.

    Args:
        coins (list of int): Values of the coins in possession.
        total (int): Target amount to meet.

    Returns:
        int: Fewest number of coins needed, 0 if total <= 0,
        or -1 if total cannot be met.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    coins = sorted(set(c for c in coins if c <= total), reverse=True)
    if not coins:
        return -1

    g = coins[0]
    for c in coins[1:]:
        g = _gcd(g, c)
    if total % g != 0:
        return -1
    if g > 1:
        total //= g
        coins = [c // g for c in coins]

    if total % coins[0] == 0:
        return total // coins[0]

    n = len(coins)
    if n > 15:
        coins.reverse()
        return _bfs_change(coins, total)

    best = total + 1

    def dfs(idx, rem, count):
        """Branch-and-bound DFS to find minimum coin count."""
        nonlocal best
        if rem == 0:
            if count < best:
                best = count
            return
        if idx == n:
            return
        c = coins[idx]
        if count + (rem + c - 1) // c >= best:
            return
        max_k = rem // c
        if idx == n - 1:
            if rem % c == 0 and count + max_k < best:
                best = count + max_k
            return
        next_c = coins[idx + 1]
        for k in range(max_k, -1, -1):
            new_rem = rem - k * c
            new_count = count + k
            if new_count + (new_rem + next_c - 1) // next_c >= best:
                break
            dfs(idx + 1, new_rem, new_count)

    dfs(0, total, 0)
    return best if best <= total else -1
