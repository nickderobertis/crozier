

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReaderStatus(enum.StrEnum):
    """
    The status of the reader object gives information about the current state of the reader.

    Possible values:

    - `unknown` - The reader status is unknown.
    - `processing` - The reader is created and waits for the physical device to confirm the pairing.
    - `paired` - The reader is paired with a merchant account and can be used with SumUp APIs.
    - `expired` - The pairing is expired and no longer usable with the account. The resource needs to get recreated.
    """

    UNKNOWN = "unknown"
    PROCESSING = "processing"
    PAIRED = "paired"
    EXPIRED = "expired"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        paired: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReaderStatus.UNKNOWN:
            return unknown()
        if self is ReaderStatus.PROCESSING:
            return processing()
        if self is ReaderStatus.PAIRED:
            return paired()
        if self is ReaderStatus.EXPIRED:
            return expired()
