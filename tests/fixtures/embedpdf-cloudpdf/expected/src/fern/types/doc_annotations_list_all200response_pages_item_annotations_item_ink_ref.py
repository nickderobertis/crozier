

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
