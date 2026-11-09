

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NotehubRouteSummary(UniversalBaseModel):
    disabled: typing.Optional[bool] = None
    label: typing.Optional[str] = None
    modified: typing.Optional[dt.datetime] = None
    type: typing.Optional[str] = None
    uid: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
