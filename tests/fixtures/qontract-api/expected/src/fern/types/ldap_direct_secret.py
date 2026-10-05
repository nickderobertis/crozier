

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LdapDirectSecret(UniversalBaseModel):
    """
    VaultSecret reference for FreeIPA direct LDAP access.

    The referenced Vault path must contain bind_dn and bind_password fields.
    No plain credentials are transmitted via API -- only Vault path references.

    Attributes:
        server_url: LDAP server URL (e.g., "ldap://freeipa.example.com")
        base_dn: Base DN for LDAP searches (e.g., "dc=example,dc=com")
        (inherited) secret_manager_url, path, field, version: Vault secret ref
    """

    base_dn: str = pydantic.Field()
    """
    Base DN for LDAP searches
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specific field within the secret
    """

    path: str = pydantic.Field()
    """
    Path to the secret
    """

    secret_manager_url: str = pydantic.Field()
    """
    Secret Manager URL
    """

    server_url: str = pydantic.Field()
    """
    LDAP server URL
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version of the secret
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
