

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_link_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemLinkRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_link_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemLinkRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_link_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemLinkRefNmPage,
)
from .doc_annotations_list200response_annotations_item_link_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemLinkRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemLinkRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemLinkRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemLinkRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemLinkRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLinkRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemLinkRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemLinkRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemLinkRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemLinkRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemLinkRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemLinkRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
