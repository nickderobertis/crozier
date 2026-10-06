

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Article(UniversalBaseModel):
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    image: typing.Optional[str] = None
    price: typing.Optional[typing.Any] = None
    quantity: typing.Optional[typing.Any] = None
    brand: typing.Optional[str] = None
    rating: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
