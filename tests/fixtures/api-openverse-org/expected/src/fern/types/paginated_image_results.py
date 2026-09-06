

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image import Image


class PaginatedImageResults(UniversalBaseModel):
    result_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of results
    """

    page_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of pages
    """

    page_size: typing.Optional[int] = None
    page: typing.Optional[int] = None
    results: typing.Optional[typing.List[Image]] = None
    warnings: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
