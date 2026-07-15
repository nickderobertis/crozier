

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connector_setting_type import ConnectorSettingType


class ConnectorSetting(UniversalBaseModel):
    id: typing.Optional[str] = None
    label: typing.Optional[str] = None
    type: typing.Optional[ConnectorSettingType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
