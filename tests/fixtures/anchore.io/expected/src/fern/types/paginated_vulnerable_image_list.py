

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .pagination_properties import PaginationProperties
from .vulnerable_image import VulnerableImage


class PaginatedVulnerableImageList(PaginationProperties):
    """
    Pagination wrapped list of images with vulnerabilties that match some filter
    """

    images: typing.Optional[typing.List[VulnerableImage]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
