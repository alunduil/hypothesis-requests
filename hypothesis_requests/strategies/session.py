"""Sessions Stratgies."""
import hypothesis.strategies
import requests


def sessions() -> hypothesis.strategies.SearchStrategy[requests.Session]:
    """Generate Sessions."""
    return hypothesis.strategies.builds(requests.Session)
