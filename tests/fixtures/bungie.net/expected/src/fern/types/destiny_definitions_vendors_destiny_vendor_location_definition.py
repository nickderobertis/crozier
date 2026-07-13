

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsVendorsDestinyVendorLocationDefinition(UniversalBaseModel):
    """
    These definitions represent vendors' locations and relevant display information at different times in the game.
    """

    background_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundImagePath")
    ] = pydantic.Field(default=None)
    """
    The relative path to the background image representing this Vendor at this location, for use in a banner.
    """

    destination_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="destinationHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash identifier for a Destination at which this vendor may be located. Each destination where a Vendor may exist will only ever have a single entry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
