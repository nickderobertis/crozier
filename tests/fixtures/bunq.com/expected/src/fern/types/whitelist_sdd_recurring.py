

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class WhitelistSddRecurring(UniversalBaseModel):
    maximum_amount_per_month: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The maximum amount of money that is allowed to be deducted based on the whitelist.
    """

    monetary_account_paying_id: int = pydantic.Field()
    """
    ID of the monetary account of which you want to pay from.
    """

    request_id: int = pydantic.Field()
    """
    ID of the request for which you want to whitelist the originating SDD.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
