

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_redact_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemRedactRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_redact_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemRedactRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_redact_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemRedactRefNmPage,
)
from .doc_annotations_list200response_annotations_item_redact_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemRedactRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemRedactRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemRedactRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemRedactRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemRedactRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemRedactRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemRedactRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemRedactRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemRedactRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemRedactRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemRedactRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemRedactRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
