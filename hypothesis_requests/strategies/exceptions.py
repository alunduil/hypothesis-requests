"""Exception Strategies."""
import typing

import hypothesis.strategies
import requests


def exceptions(
    include: typing.Optional[typing.List[requests.RequestException]] = None,
) -> hypothesis.strategies.SearchStrategy[requests.RequestException]:
    """Generate Exceptions."""
    if include is not None:
        return hypothesis.strategies.sampled_from(include)

    return hypothesis.strategies.sampled_from(
        [requests.ConnectionError(), requests.Timeout(), requests.TooManyRedirects()]
    )
