

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_text_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemTextInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_text_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemTextInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_text_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemTextInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_text_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemTextInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemTextInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemTextInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemTextInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemTextInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
