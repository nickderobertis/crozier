

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_params_set_notification_op import QueryParamsSetNotificationOp
from .query_params_set_notification_value import QueryParamsSetNotificationValue


class QueryParamsSetNotification(UniversalBaseModel):
    """
    Sets URL query parameter, replacing existing values.

        Attributes:
            key: Query parameter key.
            value: Value(s) to set.
    """

    key: str
    op: QueryParamsSetNotificationOp
    value: QueryParamsSetNotificationValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
