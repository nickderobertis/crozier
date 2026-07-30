

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ANote_Rename(UniversalBaseModel):
    type: typing.Literal["rename"] = "rename"
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANote_Move(UniversalBaseModel):
    type: typing.Literal["move"] = "move"
    folder: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANote_Delete(UniversalBaseModel):
    type: typing.Literal["delete"] = "delete"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANote_Update(UniversalBaseModel):
    type: typing.Literal["update"] = "update"
    body: str
    expected_revision: typing_extensions.Annotated[
        int, FieldMetadata(alias="expectedRevision"), pydantic.Field(alias="expectedRevision")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANote_Publish(UniversalBaseModel):
    type: typing.Literal["publish"] = "publish"
    html: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANote_Unpublish(UniversalBaseModel):
    type: typing.Literal["unpublish"] = "unpublish"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ANote_Restore(UniversalBaseModel):
    type: typing.Literal["restore"] = "restore"
    rev: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ANote = typing_extensions.Annotated[
    typing.Union[ANote_Rename, ANote_Move, ANote_Delete, ANote_Update, ANote_Publish, ANote_Unpublish, ANote_Restore],
    pydantic.Field(discriminator="type"),
]
