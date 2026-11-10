

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaystubYtdDetails(UniversalBaseModel):
    """
    The amount of income earned year to date, as based on paystub data.
    """

    gross_earnings: typing.Optional[float] = pydantic.Field(default=None)
    """
    Year-to-date gross earnings.
    """

    net_earnings: typing.Optional[float] = pydantic.Field(default=None)
    """
    Year-to-date net (take home) earnings.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
