

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
