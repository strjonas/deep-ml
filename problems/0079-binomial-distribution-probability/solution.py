import math

def binomial_probability(n: int, k: int, p: float) -> float:
    """
    Calculate the probability of exactly k successes in n Bernoulli trials.
    
    Args:
        n: Total number of trials
        k: Number of successes
        p: Probability of success on each trial
    
    Returns:
        Probability of k successes
    """
    succ = p**k
    fail = (1-p)**(n-k)
    bino = math.factorial(n) / ( math.factorial(k) * math.factorial(n-k))
    return succ * fail * bino 