

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectAdvisorsResponseOutputLintsItemCategoriesItem(enum.StrEnum):
    PERFORMANCE = "PERFORMANCE"
    SECURITY = "SECURITY"
    HEALTH = "HEALTH"

    def visit(
        self,
        performance: typing.Callable[[], T_Result],
        security: typing.Callable[[], T_Result],
        health: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ProjectAdvisorsResponseOutputLintsItemCategoriesItem.PERFORMANCE:
            return performance()
        if self is V1ProjectAdvisorsResponseOutputLintsItemCategoriesItem.SECURITY:
            return security()
        if self is V1ProjectAdvisorsResponseOutputLintsItemCategoriesItem.HEALTH:
            return health()
