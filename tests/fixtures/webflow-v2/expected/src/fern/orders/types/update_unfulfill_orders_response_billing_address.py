

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_unfulfill_orders_response_billing_address_japan_type import (
    UpdateUnfulfillOrdersResponseBillingAddressJapanType,
)
from .update_unfulfill_orders_response_billing_address_type import UpdateUnfulfillOrdersResponseBillingAddressType


class UpdateUnfulfillOrdersResponseBillingAddress(UniversalBaseModel):
    """
    The billing address
    """

    type: typing.Optional[UpdateUnfulfillOrdersResponseBillingAddressType] = pydantic.Field(default=None)
    """
    The type of the order address (billing or shipping)
    """

    japan_type: typing_extensions.Annotated[
        typing.Optional[UpdateUnfulfillOrdersResponseBillingAddressJapanType],
        FieldMetadata(alias="japanType"),
        pydantic.Field(
            alias="japanType",
            description="Represents a Japan-only address format. This field will only appear on orders placed from Japan.",
        ),
    ] = None
    """
    Represents a Japan-only address format. This field will only appear on orders placed from Japan.
    """

    addressee: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name on the address
    """

    line1: typing.Optional[str] = pydantic.Field(default=None)
    """
    The first line of the address
    """

    line2: typing.Optional[str] = pydantic.Field(default=None)
    """
    The second line of the address
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The city of the address.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The state or province of the address
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the address
    """

    postal_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="postalCode"),
        pydantic.Field(alias="postalCode", description="The postal code of the address"),
    ] = None
    """
    The postal code of the address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
