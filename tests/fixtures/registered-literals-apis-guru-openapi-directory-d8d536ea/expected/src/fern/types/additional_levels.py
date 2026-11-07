

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AdditionalLevels(UniversalBaseModel):
    level1: typing.Optional[str] = None
    level2: typing.Optional[str] = None
    level3: typing.Optional[str] = None
    level4: typing.Optional[str] = None
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
