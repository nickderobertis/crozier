

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseRealmDefaultExternalAccountsValue(UniversalBaseModel):
    """
    `{site_name}`: Dictionary containing the details of the
    default external account provider with the name of the
    website as the key.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the external account provider
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text describing the external account.
    """

    hint: typing.Optional[str] = pydantic.Field(default=None)
    """
    The help text to be displayed for the
    custom profile field in user-facing
    settings UI for configuring custom
    profile fields for this account.
    """

    url_pattern: typing.Optional[str] = pydantic.Field(default=None)
    """
    The regex pattern of the URL of a profile page
    on the external site.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
