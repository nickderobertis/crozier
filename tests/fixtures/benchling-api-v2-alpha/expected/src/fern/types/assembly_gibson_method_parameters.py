

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssemblyGibsonMethodParameters_ExistingCutSites(UniversalBaseModel):
    fragment_production_method: typing_extensions.Annotated[
        typing.Literal["EXISTING_CUT_SITES"],
        FieldMetadata(alias="fragmentProductionMethod"),
        pydantic.Field(alias="fragmentProductionMethod"),
    ] = "EXISTING_CUT_SITES"
    maximum_homology_and_binding_region_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="maximumHomologyAndBindingRegionLength"),
        pydantic.Field(alias="maximumHomologyAndBindingRegionLength"),
    ]
    minimum_binding_region_melting_temperature: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumBindingRegionMeltingTemperature"),
        pydantic.Field(alias="minimumBindingRegionMeltingTemperature"),
    ]
    minimum_homology_and_binding_region_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumHomologyAndBindingRegionLength"),
        pydantic.Field(alias="minimumHomologyAndBindingRegionLength"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssemblyGibsonMethodParameters_ExistingHomologyRegions(UniversalBaseModel):
    fragment_production_method: typing_extensions.Annotated[
        typing.Literal["EXISTING_HOMOLOGY_REGIONS"],
        FieldMetadata(alias="fragmentProductionMethod"),
        pydantic.Field(alias="fragmentProductionMethod"),
    ] = "EXISTING_HOMOLOGY_REGIONS"
    maximum_homology_and_binding_region_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="maximumHomologyAndBindingRegionLength"),
        pydantic.Field(alias="maximumHomologyAndBindingRegionLength"),
    ]
    minimum_binding_region_melting_temperature: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumBindingRegionMeltingTemperature"),
        pydantic.Field(alias="minimumBindingRegionMeltingTemperature"),
    ]
    minimum_homology_and_binding_region_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumHomologyAndBindingRegionLength"),
        pydantic.Field(alias="minimumHomologyAndBindingRegionLength"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssemblyGibsonMethodParameters_PrimerPair(UniversalBaseModel):
    fragment_production_method: typing_extensions.Annotated[
        typing.Literal["PRIMER_PAIR"],
        FieldMetadata(alias="fragmentProductionMethod"),
        pydantic.Field(alias="fragmentProductionMethod"),
    ] = "PRIMER_PAIR"
    maximum_homology_and_binding_region_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="maximumHomologyAndBindingRegionLength"),
        pydantic.Field(alias="maximumHomologyAndBindingRegionLength"),
    ]
    maximum_primer_pair_melting_temperature_difference: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="maximumPrimerPairMeltingTemperatureDifference"),
        pydantic.Field(alias="maximumPrimerPairMeltingTemperatureDifference"),
    ]
    minimum_binding_region_melting_temperature: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumBindingRegionMeltingTemperature"),
        pydantic.Field(alias="minimumBindingRegionMeltingTemperature"),
    ]
    minimum_homology_and_binding_region_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumHomologyAndBindingRegionLength"),
        pydantic.Field(alias="minimumHomologyAndBindingRegionLength"),
    ]
    minimum_primer_melting_temperature: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumPrimerMeltingTemperature"),
        pydantic.Field(alias="minimumPrimerMeltingTemperature"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AssemblyGibsonMethodParameters = typing_extensions.Annotated[
    typing.Union[
        AssemblyGibsonMethodParameters_ExistingCutSites,
        AssemblyGibsonMethodParameters_ExistingHomologyRegions,
        AssemblyGibsonMethodParameters_PrimerPair,
    ],
    pydantic.Field(discriminator="fragment_production_method"),
]
