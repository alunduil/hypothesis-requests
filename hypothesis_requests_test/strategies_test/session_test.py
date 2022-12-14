"""Test Session Strategies."""
import hypothesis
import hypothesis.strategies
import requests

import hypothesis_requests.strategies.session as sut


class TestSession:
    """Test Session generation."""

    @hypothesis.given(data=hypothesis.strategies.data())  # type: ignore[misc]
    def test_no_arguments(self, data: hypothesis.strategies.DataObject) -> None:
        """Test Session generation with no arguments."""
        result = data.draw(sut.sessions(), label="no arguments")
        assert isinstance(result, requests.Session)  # nosec

    @hypothesis.given(data=hypothesis.strategies.data())  # type: ignore[misc]
    def test_context_manager(self, data: hypothesis.strategies.DataObject) -> None:
        """Test Session generation use as a context manager."""
        result = data.draw(sut.sessions(), label="context manager")
        with result as session:
            assert isinstance(session, requests.Session)  # nosec
