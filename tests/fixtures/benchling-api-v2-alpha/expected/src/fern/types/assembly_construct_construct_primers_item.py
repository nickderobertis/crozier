

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssemblyConstructConstructPrimersItem_BulkAssemblyCreatedPrimer(UniversalBaseModel):
    type: typing.Literal["BULK_ASSEMBLY_CREATED_PRIMER"] = "BULK_ASSEMBLY_CREATED_PRIMER"
    created_oligo_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdOligoId"), pydantic.Field(alias="createdOligoId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssemblyConstructConstructPrimersItem_BulkAssemblyTransientPrimer(UniversalBaseModel):
    type: typing.Literal["BULK_ASSEMBLY_TRANSIENT_PRIMER"] = "BULK_ASSEMBLY_TRANSIENT_PRIMER"
    bases: typing.Optional[str] = None
    binding_position: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bindingPosition"), pydantic.Field(alias="bindingPosition")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AssemblyConstructConstructPrimersItem = typing_extensions.Annotated[
    typing.Union[
        AssemblyConstructConstructPrimersItem_BulkAssemblyCreatedPrimer,
        AssemblyConstructConstructPrimersItem_BulkAssemblyTransientPrimer,
    ],
    pydantic.Field(discriminator="type"),
]
