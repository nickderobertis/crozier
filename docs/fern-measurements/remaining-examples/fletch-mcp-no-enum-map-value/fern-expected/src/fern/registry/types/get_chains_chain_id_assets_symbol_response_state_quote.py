

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetChainsChainIdAssetsSymbolResponseStateQuote(UniversalBaseModel):
    bid: typing.Optional[float] = None
    ask: typing.Optional[float] = None
    trading_halt: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="tradingHalt"), pydantic.Field(alias="tradingHalt")
    ] = None
    daily_volume: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dailyVolume"), pydantic.Field(alias="dailyVolume")
    ] = None
    at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
