

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MeasurementUnitCustom(UniversalBaseModel):
    """
    The information needed to define a custom unit, provided by the seller.
    """

    abbreviation: str = pydantic.Field()
    """
    The abbreviation of the custom unit, such as "bsh" (bushel). This appears
    in the cart for the Point of Sale app, and in reports.
    """

    name: str = pydantic.Field()
    """
    The name of the custom unit, for example "bushel".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
