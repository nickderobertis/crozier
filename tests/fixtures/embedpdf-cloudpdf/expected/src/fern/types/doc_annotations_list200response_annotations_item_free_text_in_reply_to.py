

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_free_text_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_free_text_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_free_text_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_free_text_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
