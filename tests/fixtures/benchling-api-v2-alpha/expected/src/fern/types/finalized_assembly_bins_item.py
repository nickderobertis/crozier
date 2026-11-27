

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assembly_fragment_bin_fragment_production_method import AssemblyFragmentBinFragmentProductionMethod


class FinalizedAssemblyBinsItem_Constant(UniversalBaseModel):
    bin_type: typing_extensions.Annotated[
        typing.Literal["CONSTANT"], FieldMetadata(alias="binType"), pydantic.Field(alias="binType")
    ] = "CONSTANT"
    id: str
    name: str
    residues: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FinalizedAssemblyBinsItem_Fragment(UniversalBaseModel):
    bin_type: typing_extensions.Annotated[
        typing.Literal["FRAGMENT"], FieldMetadata(alias="binType"), pydantic.Field(alias="binType")
    ] = "FRAGMENT"
    fragment_production_method: typing_extensions.Annotated[
        typing.Optional[AssemblyFragmentBinFragmentProductionMethod],
        FieldMetadata(alias="fragmentProductionMethod"),
        pydantic.Field(alias="fragmentProductionMethod"),
    ] = None
    id: str
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FinalizedAssemblyBinsItem = typing_extensions.Annotated[
    typing.Union[FinalizedAssemblyBinsItem_Constant, FinalizedAssemblyBinsItem_Fragment],
    pydantic.Field(discriminator="bin_type"),
]
