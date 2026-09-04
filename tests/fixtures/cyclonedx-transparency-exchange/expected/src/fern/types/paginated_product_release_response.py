

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .pagination_details import PaginationDetails
from .product_release import ProductRelease


class PaginatedProductReleaseResponse(PaginationDetails):
    """
    A paginated response containing TEA Product Releases
    """

    results: typing.List[ProductRelease]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
