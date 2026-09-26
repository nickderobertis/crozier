

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Payable(UniversalBaseModel):
    id: typing.Optional[str] = None
    type: typing.Optional[str] = None
    amount: typing.Optional[float] = None
    currency: typing.Optional[str] = None
    supplier: typing.Optional[typing.Dict[str, typing.Any]] = None
    status: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
