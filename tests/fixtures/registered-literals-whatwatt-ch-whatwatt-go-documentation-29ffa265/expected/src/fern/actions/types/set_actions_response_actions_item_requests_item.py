

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .set_actions_response_actions_item_requests_item_http import SetActionsResponseActionsItemRequestsItemHttp
from .set_actions_response_actions_item_requests_item_modbus import SetActionsResponseActionsItemRequestsItemModbus


class SetActionsResponseActionsItemRequestsItem(UniversalBaseModel):
    http: typing.Optional[SetActionsResponseActionsItemRequestsItemHttp] = None
    modbus: typing.Optional[SetActionsResponseActionsItemRequestsItemModbus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
