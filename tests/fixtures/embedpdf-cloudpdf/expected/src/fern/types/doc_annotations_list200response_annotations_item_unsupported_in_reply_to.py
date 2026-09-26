

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_unsupported_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_unsupported_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_unsupported_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_unsupported_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
