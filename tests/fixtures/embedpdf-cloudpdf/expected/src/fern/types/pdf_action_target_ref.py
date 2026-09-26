

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PdfActionTargetRef_Name(UniversalBaseModel):
    kind: typing.Literal["name"] = "name"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfActionTargetRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="objectNumber"), pydantic.Field(alias="objectNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PdfActionTargetRef = typing_extensions.Annotated[
    typing.Union[PdfActionTargetRef_Name, PdfActionTargetRef_ObjectNumber], pydantic.Field(discriminator="kind")
]
