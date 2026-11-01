

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobPropertiesDeliveryType(enum.StrEnum):
    """
    Delivery type of Job.
    """

    NON_SCHEDULED = "NonScheduled"
    SCHEDULED = "Scheduled"

    def visit(self, non_scheduled: typing.Callable[[], T_Result], scheduled: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobPropertiesDeliveryType.NON_SCHEDULED:
            return non_scheduled()
        if self is JobPropertiesDeliveryType.SCHEDULED:
            return scheduled()
