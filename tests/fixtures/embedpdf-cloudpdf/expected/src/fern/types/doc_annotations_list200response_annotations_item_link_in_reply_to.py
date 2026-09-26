

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_link_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemLinkInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_link_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemLinkInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_link_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemLinkInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_link_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemLinkInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemLinkInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemLinkInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemLinkInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemLinkInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
