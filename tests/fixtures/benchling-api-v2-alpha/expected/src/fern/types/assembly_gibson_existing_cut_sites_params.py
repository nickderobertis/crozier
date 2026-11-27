

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssemblyGibsonExistingCutSitesParams(UniversalBaseModel):
    maximum_homology_and_binding_region_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="maximumHomologyAndBindingRegionLength"),
        pydantic.Field(
            alias="maximumHomologyAndBindingRegionLength",
            description="Maximum length, in base pairs, of the primer's binding/homology regions.",
        ),
    ]
    """
    Maximum length, in base pairs, of the primer's binding/homology regions.
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

    minimum_homology_and_binding_region_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="minimumHomologyAndBindingRegionLength"),
        pydantic.Field(
            alias="minimumHomologyAndBindingRegionLength",
            description="Minimum length, in base pairs, of the primer's binding/homology regions.",
        ),
    ]
    """
    Minimum length, in base pairs, of the primer's binding/homology regions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
