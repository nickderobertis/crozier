

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .loyalty_account_mapping import LoyaltyAccountMapping


class SearchLoyaltyAccountsRequestLoyaltyAccountQuery(UniversalBaseModel):
    """
    The search criteria for the loyalty accounts.
    """

    customer_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The set of customer IDs to use in the loyalty account search.  
    
    This cannot be combined with `mappings`.  
    
    Max: 30 customer IDs
    """

    mappings: typing.Optional[typing.List[LoyaltyAccountMapping]] = pydantic.Field(default=None)
    """
    The set of mappings to use in the loyalty account search.  
    
    This cannot be combined with `customer_ids`.  
    
    Max: 30 mappings
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
