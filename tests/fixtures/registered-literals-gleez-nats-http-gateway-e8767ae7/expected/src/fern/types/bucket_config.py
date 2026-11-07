

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bucket_config_storage import BucketConfigStorage


class BucketConfig(UniversalBaseModel):
    description: typing.Optional[str] = None
    max_value_size: typing.Optional[int] = None
    history: typing.Optional[float] = None
    ttl: typing.Optional[int] = None
    max_bytes: typing.Optional[int] = None
    storage: typing.Optional[BucketConfigStorage] = None
    replicas: typing.Optional[float] = None
    compression: typing.Optional[bool] = None
    metadata: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
