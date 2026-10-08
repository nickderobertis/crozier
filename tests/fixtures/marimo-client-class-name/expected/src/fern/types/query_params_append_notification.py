

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_params_append_notification_op import QueryParamsAppendNotificationOp


class QueryParamsAppendNotification(UniversalBaseModel):
    """
    Appends value to URL query parameter.

        Attributes:
            key: Query parameter key.
            value: Value to append.
    """

    key: str
    op: QueryParamsAppendNotificationOp
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
