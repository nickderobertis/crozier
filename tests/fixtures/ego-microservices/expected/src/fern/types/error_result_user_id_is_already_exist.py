

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_id_is_already_exist import UserIdIsAlreadyExist


class ErrorResultUserIdIsAlreadyExist(UniversalBaseModel):
    """
    ErrorResult(*, message: str, data: ~TData = None)
    """

    message: str
    data: UserIdIsAlreadyExist

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
