

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_highlight_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_highlight_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_highlight_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_highlight_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
