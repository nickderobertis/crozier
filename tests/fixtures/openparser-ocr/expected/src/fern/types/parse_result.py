

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_asset import DocumentAsset
from .document_element import DocumentElement
from .document_page import DocumentPage
from .document_provenance import DocumentProvenance
from .document_relation import DocumentRelation
from .raw_parse_result_profile import RawParseResultProfile
from .text_annotation import TextAnnotation


class ParseResult_Openparser1(UniversalBaseModel):
    output_format: typing.Literal["openparser@1"] = "openparser@1"
    document_id: str
    provenance: DocumentProvenance
    text: str
    markdown: str
    pages: typing.List[DocumentPage]
    elements: typing.List[DocumentElement]
    text_annotations: typing.List[TextAnnotation]
    relations: typing.List[DocumentRelation]
    assets: typing.List[DocumentAsset]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ParseResult_Raw(UniversalBaseModel):
    output_format: typing.Literal["raw"] = "raw"
    provider: str
    model: str
    profile: RawParseResultProfile
    result: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ParseResult = typing_extensions.Annotated[
    typing.Union[ParseResult_Openparser1, ParseResult_Raw], pydantic.Field(discriminator="output_format")
]
