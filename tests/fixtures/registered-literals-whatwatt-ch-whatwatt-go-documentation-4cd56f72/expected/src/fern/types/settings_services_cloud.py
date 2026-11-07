

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SettingsServicesCloud(UniversalBaseModel):
    what_watt: typing.Optional[bool] = None
    solar_manager: typing.Optional[bool] = None
    mystrom: typing.Optional[bool] = None
    stromkonto: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
