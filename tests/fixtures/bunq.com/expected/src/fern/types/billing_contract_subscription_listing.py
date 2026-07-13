

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BillingContractSubscriptionListing(UniversalBaseModel):
    contract_date_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date until when the billing contract is valid.
    """

    contract_date_start: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date from when the billing contract is valid.
    """

    contract_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the billing contract.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the billing contract was made.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the billing contract.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subscription status.
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subscription substatus.
    """

    subscription_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subscription type of the user. Can be one of PERSON_SUPER_LIGHT_V1, PERSON_LIGHT_V1, PERSON_MORE_V1, PERSON_FREE_V1, PERSON_PREMIUM_V1, COMPANY_V1, or COMPANY_V2.
    """

    subscription_type_downgrade: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subscription type the user will have after a subscription downgrade. Will be null if downgrading is not possible.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the billing contract was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
