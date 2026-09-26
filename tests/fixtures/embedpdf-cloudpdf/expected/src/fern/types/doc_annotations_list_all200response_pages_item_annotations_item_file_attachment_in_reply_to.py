

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_in_reply_to_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyToIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_in_reply_to_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyToIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_in_reply_to_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyToNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_in_reply_to_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyToObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyToObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyToIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyTo_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyTo_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
