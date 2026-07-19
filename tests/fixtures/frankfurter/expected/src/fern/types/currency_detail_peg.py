

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CurrencyDetailPeg(UniversalBaseModel):
    """
    Peg metadata, present only for pegged currencies
    """

    base: typing.Optional[str] = None
    rate: typing.Optional[float] = None
    authority: typing.Optional[str] = None
    source: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
