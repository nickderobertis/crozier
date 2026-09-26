

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_strikeout_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_strikeout_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_strikeout_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_strikeout_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
