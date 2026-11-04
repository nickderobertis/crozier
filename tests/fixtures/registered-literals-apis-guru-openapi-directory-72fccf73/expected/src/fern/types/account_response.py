

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_response_provider import AccountResponseProvider


class AccountResponse(UniversalBaseModel):
    access_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The provider access token (only for `messenger`)
    """

    api_key: str = pydantic.Field()
    """
    The external api key for this account
    """

    applications: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The array of associated application ids
    """

    external_id: str = pydantic.Field()
    """
    The external identifier for this account
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account name
    """

    provider: AccountResponseProvider = pydantic.Field()
    """
    The provider (will be one of `messenger, viber_service_msg, whatsapp`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
