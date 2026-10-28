

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_error_model import TransactionErrorModel


class BulkTransactionModel(UniversalBaseModel):
    """
    Bulk Transaction Model.
    """

    received: int
    success: int
    skipped: int
    errors: typing.List[TransactionErrorModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
