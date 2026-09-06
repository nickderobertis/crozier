

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType


class UpdateThreadTagRequest(UniversalBaseModel):
    name: str
    emoji_id: typing.Optional[SnowflakeType] = None
    emoji_name: typing.Optional[str] = None
    moderated: typing.Optional[bool] = None
    id: typing.Optional[SnowflakeType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
