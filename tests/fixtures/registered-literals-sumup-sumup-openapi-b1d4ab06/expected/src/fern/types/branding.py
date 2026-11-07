

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Branding(UniversalBaseModel):
    """
    Settings used to apply the Merchant's branding to email receipts, invoices, checkouts, and other products.
    """

    footer_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Footer text rendered on receipts and other customer-facing products.
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    An icon for the merchant. Must be square.
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    A logo for the merchant that will be used in place of the icon and without the merchant's name next to it if there's sufficient space.
    """

    hero: typing.Optional[str] = pydantic.Field(default=None)
    """
    Data-URL encoded hero image for the merchant business.
    """

    primary_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    A hex color value representing the primary branding color of this merchant (your brand color).
    """

    primary_color_fg: typing.Optional[str] = pydantic.Field(default=None)
    """
    A hex color value representing the color of the text displayed on branding color of this merchant.
    """

    secondary_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    A hex color value representing the secondary branding color of this merchant (accent color used for buttons).
    """

    secondary_color_fg: typing.Optional[str] = pydantic.Field(default=None)
    """
    A hex color value representing the color of the text displayed on secondary branding color of this merchant.
    """

    background_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    A hex color value representing the preferred background color of this merchant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
