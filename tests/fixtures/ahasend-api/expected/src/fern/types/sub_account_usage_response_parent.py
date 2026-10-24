

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubAccountUsageResponseParent(UniversalBaseModel):
    account_id: str = pydantic.Field()
    """
    Account ID for this usage bucket
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Sub account name when this bucket is for a sub account
    """

    reception_count: int = pydantic.Field()
    """
    Number of received messages in the billing period
    """

    allocated_cost: float = pydantic.Field()
    """
    Proportional allocated cost for this usage bucket
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
