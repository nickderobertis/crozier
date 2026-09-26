

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaginationFilter(UniversalBaseModel):
    """
    Pagination options to navigate through the list of results.
    """

    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    The page number to paginate to in the collection. If no value is specified it defaults to the first page.
    """

    per_page: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number items to display on a page. Defaults to 100. Maximum is 3000, if the value is greater that the maximum allowed it will fallback to 3000.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
