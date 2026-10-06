

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DownloadDtoOut(UniversalBaseModel):
    hash: str
    name: str
    path: str
    url: str
    failed: int
    retries: int
    completed: bool
    creation_date: dt.datetime
    completion_date: typing.Optional[dt.datetime] = None
    headers: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
