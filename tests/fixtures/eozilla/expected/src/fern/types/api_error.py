

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApiError(UniversalBaseModel):
    """
    API error based on RFC 7807
    """

    type: str
    title: typing.Optional[str] = None
    status: typing.Optional[int] = None
    detail: typing.Optional[str] = None
    instance: typing.Optional[str] = None
    traceback: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
