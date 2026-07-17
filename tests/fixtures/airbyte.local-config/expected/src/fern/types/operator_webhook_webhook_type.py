

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OperatorWebhookWebhookType(enum.StrEnum):
    DBT_CLOUD = "dbtCloud"

    def visit(self, dbt_cloud: typing.Callable[[], T_Result]) -> T_Result:
        if self is OperatorWebhookWebhookType.DBT_CLOUD:
            return dbt_cloud()
