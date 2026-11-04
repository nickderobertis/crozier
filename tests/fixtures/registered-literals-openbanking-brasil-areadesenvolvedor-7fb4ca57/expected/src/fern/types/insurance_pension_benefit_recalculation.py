

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .insurance_pension_benefit_recalculation_criterias_item import InsurancePensionBenefitRecalculationCriteriasItem
from .insurance_pension_benefit_recalculation_update_indexes_item import (
    InsurancePensionBenefitRecalculationUpdateIndexesItem,
)


class InsurancePensionBenefitRecalculation(UniversalBaseModel):
    criterias: typing.List[InsurancePensionBenefitRecalculationCriteriasItem]
    update_indexes: typing_extensions.Annotated[
        typing.List[InsurancePensionBenefitRecalculationUpdateIndexesItem],
        FieldMetadata(alias="updateIndexes"),
        pydantic.Field(alias="updateIndexes"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
