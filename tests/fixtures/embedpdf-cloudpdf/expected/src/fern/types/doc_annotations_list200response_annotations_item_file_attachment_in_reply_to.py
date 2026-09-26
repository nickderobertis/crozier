

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_file_attachment_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_file_attachment_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_file_attachment_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_file_attachment_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
