

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FileSyncRequestFileOperationsItem_Create(UniversalBaseModel):
    action: typing.Literal["create"] = "create"
    commit_message: str
    content: str
    path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FileSyncRequestFileOperationsItem_Delete(UniversalBaseModel):
    action: typing.Literal["delete"] = "delete"
    commit_message: str
    path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FileSyncRequestFileOperationsItem_Update(UniversalBaseModel):
    action: typing.Literal["update"] = "update"
    commit_message: str
    content: str
    path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FileSyncRequestFileOperationsItem = typing_extensions.Annotated[
    typing.Union[
        FileSyncRequestFileOperationsItem_Create,
        FileSyncRequestFileOperationsItem_Delete,
        FileSyncRequestFileOperationsItem_Update,
    ],
    pydantic.Field(discriminator="action"),
]
