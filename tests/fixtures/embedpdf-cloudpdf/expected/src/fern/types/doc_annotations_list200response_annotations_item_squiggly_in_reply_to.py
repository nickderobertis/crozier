

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_squiggly_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_squiggly_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_squiggly_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_squiggly_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
