

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_health_datastore import OtoroshiHealthDatastore
from .otoroshi_health_otoroshi import OtoroshiHealthOtoroshi


class OtoroshiHealth(UniversalBaseModel):
    """
    The structure that represent current Otoroshi health
    """

    datastore: OtoroshiHealthDatastore
    otoroshi: OtoroshiHealthOtoroshi

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
