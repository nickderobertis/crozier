

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .subscribe_on_yourself import SubscribeOnYourself


class ErrorResultSubscribeOnYourself(UniversalBaseModel):
    """
    ErrorResult(*, message: str, data: ~TData = None)
    """

    message: str
    data: SubscribeOnYourself

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
