

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .image_with_packages import ImageWithPackages
from .pagination_properties import PaginationProperties


class PaginatedImageList(PaginationProperties):
    """
    Pagination wrapped list of images that match some filter
    """

    images: typing.Optional[typing.List[ImageWithPackages]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
