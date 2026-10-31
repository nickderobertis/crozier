

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transport_availability_request_sku_name import TransportAvailabilityRequestSkuName


class TransportAvailabilityRequest(UniversalBaseModel):
    """
    Request body to get the transport availability for given sku.
    """

    sku_name: typing_extensions.Annotated[
        typing.Optional[TransportAvailabilityRequestSkuName],
        FieldMetadata(alias="skuName"),
        pydantic.Field(alias="skuName", description="Type of the device."),
    ] = None
    """
    Type of the device.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
