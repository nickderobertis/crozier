



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .age_adjustment import AgeAdjustment
    from .age_adjustment_criterias_item import AgeAdjustmentCriteriasItem
    from .cnpj_number import CnpjNumber
    from .coverage import Coverage
    from .coverage_attributes import CoverageAttributes
    from .coverage_attributes_indemnity_payment_frequencies_item import (
        CoverageAttributesIndemnityPaymentFrequenciesItem,
    )
    from .coverage_attributes_indemnity_payment_methods_item import CoverageAttributesIndemnityPaymentMethodsItem
    from .currency_code import CurrencyCode
    from .enum_additional import EnumAdditional
    from .enum_assistance_type import EnumAssistanceType
    from .enum_excluded_risks import EnumExcludedRisks
    from .enum_grace_period_unit import EnumGracePeriodUnit
    from .enum_insurance_pension_category import EnumInsurancePensionCategory
    from .enum_product_modality import EnumProductModality
    from .enum_risk_pension_coverage_type import EnumRiskPensionCoverageType
    from .enum_target_audience import EnumTargetAudience
    from .enum_term import EnumTerm
    from .get_risk_pension_contract_data import GetRiskPensionContractData
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
    from .get_risk_pension_contract_data_premium_payment_frequencies_item import (
        GetRiskPensionContractDataPremiumPaymentFrequenciesItem,
    )
    from .get_risk_pension_contract_data_premium_payment_payment_methods_item import (
        GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem,
    )
    from .get_risk_pension_contract_data_society import GetRiskPensionContractDataSociety
    from .get_survival_pension_contract_data import GetSurvivalPensionContractData
    from .get_survival_pension_contract_data_modality import GetSurvivalPensionContractDataModality
    from .get_survival_pension_contract_data_segment import GetSurvivalPensionContractDataSegment
    from .get_survival_pension_contract_data_society import GetSurvivalPensionContractDataSociety
    from .grace_period import GracePeriod
    from .insurance_pension_benefit_recalculation import InsurancePensionBenefitRecalculation
    from .insurance_pension_benefit_recalculation_criterias_item import (
        InsurancePensionBenefitRecalculationCriteriasItem,
    )
    from .insurance_pension_benefit_recalculation_update_indexes_item import (
        InsurancePensionBenefitRecalculationUpdateIndexesItem,
    )
    from .insurance_pension_coverage_deductible import InsurancePensionCoverageDeductible
    from .insurance_pension_coverage_differentiated_deductible import InsurancePensionCoverageDifferentiatedDeductible
    from .insurance_pension_enum_financial_regime import InsurancePensionEnumFinancialRegime
    from .insurance_pension_enum_indemnifiable_period_type import InsurancePensionEnumIndemnifiablePeriodType
    from .insurance_pension_enum_pmbac_remuneration import InsurancePensionEnumPmbacRemuneration
    from .insurance_pension_enum_pmbac_remuneration_update_indexes_item import (
        InsurancePensionEnumPmbacRemunerationUpdateIndexesItem,
    )
    from .insurance_pension_max_value import InsurancePensionMaxValue
    from .insurance_pension_min_value import InsurancePensionMinValue
    from .insurance_pension_reclaim import InsurancePensionReclaim
    from .insurance_pension_reclaim_table_item import InsurancePensionReclaimTableItem
    from .links import Links
    from .meta import Meta
    from .not_found_error_body import NotFoundErrorBody
    from .not_found_error_body_errors_item import NotFoundErrorBodyErrorsItem
    from .ok_response_risk_coverage_pension import OkResponseRiskCoveragePension
    from .ok_response_survival_coverage_pension import OkResponseSurvivalCoveragePension
    from .participant import Participant
    from .phase4meta import Phase4Meta
    from .risk_pension_minimum_requirement import RiskPensionMinimumRequirement
    from .risk_pension_minimum_requirement_contract_type import RiskPensionMinimumRequirementContractType
    from .survival_pension_costs import SurvivalPensionCosts
    from .survival_pension_defferal_period import SurvivalPensionDefferalPeriod
    from .survival_pension_defferal_period_premium_payment_methods_item import (
        SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem,
    )
    from .survival_pension_grace_period import SurvivalPensionGracePeriod
    from .survival_pension_grant_period_benefit import SurvivalPensionGrantPeriodBenefit
    from .survival_pension_grant_period_benefit_biometric_table_item import (
        SurvivalPensionGrantPeriodBenefitBiometricTableItem,
    )
    from .survival_pension_grant_period_benefit_income_modalities_item import (
        SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem,
    )
    from .survival_pension_investiment_fund import SurvivalPensionInvestimentFund
    from .survival_pension_investiment_fund_type_performance_fee import SurvivalPensionInvestimentFundTypePerformanceFee
    from .survival_pension_loading_antecipated import SurvivalPensionLoadingAntecipated
    from .survival_pension_loading_late import SurvivalPensionLoadingLate
    from .survival_pension_minimum_premium import SurvivalPensionMinimumPremium
    from .survival_pension_minimum_premium_periodicity import SurvivalPensionMinimumPremiumPeriodicity
    from .survival_pension_minimum_requirements import SurvivalPensionMinimumRequirements
    from .survival_pension_minimum_requirements_contract_type import SurvivalPensionMinimumRequirementsContractType
    from .survival_pension_type import SurvivalPensionType
    from .susep_process_number import SusepProcessNumber
    from .terms_and_conditions import TermsAndConditions
    from .update_index import UpdateIndex
_dynamic_imports: typing.Dict[str, str] = {
    "AgeAdjustment": ".age_adjustment",
    "AgeAdjustmentCriteriasItem": ".age_adjustment_criterias_item",
    "CnpjNumber": ".cnpj_number",
    "Coverage": ".coverage",
    "CoverageAttributes": ".coverage_attributes",
    "CoverageAttributesIndemnityPaymentFrequenciesItem": ".coverage_attributes_indemnity_payment_frequencies_item",
    "CoverageAttributesIndemnityPaymentMethodsItem": ".coverage_attributes_indemnity_payment_methods_item",
    "CurrencyCode": ".currency_code",
    "EnumAdditional": ".enum_additional",
    "EnumAssistanceType": ".enum_assistance_type",
    "EnumExcludedRisks": ".enum_excluded_risks",
    "EnumGracePeriodUnit": ".enum_grace_period_unit",
    "EnumInsurancePensionCategory": ".enum_insurance_pension_category",
    "EnumProductModality": ".enum_product_modality",
    "EnumRiskPensionCoverageType": ".enum_risk_pension_coverage_type",
    "EnumTargetAudience": ".enum_target_audience",
    "EnumTerm": ".enum_term",
    "GetRiskPensionContractData": ".get_risk_pension_contract_data",
    "GetRiskPensionContractDataIndemnityPaymentIncomesItem": ".get_risk_pension_contract_data_indemnity_payment_incomes_item",
    "GetRiskPensionContractDataIndemnityPaymentMethodsItem": ".get_risk_pension_contract_data_indemnity_payment_methods_item",
    "GetRiskPensionContractDataOtherGuaranteedValuesItem": ".get_risk_pension_contract_data_other_guaranteed_values_item",
    "GetRiskPensionContractDataPremiumPayment": ".get_risk_pension_contract_data_premium_payment",
    "GetRiskPensionContractDataPremiumPaymentFrequenciesItem": ".get_risk_pension_contract_data_premium_payment_frequencies_item",
    "GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem": ".get_risk_pension_contract_data_premium_payment_payment_methods_item",
    "GetRiskPensionContractDataSociety": ".get_risk_pension_contract_data_society",
    "GetSurvivalPensionContractData": ".get_survival_pension_contract_data",
    "GetSurvivalPensionContractDataModality": ".get_survival_pension_contract_data_modality",
    "GetSurvivalPensionContractDataSegment": ".get_survival_pension_contract_data_segment",
    "GetSurvivalPensionContractDataSociety": ".get_survival_pension_contract_data_society",
    "GracePeriod": ".grace_period",
    "InsurancePensionBenefitRecalculation": ".insurance_pension_benefit_recalculation",
    "InsurancePensionBenefitRecalculationCriteriasItem": ".insurance_pension_benefit_recalculation_criterias_item",
    "InsurancePensionBenefitRecalculationUpdateIndexesItem": ".insurance_pension_benefit_recalculation_update_indexes_item",
    "InsurancePensionCoverageDeductible": ".insurance_pension_coverage_deductible",
    "InsurancePensionCoverageDifferentiatedDeductible": ".insurance_pension_coverage_differentiated_deductible",
    "InsurancePensionEnumFinancialRegime": ".insurance_pension_enum_financial_regime",
    "InsurancePensionEnumIndemnifiablePeriodType": ".insurance_pension_enum_indemnifiable_period_type",
    "InsurancePensionEnumPmbacRemuneration": ".insurance_pension_enum_pmbac_remuneration",
    "InsurancePensionEnumPmbacRemunerationUpdateIndexesItem": ".insurance_pension_enum_pmbac_remuneration_update_indexes_item",
    "InsurancePensionMaxValue": ".insurance_pension_max_value",
    "InsurancePensionMinValue": ".insurance_pension_min_value",
    "InsurancePensionReclaim": ".insurance_pension_reclaim",
    "InsurancePensionReclaimTableItem": ".insurance_pension_reclaim_table_item",
    "Links": ".links",
    "Meta": ".meta",
    "NotFoundErrorBody": ".not_found_error_body",
    "NotFoundErrorBodyErrorsItem": ".not_found_error_body_errors_item",
    "OkResponseRiskCoveragePension": ".ok_response_risk_coverage_pension",
    "OkResponseSurvivalCoveragePension": ".ok_response_survival_coverage_pension",
    "Participant": ".participant",
    "Phase4Meta": ".phase4meta",
    "RiskPensionMinimumRequirement": ".risk_pension_minimum_requirement",
    "RiskPensionMinimumRequirementContractType": ".risk_pension_minimum_requirement_contract_type",
    "SurvivalPensionCosts": ".survival_pension_costs",
    "SurvivalPensionDefferalPeriod": ".survival_pension_defferal_period",
    "SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem": ".survival_pension_defferal_period_premium_payment_methods_item",
    "SurvivalPensionGracePeriod": ".survival_pension_grace_period",
    "SurvivalPensionGrantPeriodBenefit": ".survival_pension_grant_period_benefit",
    "SurvivalPensionGrantPeriodBenefitBiometricTableItem": ".survival_pension_grant_period_benefit_biometric_table_item",
    "SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem": ".survival_pension_grant_period_benefit_income_modalities_item",
    "SurvivalPensionInvestimentFund": ".survival_pension_investiment_fund",
    "SurvivalPensionInvestimentFundTypePerformanceFee": ".survival_pension_investiment_fund_type_performance_fee",
    "SurvivalPensionLoadingAntecipated": ".survival_pension_loading_antecipated",
    "SurvivalPensionLoadingLate": ".survival_pension_loading_late",
    "SurvivalPensionMinimumPremium": ".survival_pension_minimum_premium",
    "SurvivalPensionMinimumPremiumPeriodicity": ".survival_pension_minimum_premium_periodicity",
    "SurvivalPensionMinimumRequirements": ".survival_pension_minimum_requirements",
    "SurvivalPensionMinimumRequirementsContractType": ".survival_pension_minimum_requirements_contract_type",
    "SurvivalPensionType": ".survival_pension_type",
    "SusepProcessNumber": ".susep_process_number",
    "TermsAndConditions": ".terms_and_conditions",
    "UpdateIndex": ".update_index",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AgeAdjustment",
    "AgeAdjustmentCriteriasItem",
    "CnpjNumber",
    "Coverage",
    "CoverageAttributes",
    "CoverageAttributesIndemnityPaymentFrequenciesItem",
    "CoverageAttributesIndemnityPaymentMethodsItem",
    "CurrencyCode",
    "EnumAdditional",
    "EnumAssistanceType",
    "EnumExcludedRisks",
    "EnumGracePeriodUnit",
    "EnumInsurancePensionCategory",
    "EnumProductModality",
    "EnumRiskPensionCoverageType",
    "EnumTargetAudience",
    "EnumTerm",
    "GetRiskPensionContractData",
    "GetRiskPensionContractDataIndemnityPaymentIncomesItem",
    "GetRiskPensionContractDataIndemnityPaymentMethodsItem",
    "GetRiskPensionContractDataOtherGuaranteedValuesItem",
    "GetRiskPensionContractDataPremiumPayment",
    "GetRiskPensionContractDataPremiumPaymentFrequenciesItem",
    "GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem",
    "GetRiskPensionContractDataSociety",
    "GetSurvivalPensionContractData",
    "GetSurvivalPensionContractDataModality",
    "GetSurvivalPensionContractDataSegment",
    "GetSurvivalPensionContractDataSociety",
    "GracePeriod",
    "InsurancePensionBenefitRecalculation",
    "InsurancePensionBenefitRecalculationCriteriasItem",
    "InsurancePensionBenefitRecalculationUpdateIndexesItem",
    "InsurancePensionCoverageDeductible",
    "InsurancePensionCoverageDifferentiatedDeductible",
    "InsurancePensionEnumFinancialRegime",
    "InsurancePensionEnumIndemnifiablePeriodType",
    "InsurancePensionEnumPmbacRemuneration",
    "InsurancePensionEnumPmbacRemunerationUpdateIndexesItem",
    "InsurancePensionMaxValue",
    "InsurancePensionMinValue",
    "InsurancePensionReclaim",
    "InsurancePensionReclaimTableItem",
    "Links",
    "Meta",
    "NotFoundErrorBody",
    "NotFoundErrorBodyErrorsItem",
    "OkResponseRiskCoveragePension",
    "OkResponseSurvivalCoveragePension",
    "Participant",
    "Phase4Meta",
    "RiskPensionMinimumRequirement",
    "RiskPensionMinimumRequirementContractType",
    "SurvivalPensionCosts",
    "SurvivalPensionDefferalPeriod",
    "SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem",
    "SurvivalPensionGracePeriod",
    "SurvivalPensionGrantPeriodBenefit",
    "SurvivalPensionGrantPeriodBenefitBiometricTableItem",
    "SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem",
    "SurvivalPensionInvestimentFund",
    "SurvivalPensionInvestimentFundTypePerformanceFee",
    "SurvivalPensionLoadingAntecipated",
    "SurvivalPensionLoadingLate",
    "SurvivalPensionMinimumPremium",
    "SurvivalPensionMinimumPremiumPeriodicity",
    "SurvivalPensionMinimumRequirements",
    "SurvivalPensionMinimumRequirementsContractType",
    "SurvivalPensionType",
    "SusepProcessNumber",
    "TermsAndConditions",
    "UpdateIndex",
]
