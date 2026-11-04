

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .enum_target_audience import EnumTargetAudience
from .get_survival_pension_contract_data_modality import GetSurvivalPensionContractDataModality
from .get_survival_pension_contract_data_segment import GetSurvivalPensionContractDataSegment
from .get_survival_pension_contract_data_society import GetSurvivalPensionContractDataSociety
from .participant import Participant
from .survival_pension_costs import SurvivalPensionCosts
from .survival_pension_defferal_period import SurvivalPensionDefferalPeriod
from .survival_pension_grant_period_benefit import SurvivalPensionGrantPeriodBenefit
from .survival_pension_minimum_requirements import SurvivalPensionMinimumRequirements
from .survival_pension_type import SurvivalPensionType
from .terms_and_conditions import TermsAndConditions


class GetSurvivalPensionContractData(UniversalBaseModel):
    participant: Participant
    society: typing.Optional[GetSurvivalPensionContractDataSociety] = pydantic.Field(default=None)
    """
    Conjunto de informações relativas à seguradora do produto de open insurance
    """

    name: str = pydantic.Field()
    """
    Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade.
    """

    code: str = pydantic.Field()
    """
    Código único a ser definido pela sociedade.
    """

    segment: GetSurvivalPensionContractDataSegment = pydantic.Field()
    """
    Segmento do qual se trata o produto contratado
    1. Seguro de Pessoas
    2. Previdência
    """

    modality: typing.Optional[GetSurvivalPensionContractDataModality] = pydantic.Field(default=None)
    """
    1. Contribuição Variável;
    2. Benefício Definido.
    """

    additional_info: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="additionalInfo"),
        pydantic.Field(alias="additionalInfo", description="Campo aberto (possibilidade de incluir URL)"),
    ] = None
    """
    Campo aberto (possibilidade de incluir URL)
    """

    terms_and_conditions: typing_extensions.Annotated[
        typing.Optional[typing.List[TermsAndConditions]],
        FieldMetadata(alias="termsAndConditions"),
        pydantic.Field(alias="termsAndConditions"),
    ] = None
    type: SurvivalPensionType
    defferal_period: typing_extensions.Annotated[
        typing.Optional[SurvivalPensionDefferalPeriod],
        FieldMetadata(alias="defferalPeriod"),
        pydantic.Field(alias="defferalPeriod"),
    ] = None
    grant_period_benefit: typing_extensions.Annotated[
        typing.Optional[SurvivalPensionGrantPeriodBenefit],
        FieldMetadata(alias="grantPeriodBenefit"),
        pydantic.Field(alias="grantPeriodBenefit"),
    ] = None
    costs: typing.Optional[SurvivalPensionCosts] = None
    minimum_requirement: typing_extensions.Annotated[
        typing.Optional[SurvivalPensionMinimumRequirements],
        FieldMetadata(alias="minimumRequirement"),
        pydantic.Field(alias="minimumRequirement"),
    ] = None
    target_audience: typing_extensions.Annotated[
        EnumTargetAudience, FieldMetadata(alias="targetAudience"), pydantic.Field(alias="targetAudience")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
