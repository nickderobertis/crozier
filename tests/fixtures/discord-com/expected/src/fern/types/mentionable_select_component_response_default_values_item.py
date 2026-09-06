

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType


class MentionableSelectComponentResponseDefaultValuesItem_Role(UniversalBaseModel):
    type: typing.Literal["role"] = "role"
    id: SnowflakeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MentionableSelectComponentResponseDefaultValuesItem_User(UniversalBaseModel):
    type: typing.Literal["user"] = "user"
    id: SnowflakeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MentionableSelectComponentResponseDefaultValuesItem = typing_extensions.Annotated[
    typing.Union[
        MentionableSelectComponentResponseDefaultValuesItem_Role,
        MentionableSelectComponentResponseDefaultValuesItem_User,
    ],
    pydantic.Field(discriminator="type"),
]
