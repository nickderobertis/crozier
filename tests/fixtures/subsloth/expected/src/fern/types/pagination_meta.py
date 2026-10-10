

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaginationMeta(UniversalBaseModel):
    """
    Pagination metadata with current page, per-page count, total items, and total pages.
    """

    page: typing.Optional[int] = None
    per_page: typing.Optional[int] = None
    total: typing.Optional[int] = None
    total_pages: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
