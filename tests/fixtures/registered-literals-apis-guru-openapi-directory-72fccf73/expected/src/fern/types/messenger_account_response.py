

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessengerAccountResponse(UniversalBaseModel):
    access_token: str = pydantic.Field()
    """
    The provider access token
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

    provider: str = pydantic.Field()
    """
    The provider (will be `messenger`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
