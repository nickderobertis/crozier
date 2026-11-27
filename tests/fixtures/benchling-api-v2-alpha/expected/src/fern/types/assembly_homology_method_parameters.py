

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assembly_homology_method_parameters_ambiguous_construct_preference import (
    AssemblyHomologyMethodParametersAmbiguousConstructPreference,
)
from .assembly_homology_method_parameters_fragment_production_method import (
    AssemblyHomologyMethodParametersFragmentProductionMethod,
)


class AssemblyHomologyMethodParameters(UniversalBaseModel):
    ambiguous_construct_preference: typing_extensions.Annotated[
        AssemblyHomologyMethodParametersAmbiguousConstructPreference,
        FieldMetadata(alias="ambiguousConstructPreference"),
        pydantic.Field(alias="ambiguousConstructPreference"),
    ]
    fragment_production_method: typing_extensions.Annotated[
        AssemblyHomologyMethodParametersFragmentProductionMethod,
        FieldMetadata(alias="fragmentProductionMethod"),
        pydantic.Field(alias="fragmentProductionMethod"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
