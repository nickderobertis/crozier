

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sub_account_usage_breakdown import SubAccountUsageBreakdown
from .sub_account_usage_response_allocation_method import SubAccountUsageResponseAllocationMethod
from .sub_account_usage_response_billing_period import SubAccountUsageResponseBillingPeriod
from .sub_account_usage_response_parent import SubAccountUsageResponseParent
from .sub_account_usage_response_sub_accounts_item import SubAccountUsageResponseSubAccountsItem


class SubAccountUsageResponse(UniversalBaseModel):
    billing_period: SubAccountUsageResponseBillingPeriod
    currency: str = pydantic.Field()
    """
    Currency code used for cost allocation
    """

    allocation_method: SubAccountUsageResponseAllocationMethod = pydantic.Field()
    """
    Method used to allocate the pooled parent invoice cost
    """

    allocation_note: str = pydantic.Field()
    """
    Disclaimer explaining that allocated cost is not standalone sub-account pricing
    """

    parent: SubAccountUsageResponseParent
    sub_accounts: typing.List[SubAccountUsageResponseSubAccountsItem] = pydantic.Field()
    """
    Per-sub-account usage and allocated cost
    """

    removed_sub_accounts: SubAccountUsageBreakdown = pydantic.Field()
    """
    Aggregated usage from sub accounts deleted during the period; still billed to the parent and not identified individually
    """

    total: SubAccountUsageBreakdown

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
