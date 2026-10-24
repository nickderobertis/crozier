

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .domain import Domain
from .paginated_domains_response_object import PaginatedDomainsResponseObject
from .pagination_info import PaginationInfo


class PaginatedDomainsResponse(UniversalBaseModel):
    object: PaginatedDomainsResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[Domain] = pydantic.Field()
    """
    Array of domains
    """

    pagination: PaginationInfo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
