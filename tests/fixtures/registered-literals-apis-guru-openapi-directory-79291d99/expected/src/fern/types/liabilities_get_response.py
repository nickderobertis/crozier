

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_base import AccountBase
from .item import Item
from .liabilities_object import LiabilitiesObject
from .request_id import RequestId


class LiabilitiesGetResponse(UniversalBaseModel):
    """
    LiabilitiesGetResponse defines the response schema for `/liabilities/get`
    """

    accounts: typing.List[AccountBase] = pydantic.Field()
    """
    An array of accounts associated with the Item
    """

    item: Item
    liabilities: LiabilitiesObject
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
