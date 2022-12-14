"""Test Request Strategies."""
import hypothesis
import hypothesis.strategies
import requests

import hypothesis_requests.strategies.request as sut


class TestMethod:
    """Test Method generation."""

    @hypothesis.given(data=hypothesis.strategies.data())  # type: ignore[misc]
    def test_no_arguments(self, data: hypothesis.strategies.DataObject) -> None:
        """Test Method generation with no arguments."""
        result = data.draw(sut.methods(), label="no arguments")
        assert result is None or isinstance(result, str)  # nosec
        assert result is None or result in sut.METHODS  # nosec

    @hypothesis.given(data=hypothesis.strategies.data(), method=sut.methods())  # type: ignore[misc]
    def test_include(self, data: hypothesis.strategies.DataObject, method: str) -> None:
        """Test Method generation with include."""
        hypothesis.assume(method is not None)
        result = data.draw(sut.methods(include=[method]))
        assert result is not None  # nosec
        assert result == method  # nosec


class TestRequest:
    """Test Request generation."""

    @hypothesis.given(data=hypothesis.strategies.data())  # type: ignore[misc]
    def test_no_arguments(self, data: hypothesis.strategies.DataObject) -> None:
        """Test Request generation with no arguments."""
        result = data.draw(sut.requests(), label="no arguments")
        assert isinstance(result, requests.Request)  # nosec
        assert result.method is None or result.method in sut.METHODS  # nosec

    @hypothesis.given(data=hypothesis.strategies.data(), method=sut.methods())  # type: ignore[misc]
    def test_method(self, data: hypothesis.strategies.DataObject, method: str) -> None:
        """Test Request generation with a specified method."""
        result = data.draw(
            sut.requests(methods=hypothesis.strategies.just(method)),
            label="with single method",
        )
        assert isinstance(result, requests.Request)  # nosec
        assert result.method == method  # nosec
