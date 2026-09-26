

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_link_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
