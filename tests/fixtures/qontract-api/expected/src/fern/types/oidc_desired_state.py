

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_type import AccessType


class OidcDesiredState(UniversalBaseModel):
    """
    Desired OIDC configuration for a single managed SSO client.

    Every optional field here is "unmanaged" when None, not "empty"/"false" -
    Keycloak's client-registration PUT merges by field, so an unmanaged field
    is never sent and never diffed for drift - Keycloak's own default applies
    on create, and an existing client's value is left untouched on update.
    Only an explicitly-set value (including an explicit empty list) is
    applied and compared. `access_type` and `direct_access_grants_enabled`
    are the documented exceptions: both always resolve to a concrete value
    (see their validators below), since Keycloak's own create-time defaults
    for these two - public access type, and enabled direct access grants -
    are insecure (verified against a live instance).

    Caution for every other optional field: setting a value and later
    removing it from the desired state does NOT revert it - it only stops
    managing it, freezing Keycloak at whatever was last pushed. To actually
    undo a change, push back the field's previous explicit value (or its
    Keycloak default) rather than deleting the key.
    """

    access_type: typing.Optional[AccessType] = pydantic.Field(default=None)
    """
    Keycloak client type/authentication requirement (confidential/public/bearer-only). Defaults to confidential when unset - Keycloak's own create-time default for an omitted access type is public, not confidential.
    """

    consent_required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, Keycloak shows a consent screen the first time a user authorizes this client, listing requested scopes.
    """

    default_client_scopes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Client scopes automatically included in every token issued to this client. Unmanaged if unset (see class docstring).
    """

    direct_access_grants_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enables the OAuth2 Resource Owner Password Credentials grant (client collects username/password itself, no browser redirect). Only appropriate for a trusted first-party client such as an internal CLI - never a browser-based or third-party client. Defaults to False when unset - Keycloak's own create-time default for an omitted value is True.
    """

    full_scope_allowed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this client is automatically granted every realm/client role, instead of only default_client_scopes/optional_client_scopes.
    """

    optional_client_scopes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Client scopes this client may request via the scope parameter but that aren't included by default. Unmanaged if unset (see class docstring).
    """

    post_logout_redirect_uris: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Allowed URIs Keycloak may redirect back to after an RP-initiated logout. Unmanaged if unset (see class docstring).
    """

    redirect_uris: typing.List[str] = pydantic.Field()
    """
    Allowed redirect URIs for the standard login flow. Required by Keycloak - a client without at least one cannot log in.
    """

    service_accounts_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enables the OAuth2 Client Credentials grant (the client authenticates as itself for machine-to-machine calls, no end user involved). Requires access_type=confidential.
    """

    web_origins: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Allowed CORS origins for browser JavaScript calling Keycloak's endpoints directly from this client. Unmanaged if unset (see class docstring).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
