

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OperatorWebhookWebhookType(str, enum.Enum):
    DBT_CLOUD = "dbtCloud"

    def visit(self, dbt_cloud: typing.Callable[[], T_Result]) -> T_Result:
        if self is OperatorWebhookWebhookType.DBT_CLOUD:
            return dbt_cloud()
