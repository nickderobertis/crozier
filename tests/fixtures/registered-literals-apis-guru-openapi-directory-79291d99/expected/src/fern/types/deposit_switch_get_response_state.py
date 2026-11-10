

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DepositSwitchGetResponseState(enum.StrEnum):
    """

    The state, or status, of the deposit switch.

    - `initialized` – The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.

    - `processing` – The deposit switch request has been submitted and is being processed.

    - `completed` – The user's employer has fulfilled the deposit switch request.

    - `error` – There was an error processing the deposit switch request.
    """

    INITIALIZED = "initialized"
    PROCESSING = "processing"
    COMPLETED = "completed"
    ERROR = "error"

    def visit(
        self,
        initialized: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DepositSwitchGetResponseState.INITIALIZED:
            return initialized()
        if self is DepositSwitchGetResponseState.PROCESSING:
            return processing()
        if self is DepositSwitchGetResponseState.COMPLETED:
            return completed()
        if self is DepositSwitchGetResponseState.ERROR:
            return error()
