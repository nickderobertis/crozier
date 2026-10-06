

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_data_is_not_correct import UserDataIsNotCorrect


class ErrorResultUserDataIsNotCorrect(UniversalBaseModel):
    """
    ErrorResult(*, message: str, data: ~ExcData = None)
    """

    message: str
    data: UserDataIsNotCorrect

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
