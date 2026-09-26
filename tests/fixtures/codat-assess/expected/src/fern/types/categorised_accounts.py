

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .categorised_account import CategorisedAccount
from .paging_info import PagingInfo


class CategorisedAccounts(PagingInfo):
    results: typing.Optional[typing.List[CategorisedAccount]] = pydantic.Field(default=None)
    """
    A list confirmed and suggested account categories.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
