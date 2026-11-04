

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_actions_response_actions_item_requests_item_http_method import (
    GetActionsResponseActionsItemRequestsItemHttpMethod,
)


class GetActionsResponseActionsItemRequestsItemHttp(UniversalBaseModel):
    url: typing.Optional[str] = None
    method: typing.Optional[GetActionsResponseActionsItemRequestsItemHttpMethod] = None
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
