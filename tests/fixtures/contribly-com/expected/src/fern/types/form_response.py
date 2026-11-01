

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FormResponse(UniversalBaseModel):
    contribution: typing.Optional[str] = None
    date: typing.Optional[dt.datetime] = None
    form: typing.Optional[str] = None
    id: typing.Optional[str] = None
    responses: typing.Optional[typing.Dict[str, str]] = None
    user: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
