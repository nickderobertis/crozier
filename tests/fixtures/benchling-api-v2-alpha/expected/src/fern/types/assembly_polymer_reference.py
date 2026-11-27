

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssemblyPolymerReference_AaSequence(UniversalBaseModel):
    polymer_type: typing_extensions.Annotated[
        typing.Literal["AA_SEQUENCE"], FieldMetadata(alias="polymerType"), pydantic.Field(alias="polymerType")
    ] = "AA_SEQUENCE"
    protein_id: typing_extensions.Annotated[str, FieldMetadata(alias="proteinId"), pydantic.Field(alias="proteinId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssemblyPolymerReference_NucleotideSequence(UniversalBaseModel):
    polymer_type: typing_extensions.Annotated[
        typing.Literal["NUCLEOTIDE_SEQUENCE"], FieldMetadata(alias="polymerType"), pydantic.Field(alias="polymerType")
    ] = "NUCLEOTIDE_SEQUENCE"
    sequence_id: typing_extensions.Annotated[str, FieldMetadata(alias="sequenceId"), pydantic.Field(alias="sequenceId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AssemblyPolymerReference = typing_extensions.Annotated[
    typing.Union[AssemblyPolymerReference_AaSequence, AssemblyPolymerReference_NucleotideSequence],
    pydantic.Field(discriminator="polymer_type"),
]
