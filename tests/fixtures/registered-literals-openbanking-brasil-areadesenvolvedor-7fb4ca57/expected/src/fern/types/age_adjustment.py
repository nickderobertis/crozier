

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .age_adjustment_criterias_item import AgeAdjustmentCriteriasItem


class AgeAdjustment(UniversalBaseModel):
    criterias: typing.List[AgeAdjustmentCriteriasItem]
    frequency: int = pydantic.Field()
    """
    Período em anos, caso critério de reenquadramento após ou a cada período em anos.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
