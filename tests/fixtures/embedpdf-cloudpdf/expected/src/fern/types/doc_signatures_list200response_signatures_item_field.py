

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocSignaturesList200ResponseSignaturesItemField_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocSignaturesList200ResponseSignaturesItemField_Fqn(UniversalBaseModel):
    kind: typing.Literal["fqn"] = "fqn"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocSignaturesList200ResponseSignaturesItemField = typing_extensions.Annotated[
    typing.Union[
        DocSignaturesList200ResponseSignaturesItemField_ObjectNumber,
        DocSignaturesList200ResponseSignaturesItemField_Fqn,
    ],
    pydantic.Field(discriminator="kind"),
]
