

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv(enum.StrEnum):
    ONE = "1"
    TWO = "2"

    def visit(self, one: typing.Callable[[], T_Result], two: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv.ONE:
            return one()
        if self is ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv.TWO:
            return two()
