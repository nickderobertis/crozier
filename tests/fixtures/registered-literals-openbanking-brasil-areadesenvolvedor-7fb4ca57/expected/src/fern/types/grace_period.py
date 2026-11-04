

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .enum_grace_period_unit import EnumGracePeriodUnit


class GracePeriod(UniversalBaseModel):
    amount: int = pydantic.Field()
    """
    Informar o prazo de carência
    """

    unit: EnumGracePeriodUnit

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
