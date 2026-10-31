

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transport_preferences_preferred_shipment_type import TransportPreferencesPreferredShipmentType


class TransportPreferences(UniversalBaseModel):
    """
    Preferences related to the shipment logistics of the sku
    """

    preferred_shipment_type: typing_extensions.Annotated[
        TransportPreferencesPreferredShipmentType,
        FieldMetadata(alias="preferredShipmentType"),
        pydantic.Field(
            alias="preferredShipmentType", description="Indicates Shipment Logistics type that the customer preferred."
        ),
    ]
    """
    Indicates Shipment Logistics type that the customer preferred.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
