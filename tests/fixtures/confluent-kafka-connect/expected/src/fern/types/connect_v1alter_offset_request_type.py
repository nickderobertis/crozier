

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectV1AlterOffsetRequestType(enum.StrEnum):
    """
    The type of alter operation. PATCH will update the offset to the provided values.
    The update will only happen for the partitions provided in the request.
    DELETE will delete the offset for the provided partitions and reset them back to the
    base state. It is as if, a fresh new connector was created.

    For sink connectors PATCH/DELETE will move the offsets to the provided point in the
    topic partition. If the offset provided is not present in the topic partition it will
    by default reset to the earliest offset in the topic partition.

    For source connectors, post PATCH/DELETE the connector will attempt to read from the
    position defined in the altered offsets.
    """

    PATCH = "PATCH"
    DELETE = "DELETE"

    def visit(self, patch: typing.Callable[[], T_Result], delete: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectV1AlterOffsetRequestType.PATCH:
            return patch()
        if self is ConnectV1AlterOffsetRequestType.DELETE:
            return delete()
