

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssemblyGoldenGatePrimerPairParams(UniversalBaseModel):
    maximum_primer_pair_melting_temperature_difference: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="maximumPrimerPairMeltingTemperatureDifference"),
        pydantic.Field(
            alias="maximumPrimerPairMeltingTemperatureDifference",
            description="Maximum difference of melting temperature between both primers in a pair.",
        ),
    ]
    """
    Maximum difference of melting temperature between both primers in a pair.
    """

    minimum_binding_region_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumBindingRegionLength"),
        pydantic.Field(alias="minimumBindingRegionLength", description="Minimum length of the primer binding region."),
    ]
    """
    Minimum length of the primer binding region.
    """

    minimum_binding_region_melting_temperature: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumBindingRegionMeltingTemperature"),
        pydantic.Field(
            alias="minimumBindingRegionMeltingTemperature",
            description="Minimum melting temperature of the primer binding region.",
        ),
    ]
    """
    Minimum melting temperature of the primer binding region.
    """

    pre_recognition_site_bases: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="preRecognitionSiteBases"),
        pydantic.Field(
            alias="preRecognitionSiteBases",
            description="Specific base pairs to insert before the type IIS enzyme recognition site.",
        ),
    ]
    """
    Specific base pairs to insert before the type IIS enzyme recognition site.
    """

    pre_recognition_site_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="preRecognitionSiteLength"),
        pydantic.Field(
            alias="preRecognitionSiteLength",
            description="Number of base pairs to insert before the type IIS enzyme recognition site.",
        ),
    ]
    """
    Number of base pairs to insert before the type IIS enzyme recognition site.
    """

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
