

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OutageStrategy(str, enum.Enum):
    ONE_SERVICE_PER_GROUP = "OneServicePerGroup"
    ALL_SERVICES_PER_GROUP = "AllServicesPerGroup"

    def visit(
        self,
        one_service_per_group: typing.Callable[[], T_Result],
        all_services_per_group: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OutageStrategy.ONE_SERVICE_PER_GROUP:
            return one_service_per_group()
        if self is OutageStrategy.ALL_SERVICES_PER_GROUP:
            return all_services_per_group()
