"""Test Exception Strategies."""
import hypothesis
import hypothesis.strategies
import requests

import hypothesis_requests.strategies.exceptions as sut


class TestExceptions:
    """Test Exception strategies."""

    @hypothesis.given(data=hypothesis.strategies.data())  # type: ignore[misc]
    def test_no_arguments(self, data: hypothesis.strategies.DataObject) -> None:
        """Test Exceptions strategy with no arguments."""
        result = data.draw(sut.exceptions(), label="no arguments")
        assert isinstance(result, requests.RequestException)  # nosec

    @hypothesis.given(data=hypothesis.strategies.data(), exception=sut.exceptions())  # type: ignore[misc]
    def test_only_toomanyredirects(
        self,
        data: hypothesis.strategies.DataObject,
        exception: requests.RequestException,
    ) -> None:
        """Test Exceptions strategy with only TooManyRedirects."""
        result = data.draw(sut.exceptions(include=[exception]))
        assert isinstance(result, exception.__class__)  # nosec
