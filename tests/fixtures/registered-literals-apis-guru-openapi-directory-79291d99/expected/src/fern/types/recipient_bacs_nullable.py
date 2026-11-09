

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .recipient_bacs import RecipientBacs


class RecipientBacsNullable(RecipientBacs):
    """
    An object containing a BACS account number and sort code. If an IBAN is not provided or if this recipient needs to accept domestic GBP-denominated payments, BACS data is required.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
