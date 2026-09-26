

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_caret_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_caret_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_caret_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_caret_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
