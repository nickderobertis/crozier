

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
