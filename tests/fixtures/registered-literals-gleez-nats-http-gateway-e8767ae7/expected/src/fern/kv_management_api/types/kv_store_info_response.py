

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class KvStoreInfoResponse(UniversalBaseModel):
    name: typing.Optional[str] = None
    values: typing.Optional[int] = None
    history: typing.Optional[float] = None
    ttl: typing.Optional[int] = None
    backing_store: typing.Optional[str] = None
    size: typing.Optional[int] = None
    compression: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
