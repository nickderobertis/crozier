

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .component import Component
from .pagination_details import PaginationDetails


class PaginatedComponentResponse(PaginationDetails):
    """
    A paginated response containing TEA Components
    """

    results: typing.List[Component]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
