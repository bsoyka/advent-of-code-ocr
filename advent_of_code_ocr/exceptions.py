"""Exceptions for the Advent of Code OCR library."""


class UnevenRowsError(ValueError):
    """Raised when the input has uneven rows."""


class IncorrectRowCountError(ValueError):
    """Raised when the input does not have exactly 6 rows."""

    def __init__(self, *, expected: int = 6, actual: int | None = None) -> None:
        """Initialize the error with a message about the expected/actual row count."""
        message = f'Incorrect number of rows (expected {expected})'
        if actual is not None:
            message += f', got {actual}'
        super().__init__(message)
