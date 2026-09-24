

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchResponseModelSearchModelSearchType(enum.StrEnum):
    """
    Search Type
    """

    NETWORK = "network"
    AUDIT_EVENT = "audit_event"
    CONFIG = "config"
    ASSET = "asset"

    def visit(
        self,
        network: typing.Callable[[], T_Result],
        audit_event: typing.Callable[[], T_Result],
        config: typing.Callable[[], T_Result],
        asset: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchResponseModelSearchModelSearchType.NETWORK:
            return network()
        if self is SearchResponseModelSearchModelSearchType.AUDIT_EVENT:
            return audit_event()
        if self is SearchResponseModelSearchModelSearchType.CONFIG:
            return config()
        if self is SearchResponseModelSearchModelSearchType.ASSET:
            return asset()
