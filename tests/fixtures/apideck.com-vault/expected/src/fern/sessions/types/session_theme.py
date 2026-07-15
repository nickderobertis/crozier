

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SessionTheme(UniversalBaseModel):
    """
    Theming options to change the look and feel of Vault.
    """

    favicon: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to the favicon to use for Vault.
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to the logo to use for Vault.
    """

    primary_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The primary color to use for Vault.
    """

    privacy_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to the privacy policy that will be shown in the sidebar.
    """

    sidepanel_background_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The background color to use for the sidebar.
    """

    sidepanel_text_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text color to use for the sidebar.
    """

    terms_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to the terms and conditions that will be shown in the sidebar.
    """

    vault_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name that will be shown in the sidebar.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
