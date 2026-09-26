

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_file_attachment_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_file_attachment_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_file_attachment_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRefNmPage,
)
from .doc_annotations_list200response_annotations_item_file_attachment_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
