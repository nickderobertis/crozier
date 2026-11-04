

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..image.types.image_data import ImageData
from .pagination_metadata import PaginationMetadata


class PaginatedImageResponse(UniversalBaseModel):
    """
    Paginated list of images
    """

    data: typing.Optional[typing.List[ImageData]] = None
    pagination: typing.Optional[PaginationMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
