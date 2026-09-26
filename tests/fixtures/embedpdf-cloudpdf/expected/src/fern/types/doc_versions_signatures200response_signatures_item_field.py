

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocVersionsSignatures200ResponseSignaturesItemField_ObjectNumber(UniversalBaseModel):
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


class DocVersionsSignatures200ResponseSignaturesItemField_Fqn(UniversalBaseModel):
    kind: typing.Literal["fqn"] = "fqn"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocVersionsSignatures200ResponseSignaturesItemField = typing_extensions.Annotated[
    typing.Union[
        DocVersionsSignatures200ResponseSignaturesItemField_ObjectNumber,
        DocVersionsSignatures200ResponseSignaturesItemField_Fqn,
    ],
    pydantic.Field(discriminator="kind"),
]
