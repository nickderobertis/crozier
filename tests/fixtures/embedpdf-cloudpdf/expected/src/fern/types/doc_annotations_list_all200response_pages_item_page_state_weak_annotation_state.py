

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocAnnotationsListAll200ResponsePagesItemPageStateWeakAnnotationState_Unknown(UniversalBaseModel):
    kind: typing.Literal["unknown"] = "unknown"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemPageStateWeakAnnotationState_Known(UniversalBaseModel):
    kind: typing.Literal["known"] = "known"
    has_any_weak_annotations: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasAnyWeakAnnotations"), pydantic.Field(alias="hasAnyWeakAnnotations")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemPageStateWeakAnnotationState = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemPageStateWeakAnnotationState_Unknown,
        DocAnnotationsListAll200ResponsePagesItemPageStateWeakAnnotationState_Known,
    ],
    pydantic.Field(discriminator="kind"),
]
