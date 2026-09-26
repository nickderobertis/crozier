

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .self_managed_cart_response import SelfManagedCartResponse


class SelfManagedCartCalculateResponseBody(UniversalBaseModel):
    items: typing.Optional[typing.List[SelfManagedCartResponse]] = pydantic.Field(default=None)
    """
    One calculated cart per submitted cart, in the same order, with per-line-item tax rates and amounts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
