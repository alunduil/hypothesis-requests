"""Hypothesis Strategies for Responses."""
import hypothesis
import hypothesis.strategies
import requests


def responses() -> hypothesis.strategies.SearchStrategy[requests.Response]:
    """Hypothesis strategy for `requests.Response`_."""
    return hypothesis.strategies.builds(requests.Response)
