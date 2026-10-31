

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .address_validation_properties_validation_status import AddressValidationPropertiesValidationStatus
from .shipping_address import ShippingAddress
from .validation_input_response import ValidationInputResponse


class AddressValidationProperties(ValidationInputResponse):
    """
    The address validation output.
    """

    alternate_addresses: typing_extensions.Annotated[
        typing.Optional[typing.List[ShippingAddress]],
        FieldMetadata(alias="alternateAddresses"),
        pydantic.Field(alias="alternateAddresses", description="List of alternate addresses."),
    ] = None
    """
    List of alternate addresses.
    """

    validation_status: typing_extensions.Annotated[
        typing.Optional[AddressValidationPropertiesValidationStatus],
        FieldMetadata(alias="validationStatus"),
        pydantic.Field(alias="validationStatus", description="The address validation status."),
    ] = None
    """
    The address validation status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
