

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_actions_response_actions_item_requests_item_http import GetActionsResponseActionsItemRequestsItemHttp
from .get_actions_response_actions_item_requests_item_modbus import GetActionsResponseActionsItemRequestsItemModbus


class GetActionsResponseActionsItemRequestsItem(UniversalBaseModel):
    http: typing.Optional[GetActionsResponseActionsItemRequestsItemHttp] = None
    modbus: typing.Optional[GetActionsResponseActionsItemRequestsItemModbus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
