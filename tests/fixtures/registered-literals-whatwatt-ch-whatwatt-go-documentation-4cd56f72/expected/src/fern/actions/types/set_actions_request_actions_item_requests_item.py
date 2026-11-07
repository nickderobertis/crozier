

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .set_actions_request_actions_item_requests_item_http import SetActionsRequestActionsItemRequestsItemHttp
from .set_actions_request_actions_item_requests_item_modbus import SetActionsRequestActionsItemRequestsItemModbus


class SetActionsRequestActionsItemRequestsItem(UniversalBaseModel):
    http: typing.Optional[SetActionsRequestActionsItemRequestsItemHttp] = None
    modbus: typing.Optional[SetActionsRequestActionsItemRequestsItemModbus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
