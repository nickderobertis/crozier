

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_widget_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_widget_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_widget_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_widget_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
