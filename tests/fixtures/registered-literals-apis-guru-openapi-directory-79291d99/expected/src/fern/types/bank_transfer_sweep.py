

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BankTransferSweep(UniversalBaseModel):
    """
    BankTransferSweep describes a sweep transfer.
    """

    amount: str = pydantic.Field()
    """
    The amount of the sweep.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The datetime when the sweep occurred, in RFC 3339 format.
    """

    id: str = pydantic.Field()
    """
    Identifier of the sweep.
    """

    iso_currency_code: str = pydantic.Field()
    """
    The currency of the sweep, e.g. "USD".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
