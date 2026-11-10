

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RemovedTransaction(UniversalBaseModel):
    """
    A representation of a removed transaction
    """

    transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the removed transaction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
