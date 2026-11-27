

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assembly_concatenation_method_parameters import AssemblyConcatenationMethodParameters
from .assembly_gibson_method_parameters import AssemblyGibsonMethodParameters
from .assembly_golden_gate_method_parameters import AssemblyGoldenGateMethodParameters
from .assembly_homology_method_parameters import AssemblyHomologyMethodParameters


class AssemblySpecSharedAssemblyParameters_Concatenation(UniversalBaseModel):
    """
    Assembly-wide parameters to describe requirements and procedures for the assembly.
    """

    type: typing.Literal["CONCATENATION"] = "CONCATENATION"
    parameters: AssemblyConcatenationMethodParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssemblySpecSharedAssemblyParameters_Gibson(UniversalBaseModel):
    """
    Assembly-wide parameters to describe requirements and procedures for the assembly.
    """

    type: typing.Literal["GIBSON"] = "GIBSON"
    parameters: AssemblyGibsonMethodParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssemblySpecSharedAssemblyParameters_GoldenGate(UniversalBaseModel):
    """
    Assembly-wide parameters to describe requirements and procedures for the assembly.
    """

    type: typing.Literal["GOLDEN_GATE"] = "GOLDEN_GATE"
    parameters: AssemblyGoldenGateMethodParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssemblySpecSharedAssemblyParameters_Homology(UniversalBaseModel):
    """
    Assembly-wide parameters to describe requirements and procedures for the assembly.
    """

    type: typing.Literal["HOMOLOGY"] = "HOMOLOGY"
    parameters: AssemblyHomologyMethodParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AssemblySpecSharedAssemblyParameters = typing_extensions.Annotated[
    typing.Union[
        AssemblySpecSharedAssemblyParameters_Concatenation,
        AssemblySpecSharedAssemblyParameters_Gibson,
        AssemblySpecSharedAssemblyParameters_GoldenGate,
        AssemblySpecSharedAssemblyParameters_Homology,
    ],
    pydantic.Field(discriminator="type"),
]
