

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_params_clear_notification_op import QueryParamsClearNotificationOp


class QueryParamsClearNotification(UniversalBaseModel):
    """
    Clears all URL query parameters.
    """

    op: QueryParamsClearNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
