

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assembly_concatenation_method_parameters_fragment_production_method import (
    AssemblyConcatenationMethodParametersFragmentProductionMethod,
)
from .assembly_concatenation_method_parameters_polymer_type import AssemblyConcatenationMethodParametersPolymerType


class AssemblyConcatenationMethodParameters(UniversalBaseModel):
    fragment_production_method: typing_extensions.Annotated[
        AssemblyConcatenationMethodParametersFragmentProductionMethod,
        FieldMetadata(alias="fragmentProductionMethod"),
        pydantic.Field(alias="fragmentProductionMethod"),
    ]
    polymer_type: typing_extensions.Annotated[
        AssemblyConcatenationMethodParametersPolymerType,
        FieldMetadata(alias="polymerType"),
        pydantic.Field(alias="polymerType"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
