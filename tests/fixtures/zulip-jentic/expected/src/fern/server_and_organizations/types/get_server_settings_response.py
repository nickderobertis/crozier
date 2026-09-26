

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_server_settings_response_authentication_methods import GetServerSettingsResponseAuthenticationMethods
from .get_server_settings_response_external_authentication_methods_item import (
    GetServerSettingsResponseExternalAuthenticationMethodsItem,
)


class GetServerSettingsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    authentication_methods: typing.Optional[GetServerSettingsResponseAuthenticationMethods] = pydantic.Field(
        default=None
    )
    """
    Each key-value pair in the object indicates whether the authentication
    method is enabled on this server.
    
    **Changes**: Deprecated in Zulip 2.1.0, in favor of the more expressive
    `external_authentication_methods`.
    """

    external_authentication_methods: typing.Optional[
        typing.List[GetServerSettingsResponseExternalAuthenticationMethodsItem]
    ] = pydantic.Field(default=None)
    """
    A list of dictionaries describing the available external
    authentication methods (E.g. Google, GitHub, or SAML)
    enabled for this organization.
    
    The list is sorted in the order in which these
    authentication methods should be displayed.
    
    **Changes**: New in Zulip 2.1.0.
    """

    zulip_feature_level: typing.Optional[int] = pydantic.Field(default=None)
    """
    An integer indicating what features are
    available on the server. The feature level increases monotonically;
    a value of N means the server supports all API features introduced
    before feature level N. This is designed to provide a simple way
    for client apps to decide whether the server supports a given
    feature or API change. See the [changelog](/api/changelog) for
    details on what each feature level means.
    
    **Changes**: New in Zulip 3.0 (feature level 1). We recommend using an
    implied value of 0 for Zulip servers that do not send this field.
    """

    zulip_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The server's version number. This is often a release version number,
    like `2.1.7`. But for a server running a [version from Git][git-release],
    it will be a Git reference to the commit, like `5.0-dev-1650-gc3fd37755f`.
    
    [git-release]: https://zulip.readthedocs.io/en/latest/overview/release-lifecycle.html#git-versions
    """

    zulip_merge_base: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `git merge-base` between `zulip_version` and official branches
    in the public
    [Zulip server and web app repository](https://github.com/zulip/zulip),
    in the same format as `zulip_version`. This will equal
    `zulip_version` if the server is not running a fork of the Zulip server.
    
    This will be `""` if unavailable.
    
    **Changes**: New in Zulip 5.0 (feature level 88).
    """

    push_notifications_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether mobile/push notifications are configured.
    """

    is_incompatible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the Zulip client that has sent a request to this endpoint is
    deemed incompatible with the server.
    """

    email_auth_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Setting for allowing users authenticate with an email-password
    combination.
    """

    require_email_format_usernames: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether all valid usernames for authentication to this
    organization will be email addresses. This is important
    for clients to know whether to do client side validation
    of email address format in a login prompt.
    
    This value will be false if the server has [LDAP
    authentication][ldap-auth] enabled with a username and
    password combination.
    
    [ldap-auth]: https://zulip.readthedocs.io/en/latest/production/authentication-methods.html#ldap-including-active-directory
    """

    realm_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    The organization's canonical URL. Alias of `realm_url`.
    
    **Changes**: Deprecated in Zulip 9.0 (feature level 257). The term
    "URI" is deprecated in [web standards](https://url.spec.whatwg.org/#goals).
    """

    realm_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The organization's canonical URL.
    
    **Changes**: New in Zulip 9.0 (feature level 257), replacing the
    deprecated `realm_uri`.
    """

    realm_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The organization's name (for display purposes).
    """

    realm_icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for the organization's logo formatted as a square image,
    used for identifying the organization in small locations in the
    mobile and desktop apps.
    """

    realm_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTML description of the organization, as configured by the [organization
    profile](/help/create-your-organization-profile).
    """

    realm_web_public_access_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the organization has enabled the creation of
    [web-public channels](/help/public-access-option) and
    at least one web-public channel on the server currently
    exists. Clients that support viewing content
    in web-public channels without an account can
    use this to determine whether to offer that
    feature on the login page for an organization.
    
    **Changes**: New in Zulip 5.0 (feature level 116).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
