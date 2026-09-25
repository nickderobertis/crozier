

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserMessageContentItem_File(UniversalBaseModel):
    type: typing.Literal["file"] = "file"
    data: str
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UserMessageContentItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UserMessageContentItem = typing_extensions.Annotated[
    typing.Union[UserMessageContentItem_File, UserMessageContentItem_Text], pydantic.Field(discriminator="type")
]
