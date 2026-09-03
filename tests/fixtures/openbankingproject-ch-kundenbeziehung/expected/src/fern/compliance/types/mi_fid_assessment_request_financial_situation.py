

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.monetary_amount import MonetaryAmount
from .mi_fid_assessment_request_financial_situation_liquidity_needs import (
    MiFidAssessmentRequestFinancialSituationLiquidityNeeds,
)


class MiFidAssessmentRequestFinancialSituation(UniversalBaseModel):
    net_wealth: typing_extensions.Annotated[
        typing.Optional[MonetaryAmount], FieldMetadata(alias="netWealth"), pydantic.Field(alias="netWealth")
    ] = None
    liquidity_needs: typing_extensions.Annotated[
        typing.Optional[MiFidAssessmentRequestFinancialSituationLiquidityNeeds],
        FieldMetadata(alias="liquidityNeeds"),
        pydantic.Field(alias="liquidityNeeds"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
