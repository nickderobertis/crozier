

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .emission_zone_type import EmissionZoneType


class Exclusions(UniversalBaseModel):
    """
    Exclusions
    """

    emission_zone_types: typing_extensions.Annotated[
        typing.Optional[typing.List[EmissionZoneType]],
        FieldMetadata(alias="emissionZoneTypes"),
        pydantic.Field(
            alias="emissionZoneTypes",
            description="Excludes the emission zone with types from the accessibility calculation",
        ),
    ] = None
    """
    Excludes the emission zone with types from the accessibility calculation
    """

    emission_zone_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="emissionZoneIds"),
        pydantic.Field(
            alias="emissionZoneIds",
            description="Excludes the emission zone with ids from the accessibility calculation",
        ),
    ] = None
    """
    Excludes the emission zone with ids from the accessibility calculation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
