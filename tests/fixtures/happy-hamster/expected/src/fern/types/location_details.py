

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .location_type import LocationType


class LocationDetails(UniversalBaseModel):
    """
    Locaiton details
    """

    type: typing.Optional[LocationType] = None
    brand: typing.Optional[str] = pydantic.Field(default=None)
    """
    Brand of the shop
    """

    opening_hours: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="openingHours"),
        pydantic.Field(alias="openingHours", description="Opening hours of the shop"),
    ] = None
    """
    Opening hours of the shop
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
