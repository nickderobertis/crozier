

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_ink_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemInkInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_ink_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemInkInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_ink_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemInkInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_ink_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemInkInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemInkInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemInkInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemInkInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemInkInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemInkInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemInkInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemInkInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemInkInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemInkInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemInkInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemInkInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
