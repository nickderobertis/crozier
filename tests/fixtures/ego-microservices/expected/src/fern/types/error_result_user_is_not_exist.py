

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_is_not_exist import UserIsNotExist


class ErrorResultUserIsNotExist(UniversalBaseModel):
    """
    ErrorResult(*, message: str, data: ~TData = None)
    """

    message: str
    data: UserIsNotExist

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
