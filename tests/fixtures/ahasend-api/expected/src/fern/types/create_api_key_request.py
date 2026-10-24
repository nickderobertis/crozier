

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateApiKeyRequest(UniversalBaseModel):
    label: str = pydantic.Field()
    """
    Human-readable label for the API key; must not be empty
    """

    scopes: typing.List[str] = pydantic.Field()
    """
    Array of scope strings to grant to this API key
    """

    ip_allow_list: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Optional list of source IPs allowed to authenticate with this key. Each entry is a CIDR block (e.g. `203.0.113.0/24`) or a bare IPv4/IPv6 address (stored as a `/32` or `/128`). Entries are canonicalized (host bits are masked) and de-duplicated. The allow-all prefixes `0.0.0.0/0` and `::/0` are rejected, and at most 100 entries are allowed after de-duplication. Omit the field or pass an empty array to leave the key usable from any IP.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
