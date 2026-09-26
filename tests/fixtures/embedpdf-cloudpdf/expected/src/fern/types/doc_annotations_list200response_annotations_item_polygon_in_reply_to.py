

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_polygon_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_polygon_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_polygon_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_polygon_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
