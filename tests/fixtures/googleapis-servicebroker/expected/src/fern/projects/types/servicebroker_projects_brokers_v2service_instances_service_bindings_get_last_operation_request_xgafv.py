

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv(enum.StrEnum):
    ONE = "1"
    TWO = "2"

    def visit(self, one: typing.Callable[[], T_Result], two: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv.ONE:
            return one()
        if self is ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv.TWO:
            return two()
