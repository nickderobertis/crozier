

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assembly_concatenation_method_parameters import AssemblyConcatenationMethodParameters
from .assembly_gibson_method_parameters import AssemblyGibsonMethodParameters
from .assembly_golden_gate_method_parameters import AssemblyGoldenGateMethodParameters
from .assembly_homology_method_parameters import AssemblyHomologyMethodParameters


class FinalizedAssemblyMethod_Concatenation(UniversalBaseModel):
    type: typing.Literal["CONCATENATION"] = "CONCATENATION"
    parameters: AssemblyConcatenationMethodParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FinalizedAssemblyMethod_Gibson(UniversalBaseModel):
    type: typing.Literal["GIBSON"] = "GIBSON"
    parameters: AssemblyGibsonMethodParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FinalizedAssemblyMethod_GoldenGate(UniversalBaseModel):
    type: typing.Literal["GOLDEN_GATE"] = "GOLDEN_GATE"
    parameters: AssemblyGoldenGateMethodParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FinalizedAssemblyMethod_Homology(UniversalBaseModel):
    type: typing.Literal["HOMOLOGY"] = "HOMOLOGY"
    parameters: AssemblyHomologyMethodParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FinalizedAssemblyMethod = typing_extensions.Annotated[
    typing.Union[
        FinalizedAssemblyMethod_Concatenation,
        FinalizedAssemblyMethod_Gibson,
        FinalizedAssemblyMethod_GoldenGate,
        FinalizedAssemblyMethod_Homology,
    ],
    pydantic.Field(discriminator="type"),
]
