

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SavedFilter(UniversalBaseModel):
    content_types: typing.List[str]
    created: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    parameters: typing.Dict[str, typing.Any]
    shared: typing.Optional[bool] = None
    slug: str
    url: typing.Optional[str] = None
    user: typing.Optional[int] = None
    weight: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
