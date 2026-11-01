

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .sku_availability_validation_request_device_type import SkuAvailabilityValidationRequestDeviceType
from .sku_availability_validation_request_transfer_type import SkuAvailabilityValidationRequestTransferType
from .validation_input_request import ValidationInputRequest


class SkuAvailabilityValidationRequest(ValidationInputRequest):
    """
    Request to validate sku availability.
    """

    country: str = pydantic.Field()
    """
    ISO country code. Country for hardware shipment. For codes check: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements
    """

    device_type: typing_extensions.Annotated[
        SkuAvailabilityValidationRequestDeviceType,
        FieldMetadata(alias="deviceType"),
        pydantic.Field(alias="deviceType", description="Device type to be used for the job."),
    ]
    """
    Device type to be used for the job.
    """

    location: str = pydantic.Field()
    """
    Location for data transfer. For locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version=2018-01-01
    """

    transfer_type: typing_extensions.Annotated[
        SkuAvailabilityValidationRequestTransferType,
        FieldMetadata(alias="transferType"),
        pydantic.Field(alias="transferType", description="Type of the transfer."),
    ]
    """
    Type of the transfer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
