

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connection_configuration_item_defaults_item import ConnectionConfigurationItemDefaultsItem


class ConnectionConfigurationItem(UniversalBaseModel):
    defaults: typing.Optional[typing.List[ConnectionConfigurationItemDefaultsItem]] = None
    resource: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
