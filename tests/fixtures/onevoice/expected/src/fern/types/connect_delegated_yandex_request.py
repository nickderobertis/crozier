

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectDelegatedYandexRequest(UniversalBaseModel):
    """
    Connect a Yandex organization via delegated-representative access. The owner supplies only their organization permalink (or a Maps/Sprav URL); no customer credential is captured. Exactly one of permalink or maps_url must be provided.
    """

    permalink: typing.Optional[str] = pydantic.Field(default=None)
    """
    Numeric Yandex organization permalink.
    """

    maps_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pasted Yandex Maps/Sprav URL to extract the permalink from.
    """

    business_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
