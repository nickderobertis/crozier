

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_result_union_invalid_gender_invalid_birthday_date_data import (
    ErrorResultUnionInvalidGenderInvalidBirthdayDateData,
)


class ErrorResultUnionInvalidGenderInvalidBirthdayDate(UniversalBaseModel):
    """
    ErrorResult(*, message: str, data: ~TData = None)
    """

    message: str
    data: ErrorResultUnionInvalidGenderInvalidBirthdayDateData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
