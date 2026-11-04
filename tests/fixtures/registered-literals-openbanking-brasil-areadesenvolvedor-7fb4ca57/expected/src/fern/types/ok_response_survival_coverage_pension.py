

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_survival_pension_contract_data import GetSurvivalPensionContractData
from .links import Links
from .phase4meta import Phase4Meta


class OkResponseSurvivalCoveragePension(UniversalBaseModel):
    data: typing.List[GetSurvivalPensionContractData]
    links: Links
    meta: Phase4Meta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
