

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DepositCapabilityIdMinting(enum.StrEnum):
    """
    How RO-Crate IDs are minted at deposit creation. `client` - the client MUST propose an ID; `server` - the server always mints one; `both` - the client MAY propose an ID and the server mints one when absent.
    """

    CLIENT = "client"
    SERVER = "server"
    BOTH = "both"

    def visit(
        self,
        client: typing.Callable[[], T_Result],
        server: typing.Callable[[], T_Result],
        both: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DepositCapabilityIdMinting.CLIENT:
            return client()
        if self is DepositCapabilityIdMinting.SERVER:
            return server()
        if self is DepositCapabilityIdMinting.BOTH:
            return both()
