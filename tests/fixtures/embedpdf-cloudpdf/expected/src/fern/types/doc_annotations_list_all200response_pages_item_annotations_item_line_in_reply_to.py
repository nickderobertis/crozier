

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_line_in_reply_to_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyToIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_in_reply_to_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyToIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_in_reply_to_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyToNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_in_reply_to_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyToObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyToObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyToIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyTo_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyTo_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
