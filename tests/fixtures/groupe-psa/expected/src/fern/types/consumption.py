

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Consumption(UniversalBaseModel):
    """
    Vehicle consumption related to a specific type of energy. Expressed in cl for fuel energy type or in Wh for eletric one.
    """

    consumption: float = pydantic.Field()
    """
    Consumption value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
