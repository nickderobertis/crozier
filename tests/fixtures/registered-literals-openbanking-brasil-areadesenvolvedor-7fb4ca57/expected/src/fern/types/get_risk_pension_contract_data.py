

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .age_adjustment import AgeAdjustment
from .coverage import Coverage
from .enum_additional import EnumAdditional
from .enum_assistance_type import EnumAssistanceType
from .enum_insurance_pension_category import EnumInsurancePensionCategory
from .enum_product_modality import EnumProductModality
from .enum_target_audience import EnumTargetAudience
from .enum_term import EnumTerm
from .get_risk_pension_contract_data_indemnity_payment_incomes_item import (
    GetRiskPensionContractDataIndemnityPaymentIncomesItem,
)
from .get_risk_pension_contract_data_indemnity_payment_methods_item import (
    GetRiskPensionContractDataIndemnityPaymentMethodsItem,
)
from .get_risk_pension_contract_data_other_guaranteed_values_item import (
    GetRiskPensionContractDataOtherGuaranteedValuesItem,
)
from .get_risk_pension_contract_data_premium_payment import GetRiskPensionContractDataPremiumPayment
from .get_risk_pension_contract_data_society import GetRiskPensionContractDataSociety
from .grace_period import GracePeriod
from .insurance_pension_benefit_recalculation import InsurancePensionBenefitRecalculation
from .insurance_pension_enum_financial_regime import InsurancePensionEnumFinancialRegime
from .insurance_pension_enum_pmbac_remuneration import InsurancePensionEnumPmbacRemuneration
from .insurance_pension_reclaim import InsurancePensionReclaim
from .participant import Participant
from .risk_pension_minimum_requirement import RiskPensionMinimumRequirement
from .terms_and_conditions import TermsAndConditions


class GetRiskPensionContractData(UniversalBaseModel):
    participant: Participant
    society: GetRiskPensionContractDataSociety = pydantic.Field()
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

    category: typing.Optional[EnumInsurancePensionCategory] = None
    modality: typing.Optional[EnumProductModality] = None
    coverages: typing.List[Coverage]
    assistance_types: typing_extensions.Annotated[
        typing.List[EnumAssistanceType], FieldMetadata(alias="assistanceTypes"), pydantic.Field(alias="assistanceTypes")
    ]
    assistance_types_additional_infos: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="assistanceTypesAdditionalInfos"),
        pydantic.Field(
            alias="assistanceTypesAdditionalInfos",
            description="Lista a ser preenchida pelas participantes quando houver 'Outros' no campo 'Tipo de Assistência'.",
        ),
    ] = None
    """
    Lista a ser preenchida pelas participantes quando houver 'Outros' no campo 'Tipo de Assistência'.
    """

    additionals: typing.List[EnumAdditional]
    terms_and_conditions: typing_extensions.Annotated[
        typing.List[TermsAndConditions],
        FieldMetadata(alias="termsAndConditions"),
        pydantic.Field(alias="termsAndConditions"),
    ]
    global_capital: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="globalCapital"),
        pydantic.Field(
            alias="globalCapital",
            description="A considerar os seguintes domínios&#58;<br><ol><li>true</li><li>false</li></ol>",
        ),
    ] = None
    """
    A considerar os seguintes domínios&#58;<br><ol><li>true</li><li>false</li></ol>
    """

    terms: typing.List[EnumTerm]
    pmbac_remuneration: typing_extensions.Annotated[
        typing.Optional[InsurancePensionEnumPmbacRemuneration],
        FieldMetadata(alias="pmbacRemuneration"),
        pydantic.Field(alias="pmbacRemuneration"),
    ] = None
    benefit_recalculation: typing_extensions.Annotated[
        InsurancePensionBenefitRecalculation,
        FieldMetadata(alias="benefitRecalculation"),
        pydantic.Field(alias="benefitRecalculation"),
    ]
    age_adjustment: typing_extensions.Annotated[
        typing.Optional[AgeAdjustment], FieldMetadata(alias="ageAdjustment"), pydantic.Field(alias="ageAdjustment")
    ] = None
    financial_regime_contract_types: typing_extensions.Annotated[
        typing.Optional[typing.List[InsurancePensionEnumFinancialRegime]],
        FieldMetadata(alias="financialRegimeContractTypes"),
        pydantic.Field(alias="financialRegimeContractTypes"),
    ] = None
    reclaim: typing.Optional[InsurancePensionReclaim] = None
    other_guaranteed_values: typing_extensions.Annotated[
        typing.Optional[typing.List[GetRiskPensionContractDataOtherGuaranteedValuesItem]],
        FieldMetadata(alias="otherGuaranteedValues"),
        pydantic.Field(alias="otherGuaranteedValues"),
    ] = None
    allow_portability: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowPortability"),
        pydantic.Field(alias="allowPortability", description="<ol><li>true</li><li>false</li></ol>"),
    ] = None
    """
    <ol><li>true</li><li>false</li></ol>
    """

    portability_grace_time: typing_extensions.Annotated[
        typing.Optional[GracePeriod],
        FieldMetadata(alias="portabilityGraceTime"),
        pydantic.Field(alias="portabilityGraceTime"),
    ] = None
    indemnity_payment_methods: typing_extensions.Annotated[
        typing.Optional[typing.List[GetRiskPensionContractDataIndemnityPaymentMethodsItem]],
        FieldMetadata(alias="indemnityPaymentMethods"),
        pydantic.Field(alias="indemnityPaymentMethods"),
    ] = None
    indemnity_payment_incomes: typing_extensions.Annotated[
        typing.Optional[typing.List[GetRiskPensionContractDataIndemnityPaymentIncomesItem]],
        FieldMetadata(alias="indemnityPaymentIncomes"),
        pydantic.Field(alias="indemnityPaymentIncomes"),
    ] = None
    premium_payment: typing_extensions.Annotated[
        GetRiskPensionContractDataPremiumPayment,
        FieldMetadata(alias="premiumPayment"),
        pydantic.Field(alias="premiumPayment"),
    ]
    minimum_requirement: typing_extensions.Annotated[
        typing.Optional[RiskPensionMinimumRequirement],
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
