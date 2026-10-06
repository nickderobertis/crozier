

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .username_is_already_exist import UsernameIsAlreadyExist


class ErrorResultUsernameIsAlreadyExist(UniversalBaseModel):
    """
    ErrorResult(*, message: str, data: ~ExcData = None)
    """

    message: str
    data: UsernameIsAlreadyExist

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
