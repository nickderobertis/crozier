

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1Alpha1ResourceMetadata(UniversalBaseModel):
    uid: typing.Optional[str] = None
    name: str
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None
    annotations: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
