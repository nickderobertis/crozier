

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Address(UniversalBaseModel):
    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The city.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country as an ISO 3166-1 alpha-2 country code.
    """

    extra: typing.Optional[str] = pydantic.Field(default=None)
    """
    The apartment, building or other extra information for addresses.
    """

    house_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The house number.
    """

    is_user_address_updated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    To show whether user created or updated her address for app event listing.
    """

    mailbox_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name on the mailbox (only used for Postal addresses).
    """

    po_box: typing.Optional[str] = pydantic.Field(default=None)
    """
    The PO box.
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal code.
    """

    province: typing.Optional[str] = pydantic.Field(default=None)
    """
    The province according to local standard.
    """

    street: typing.Optional[str] = pydantic.Field(default=None)
    """
    The street.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
