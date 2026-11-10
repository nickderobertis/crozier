

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .recipient_bacs import RecipientBacs


class PaymentInitiationOptionalRestrictionBacs(RecipientBacs):
    """
    An optional object used to restrict the accounts used for payments. If provided, the end user will be able to send payments only from the specified bank account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
