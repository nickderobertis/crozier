

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_in_reply_to_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyToIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_in_reply_to_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyToIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_in_reply_to_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyToNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_in_reply_to_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyToObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyToObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyToIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyTo_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyTo_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
