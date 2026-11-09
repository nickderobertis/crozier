

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .recurring_transfer import RecurringTransfer


class RecurringTransferNullable(RecurringTransfer):
    """
    Represents a recurring transfer within the Transfers API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
