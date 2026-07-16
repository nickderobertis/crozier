

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class ProcessingFee(UniversalBaseModel):
    """
    Represents the Square processing fee.
    """

    amount_money: typing.Optional[Money] = None
    effective_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the fee takes effect, in RFC 3339 format.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of fee assessed or adjusted. The fee type can be `INITIAL` or `ADJUSTMENT`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
