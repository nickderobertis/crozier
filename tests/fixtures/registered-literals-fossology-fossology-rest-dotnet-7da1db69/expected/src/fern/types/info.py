

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .info_type import InfoType


class Info(UniversalBaseModel):
    code: typing.Optional[int] = pydantic.Field(default=None)
    """
    HTTP status code
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Message in the info
    """

    type: typing.Optional[InfoType] = pydantic.Field(default=None)
    """
    Denotes if info was created on error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
