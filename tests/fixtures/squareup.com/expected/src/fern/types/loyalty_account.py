

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .loyalty_account_expiring_point_deadline import LoyaltyAccountExpiringPointDeadline
from .loyalty_account_mapping import LoyaltyAccountMapping


class LoyaltyAccount(UniversalBaseModel):
    """
    Describes a loyalty account. For more information, see
    [Manage Loyalty Accounts Using the Loyalty API](https://developer.squareup.com/docs/loyalty-api/overview).
    """

    balance: typing.Optional[int] = pydantic.Field(default=None)
    """
    The available point balance in the loyalty account. If points are scheduled to expire, they are listed in the `expiring_point_deadlines` field.
    
    Your application should be able to handle loyalty accounts that have a negative point balance (`balance` is less than 0). This might occur if a seller makes a manual adjustment or as a result of a refund or exchange.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the loyalty account was created, in RFC 3339 format.
    """

    customer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) that is associated with the account.
    """

    enrolled_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when enrollment occurred, in RFC 3339 format.
    """

    expiring_point_deadlines: typing.Optional[typing.List[LoyaltyAccountExpiringPointDeadline]] = pydantic.Field(
        default=None
    )
    """
    The schedule for when points expire in the loyalty account balance. This field is present only if the account has points that are scheduled to expire. 
    
    The total number of points in this field equals the number of points in the `balance` field.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the loyalty account.
    """

    lifetime_points: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total points accrued during the lifetime of the account.
    """

    mapping: typing.Optional[LoyaltyAccountMapping] = None
    program_id: str = pydantic.Field()
    """
    The Square-assigned ID of the [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram) to which the account belongs.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the loyalty account was last updated, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
