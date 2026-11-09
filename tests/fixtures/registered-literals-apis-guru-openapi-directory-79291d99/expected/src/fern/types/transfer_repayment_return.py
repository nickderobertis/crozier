

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferRepaymentReturn(UniversalBaseModel):
    """
    Represents a return on a Guaranteed ACH transfer that is included in the specified repayment.
    """

    amount: str = pydantic.Field()
    """
    The value of the returned transfer.
    """

    event_id: int = pydantic.Field()
    """
    The unique identifier of the corresponding `returned` transfer event.
    """

    iso_currency_code: str = pydantic.Field()
    """
    The currency of the repayment, e.g. "USD".
    """

    transfer_id: str = pydantic.Field()
    """
    The unique identifier of the guaranteed transfer that was returned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
