

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssemblyGoldenGateMethodParameters_ExistingCutSites(UniversalBaseModel):
    fragment_production_method: typing_extensions.Annotated[
        typing.Literal["EXISTING_CUT_SITES"],
        FieldMetadata(alias="fragmentProductionMethod"),
        pydantic.Field(alias="fragmentProductionMethod"),
    ] = "EXISTING_CUT_SITES"
    type2s_restriction_enzyme_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="type2SRestrictionEnzymeId"), pydantic.Field(alias="type2SRestrictionEnzymeId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssemblyGoldenGateMethodParameters_PrimerPair(UniversalBaseModel):
    fragment_production_method: typing_extensions.Annotated[
        typing.Literal["PRIMER_PAIR"],
        FieldMetadata(alias="fragmentProductionMethod"),
        pydantic.Field(alias="fragmentProductionMethod"),
    ] = "PRIMER_PAIR"
    maximum_primer_pair_melting_temperature_difference: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="maximumPrimerPairMeltingTemperatureDifference"),
        pydantic.Field(alias="maximumPrimerPairMeltingTemperatureDifference"),
    ]
    minimum_binding_region_length: typing_extensions.Annotated[
        float, FieldMetadata(alias="minimumBindingRegionLength"), pydantic.Field(alias="minimumBindingRegionLength")
    ]
    minimum_binding_region_melting_temperature: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumBindingRegionMeltingTemperature"),
        pydantic.Field(alias="minimumBindingRegionMeltingTemperature"),
    ]
    pre_recognition_site_bases: typing_extensions.Annotated[
        str, FieldMetadata(alias="preRecognitionSiteBases"), pydantic.Field(alias="preRecognitionSiteBases")
    ]
    pre_recognition_site_length: typing_extensions.Annotated[
        float, FieldMetadata(alias="preRecognitionSiteLength"), pydantic.Field(alias="preRecognitionSiteLength")
    ]
    type2s_restriction_enzyme_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="type2SRestrictionEnzymeId"), pydantic.Field(alias="type2SRestrictionEnzymeId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AssemblyGoldenGateMethodParameters = typing_extensions.Annotated[
    typing.Union[AssemblyGoldenGateMethodParameters_ExistingCutSites, AssemblyGoldenGateMethodParameters_PrimerPair],
    pydantic.Field(discriminator="fragment_production_method"),
]
