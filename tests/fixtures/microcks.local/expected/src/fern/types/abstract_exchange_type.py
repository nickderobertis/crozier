

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AbstractExchangeType(str, enum.Enum):
    """
    Discriminant type for identifying kind of exchange
    """

    REQ_RESP_PAIR = "reqRespPair"
    UNIDIR_EVENT = "unidirEvent"

    def visit(
        self, req_resp_pair: typing.Callable[[], T_Result], unidir_event: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AbstractExchangeType.REQ_RESP_PAIR:
            return req_resp_pair()
        if self is AbstractExchangeType.UNIDIR_EVENT:
            return unidir_event()
