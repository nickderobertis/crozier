

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_key import ApiKey
from .paginated_api_keys_response_object import PaginatedApiKeysResponseObject
from .pagination_info import PaginationInfo


class PaginatedApiKeysResponse(UniversalBaseModel):
    object: PaginatedApiKeysResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[ApiKey] = pydantic.Field()
    """
    Array of API keys
    """

    pagination: PaginationInfo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
