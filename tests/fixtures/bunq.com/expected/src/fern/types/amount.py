

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Amount(UniversalBaseModel):
    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency of the amount. It is an ISO 4217 formatted currency code.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The amount formatted to two decimal places.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
