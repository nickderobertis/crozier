

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaginationInfo(UniversalBaseModel):
    has_more: bool = pydantic.Field()
    """
    Whether more items exist after the last item of this page
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pass as `after` to fetch the next page
    """

    previous_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pass as `before` to fetch the previous page; absent on a `before` page when the start of the list has been reached
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
