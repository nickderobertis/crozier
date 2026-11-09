

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_base import AccountBase
from .holding import Holding
from .item import Item
from .request_id import RequestId
from .security import Security


class InvestmentsHoldingsGetResponse(UniversalBaseModel):
    """
    InvestmentsHoldingsGetResponse defines the response schema for `/investments/holdings/get`
    """

    accounts: typing.List[AccountBase] = pydantic.Field()
    """
    The accounts associated with the Item
    """

    holdings: typing.List[Holding] = pydantic.Field()
    """
    The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the `securities` field. 
    """

    item: Item
    request_id: RequestId
    securities: typing.List[Security] = pydantic.Field()
    """
    Objects describing the securities held in the accounts associated with the Item. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
