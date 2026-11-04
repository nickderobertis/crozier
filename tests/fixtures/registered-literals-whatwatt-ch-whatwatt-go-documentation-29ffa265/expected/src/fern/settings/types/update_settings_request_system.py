

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateSettingsRequestSystem(UniversalBaseModel):
    name: typing.Optional[str] = None
    host_name: typing.Optional[str] = None
    protection: typing.Optional[bool] = None
    password: typing.Optional[str] = None
    power_save: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
