

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_redact_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemRedactInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_redact_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemRedactInReplyToIndexRevision,
)
from .doc_annotations_list200response_annotations_item_redact_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemRedactInReplyToNmPage,
)
from .doc_annotations_list200response_annotations_item_redact_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemRedactInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemRedactInReplyTo_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemRedactInReplyToObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemRedactInReplyTo_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemRedactInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemRedactInReplyTo_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemRedactInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemRedactInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemRedactInReplyTo = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemRedactInReplyTo_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemRedactInReplyTo_Nm,
        DocAnnotationsList200ResponseAnnotationsItemRedactInReplyTo_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
