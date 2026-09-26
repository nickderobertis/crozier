

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pdf_destination import PdfDestination


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Goto(UniversalBaseModel):
    kind: typing.Literal["goto"] = "goto"
    destination: PdfDestination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Uri(UniversalBaseModel):
    kind: typing.Literal["uri"] = "uri"
    uri: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_GotoRemote(UniversalBaseModel):
    kind: typing.Literal["goto-remote"] = "goto-remote"
    file: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Launch(UniversalBaseModel):
    kind: typing.Literal["launch"] = "launch"
    path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Javascript(UniversalBaseModel):
    kind: typing.Literal["javascript"] = "javascript"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Named(UniversalBaseModel):
    kind: typing.Literal["named"] = "named"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Unsupported(UniversalBaseModel):
    kind: typing.Literal["unsupported"] = "unsupported"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Goto,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Uri,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_GotoRemote,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Launch,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Javascript,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Named,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget_Unsupported,
    ],
    pydantic.Field(discriminator="kind"),
]
