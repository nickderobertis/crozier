

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_category import ProviderCategory
from .provider_type import ProviderType


class Provider(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the provider, lazily created by the database manager.
    """

    name: str = pydantic.Field()
    """
    The name of the provider
    """

    provider_type: ProviderType = pydantic.Field()
    """
    The type of the provider
    """

    provider_category: ProviderCategory = pydantic.Field()
    """
    The category of the provider (base or byok)
    """

    api_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    API key or secret key used for requests to the provider.
    """

    base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base URL for the provider.
    """

    access_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Access key used for requests to the provider.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    Region used for requests to the provider.
    """

    api_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    API version used for requests to the provider.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last update timestamp of the provider.
    """

    last_synced: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time models were synced for this provider.
    """

    api_key_enc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Encrypted API key as Secret object
    """

    access_key_enc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Encrypted access key as Secret object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
