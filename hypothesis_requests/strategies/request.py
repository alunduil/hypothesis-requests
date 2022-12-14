"""Requests Strategies."""
import typing

import hypothesis.strategies
import requests as _requests

METHODS = ["get", "post", "put", "patch", "delete"]


def methods(
    include: typing.Optional[typing.List[str]] = None,
) -> hypothesis.strategies.SearchStrategy[typing.Optional[str]]:
    """Generate Methods."""
    if include is not None:
        return hypothesis.strategies.sampled_from(include)

    return hypothesis.strategies.one_of(
        hypothesis.strategies.none(), hypothesis.strategies.sampled_from(METHODS)
    )


def requests(
    methods: hypothesis.strategies.SearchStrategy[  # pylint: disable=W0621
        typing.Optional[str]
    ] = methods(),
) -> hypothesis.strategies.SearchStrategy[_requests.Request]:
    """Generate Requests."""
    return hypothesis.strategies.builds(_requests.Request, method=methods)
