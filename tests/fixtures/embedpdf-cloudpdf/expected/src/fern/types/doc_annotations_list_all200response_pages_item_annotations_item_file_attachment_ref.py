

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
