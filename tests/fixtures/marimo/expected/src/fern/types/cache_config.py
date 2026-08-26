

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cache_config_store import CacheConfigStore
from .cache_config_verification import CacheConfigVerification


class CacheConfig(UniversalBaseModel):
    """
    Configuration for caching.

        `verification` is the signature-checking posture; `store` is the backing
        store, or a list of stores composed into a `TieredStore`.
    """

    store: typing.Optional[CacheConfigStore] = None
    verification: typing.Optional[CacheConfigVerification] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
