

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Error(UniversalBaseModel):
    detail: typing.Optional[str] = None
    error: int
    title: typing.Optional[str] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    unique uri for this error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
