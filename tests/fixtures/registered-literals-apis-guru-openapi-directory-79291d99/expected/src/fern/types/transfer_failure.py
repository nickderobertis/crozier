

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferFailure(UniversalBaseModel):
    """
    The failure reason if the event type for a transfer is `"failed"` or `"returned"`. Null value otherwise.
    """

    ach_return_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ACH return code, e.g. `R01`.  A return code will be provided if and only if the transfer status is `returned`. For a full listing of ACH return codes, see [Transfer errors](https://plaid.com/docs/errors/transfer/#ach-return-codes).
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable description of the reason for the failure or reversal.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
