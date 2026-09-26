

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
