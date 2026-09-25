

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .coded_error_base_result import CodedErrorBaseResult


class CodedErrorBase(UniversalBaseModel):
    result: CodedErrorBaseResult
    msg: str
    code: str = pydantic.Field()
    """
    A string that identifies the error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
