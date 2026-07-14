

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connection_configuration_item_defaults_item_target import ConnectionConfigurationItemDefaultsItemTarget
from .connection_configuration_item_defaults_item_value import ConnectionConfigurationItemDefaultsItemValue
from .form_field_option import FormFieldOption


class ConnectionConfigurationItemDefaultsItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    options: typing.Optional[typing.List[FormFieldOption]] = None
    target: typing.Optional[ConnectionConfigurationItemDefaultsItemTarget] = None
    value: typing.Optional[ConnectionConfigurationItemDefaultsItemValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
