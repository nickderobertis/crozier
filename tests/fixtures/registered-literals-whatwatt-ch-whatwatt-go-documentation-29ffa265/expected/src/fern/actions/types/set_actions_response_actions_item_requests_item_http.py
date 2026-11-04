

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .set_actions_response_actions_item_requests_item_http_method import (
    SetActionsResponseActionsItemRequestsItemHttpMethod,
)


class SetActionsResponseActionsItemRequestsItemHttp(UniversalBaseModel):
    url: typing.Optional[str] = None
    method: typing.Optional[SetActionsResponseActionsItemRequestsItemHttpMethod] = None
    payload: typing.Optional[str] = None
    headers: typing.Optional[typing.Dict[str, str]] = None
    timeout: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
