

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigLspOneValueCommand(UniversalBaseModel):
    command: typing.List[str]
    extensions: typing.Optional[typing.List[str]] = None
    disabled: typing.Optional[bool] = None
    env: typing.Optional[typing.Dict[str, str]] = None
    initialization: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
