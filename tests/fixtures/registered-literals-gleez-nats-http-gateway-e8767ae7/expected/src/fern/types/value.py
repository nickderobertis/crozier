

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .value_operation import ValueOperation


class Value(UniversalBaseModel):
    bucket: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    revision: typing.Optional[int] = None
    delta: typing.Optional[int] = None
    operation: typing.Optional[ValueOperation] = None
    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    value is base64 encoded
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
