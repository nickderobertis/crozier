

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paginated_sub_accounts_response_object import PaginatedSubAccountsResponseObject
from .pagination_info import PaginationInfo
from .sub_account import SubAccount


class PaginatedSubAccountsResponse(UniversalBaseModel):
    object: PaginatedSubAccountsResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[SubAccount] = pydantic.Field()
    """
    Array of sub accounts
    """

    pagination: PaginationInfo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
