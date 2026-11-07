

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RadRoute(UniversalBaseModel):
    client_id: typing.Optional[str] = None
    client_secret: typing.Optional[str] = None
    data_feed_key: typing.Optional[str] = None
    event_id: typing.Optional[int] = None
    fleets: typing.Optional[typing.List[str]] = None
    test_api: typing.Optional[bool] = None
    throttle_ms: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
