

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interaction_types import InteractionTypes
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class MessageInteractionResponse(UniversalBaseModel):
    id: SnowflakeType
    type: InteractionTypes
    name: str
    user: typing.Optional[UserResponse] = None
    name_localized: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
