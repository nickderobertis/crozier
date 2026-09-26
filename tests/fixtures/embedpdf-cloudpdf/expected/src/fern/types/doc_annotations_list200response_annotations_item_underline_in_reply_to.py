

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_underline_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_underline_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_underline_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_underline_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
