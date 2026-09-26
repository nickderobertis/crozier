

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_line_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemLineInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_line_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemLineInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_line_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemLineInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_line_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemLineInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemLineInReplyToObjectNumberPage
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemLineInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemLineInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemLineInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
