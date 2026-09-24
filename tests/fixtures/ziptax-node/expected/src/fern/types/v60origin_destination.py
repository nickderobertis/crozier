

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v60origin_destination_value import V60OriginDestinationValue


class V60OriginDestination(UniversalBaseModel):
    adjustment_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="adjustmentType"),
        pydantic.Field(
            alias="adjustmentType", description="Sourcing ruleset name. Currently always 'ORIGIN_DESTINATION'."
        ),
    ]
    """
    Sourcing ruleset name. Currently always 'ORIGIN_DESTINATION'.
    """

    description: str = pydantic.Field()
    """
    Human-readable description of the sourcing model applied (e.g. 'Destination Based Taxation').
    """

    value: V60OriginDestinationValue = pydantic.Field()
    """
    Sourcing basis for the location: 'O' = origin-based (ship-from rate), 'D' = destination-based (ship-to rate).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
