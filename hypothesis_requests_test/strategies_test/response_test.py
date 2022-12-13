"""Test Response Strategies."""
import hypothesis_requests.strategies.response as sut


class TestResponses:  # pylint: disable=R0903
    """Test Response Strategy."""

    def test_no_arguments(self) -> None:
        """Test Response Strategy with no arguments."""
        sut.responses()
