

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recurring_transfer import RecurringTransfer
from .request_id import RequestId


class TransferRecurringListResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/recurring/list`
    """

    recurring_transfers: typing.List[RecurringTransfer]
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
