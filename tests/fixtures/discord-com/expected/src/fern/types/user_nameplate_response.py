

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nameplate_palette import NameplatePalette
from .snowflake_type import SnowflakeType


class UserNameplateResponse(UniversalBaseModel):
    sku_id: typing.Optional[SnowflakeType] = None
    asset: typing.Optional[str] = None
    label: typing.Optional[str] = None
    palette: typing.Optional[NameplatePalette] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
