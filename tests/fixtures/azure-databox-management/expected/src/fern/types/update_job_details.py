

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contact_details import ContactDetails
from .shipping_address import ShippingAddress


class UpdateJobDetails(UniversalBaseModel):
    """
    Job details for update.
    """

    contact_details: typing_extensions.Annotated[
        typing.Optional[ContactDetails],
        FieldMetadata(alias="contactDetails"),
        pydantic.Field(alias="contactDetails", description="Contact details for notification and shipping."),
    ] = None
    """
    Contact details for notification and shipping.
    """

    shipping_address: typing_extensions.Annotated[
        typing.Optional[ShippingAddress],
        FieldMetadata(alias="shippingAddress"),
        pydantic.Field(alias="shippingAddress", description="Shipping address of the customer."),
    ] = None
    """
    Shipping address of the customer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
