

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1StatesUpdateState(UniversalBaseModel):
    name: typing.Optional[str] = None
    icon: typing.Optional[str] = None
    color: typing.Optional[str] = None
    billed: typing.Optional[bool] = None
    locked: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
