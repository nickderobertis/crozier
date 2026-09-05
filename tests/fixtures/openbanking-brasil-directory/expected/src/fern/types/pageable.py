

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sort import Sort


class Pageable(UniversalBaseModel):
    number: typing.Optional[int] = pydantic.Field(default=None)
    """
    Page number
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Offset
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of the page
    """

    sort: typing.Optional[Sort] = None
    sorted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is the page sorted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
