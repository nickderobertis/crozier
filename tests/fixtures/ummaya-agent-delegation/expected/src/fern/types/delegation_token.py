

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delegation_token_aal_asserted import DelegationTokenAalAsserted
from .delegation_token_token_type import DelegationTokenTokenType


class DelegationToken(UniversalBaseModel):
    access_token: str = pydantic.Field()
    """
    JWT per RFC 9068. MUST carry `aal_asserted` claim.
    """

    token_type: DelegationTokenTokenType
    expires_in: int
    aal_asserted: DelegationTokenAalAsserted
    scope: typing.List[str]
    introspection_endpoint: str
    revocation_endpoint: str
    issuer: str
    audience: str
    dpa_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Non-null when any scope is PII-bound.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
