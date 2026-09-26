

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesAnalysis200ResponseCurrentMethod(enum.StrEnum):
    NET_STATE = "net-state"
    NET_STATE_REPLAY = "net-state+replay"

    def visit(
        self, net_state: typing.Callable[[], T_Result], net_state_replay: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DocSignaturesAnalysis200ResponseCurrentMethod.NET_STATE:
            return net_state()
        if self is DocSignaturesAnalysis200ResponseCurrentMethod.NET_STATE_REPLAY:
            return net_state_replay()
