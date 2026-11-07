

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JsonPatchItem_Add(UniversalBaseModel):
    op: typing.Literal["add"] = "add"
    path: str
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class JsonPatchItem_Replace(UniversalBaseModel):
    op: typing.Literal["replace"] = "replace"
    path: str
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class JsonPatchItem_Test(UniversalBaseModel):
    op: typing.Literal["test"] = "test"
    path: str
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class JsonPatchItem_Remove(UniversalBaseModel):
    op: typing.Literal["remove"] = "remove"
    path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class JsonPatchItem_Move(UniversalBaseModel):
    op: typing.Literal["move"] = "move"
    from_: typing_extensions.Annotated[str, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class JsonPatchItem_Copy(UniversalBaseModel):
    op: typing.Literal["copy"] = "copy"
    from_: typing_extensions.Annotated[str, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


JsonPatchItem = typing_extensions.Annotated[
    typing.Union[
        JsonPatchItem_Add,
        JsonPatchItem_Replace,
        JsonPatchItem_Test,
        JsonPatchItem_Remove,
        JsonPatchItem_Move,
        JsonPatchItem_Copy,
    ],
    pydantic.Field(discriminator="op"),
]
