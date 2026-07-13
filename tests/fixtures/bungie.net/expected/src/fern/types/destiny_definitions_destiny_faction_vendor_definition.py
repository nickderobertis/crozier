

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyFactionVendorDefinition(UniversalBaseModel):
    """
    These definitions represent faction vendors at different points in the game.
    A single faction may contain multiple vendors, or the same vendor available at two different locations.
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

    vendor_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="vendorHash")] = pydantic.Field(
        default=None
    )
    """
    The faction vendor hash.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
