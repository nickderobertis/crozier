

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transport_preferences import TransportPreferences


class Preferences(UniversalBaseModel):
    """
    Preferences related to the order
    """

    preferred_data_center_region: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="preferredDataCenterRegion"),
        pydantic.Field(alias="preferredDataCenterRegion", description="Preferred Data Center Region."),
    ] = None
    """
    Preferred Data Center Region.
    """

    transport_preferences: typing_extensions.Annotated[
        typing.Optional[TransportPreferences],
        FieldMetadata(alias="transportPreferences"),
        pydantic.Field(
            alias="transportPreferences", description="Preferences related to the shipment logistics of the sku."
        ),
    ] = None
    """
    Preferences related to the shipment logistics of the sku.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
