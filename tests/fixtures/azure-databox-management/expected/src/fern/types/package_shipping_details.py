

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PackageShippingDetails(UniversalBaseModel):
    """
    Shipping details.
    """

    carrier_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="carrierName"),
        pydantic.Field(alias="carrierName", description="Name of the carrier."),
    ] = None
    """
    Name of the carrier.
    """

    tracking_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="trackingId"),
        pydantic.Field(alias="trackingId", description="Tracking Id of shipment."),
    ] = None
    """
    Tracking Id of shipment.
    """

    tracking_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="trackingUrl"),
        pydantic.Field(alias="trackingUrl", description="Url where shipment can be tracked."),
    ] = None
    """
    Url where shipment can be tracked.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
