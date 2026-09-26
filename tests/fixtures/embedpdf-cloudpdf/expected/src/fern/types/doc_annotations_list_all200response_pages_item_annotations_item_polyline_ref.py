

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
