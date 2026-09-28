

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class YandexDelegatedConfigResponse(UniversalBaseModel):
    available: bool = pydantic.Field()
    """
    True when delegated-representative access is provisioned on this deployment (both the shared representative login and the shared session are configured). When false, the delegated connect flow is unavailable and clients should fall back to cookie paste.
    """

    rep_login: str = pydantic.Field()
    """
    The shared representative Yandex login owners must add as a representative to their organization. Empty when not configured.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
