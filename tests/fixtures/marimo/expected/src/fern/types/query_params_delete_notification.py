

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_params_delete_notification_op import QueryParamsDeleteNotificationOp


class QueryParamsDeleteNotification(UniversalBaseModel):
    """
    Deletes URL query parameter values.

        Attributes:
            key: Query parameter key.
            value: Specific value to delete. If None, deletes all values for key.
    """

    key: str
    op: QueryParamsDeleteNotificationOp
    value: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
