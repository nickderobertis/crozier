

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pdf_destination import PdfDestination


class DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Goto(UniversalBaseModel):
    kind: typing.Literal["goto"] = "goto"
    destination: PdfDestination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Uri(UniversalBaseModel):
    kind: typing.Literal["uri"] = "uri"
    uri: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLinkTarget_GotoRemote(UniversalBaseModel):
    kind: typing.Literal["goto-remote"] = "goto-remote"
    file: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Launch(UniversalBaseModel):
    kind: typing.Literal["launch"] = "launch"
    path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Javascript(UniversalBaseModel):
    kind: typing.Literal["javascript"] = "javascript"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Named(UniversalBaseModel):
    kind: typing.Literal["named"] = "named"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Unsupported(UniversalBaseModel):
    kind: typing.Literal["unsupported"] = "unsupported"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemLinkTarget = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Goto,
        DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Uri,
        DocAnnotationsList200ResponseAnnotationsItemLinkTarget_GotoRemote,
        DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Launch,
        DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Javascript,
        DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Named,
        DocAnnotationsList200ResponseAnnotationsItemLinkTarget_Unsupported,
    ],
    pydantic.Field(discriminator="kind"),
]
