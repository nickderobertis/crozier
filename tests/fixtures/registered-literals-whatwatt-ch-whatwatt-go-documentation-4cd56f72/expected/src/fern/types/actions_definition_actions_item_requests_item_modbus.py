

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .actions_definition_actions_item_requests_item_modbus_type import (
    ActionsDefinitionActionsItemRequestsItemModbusType,
)


class ActionsDefinitionActionsItemRequestsItemModbus(UniversalBaseModel):
    host: typing.Optional[str] = None
    port: typing.Optional[int] = None
    unit_id: typing.Optional[int] = None
    func: typing.Optional[int] = None
    address: typing.Optional[int] = None
    type: typing.Optional[ActionsDefinitionActionsItemRequestsItemModbusType] = None
    value: typing.Optional[str] = None
    timeout: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
