

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
