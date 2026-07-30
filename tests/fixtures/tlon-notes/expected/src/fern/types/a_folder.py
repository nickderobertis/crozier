

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AFolder_Rename(UniversalBaseModel):
    type: typing.Literal["rename"] = "rename"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AFolder_Move(UniversalBaseModel):
    type: typing.Literal["move"] = "move"
    new_parent: typing_extensions.Annotated[int, FieldMetadata(alias="newParent"), pydantic.Field(alias="newParent")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AFolder_Delete(UniversalBaseModel):
    type: typing.Literal["delete"] = "delete"
    recursive: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AFolder = typing_extensions.Annotated[
    typing.Union[AFolder_Rename, AFolder_Move, AFolder_Delete], pydantic.Field(discriminator="type")
]
