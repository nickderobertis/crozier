

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .action_error import ActionError
from .notebook_summary import NotebookSummary
from .poke_status import PokeStatus
from .r_notes import RNotes


class ResponseBody_Ok(UniversalBaseModel):
    type: typing.Literal["ok"] = "ok"
    response: RNotes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseBody_NoChange(UniversalBaseModel):
    type: typing.Literal["no-change"] = "no-change"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseBody_Notebook(UniversalBaseModel):
    type: typing.Literal["notebook"] = "notebook"
    notebook: NotebookSummary

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseBody_ApiKey(UniversalBaseModel):
    type: typing.Literal["api-key"] = "api-key"
    api_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseBody_Error(UniversalBaseModel):
    type: typing.Literal["error"] = "error"
    error_type: typing_extensions.Annotated[
        ActionError, FieldMetadata(alias="errorType"), pydantic.Field(alias="errorType")
    ]
    message: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseBody_Pending(UniversalBaseModel):
    type: typing.Literal["pending"] = "pending"
    status: PokeStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ResponseBody = typing_extensions.Annotated[
    typing.Union[
        ResponseBody_Ok,
        ResponseBody_NoChange,
        ResponseBody_Notebook,
        ResponseBody_ApiKey,
        ResponseBody_Error,
        ResponseBody_Pending,
    ],
    pydantic.Field(discriminator="type"),
]
