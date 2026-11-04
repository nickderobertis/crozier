

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .actions_definition_actions_item_requests_item_http import ActionsDefinitionActionsItemRequestsItemHttp
from .actions_definition_actions_item_requests_item_modbus import ActionsDefinitionActionsItemRequestsItemModbus


class ActionsDefinitionActionsItemRequestsItem(UniversalBaseModel):
    http: typing.Optional[ActionsDefinitionActionsItemRequestsItemHttp] = None
    modbus: typing.Optional[ActionsDefinitionActionsItemRequestsItemModbus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
