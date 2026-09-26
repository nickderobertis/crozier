

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pdf_action_node_submit_form_payload import PdfActionNodeSubmitFormPayload
from .pdf_action_target_ref import PdfActionTargetRef
from .pdf_destination import PdfDestination


class PdfActionNode_Javascript(UniversalBaseModel):
    type: typing.Literal["javascript"] = "javascript"
    subtype: str
    next: typing.List[typing.Any]
    script: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Goto(UniversalBaseModel):
    type: typing.Literal["goto"] = "goto"
    subtype: str
    next: typing.List[typing.Any]
    destination: PdfDestination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Uri(UniversalBaseModel):
    type: typing.Literal["uri"] = "uri"
    subtype: str
    next: typing.List[typing.Any]
    uri: str
    is_map: typing_extensions.Annotated[bool, FieldMetadata(alias="isMap"), pydantic.Field(alias="isMap")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Named(UniversalBaseModel):
    type: typing.Literal["named"] = "named"
    subtype: str
    next: typing.List[typing.Any]
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Hide(UniversalBaseModel):
    type: typing.Literal["hide"] = "hide"
    subtype: str
    next: typing.List[typing.Any]
    targets: typing.List[PdfActionTargetRef]
    hide: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_ResetForm(UniversalBaseModel):
    type: typing.Literal["reset-form"] = "reset-form"
    subtype: str
    next: typing.List[typing.Any]
    fields: typing.Optional[typing.List[PdfActionTargetRef]] = None
    exclude: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_GotoRemote(UniversalBaseModel):
    type: typing.Literal["goto-remote"] = "goto-remote"
    subtype: str
    next: typing.List[typing.Any]
    file_path: typing_extensions.Annotated[str, FieldMetadata(alias="filePath"), pydantic.Field(alias="filePath")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_GotoEmbedded(UniversalBaseModel):
    type: typing.Literal["goto-embedded"] = "goto-embedded"
    subtype: str
    next: typing.List[typing.Any]
    file_path: typing_extensions.Annotated[str, FieldMetadata(alias="filePath"), pydantic.Field(alias="filePath")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Launch(UniversalBaseModel):
    type: typing.Literal["launch"] = "launch"
    subtype: str
    next: typing.List[typing.Any]
    file_path: typing_extensions.Annotated[str, FieldMetadata(alias="filePath"), pydantic.Field(alias="filePath")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Rendition(UniversalBaseModel):
    type: typing.Literal["rendition"] = "rendition"
    subtype: str
    next: typing.List[typing.Any]
    script: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_SubmitForm(UniversalBaseModel):
    type: typing.Literal["submit-form"] = "submit-form"
    subtype: str
    next: typing.List[typing.Any]
    payload: typing.Optional[PdfActionNodeSubmitFormPayload] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Thread(UniversalBaseModel):
    type: typing.Literal["thread"] = "thread"
    subtype: str
    next: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Sound(UniversalBaseModel):
    type: typing.Literal["sound"] = "sound"
    subtype: str
    next: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Movie(UniversalBaseModel):
    type: typing.Literal["movie"] = "movie"
    subtype: str
    next: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_ImportData(UniversalBaseModel):
    type: typing.Literal["import-data"] = "import-data"
    subtype: str
    next: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_SetOcgState(UniversalBaseModel):
    type: typing.Literal["set-ocg-state"] = "set-ocg-state"
    subtype: str
    next: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Transition(UniversalBaseModel):
    type: typing.Literal["transition"] = "transition"
    subtype: str
    next: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Goto3DView(UniversalBaseModel):
    type: typing.Literal["goto-3d-view"] = "goto-3d-view"
    subtype: str
    next: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionNode_Unknown(UniversalBaseModel):
    type: typing.Literal["unknown"] = "unknown"
    subtype: str
    next: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PdfActionNode = typing_extensions.Annotated[
    typing.Union[
        PdfActionNode_Javascript,
        PdfActionNode_Goto,
        PdfActionNode_Uri,
        PdfActionNode_Named,
        PdfActionNode_Hide,
        PdfActionNode_ResetForm,
        PdfActionNode_GotoRemote,
        PdfActionNode_GotoEmbedded,
        PdfActionNode_Launch,
        PdfActionNode_Rendition,
        PdfActionNode_SubmitForm,
        PdfActionNode_Thread,
        PdfActionNode_Sound,
        PdfActionNode_Movie,
        PdfActionNode_ImportData,
        PdfActionNode_SetOcgState,
        PdfActionNode_Transition,
        PdfActionNode_Goto3DView,
        PdfActionNode_Unknown,
    ],
    pydantic.Field(discriminator="type"),
]
