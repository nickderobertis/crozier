

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DecodeSwapstringResponse(UniversalBaseModel):
    qty_from: int
    qty_to: int
    from_asset: typing.Optional[str] = None
    to_asset: typing.Optional[str] = None
    expiry: int
    payment_hash: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
