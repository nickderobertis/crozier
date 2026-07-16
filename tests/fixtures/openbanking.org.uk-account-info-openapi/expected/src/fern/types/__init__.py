



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account_id import AccountId
    from .active_or_historic_currency_code0 import ActiveOrHistoricCurrencyCode0
    from .active_or_historic_currency_code1 import ActiveOrHistoricCurrencyCode1
    from .address_line import AddressLine
    from .beneficiary_id import BeneficiaryId
    from .booking_date_time import BookingDateTime
    from .building_number import BuildingNumber
    from .country_code import CountryCode
    from .country_sub_division import CountrySubDivision
    from .creation_date_time import CreationDateTime
    from .date_time import DateTime
    from .debtor_reference import DebtorReference
    from .description0 import Description0
    from .description1 import Description1
    from .description2 import Description2
    from .description3 import Description3
    from .direct_debit_id import DirectDebitId
    from .email_address import EmailAddress
    from .end_date_time import EndDateTime
    from .file import File
    from .final_payment_date_time import FinalPaymentDateTime
    from .first_payment_date_time import FirstPaymentDateTime
    from .frequency0 import Frequency0
    from .frequency1 import Frequency1
    from .full_legal_name import FullLegalName
    from .identification0 import Identification0
    from .identification1 import Identification1
    from .identification2 import Identification2
    from .iso_date_time import IsoDateTime
    from .last_payment_date_time import LastPaymentDateTime
    from .links import Links
    from .mandate_identification import MandateIdentification
    from .maturity_date import MaturityDate
    from .meta import Meta
    from .model import Model
    from .name0 import Name0
    from .name1 import Name1
    from .name2 import Name2
    from .name3 import Name3
    from .name4 import Name4
    from .next_payment_date_time import NextPaymentDateTime
    from .nickname import Nickname
    from .number0 import Number0
    from .number1 import Number1
    from .number_of_payments import NumberOfPayments
    from .oauth_scope import OauthScope
    from .ob_account4 import ObAccount4
    from .ob_account4account_item import ObAccount4AccountItem
    from .ob_account4basic import ObAccount4Basic
    from .ob_account4detail import ObAccount4Detail
    from .ob_account4detail_account_item import ObAccount4DetailAccountItem
    from .ob_account6 import ObAccount6
    from .ob_account6account_item import ObAccount6AccountItem
    from .ob_account6basic import ObAccount6Basic
    from .ob_account6detail import ObAccount6Detail
    from .ob_account6detail_account_item import ObAccount6DetailAccountItem
    from .ob_account_status1code import ObAccountStatus1Code
    from .ob_active_currency_and_amount_simple_type import ObActiveCurrencyAndAmountSimpleType
    from .ob_active_or_historic_currency_and_amount0 import ObActiveOrHistoricCurrencyAndAmount0
    from .ob_active_or_historic_currency_and_amount1 import ObActiveOrHistoricCurrencyAndAmount1
    from .ob_active_or_historic_currency_and_amount10 import ObActiveOrHistoricCurrencyAndAmount10
    from .ob_active_or_historic_currency_and_amount11 import ObActiveOrHistoricCurrencyAndAmount11
    from .ob_active_or_historic_currency_and_amount2 import ObActiveOrHistoricCurrencyAndAmount2
    from .ob_active_or_historic_currency_and_amount3 import ObActiveOrHistoricCurrencyAndAmount3
    from .ob_active_or_historic_currency_and_amount4 import ObActiveOrHistoricCurrencyAndAmount4
    from .ob_active_or_historic_currency_and_amount5 import ObActiveOrHistoricCurrencyAndAmount5
    from .ob_active_or_historic_currency_and_amount6 import ObActiveOrHistoricCurrencyAndAmount6
    from .ob_active_or_historic_currency_and_amount7 import ObActiveOrHistoricCurrencyAndAmount7
    from .ob_active_or_historic_currency_and_amount8 import ObActiveOrHistoricCurrencyAndAmount8
    from .ob_active_or_historic_currency_and_amount9 import ObActiveOrHistoricCurrencyAndAmount9
    from .ob_address_type_code import ObAddressTypeCode
    from .ob_amount10 import ObAmount10
    from .ob_amount11 import ObAmount11
    from .ob_amount12 import ObAmount12
    from .ob_amount13 import ObAmount13
    from .ob_amount14 import ObAmount14
    from .ob_balance_type1code import ObBalanceType1Code
    from .ob_bank_transaction_code_structure1 import ObBankTransactionCodeStructure1
    from .ob_beneficiary5 import ObBeneficiary5
    from .ob_beneficiary5basic import ObBeneficiary5Basic
    from .ob_beneficiary5detail import ObBeneficiary5Detail
    from .ob_beneficiary_type1code import ObBeneficiaryType1Code
    from .ob_branch_and_financial_institution_identification50 import ObBranchAndFinancialInstitutionIdentification50
    from .ob_branch_and_financial_institution_identification51 import ObBranchAndFinancialInstitutionIdentification51
    from .ob_branch_and_financial_institution_identification60 import ObBranchAndFinancialInstitutionIdentification60
    from .ob_branch_and_financial_institution_identification61 import ObBranchAndFinancialInstitutionIdentification61
    from .ob_branch_and_financial_institution_identification62 import ObBranchAndFinancialInstitutionIdentification62
    from .ob_cash_account50 import ObCashAccount50
    from .ob_cash_account51 import ObCashAccount51
    from .ob_cash_account60 import ObCashAccount60
    from .ob_cash_account61 import ObCashAccount61
    from .ob_code_mnemonic import ObCodeMnemonic
    from .ob_credit_debit_code0 import ObCreditDebitCode0
    from .ob_credit_debit_code1 import ObCreditDebitCode1
    from .ob_credit_debit_code2 import ObCreditDebitCode2
    from .ob_currency_exchange5 import ObCurrencyExchange5
    from .ob_currency_exchange5instructed_amount import ObCurrencyExchange5InstructedAmount
    from .ob_entry_status1code import ObEntryStatus1Code
    from .ob_error1 import ObError1
    from .ob_error_response1 import ObErrorResponse1
    from .ob_external_account_identification4code import ObExternalAccountIdentification4Code
    from .ob_external_account_role1code import ObExternalAccountRole1Code
    from .ob_external_account_sub_type1code import ObExternalAccountSubType1Code
    from .ob_external_account_type1code import ObExternalAccountType1Code
    from .ob_external_direct_debit_status1code import ObExternalDirectDebitStatus1Code
    from .ob_external_financial_institution_identification4code import ObExternalFinancialInstitutionIdentification4Code
    from .ob_external_legal_structure_type1code import ObExternalLegalStructureType1Code
    from .ob_external_party_type1code import ObExternalPartyType1Code
    from .ob_external_schedule_type1code import ObExternalScheduleType1Code
    from .ob_external_standing_order_status1code import ObExternalStandingOrderStatus1Code
    from .ob_external_statement_amount_type1code import ObExternalStatementAmountType1Code
    from .ob_external_statement_benefit_type1code import ObExternalStatementBenefitType1Code
    from .ob_external_statement_date_time_type1code import ObExternalStatementDateTimeType1Code
    from .ob_external_statement_fee_frequency1code import ObExternalStatementFeeFrequency1Code
    from .ob_external_statement_fee_rate_type1code import ObExternalStatementFeeRateType1Code
    from .ob_external_statement_fee_type1code import ObExternalStatementFeeType1Code
    from .ob_external_statement_interest_frequency1code import ObExternalStatementInterestFrequency1Code
    from .ob_external_statement_interest_rate_type1code import ObExternalStatementInterestRateType1Code
    from .ob_external_statement_interest_type1code import ObExternalStatementInterestType1Code
    from .ob_external_statement_rate_type1code import ObExternalStatementRateType1Code
    from .ob_external_statement_type1code import ObExternalStatementType1Code
    from .ob_external_statement_value_type1code import ObExternalStatementValueType1Code
    from .ob_external_switch_status_code import ObExternalSwitchStatusCode
    from .ob_fee_category1code import ObFeeCategory1Code
    from .ob_fee_frequency1code0 import ObFeeFrequency1Code0
    from .ob_fee_frequency1code1 import ObFeeFrequency1Code1
    from .ob_fee_frequency1code2 import ObFeeFrequency1Code2
    from .ob_fee_frequency1code3 import ObFeeFrequency1Code3
    from .ob_fee_frequency1code4 import ObFeeFrequency1Code4
    from .ob_fee_type1code import ObFeeType1Code
    from .ob_interest_calculation_method1code import ObInterestCalculationMethod1Code
    from .ob_interest_fixed_variable_type1code import ObInterestFixedVariableType1Code
    from .ob_interest_rate_type1code0 import ObInterestRateType1Code0
    from .ob_interest_rate_type1code1 import ObInterestRateType1Code1
    from .ob_merchant_details1 import ObMerchantDetails1
    from .ob_min_max_type1code import ObMinMaxType1Code
    from .ob_other_code_type10 import ObOtherCodeType10
    from .ob_other_code_type11 import ObOtherCodeType11
    from .ob_other_code_type12 import ObOtherCodeType12
    from .ob_other_code_type13 import ObOtherCodeType13
    from .ob_other_code_type14 import ObOtherCodeType14
    from .ob_other_code_type15 import ObOtherCodeType15
    from .ob_other_code_type16 import ObOtherCodeType16
    from .ob_other_code_type17 import ObOtherCodeType17
    from .ob_other_code_type18 import ObOtherCodeType18
    from .ob_other_fee_charge_detail_type import ObOtherFeeChargeDetailType
    from .ob_overdraft_fee_type1code import ObOverdraftFeeType1Code
    from .ob_party2 import ObParty2
    from .ob_party2address_item import ObParty2AddressItem
    from .ob_party_relationships1 import ObPartyRelationships1
    from .ob_party_relationships1account import ObPartyRelationships1Account
    from .ob_period1code import ObPeriod1Code
    from .ob_postal_address6 import ObPostalAddress6
    from .ob_rate10 import ObRate10
    from .ob_rate11 import ObRate11
    from .ob_read_account6 import ObReadAccount6
    from .ob_read_account6data import ObReadAccount6Data
    from .ob_read_balance1 import ObReadBalance1
    from .ob_read_balance1data import ObReadBalance1Data
    from .ob_read_balance1data_balance_item import ObReadBalance1DataBalanceItem
    from .ob_read_balance1data_balance_item_amount import ObReadBalance1DataBalanceItemAmount
    from .ob_read_balance1data_balance_item_credit_line_item import ObReadBalance1DataBalanceItemCreditLineItem
    from .ob_read_balance1data_balance_item_credit_line_item_amount import (
        ObReadBalance1DataBalanceItemCreditLineItemAmount,
    )
    from .ob_read_balance1data_balance_item_credit_line_item_type import ObReadBalance1DataBalanceItemCreditLineItemType
    from .ob_read_beneficiary5 import ObReadBeneficiary5
    from .ob_read_beneficiary5data import ObReadBeneficiary5Data
    from .ob_read_consent_response1 import ObReadConsentResponse1
    from .ob_read_consent_response1data import ObReadConsentResponse1Data
    from .ob_read_consent_response1data_permissions_item import ObReadConsentResponse1DataPermissionsItem
    from .ob_read_consent_response1data_status import ObReadConsentResponse1DataStatus
    from .ob_read_data_statement2 import ObReadDataStatement2
    from .ob_read_data_transaction6 import ObReadDataTransaction6
    from .ob_read_direct_debit2 import ObReadDirectDebit2
    from .ob_read_direct_debit2data import ObReadDirectDebit2Data
    from .ob_read_direct_debit2data_direct_debit_item import ObReadDirectDebit2DataDirectDebitItem
    from .ob_read_offer1 import ObReadOffer1
    from .ob_read_offer1data import ObReadOffer1Data
    from .ob_read_offer1data_offer_item import ObReadOffer1DataOfferItem
    from .ob_read_offer1data_offer_item_amount import ObReadOffer1DataOfferItemAmount
    from .ob_read_offer1data_offer_item_fee import ObReadOffer1DataOfferItemFee
    from .ob_read_offer1data_offer_item_offer_type import ObReadOffer1DataOfferItemOfferType
    from .ob_read_party2 import ObReadParty2
    from .ob_read_party2data import ObReadParty2Data
    from .ob_read_party3 import ObReadParty3
    from .ob_read_party3data import ObReadParty3Data
    from .ob_read_product2 import ObReadProduct2
    from .ob_read_product2data import ObReadProduct2Data
    from .ob_read_product2data_product_item import ObReadProduct2DataProductItem
    from .ob_read_product2data_product_item_other_product_type import ObReadProduct2DataProductItemOtherProductType
    from .ob_read_product2data_product_item_other_product_type_credit_interest import (
        ObReadProduct2DataProductItemOtherProductTypeCreditInterest,
    )
    from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item import (
        ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItem,
    )
    from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_destination import (
        ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemDestination,
    )
    from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item import (
        ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItem,
    )
    from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_application_frequency import (
        ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency,
    )
    from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type import (
        ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType,
    )
    from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_calculation_frequency import (
        ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemCalculationFrequency,
    )
    from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage import (
        ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage,
    )
    from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type import (
        ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType,
    )
    from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_method import (
        ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandMethod,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterest,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_other_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemOtherFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_detail_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_other_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemOtherFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_detail_item import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItem,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_provider_interest_rate_type import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_max_term_period import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMaxTermPeriod,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_min_term_period import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_other_loan_provider_interest_rate_type import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType,
    )
    from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_tier_band_method import (
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemTierBandMethod,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItem,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItem,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item_other_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemOtherFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItem,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_applicable_range import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_other_tariff_type import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemOtherTariffType,
    )
    from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_tariff_type import (
        ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemTariffType,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraft,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_agreement_period import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_type import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftType,
    )
    from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_tier_band_method import (
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemTierBandMethod,
    )
    from .ob_read_product2data_product_item_other_product_type_product_details import (
        ObReadProduct2DataProductItemOtherProductTypeProductDetails,
    )
    from .ob_read_product2data_product_item_other_product_type_product_details_fee_free_length_period import (
        ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod,
    )
    from .ob_read_product2data_product_item_other_product_type_product_details_segment_item import (
        ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment import (
        ObReadProduct2DataProductItemOtherProductTypeRepayment,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_amount_type import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_other_amount_type import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_other_repayment_frequency import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_other_repayment_type import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItem,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item_other_fee_type_item import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemOtherFeeTypeItem,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_detail_item import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetailItem,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_repayment_frequency import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_repayment_holiday_item import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItem,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_repayment_holiday_item_max_holiday_period import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod,
    )
    from .ob_read_product2data_product_item_other_product_type_repayment_repayment_type import (
        ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType,
    )
    from .ob_read_product2data_product_item_product_type import ObReadProduct2DataProductItemProductType
    from .ob_read_scheduled_payment3 import ObReadScheduledPayment3
    from .ob_read_scheduled_payment3data import ObReadScheduledPayment3Data
    from .ob_read_standing_order6 import ObReadStandingOrder6
    from .ob_read_standing_order6data import ObReadStandingOrder6Data
    from .ob_read_statement2 import ObReadStatement2
    from .ob_read_transaction6 import ObReadTransaction6
    from .ob_risk2 import ObRisk2
    from .ob_scheduled_payment3 import ObScheduledPayment3
    from .ob_scheduled_payment3basic import ObScheduledPayment3Basic
    from .ob_scheduled_payment3detail import ObScheduledPayment3Detail
    from .ob_standing_order6 import ObStandingOrder6
    from .ob_standing_order6basic import ObStandingOrder6Basic
    from .ob_standing_order6detail import ObStandingOrder6Detail
    from .ob_statement2 import ObStatement2
    from .ob_statement2basic import ObStatement2Basic
    from .ob_statement2basic_statement_benefit_item import ObStatement2BasicStatementBenefitItem
    from .ob_statement2basic_statement_date_time_item import ObStatement2BasicStatementDateTimeItem
    from .ob_statement2basic_statement_fee_item import ObStatement2BasicStatementFeeItem
    from .ob_statement2basic_statement_interest_item import ObStatement2BasicStatementInterestItem
    from .ob_statement2basic_statement_rate_item import ObStatement2BasicStatementRateItem
    from .ob_statement2basic_statement_value_item import ObStatement2BasicStatementValueItem
    from .ob_statement2detail import ObStatement2Detail
    from .ob_statement2detail_statement_amount_item import ObStatement2DetailStatementAmountItem
    from .ob_statement2detail_statement_benefit_item import ObStatement2DetailStatementBenefitItem
    from .ob_statement2detail_statement_date_time_item import ObStatement2DetailStatementDateTimeItem
    from .ob_statement2detail_statement_fee_item import ObStatement2DetailStatementFeeItem
    from .ob_statement2detail_statement_interest_item import ObStatement2DetailStatementInterestItem
    from .ob_statement2detail_statement_rate_item import ObStatement2DetailStatementRateItem
    from .ob_statement2detail_statement_value_item import ObStatement2DetailStatementValueItem
    from .ob_statement2statement_amount_item import ObStatement2StatementAmountItem
    from .ob_statement2statement_benefit_item import ObStatement2StatementBenefitItem
    from .ob_statement2statement_date_time_item import ObStatement2StatementDateTimeItem
    from .ob_statement2statement_fee_item import ObStatement2StatementFeeItem
    from .ob_statement2statement_interest_item import ObStatement2StatementInterestItem
    from .ob_statement2statement_rate_item import ObStatement2StatementRateItem
    from .ob_statement2statement_value_item import ObStatement2StatementValueItem
    from .ob_supplementary_data1 import ObSupplementaryData1
    from .ob_transaction6 import ObTransaction6
    from .ob_transaction6basic import ObTransaction6Basic
    from .ob_transaction6detail import ObTransaction6Detail
    from .ob_transaction_card_instrument1 import ObTransactionCardInstrument1
    from .ob_transaction_card_instrument1authorisation_type import ObTransactionCardInstrument1AuthorisationType
    from .ob_transaction_card_instrument1card_scheme_name import ObTransactionCardInstrument1CardSchemeName
    from .ob_transaction_cash_balance import ObTransactionCashBalance
    from .ob_transaction_cash_balance_amount import ObTransactionCashBalanceAmount
    from .ob_transaction_mutability1code import ObTransactionMutability1Code
    from .obbca_data1 import ObbcaData1
    from .obbca_data1credit_interest import ObbcaData1CreditInterest
    from .obbca_data1credit_interest_tier_band_set_item import ObbcaData1CreditInterestTierBandSetItem
    from .obbca_data1credit_interest_tier_band_set_item_calculation_method import (
        ObbcaData1CreditInterestTierBandSetItemCalculationMethod,
    )
    from .obbca_data1credit_interest_tier_band_set_item_destination import (
        ObbcaData1CreditInterestTierBandSetItemDestination,
    )
    from .obbca_data1credit_interest_tier_band_set_item_tier_band_item import (
        ObbcaData1CreditInterestTierBandSetItemTierBandItem,
    )
    from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_application_frequency import (
        ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency,
    )
    from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type import (
        ObbcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType,
    )
    from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_calculation_frequency import (
        ObbcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency,
    )
    from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage import (
        ObbcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage,
    )
    from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_fixed_variable_interest_rate_type import (
        ObbcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType,
    )
    from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_application_frequency import (
        ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency,
    )
    from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type import (
        ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType,
    )
    from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_calculation_frequency import (
        ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency,
    )
    from .obbca_data1credit_interest_tier_band_set_item_tier_band_method import (
        ObbcaData1CreditInterestTierBandSetItemTierBandMethod,
    )
    from .obbca_data1other_fees_charges_item import ObbcaData1OtherFeesChargesItem
    from .obbca_data1other_fees_charges_item_fee_charge_cap_item import ObbcaData1OtherFeesChargesItemFeeChargeCapItem
    from .obbca_data1other_fees_charges_item_fee_charge_cap_item_capping_period import (
        ObbcaData1OtherFeesChargesItemFeeChargeCapItemCappingPeriod,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_cap_item_fee_type_item import (
        ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_cap_item_min_max_type import (
        ObbcaData1OtherFeesChargesItemFeeChargeCapItemMinMaxType,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_cap_item_other_fee_type_item import (
        ObbcaData1OtherFeesChargesItemFeeChargeCapItemOtherFeeTypeItem,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItem,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_application_frequency import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_calculation_frequency import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemCalculationFrequency,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_applicable_range import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_category import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeCategory,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_capping_period import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemCappingPeriod,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_fee_type_item import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeTypeItem,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_min_max_type import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemMinMaxType,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_rate_type import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeRateType,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_type import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeType,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_application_frequency import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_calculation_frequency import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_category_type import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_rate_type import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_type import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType,
    )
    from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_type_fee_category import (
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeTypeFeeCategory,
    )
    from .obbca_data1other_fees_charges_item_other_tariff_type import ObbcaData1OtherFeesChargesItemOtherTariffType
    from .obbca_data1other_fees_charges_item_tariff_type import ObbcaData1OtherFeesChargesItemTariffType
    from .obbca_data1overdraft import ObbcaData1Overdraft
    from .obbca_data1overdraft_overdraft_tier_band_set_item import ObbcaData1OverdraftOverdraftTierBandSetItem
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_capping_period import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemCappingPeriod,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_min_max_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_agreement_period import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_capping_period import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemCappingPeriod,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_min_max_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_type import (
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftType,
    )
    from .obbca_data1overdraft_overdraft_tier_band_set_item_tier_band_method import (
        ObbcaData1OverdraftOverdraftTierBandSetItemTierBandMethod,
    )
    from .obbca_data1product_details import ObbcaData1ProductDetails
    from .obbca_data1product_details_fee_free_length_period import ObbcaData1ProductDetailsFeeFreeLengthPeriod
    from .obbca_data1product_details_segment_item import ObbcaData1ProductDetailsSegmentItem
    from .obpca_data1 import ObpcaData1
    from .obpca_data1credit_interest import ObpcaData1CreditInterest
    from .obpca_data1credit_interest_tier_band_set_item import ObpcaData1CreditInterestTierBandSetItem
    from .obpca_data1credit_interest_tier_band_set_item_calculation_method import (
        ObpcaData1CreditInterestTierBandSetItemCalculationMethod,
    )
    from .obpca_data1credit_interest_tier_band_set_item_destination import (
        ObpcaData1CreditInterestTierBandSetItemDestination,
    )
    from .obpca_data1credit_interest_tier_band_set_item_tier_band_item import (
        ObpcaData1CreditInterestTierBandSetItemTierBandItem,
    )
    from .obpca_data1credit_interest_tier_band_set_item_tier_band_item_application_frequency import (
        ObpcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency,
    )
    from .obpca_data1credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type import (
        ObpcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType,
    )
    from .obpca_data1credit_interest_tier_band_set_item_tier_band_item_calculation_frequency import (
        ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency,
    )
    from .obpca_data1credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage import (
        ObpcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage,
    )
    from .obpca_data1credit_interest_tier_band_set_item_tier_band_item_fixed_variable_interest_rate_type import (
        ObpcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType,
    )
    from .obpca_data1credit_interest_tier_band_set_item_tier_band_item_other_application_frequency import (
        ObpcaData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency,
    )
    from .obpca_data1credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type import (
        ObpcaData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType,
    )
    from .obpca_data1credit_interest_tier_band_set_item_tier_band_item_other_calculation_frequency import (
        ObpcaData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency,
    )
    from .obpca_data1credit_interest_tier_band_set_item_tier_band_method import (
        ObpcaData1CreditInterestTierBandSetItemTierBandMethod,
    )
    from .obpca_data1other_fees_charges import ObpcaData1OtherFeesCharges
    from .obpca_data1other_fees_charges_fee_charge_cap_item import ObpcaData1OtherFeesChargesFeeChargeCapItem
    from .obpca_data1other_fees_charges_fee_charge_cap_item_capping_period import (
        ObpcaData1OtherFeesChargesFeeChargeCapItemCappingPeriod,
    )
    from .obpca_data1other_fees_charges_fee_charge_cap_item_fee_type_item import (
        ObpcaData1OtherFeesChargesFeeChargeCapItemFeeTypeItem,
    )
    from .obpca_data1other_fees_charges_fee_charge_cap_item_min_max_type import (
        ObpcaData1OtherFeesChargesFeeChargeCapItemMinMaxType,
    )
    from .obpca_data1other_fees_charges_fee_charge_cap_item_other_fee_type_item import (
        ObpcaData1OtherFeesChargesFeeChargeCapItemOtherFeeTypeItem,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item import ObpcaData1OtherFeesChargesFeeChargeDetailItem
    from .obpca_data1other_fees_charges_fee_charge_detail_item_application_frequency import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemApplicationFrequency,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_calculation_frequency import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemCalculationFrequency,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_fee_applicable_range import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeApplicableRange,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_fee_category import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeCategory,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItem,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_capping_period import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemCappingPeriod,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_fee_type_item import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemFeeTypeItem,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_min_max_type import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemMinMaxType,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_fee_rate_type import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeRateType,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_fee_type import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeType,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_other_application_frequency import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherApplicationFrequency,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_other_calculation_frequency import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherCalculationFrequency,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_category_type import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeCategoryType,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_rate_type import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeRateType,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_type import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeType,
    )
    from .obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_type_fee_category import (
        ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeTypeFeeCategory,
    )
    from .obpca_data1overdraft import ObpcaData1Overdraft
    from .obpca_data1overdraft_overdraft_tier_band_set_item import ObpcaData1OverdraftOverdraftTierBandSetItem
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_capping_period import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_fee_type_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_min_max_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapMinMaxType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_other_fee_type_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapOtherFeeTypeItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_capping_period import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_fee_type_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_min_max_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapMinMaxType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_other_fee_type_item import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapOtherFeeTypeItem,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_type import (
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftType,
    )
    from .obpca_data1overdraft_overdraft_tier_band_set_item_tier_band_method import (
        ObpcaData1OverdraftOverdraftTierBandSetItemTierBandMethod,
    )
    from .obpca_data1product_details import ObpcaData1ProductDetails
    from .obpca_data1product_details_segment_item import ObpcaData1ProductDetailsSegmentItem
    from .opening_date import OpeningDate
    from .party_id import PartyId
    from .party_number import PartyNumber
    from .phone_number0 import PhoneNumber0
    from .phone_number1 import PhoneNumber1
    from .post_code import PostCode
    from .previous_payment_date_time import PreviousPaymentDateTime
    from .proprietary_bank_transaction_code_structure1 import ProprietaryBankTransactionCodeStructure1
    from .rate import Rate
    from .reference import Reference
    from .scheduled_payment_date_time import ScheduledPaymentDateTime
    from .scheduled_payment_id import ScheduledPaymentId
    from .secondary_identification import SecondaryIdentification
    from .standing_order_id import StandingOrderId
    from .start_date_time import StartDateTime
    from .statement_id import StatementId
    from .statement_reference import StatementReference
    from .status_update_date_time import StatusUpdateDateTime
    from .street_name import StreetName
    from .town_name import TownName
    from .transaction_id import TransactionId
    from .transaction_information import TransactionInformation
    from .transaction_reference import TransactionReference
    from .value import Value
    from .value_date_time import ValueDateTime
_dynamic_imports: typing.Dict[str, str] = {
    "AccountId": ".account_id",
    "ActiveOrHistoricCurrencyCode0": ".active_or_historic_currency_code0",
    "ActiveOrHistoricCurrencyCode1": ".active_or_historic_currency_code1",
    "AddressLine": ".address_line",
    "BeneficiaryId": ".beneficiary_id",
    "BookingDateTime": ".booking_date_time",
    "BuildingNumber": ".building_number",
    "CountryCode": ".country_code",
    "CountrySubDivision": ".country_sub_division",
    "CreationDateTime": ".creation_date_time",
    "DateTime": ".date_time",
    "DebtorReference": ".debtor_reference",
    "Description0": ".description0",
    "Description1": ".description1",
    "Description2": ".description2",
    "Description3": ".description3",
    "DirectDebitId": ".direct_debit_id",
    "EmailAddress": ".email_address",
    "EndDateTime": ".end_date_time",
    "File": ".file",
    "FinalPaymentDateTime": ".final_payment_date_time",
    "FirstPaymentDateTime": ".first_payment_date_time",
    "Frequency0": ".frequency0",
    "Frequency1": ".frequency1",
    "FullLegalName": ".full_legal_name",
    "Identification0": ".identification0",
    "Identification1": ".identification1",
    "Identification2": ".identification2",
    "IsoDateTime": ".iso_date_time",
    "LastPaymentDateTime": ".last_payment_date_time",
    "Links": ".links",
    "MandateIdentification": ".mandate_identification",
    "MaturityDate": ".maturity_date",
    "Meta": ".meta",
    "Model": ".model",
    "Name0": ".name0",
    "Name1": ".name1",
    "Name2": ".name2",
    "Name3": ".name3",
    "Name4": ".name4",
    "NextPaymentDateTime": ".next_payment_date_time",
    "Nickname": ".nickname",
    "Number0": ".number0",
    "Number1": ".number1",
    "NumberOfPayments": ".number_of_payments",
    "OauthScope": ".oauth_scope",
    "ObAccount4": ".ob_account4",
    "ObAccount4AccountItem": ".ob_account4account_item",
    "ObAccount4Basic": ".ob_account4basic",
    "ObAccount4Detail": ".ob_account4detail",
    "ObAccount4DetailAccountItem": ".ob_account4detail_account_item",
    "ObAccount6": ".ob_account6",
    "ObAccount6AccountItem": ".ob_account6account_item",
    "ObAccount6Basic": ".ob_account6basic",
    "ObAccount6Detail": ".ob_account6detail",
    "ObAccount6DetailAccountItem": ".ob_account6detail_account_item",
    "ObAccountStatus1Code": ".ob_account_status1code",
    "ObActiveCurrencyAndAmountSimpleType": ".ob_active_currency_and_amount_simple_type",
    "ObActiveOrHistoricCurrencyAndAmount0": ".ob_active_or_historic_currency_and_amount0",
    "ObActiveOrHistoricCurrencyAndAmount1": ".ob_active_or_historic_currency_and_amount1",
    "ObActiveOrHistoricCurrencyAndAmount10": ".ob_active_or_historic_currency_and_amount10",
    "ObActiveOrHistoricCurrencyAndAmount11": ".ob_active_or_historic_currency_and_amount11",
    "ObActiveOrHistoricCurrencyAndAmount2": ".ob_active_or_historic_currency_and_amount2",
    "ObActiveOrHistoricCurrencyAndAmount3": ".ob_active_or_historic_currency_and_amount3",
    "ObActiveOrHistoricCurrencyAndAmount4": ".ob_active_or_historic_currency_and_amount4",
    "ObActiveOrHistoricCurrencyAndAmount5": ".ob_active_or_historic_currency_and_amount5",
    "ObActiveOrHistoricCurrencyAndAmount6": ".ob_active_or_historic_currency_and_amount6",
    "ObActiveOrHistoricCurrencyAndAmount7": ".ob_active_or_historic_currency_and_amount7",
    "ObActiveOrHistoricCurrencyAndAmount8": ".ob_active_or_historic_currency_and_amount8",
    "ObActiveOrHistoricCurrencyAndAmount9": ".ob_active_or_historic_currency_and_amount9",
    "ObAddressTypeCode": ".ob_address_type_code",
    "ObAmount10": ".ob_amount10",
    "ObAmount11": ".ob_amount11",
    "ObAmount12": ".ob_amount12",
    "ObAmount13": ".ob_amount13",
    "ObAmount14": ".ob_amount14",
    "ObBalanceType1Code": ".ob_balance_type1code",
    "ObBankTransactionCodeStructure1": ".ob_bank_transaction_code_structure1",
    "ObBeneficiary5": ".ob_beneficiary5",
    "ObBeneficiary5Basic": ".ob_beneficiary5basic",
    "ObBeneficiary5Detail": ".ob_beneficiary5detail",
    "ObBeneficiaryType1Code": ".ob_beneficiary_type1code",
    "ObBranchAndFinancialInstitutionIdentification50": ".ob_branch_and_financial_institution_identification50",
    "ObBranchAndFinancialInstitutionIdentification51": ".ob_branch_and_financial_institution_identification51",
    "ObBranchAndFinancialInstitutionIdentification60": ".ob_branch_and_financial_institution_identification60",
    "ObBranchAndFinancialInstitutionIdentification61": ".ob_branch_and_financial_institution_identification61",
    "ObBranchAndFinancialInstitutionIdentification62": ".ob_branch_and_financial_institution_identification62",
    "ObCashAccount50": ".ob_cash_account50",
    "ObCashAccount51": ".ob_cash_account51",
    "ObCashAccount60": ".ob_cash_account60",
    "ObCashAccount61": ".ob_cash_account61",
    "ObCodeMnemonic": ".ob_code_mnemonic",
    "ObCreditDebitCode0": ".ob_credit_debit_code0",
    "ObCreditDebitCode1": ".ob_credit_debit_code1",
    "ObCreditDebitCode2": ".ob_credit_debit_code2",
    "ObCurrencyExchange5": ".ob_currency_exchange5",
    "ObCurrencyExchange5InstructedAmount": ".ob_currency_exchange5instructed_amount",
    "ObEntryStatus1Code": ".ob_entry_status1code",
    "ObError1": ".ob_error1",
    "ObErrorResponse1": ".ob_error_response1",
    "ObExternalAccountIdentification4Code": ".ob_external_account_identification4code",
    "ObExternalAccountRole1Code": ".ob_external_account_role1code",
    "ObExternalAccountSubType1Code": ".ob_external_account_sub_type1code",
    "ObExternalAccountType1Code": ".ob_external_account_type1code",
    "ObExternalDirectDebitStatus1Code": ".ob_external_direct_debit_status1code",
    "ObExternalFinancialInstitutionIdentification4Code": ".ob_external_financial_institution_identification4code",
    "ObExternalLegalStructureType1Code": ".ob_external_legal_structure_type1code",
    "ObExternalPartyType1Code": ".ob_external_party_type1code",
    "ObExternalScheduleType1Code": ".ob_external_schedule_type1code",
    "ObExternalStandingOrderStatus1Code": ".ob_external_standing_order_status1code",
    "ObExternalStatementAmountType1Code": ".ob_external_statement_amount_type1code",
    "ObExternalStatementBenefitType1Code": ".ob_external_statement_benefit_type1code",
    "ObExternalStatementDateTimeType1Code": ".ob_external_statement_date_time_type1code",
    "ObExternalStatementFeeFrequency1Code": ".ob_external_statement_fee_frequency1code",
    "ObExternalStatementFeeRateType1Code": ".ob_external_statement_fee_rate_type1code",
    "ObExternalStatementFeeType1Code": ".ob_external_statement_fee_type1code",
    "ObExternalStatementInterestFrequency1Code": ".ob_external_statement_interest_frequency1code",
    "ObExternalStatementInterestRateType1Code": ".ob_external_statement_interest_rate_type1code",
    "ObExternalStatementInterestType1Code": ".ob_external_statement_interest_type1code",
    "ObExternalStatementRateType1Code": ".ob_external_statement_rate_type1code",
    "ObExternalStatementType1Code": ".ob_external_statement_type1code",
    "ObExternalStatementValueType1Code": ".ob_external_statement_value_type1code",
    "ObExternalSwitchStatusCode": ".ob_external_switch_status_code",
    "ObFeeCategory1Code": ".ob_fee_category1code",
    "ObFeeFrequency1Code0": ".ob_fee_frequency1code0",
    "ObFeeFrequency1Code1": ".ob_fee_frequency1code1",
    "ObFeeFrequency1Code2": ".ob_fee_frequency1code2",
    "ObFeeFrequency1Code3": ".ob_fee_frequency1code3",
    "ObFeeFrequency1Code4": ".ob_fee_frequency1code4",
    "ObFeeType1Code": ".ob_fee_type1code",
    "ObInterestCalculationMethod1Code": ".ob_interest_calculation_method1code",
    "ObInterestFixedVariableType1Code": ".ob_interest_fixed_variable_type1code",
    "ObInterestRateType1Code0": ".ob_interest_rate_type1code0",
    "ObInterestRateType1Code1": ".ob_interest_rate_type1code1",
    "ObMerchantDetails1": ".ob_merchant_details1",
    "ObMinMaxType1Code": ".ob_min_max_type1code",
    "ObOtherCodeType10": ".ob_other_code_type10",
    "ObOtherCodeType11": ".ob_other_code_type11",
    "ObOtherCodeType12": ".ob_other_code_type12",
    "ObOtherCodeType13": ".ob_other_code_type13",
    "ObOtherCodeType14": ".ob_other_code_type14",
    "ObOtherCodeType15": ".ob_other_code_type15",
    "ObOtherCodeType16": ".ob_other_code_type16",
    "ObOtherCodeType17": ".ob_other_code_type17",
    "ObOtherCodeType18": ".ob_other_code_type18",
    "ObOtherFeeChargeDetailType": ".ob_other_fee_charge_detail_type",
    "ObOverdraftFeeType1Code": ".ob_overdraft_fee_type1code",
    "ObParty2": ".ob_party2",
    "ObParty2AddressItem": ".ob_party2address_item",
    "ObPartyRelationships1": ".ob_party_relationships1",
    "ObPartyRelationships1Account": ".ob_party_relationships1account",
    "ObPeriod1Code": ".ob_period1code",
    "ObPostalAddress6": ".ob_postal_address6",
    "ObRate10": ".ob_rate10",
    "ObRate11": ".ob_rate11",
    "ObReadAccount6": ".ob_read_account6",
    "ObReadAccount6Data": ".ob_read_account6data",
    "ObReadBalance1": ".ob_read_balance1",
    "ObReadBalance1Data": ".ob_read_balance1data",
    "ObReadBalance1DataBalanceItem": ".ob_read_balance1data_balance_item",
    "ObReadBalance1DataBalanceItemAmount": ".ob_read_balance1data_balance_item_amount",
    "ObReadBalance1DataBalanceItemCreditLineItem": ".ob_read_balance1data_balance_item_credit_line_item",
    "ObReadBalance1DataBalanceItemCreditLineItemAmount": ".ob_read_balance1data_balance_item_credit_line_item_amount",
    "ObReadBalance1DataBalanceItemCreditLineItemType": ".ob_read_balance1data_balance_item_credit_line_item_type",
    "ObReadBeneficiary5": ".ob_read_beneficiary5",
    "ObReadBeneficiary5Data": ".ob_read_beneficiary5data",
    "ObReadConsentResponse1": ".ob_read_consent_response1",
    "ObReadConsentResponse1Data": ".ob_read_consent_response1data",
    "ObReadConsentResponse1DataPermissionsItem": ".ob_read_consent_response1data_permissions_item",
    "ObReadConsentResponse1DataStatus": ".ob_read_consent_response1data_status",
    "ObReadDataStatement2": ".ob_read_data_statement2",
    "ObReadDataTransaction6": ".ob_read_data_transaction6",
    "ObReadDirectDebit2": ".ob_read_direct_debit2",
    "ObReadDirectDebit2Data": ".ob_read_direct_debit2data",
    "ObReadDirectDebit2DataDirectDebitItem": ".ob_read_direct_debit2data_direct_debit_item",
    "ObReadOffer1": ".ob_read_offer1",
    "ObReadOffer1Data": ".ob_read_offer1data",
    "ObReadOffer1DataOfferItem": ".ob_read_offer1data_offer_item",
    "ObReadOffer1DataOfferItemAmount": ".ob_read_offer1data_offer_item_amount",
    "ObReadOffer1DataOfferItemFee": ".ob_read_offer1data_offer_item_fee",
    "ObReadOffer1DataOfferItemOfferType": ".ob_read_offer1data_offer_item_offer_type",
    "ObReadParty2": ".ob_read_party2",
    "ObReadParty2Data": ".ob_read_party2data",
    "ObReadParty3": ".ob_read_party3",
    "ObReadParty3Data": ".ob_read_party3data",
    "ObReadProduct2": ".ob_read_product2",
    "ObReadProduct2Data": ".ob_read_product2data",
    "ObReadProduct2DataProductItem": ".ob_read_product2data_product_item",
    "ObReadProduct2DataProductItemOtherProductType": ".ob_read_product2data_product_item_other_product_type",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterest": ".ob_read_product2data_product_item_other_product_type_credit_interest",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItem": ".ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemDestination": ".ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_destination",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItem": ".ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency": ".ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_application_frequency",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType": ".ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemCalculationFrequency": ".ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_calculation_frequency",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage": ".ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType": ".ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandMethod": ".ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_method",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterest": ".ob_read_product2data_product_item_other_product_type_loan_interest",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemOtherFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_other_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_detail_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemOtherFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_other_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItem": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_detail_item",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_provider_interest_rate_type",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMaxTermPeriod": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_max_term_period",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_min_term_period",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_other_loan_provider_interest_rate_type",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemTierBandMethod": ".ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_tier_band_method",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItem": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItem": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemOtherFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item_other_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItem": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_applicable_range",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemOtherTariffType": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item_other_tariff_type",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemTariffType": ".ob_read_product2data_product_item_other_product_type_other_fees_charges_item_tariff_type",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraft": ".ob_read_product2data_product_item_other_product_type_overdraft",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_agreement_period",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftType": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_type",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemTierBandMethod": ".ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_tier_band_method",
    "ObReadProduct2DataProductItemOtherProductTypeProductDetails": ".ob_read_product2data_product_item_other_product_type_product_details",
    "ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod": ".ob_read_product2data_product_item_other_product_type_product_details_fee_free_length_period",
    "ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem": ".ob_read_product2data_product_item_other_product_type_product_details_segment_item",
    "ObReadProduct2DataProductItemOtherProductTypeRepayment": ".ob_read_product2data_product_item_other_product_type_repayment",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType": ".ob_read_product2data_product_item_other_product_type_repayment_amount_type",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType": ".ob_read_product2data_product_item_other_product_type_repayment_other_amount_type",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency": ".ob_read_product2data_product_item_other_product_type_repayment_other_repayment_frequency",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType": ".ob_read_product2data_product_item_other_product_type_repayment_other_repayment_type",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges": ".ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItem": ".ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemOtherFeeTypeItem": ".ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item_other_fee_type_item",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetailItem": ".ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_detail_item",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency": ".ob_read_product2data_product_item_other_product_type_repayment_repayment_frequency",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItem": ".ob_read_product2data_product_item_other_product_type_repayment_repayment_holiday_item",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod": ".ob_read_product2data_product_item_other_product_type_repayment_repayment_holiday_item_max_holiday_period",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType": ".ob_read_product2data_product_item_other_product_type_repayment_repayment_type",
    "ObReadProduct2DataProductItemProductType": ".ob_read_product2data_product_item_product_type",
    "ObReadScheduledPayment3": ".ob_read_scheduled_payment3",
    "ObReadScheduledPayment3Data": ".ob_read_scheduled_payment3data",
    "ObReadStandingOrder6": ".ob_read_standing_order6",
    "ObReadStandingOrder6Data": ".ob_read_standing_order6data",
    "ObReadStatement2": ".ob_read_statement2",
    "ObReadTransaction6": ".ob_read_transaction6",
    "ObRisk2": ".ob_risk2",
    "ObScheduledPayment3": ".ob_scheduled_payment3",
    "ObScheduledPayment3Basic": ".ob_scheduled_payment3basic",
    "ObScheduledPayment3Detail": ".ob_scheduled_payment3detail",
    "ObStandingOrder6": ".ob_standing_order6",
    "ObStandingOrder6Basic": ".ob_standing_order6basic",
    "ObStandingOrder6Detail": ".ob_standing_order6detail",
    "ObStatement2": ".ob_statement2",
    "ObStatement2Basic": ".ob_statement2basic",
    "ObStatement2BasicStatementBenefitItem": ".ob_statement2basic_statement_benefit_item",
    "ObStatement2BasicStatementDateTimeItem": ".ob_statement2basic_statement_date_time_item",
    "ObStatement2BasicStatementFeeItem": ".ob_statement2basic_statement_fee_item",
    "ObStatement2BasicStatementInterestItem": ".ob_statement2basic_statement_interest_item",
    "ObStatement2BasicStatementRateItem": ".ob_statement2basic_statement_rate_item",
    "ObStatement2BasicStatementValueItem": ".ob_statement2basic_statement_value_item",
    "ObStatement2Detail": ".ob_statement2detail",
    "ObStatement2DetailStatementAmountItem": ".ob_statement2detail_statement_amount_item",
    "ObStatement2DetailStatementBenefitItem": ".ob_statement2detail_statement_benefit_item",
    "ObStatement2DetailStatementDateTimeItem": ".ob_statement2detail_statement_date_time_item",
    "ObStatement2DetailStatementFeeItem": ".ob_statement2detail_statement_fee_item",
    "ObStatement2DetailStatementInterestItem": ".ob_statement2detail_statement_interest_item",
    "ObStatement2DetailStatementRateItem": ".ob_statement2detail_statement_rate_item",
    "ObStatement2DetailStatementValueItem": ".ob_statement2detail_statement_value_item",
    "ObStatement2StatementAmountItem": ".ob_statement2statement_amount_item",
    "ObStatement2StatementBenefitItem": ".ob_statement2statement_benefit_item",
    "ObStatement2StatementDateTimeItem": ".ob_statement2statement_date_time_item",
    "ObStatement2StatementFeeItem": ".ob_statement2statement_fee_item",
    "ObStatement2StatementInterestItem": ".ob_statement2statement_interest_item",
    "ObStatement2StatementRateItem": ".ob_statement2statement_rate_item",
    "ObStatement2StatementValueItem": ".ob_statement2statement_value_item",
    "ObSupplementaryData1": ".ob_supplementary_data1",
    "ObTransaction6": ".ob_transaction6",
    "ObTransaction6Basic": ".ob_transaction6basic",
    "ObTransaction6Detail": ".ob_transaction6detail",
    "ObTransactionCardInstrument1": ".ob_transaction_card_instrument1",
    "ObTransactionCardInstrument1AuthorisationType": ".ob_transaction_card_instrument1authorisation_type",
    "ObTransactionCardInstrument1CardSchemeName": ".ob_transaction_card_instrument1card_scheme_name",
    "ObTransactionCashBalance": ".ob_transaction_cash_balance",
    "ObTransactionCashBalanceAmount": ".ob_transaction_cash_balance_amount",
    "ObTransactionMutability1Code": ".ob_transaction_mutability1code",
    "ObbcaData1": ".obbca_data1",
    "ObbcaData1CreditInterest": ".obbca_data1credit_interest",
    "ObbcaData1CreditInterestTierBandSetItem": ".obbca_data1credit_interest_tier_band_set_item",
    "ObbcaData1CreditInterestTierBandSetItemCalculationMethod": ".obbca_data1credit_interest_tier_band_set_item_calculation_method",
    "ObbcaData1CreditInterestTierBandSetItemDestination": ".obbca_data1credit_interest_tier_band_set_item_destination",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItem": ".obbca_data1credit_interest_tier_band_set_item_tier_band_item",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency": ".obbca_data1credit_interest_tier_band_set_item_tier_band_item_application_frequency",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType": ".obbca_data1credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency": ".obbca_data1credit_interest_tier_band_set_item_tier_band_item_calculation_frequency",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage": ".obbca_data1credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType": ".obbca_data1credit_interest_tier_band_set_item_tier_band_item_fixed_variable_interest_rate_type",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency": ".obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_application_frequency",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType": ".obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency": ".obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_calculation_frequency",
    "ObbcaData1CreditInterestTierBandSetItemTierBandMethod": ".obbca_data1credit_interest_tier_band_set_item_tier_band_method",
    "ObbcaData1OtherFeesChargesItem": ".obbca_data1other_fees_charges_item",
    "ObbcaData1OtherFeesChargesItemFeeChargeCapItem": ".obbca_data1other_fees_charges_item_fee_charge_cap_item",
    "ObbcaData1OtherFeesChargesItemFeeChargeCapItemCappingPeriod": ".obbca_data1other_fees_charges_item_fee_charge_cap_item_capping_period",
    "ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem": ".obbca_data1other_fees_charges_item_fee_charge_cap_item_fee_type_item",
    "ObbcaData1OtherFeesChargesItemFeeChargeCapItemMinMaxType": ".obbca_data1other_fees_charges_item_fee_charge_cap_item_min_max_type",
    "ObbcaData1OtherFeesChargesItemFeeChargeCapItemOtherFeeTypeItem": ".obbca_data1other_fees_charges_item_fee_charge_cap_item_other_fee_type_item",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItem": ".obbca_data1other_fees_charges_item_fee_charge_detail_item",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_application_frequency",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemCalculationFrequency": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_calculation_frequency",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_applicable_range",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeCategory": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_category",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemCappingPeriod": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_capping_period",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeTypeItem": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_fee_type_item",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemMinMaxType": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_min_max_type",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeRateType": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_rate_type",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeType": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_type",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_other_application_frequency",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_other_calculation_frequency",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_category_type",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_rate_type",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_type",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeTypeFeeCategory": ".obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_type_fee_category",
    "ObbcaData1OtherFeesChargesItemOtherTariffType": ".obbca_data1other_fees_charges_item_other_tariff_type",
    "ObbcaData1OtherFeesChargesItemTariffType": ".obbca_data1other_fees_charges_item_tariff_type",
    "ObbcaData1Overdraft": ".obbca_data1overdraft",
    "ObbcaData1OverdraftOverdraftTierBandSetItem": ".obbca_data1overdraft_overdraft_tier_band_set_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemCappingPeriod": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_capping_period",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_min_max_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_agreement_period",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemCappingPeriod": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_capping_period",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_min_max_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftType": ".obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_type",
    "ObbcaData1OverdraftOverdraftTierBandSetItemTierBandMethod": ".obbca_data1overdraft_overdraft_tier_band_set_item_tier_band_method",
    "ObbcaData1ProductDetails": ".obbca_data1product_details",
    "ObbcaData1ProductDetailsFeeFreeLengthPeriod": ".obbca_data1product_details_fee_free_length_period",
    "ObbcaData1ProductDetailsSegmentItem": ".obbca_data1product_details_segment_item",
    "ObpcaData1": ".obpca_data1",
    "ObpcaData1CreditInterest": ".obpca_data1credit_interest",
    "ObpcaData1CreditInterestTierBandSetItem": ".obpca_data1credit_interest_tier_band_set_item",
    "ObpcaData1CreditInterestTierBandSetItemCalculationMethod": ".obpca_data1credit_interest_tier_band_set_item_calculation_method",
    "ObpcaData1CreditInterestTierBandSetItemDestination": ".obpca_data1credit_interest_tier_band_set_item_destination",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItem": ".obpca_data1credit_interest_tier_band_set_item_tier_band_item",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency": ".obpca_data1credit_interest_tier_band_set_item_tier_band_item_application_frequency",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType": ".obpca_data1credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency": ".obpca_data1credit_interest_tier_band_set_item_tier_band_item_calculation_frequency",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage": ".obpca_data1credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType": ".obpca_data1credit_interest_tier_band_set_item_tier_band_item_fixed_variable_interest_rate_type",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency": ".obpca_data1credit_interest_tier_band_set_item_tier_band_item_other_application_frequency",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType": ".obpca_data1credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency": ".obpca_data1credit_interest_tier_band_set_item_tier_band_item_other_calculation_frequency",
    "ObpcaData1CreditInterestTierBandSetItemTierBandMethod": ".obpca_data1credit_interest_tier_band_set_item_tier_band_method",
    "ObpcaData1OtherFeesCharges": ".obpca_data1other_fees_charges",
    "ObpcaData1OtherFeesChargesFeeChargeCapItem": ".obpca_data1other_fees_charges_fee_charge_cap_item",
    "ObpcaData1OtherFeesChargesFeeChargeCapItemCappingPeriod": ".obpca_data1other_fees_charges_fee_charge_cap_item_capping_period",
    "ObpcaData1OtherFeesChargesFeeChargeCapItemFeeTypeItem": ".obpca_data1other_fees_charges_fee_charge_cap_item_fee_type_item",
    "ObpcaData1OtherFeesChargesFeeChargeCapItemMinMaxType": ".obpca_data1other_fees_charges_fee_charge_cap_item_min_max_type",
    "ObpcaData1OtherFeesChargesFeeChargeCapItemOtherFeeTypeItem": ".obpca_data1other_fees_charges_fee_charge_cap_item_other_fee_type_item",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItem": ".obpca_data1other_fees_charges_fee_charge_detail_item",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemApplicationFrequency": ".obpca_data1other_fees_charges_fee_charge_detail_item_application_frequency",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemCalculationFrequency": ".obpca_data1other_fees_charges_fee_charge_detail_item_calculation_frequency",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeApplicableRange": ".obpca_data1other_fees_charges_fee_charge_detail_item_fee_applicable_range",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeCategory": ".obpca_data1other_fees_charges_fee_charge_detail_item_fee_category",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItem": ".obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemCappingPeriod": ".obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_capping_period",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemFeeTypeItem": ".obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_fee_type_item",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemMinMaxType": ".obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_min_max_type",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem": ".obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeRateType": ".obpca_data1other_fees_charges_fee_charge_detail_item_fee_rate_type",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeType": ".obpca_data1other_fees_charges_fee_charge_detail_item_fee_type",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherApplicationFrequency": ".obpca_data1other_fees_charges_fee_charge_detail_item_other_application_frequency",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherCalculationFrequency": ".obpca_data1other_fees_charges_fee_charge_detail_item_other_calculation_frequency",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeCategoryType": ".obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_category_type",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeRateType": ".obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_rate_type",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeType": ".obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_type",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeTypeFeeCategory": ".obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_type_fee_category",
    "ObpcaData1Overdraft": ".obpca_data1overdraft",
    "ObpcaData1OverdraftOverdraftTierBandSetItem": ".obpca_data1overdraft_overdraft_tier_band_set_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_capping_period",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_fee_type_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapMinMaxType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_min_max_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapOtherFeeTypeItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_other_fee_type_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_capping_period",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_fee_type_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapMinMaxType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_min_max_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapOtherFeeTypeItem": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_other_fee_type_item",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftType": ".obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_type",
    "ObpcaData1OverdraftOverdraftTierBandSetItemTierBandMethod": ".obpca_data1overdraft_overdraft_tier_band_set_item_tier_band_method",
    "ObpcaData1ProductDetails": ".obpca_data1product_details",
    "ObpcaData1ProductDetailsSegmentItem": ".obpca_data1product_details_segment_item",
    "OpeningDate": ".opening_date",
    "PartyId": ".party_id",
    "PartyNumber": ".party_number",
    "PhoneNumber0": ".phone_number0",
    "PhoneNumber1": ".phone_number1",
    "PostCode": ".post_code",
    "PreviousPaymentDateTime": ".previous_payment_date_time",
    "ProprietaryBankTransactionCodeStructure1": ".proprietary_bank_transaction_code_structure1",
    "Rate": ".rate",
    "Reference": ".reference",
    "ScheduledPaymentDateTime": ".scheduled_payment_date_time",
    "ScheduledPaymentId": ".scheduled_payment_id",
    "SecondaryIdentification": ".secondary_identification",
    "StandingOrderId": ".standing_order_id",
    "StartDateTime": ".start_date_time",
    "StatementId": ".statement_id",
    "StatementReference": ".statement_reference",
    "StatusUpdateDateTime": ".status_update_date_time",
    "StreetName": ".street_name",
    "TownName": ".town_name",
    "TransactionId": ".transaction_id",
    "TransactionInformation": ".transaction_information",
    "TransactionReference": ".transaction_reference",
    "Value": ".value",
    "ValueDateTime": ".value_date_time",
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
    "AccountId",
    "ActiveOrHistoricCurrencyCode0",
    "ActiveOrHistoricCurrencyCode1",
    "AddressLine",
    "BeneficiaryId",
    "BookingDateTime",
    "BuildingNumber",
    "CountryCode",
    "CountrySubDivision",
    "CreationDateTime",
    "DateTime",
    "DebtorReference",
    "Description0",
    "Description1",
    "Description2",
    "Description3",
    "DirectDebitId",
    "EmailAddress",
    "EndDateTime",
    "File",
    "FinalPaymentDateTime",
    "FirstPaymentDateTime",
    "Frequency0",
    "Frequency1",
    "FullLegalName",
    "Identification0",
    "Identification1",
    "Identification2",
    "IsoDateTime",
    "LastPaymentDateTime",
    "Links",
    "MandateIdentification",
    "MaturityDate",
    "Meta",
    "Model",
    "Name0",
    "Name1",
    "Name2",
    "Name3",
    "Name4",
    "NextPaymentDateTime",
    "Nickname",
    "Number0",
    "Number1",
    "NumberOfPayments",
    "OauthScope",
    "ObAccount4",
    "ObAccount4AccountItem",
    "ObAccount4Basic",
    "ObAccount4Detail",
    "ObAccount4DetailAccountItem",
    "ObAccount6",
    "ObAccount6AccountItem",
    "ObAccount6Basic",
    "ObAccount6Detail",
    "ObAccount6DetailAccountItem",
    "ObAccountStatus1Code",
    "ObActiveCurrencyAndAmountSimpleType",
    "ObActiveOrHistoricCurrencyAndAmount0",
    "ObActiveOrHistoricCurrencyAndAmount1",
    "ObActiveOrHistoricCurrencyAndAmount10",
    "ObActiveOrHistoricCurrencyAndAmount11",
    "ObActiveOrHistoricCurrencyAndAmount2",
    "ObActiveOrHistoricCurrencyAndAmount3",
    "ObActiveOrHistoricCurrencyAndAmount4",
    "ObActiveOrHistoricCurrencyAndAmount5",
    "ObActiveOrHistoricCurrencyAndAmount6",
    "ObActiveOrHistoricCurrencyAndAmount7",
    "ObActiveOrHistoricCurrencyAndAmount8",
    "ObActiveOrHistoricCurrencyAndAmount9",
    "ObAddressTypeCode",
    "ObAmount10",
    "ObAmount11",
    "ObAmount12",
    "ObAmount13",
    "ObAmount14",
    "ObBalanceType1Code",
    "ObBankTransactionCodeStructure1",
    "ObBeneficiary5",
    "ObBeneficiary5Basic",
    "ObBeneficiary5Detail",
    "ObBeneficiaryType1Code",
    "ObBranchAndFinancialInstitutionIdentification50",
    "ObBranchAndFinancialInstitutionIdentification51",
    "ObBranchAndFinancialInstitutionIdentification60",
    "ObBranchAndFinancialInstitutionIdentification61",
    "ObBranchAndFinancialInstitutionIdentification62",
    "ObCashAccount50",
    "ObCashAccount51",
    "ObCashAccount60",
    "ObCashAccount61",
    "ObCodeMnemonic",
    "ObCreditDebitCode0",
    "ObCreditDebitCode1",
    "ObCreditDebitCode2",
    "ObCurrencyExchange5",
    "ObCurrencyExchange5InstructedAmount",
    "ObEntryStatus1Code",
    "ObError1",
    "ObErrorResponse1",
    "ObExternalAccountIdentification4Code",
    "ObExternalAccountRole1Code",
    "ObExternalAccountSubType1Code",
    "ObExternalAccountType1Code",
    "ObExternalDirectDebitStatus1Code",
    "ObExternalFinancialInstitutionIdentification4Code",
    "ObExternalLegalStructureType1Code",
    "ObExternalPartyType1Code",
    "ObExternalScheduleType1Code",
    "ObExternalStandingOrderStatus1Code",
    "ObExternalStatementAmountType1Code",
    "ObExternalStatementBenefitType1Code",
    "ObExternalStatementDateTimeType1Code",
    "ObExternalStatementFeeFrequency1Code",
    "ObExternalStatementFeeRateType1Code",
    "ObExternalStatementFeeType1Code",
    "ObExternalStatementInterestFrequency1Code",
    "ObExternalStatementInterestRateType1Code",
    "ObExternalStatementInterestType1Code",
    "ObExternalStatementRateType1Code",
    "ObExternalStatementType1Code",
    "ObExternalStatementValueType1Code",
    "ObExternalSwitchStatusCode",
    "ObFeeCategory1Code",
    "ObFeeFrequency1Code0",
    "ObFeeFrequency1Code1",
    "ObFeeFrequency1Code2",
    "ObFeeFrequency1Code3",
    "ObFeeFrequency1Code4",
    "ObFeeType1Code",
    "ObInterestCalculationMethod1Code",
    "ObInterestFixedVariableType1Code",
    "ObInterestRateType1Code0",
    "ObInterestRateType1Code1",
    "ObMerchantDetails1",
    "ObMinMaxType1Code",
    "ObOtherCodeType10",
    "ObOtherCodeType11",
    "ObOtherCodeType12",
    "ObOtherCodeType13",
    "ObOtherCodeType14",
    "ObOtherCodeType15",
    "ObOtherCodeType16",
    "ObOtherCodeType17",
    "ObOtherCodeType18",
    "ObOtherFeeChargeDetailType",
    "ObOverdraftFeeType1Code",
    "ObParty2",
    "ObParty2AddressItem",
    "ObPartyRelationships1",
    "ObPartyRelationships1Account",
    "ObPeriod1Code",
    "ObPostalAddress6",
    "ObRate10",
    "ObRate11",
    "ObReadAccount6",
    "ObReadAccount6Data",
    "ObReadBalance1",
    "ObReadBalance1Data",
    "ObReadBalance1DataBalanceItem",
    "ObReadBalance1DataBalanceItemAmount",
    "ObReadBalance1DataBalanceItemCreditLineItem",
    "ObReadBalance1DataBalanceItemCreditLineItemAmount",
    "ObReadBalance1DataBalanceItemCreditLineItemType",
    "ObReadBeneficiary5",
    "ObReadBeneficiary5Data",
    "ObReadConsentResponse1",
    "ObReadConsentResponse1Data",
    "ObReadConsentResponse1DataPermissionsItem",
    "ObReadConsentResponse1DataStatus",
    "ObReadDataStatement2",
    "ObReadDataTransaction6",
    "ObReadDirectDebit2",
    "ObReadDirectDebit2Data",
    "ObReadDirectDebit2DataDirectDebitItem",
    "ObReadOffer1",
    "ObReadOffer1Data",
    "ObReadOffer1DataOfferItem",
    "ObReadOffer1DataOfferItemAmount",
    "ObReadOffer1DataOfferItemFee",
    "ObReadOffer1DataOfferItemOfferType",
    "ObReadParty2",
    "ObReadParty2Data",
    "ObReadParty3",
    "ObReadParty3Data",
    "ObReadProduct2",
    "ObReadProduct2Data",
    "ObReadProduct2DataProductItem",
    "ObReadProduct2DataProductItemOtherProductType",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterest",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItem",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemDestination",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItem",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemCalculationFrequency",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType",
    "ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandMethod",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterest",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemOtherFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemOtherFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItem",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMaxTermPeriod",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType",
    "ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemTierBandMethod",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItem",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItem",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemOtherFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItem",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemOtherTariffType",
    "ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemTariffType",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraft",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftType",
    "ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemTierBandMethod",
    "ObReadProduct2DataProductItemOtherProductTypeProductDetails",
    "ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod",
    "ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem",
    "ObReadProduct2DataProductItemOtherProductTypeRepayment",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItem",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemOtherFeeTypeItem",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetailItem",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItem",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod",
    "ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType",
    "ObReadProduct2DataProductItemProductType",
    "ObReadScheduledPayment3",
    "ObReadScheduledPayment3Data",
    "ObReadStandingOrder6",
    "ObReadStandingOrder6Data",
    "ObReadStatement2",
    "ObReadTransaction6",
    "ObRisk2",
    "ObScheduledPayment3",
    "ObScheduledPayment3Basic",
    "ObScheduledPayment3Detail",
    "ObStandingOrder6",
    "ObStandingOrder6Basic",
    "ObStandingOrder6Detail",
    "ObStatement2",
    "ObStatement2Basic",
    "ObStatement2BasicStatementBenefitItem",
    "ObStatement2BasicStatementDateTimeItem",
    "ObStatement2BasicStatementFeeItem",
    "ObStatement2BasicStatementInterestItem",
    "ObStatement2BasicStatementRateItem",
    "ObStatement2BasicStatementValueItem",
    "ObStatement2Detail",
    "ObStatement2DetailStatementAmountItem",
    "ObStatement2DetailStatementBenefitItem",
    "ObStatement2DetailStatementDateTimeItem",
    "ObStatement2DetailStatementFeeItem",
    "ObStatement2DetailStatementInterestItem",
    "ObStatement2DetailStatementRateItem",
    "ObStatement2DetailStatementValueItem",
    "ObStatement2StatementAmountItem",
    "ObStatement2StatementBenefitItem",
    "ObStatement2StatementDateTimeItem",
    "ObStatement2StatementFeeItem",
    "ObStatement2StatementInterestItem",
    "ObStatement2StatementRateItem",
    "ObStatement2StatementValueItem",
    "ObSupplementaryData1",
    "ObTransaction6",
    "ObTransaction6Basic",
    "ObTransaction6Detail",
    "ObTransactionCardInstrument1",
    "ObTransactionCardInstrument1AuthorisationType",
    "ObTransactionCardInstrument1CardSchemeName",
    "ObTransactionCashBalance",
    "ObTransactionCashBalanceAmount",
    "ObTransactionMutability1Code",
    "ObbcaData1",
    "ObbcaData1CreditInterest",
    "ObbcaData1CreditInterestTierBandSetItem",
    "ObbcaData1CreditInterestTierBandSetItemCalculationMethod",
    "ObbcaData1CreditInterestTierBandSetItemDestination",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItem",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType",
    "ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency",
    "ObbcaData1CreditInterestTierBandSetItemTierBandMethod",
    "ObbcaData1OtherFeesChargesItem",
    "ObbcaData1OtherFeesChargesItemFeeChargeCapItem",
    "ObbcaData1OtherFeesChargesItemFeeChargeCapItemCappingPeriod",
    "ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem",
    "ObbcaData1OtherFeesChargesItemFeeChargeCapItemMinMaxType",
    "ObbcaData1OtherFeesChargesItemFeeChargeCapItemOtherFeeTypeItem",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItem",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemCalculationFrequency",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeCategory",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemCappingPeriod",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeTypeItem",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemMinMaxType",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeRateType",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeType",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType",
    "ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeTypeFeeCategory",
    "ObbcaData1OtherFeesChargesItemOtherTariffType",
    "ObbcaData1OtherFeesChargesItemTariffType",
    "ObbcaData1Overdraft",
    "ObbcaData1OverdraftOverdraftTierBandSetItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemCappingPeriod",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemCappingPeriod",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage",
    "ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftType",
    "ObbcaData1OverdraftOverdraftTierBandSetItemTierBandMethod",
    "ObbcaData1ProductDetails",
    "ObbcaData1ProductDetailsFeeFreeLengthPeriod",
    "ObbcaData1ProductDetailsSegmentItem",
    "ObpcaData1",
    "ObpcaData1CreditInterest",
    "ObpcaData1CreditInterestTierBandSetItem",
    "ObpcaData1CreditInterestTierBandSetItemCalculationMethod",
    "ObpcaData1CreditInterestTierBandSetItemDestination",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItem",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType",
    "ObpcaData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency",
    "ObpcaData1CreditInterestTierBandSetItemTierBandMethod",
    "ObpcaData1OtherFeesCharges",
    "ObpcaData1OtherFeesChargesFeeChargeCapItem",
    "ObpcaData1OtherFeesChargesFeeChargeCapItemCappingPeriod",
    "ObpcaData1OtherFeesChargesFeeChargeCapItemFeeTypeItem",
    "ObpcaData1OtherFeesChargesFeeChargeCapItemMinMaxType",
    "ObpcaData1OtherFeesChargesFeeChargeCapItemOtherFeeTypeItem",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItem",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemApplicationFrequency",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemCalculationFrequency",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeApplicableRange",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeCategory",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItem",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemCappingPeriod",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemFeeTypeItem",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemMinMaxType",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeRateType",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeType",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherApplicationFrequency",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherCalculationFrequency",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeCategoryType",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeRateType",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeType",
    "ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeTypeFeeCategory",
    "ObpcaData1Overdraft",
    "ObpcaData1OverdraftOverdraftTierBandSetItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapMinMaxType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapOtherFeeTypeItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapMinMaxType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapOtherFeeTypeItem",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage",
    "ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftType",
    "ObpcaData1OverdraftOverdraftTierBandSetItemTierBandMethod",
    "ObpcaData1ProductDetails",
    "ObpcaData1ProductDetailsSegmentItem",
    "OpeningDate",
    "PartyId",
    "PartyNumber",
    "PhoneNumber0",
    "PhoneNumber1",
    "PostCode",
    "PreviousPaymentDateTime",
    "ProprietaryBankTransactionCodeStructure1",
    "Rate",
    "Reference",
    "ScheduledPaymentDateTime",
    "ScheduledPaymentId",
    "SecondaryIdentification",
    "StandingOrderId",
    "StartDateTime",
    "StatementId",
    "StatementReference",
    "StatusUpdateDateTime",
    "StreetName",
    "TownName",
    "TransactionId",
    "TransactionInformation",
    "TransactionReference",
    "Value",
    "ValueDateTime",
]
