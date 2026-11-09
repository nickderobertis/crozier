

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .technical_user_credentials_dto_grant_type import TechnicalUserCredentialsDtoGrantType


class TechnicalUserCredentialsDto(UniversalBaseModel):
    client_id: str = pydantic.Field()
    """
    The client identifier for the M2M client
    """

    client_secret: str = pydantic.Field()
    """
    The client secret for authentication
    """

    grant_type: TechnicalUserCredentialsDtoGrantType = pydantic.Field()
    """
    The OAuth2 grant type (must be 'client_credentials')
    """

    client_secret_expires_at: int = pydantic.Field()
    """
    Time at which the client secret will expire, as the number of seconds from 1970-01-01T00:00:00Z (Unix epoch), or 0 if it will not expire. Per RFC 7591 Section 3.2.1, this field is required when a client_secret is issued. 
    """

    roles: typing.List[str] = pydantic.Field()
    """
    The roles assigned to the M2M client
    """

    client_id_issued_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time at which the client identifier was issued, as the number of seconds from 1970-01-01T00:00:00Z (Unix epoch) per RFC 7591 Section 3.2.1. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
