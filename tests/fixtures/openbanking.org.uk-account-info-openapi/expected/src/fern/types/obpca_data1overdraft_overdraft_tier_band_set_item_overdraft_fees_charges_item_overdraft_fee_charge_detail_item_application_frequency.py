

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency(
    str, enum.Enum
):
    """
    Frequency at which the overdraft charge is applied to the account
    """

    ACCOUNT_CLOSING = "AccountClosing"
    ACCOUNT_OPENING = "AccountOpening"
    ACADEMIC_TERM = "AcademicTerm"
    CHARGING_PERIOD = "ChargingPeriod"
    DAILY = "Daily"
    PER_ITEM = "PerItem"
    MONTHLY = "Monthly"
    ON_ACCOUNT_ANNIVERSARY = "OnAccountAnniversary"
    OTHER = "Other"
    PER_HOUR = "PerHour"
    PER_OCCURRENCE = "PerOccurrence"
    PER_SHEET = "PerSheet"
    PER_TRANSACTION = "PerTransaction"
    PER_TRANSACTION_AMOUNT = "PerTransactionAmount"
    PER_TRANSACTION_PERCENTAGE = "PerTransactionPercentage"
    QUARTERLY = "Quarterly"
    SIX_MONTHLY = "SixMonthly"
    STATEMENT_MONTHLY = "StatementMonthly"
    WEEKLY = "Weekly"
    YEARLY = "Yearly"

    def visit(
        self,
        account_closing: typing.Callable[[], T_Result],
        account_opening: typing.Callable[[], T_Result],
        academic_term: typing.Callable[[], T_Result],
        charging_period: typing.Callable[[], T_Result],
        daily: typing.Callable[[], T_Result],
        per_item: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        on_account_anniversary: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        per_hour: typing.Callable[[], T_Result],
        per_occurrence: typing.Callable[[], T_Result],
        per_sheet: typing.Callable[[], T_Result],
        per_transaction: typing.Callable[[], T_Result],
        per_transaction_amount: typing.Callable[[], T_Result],
        per_transaction_percentage: typing.Callable[[], T_Result],
        quarterly: typing.Callable[[], T_Result],
        six_monthly: typing.Callable[[], T_Result],
        statement_monthly: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        yearly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.ACCOUNT_CLOSING
        ):
            return account_closing()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.ACCOUNT_OPENING
        ):
            return account_opening()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.ACADEMIC_TERM
        ):
            return academic_term()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.CHARGING_PERIOD
        ):
            return charging_period()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.DAILY
        ):
            return daily()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.PER_ITEM
        ):
            return per_item()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.MONTHLY
        ):
            return monthly()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.ON_ACCOUNT_ANNIVERSARY
        ):
            return on_account_anniversary()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.OTHER
        ):
            return other()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.PER_HOUR
        ):
            return per_hour()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.PER_OCCURRENCE
        ):
            return per_occurrence()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.PER_SHEET
        ):
            return per_sheet()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.PER_TRANSACTION
        ):
            return per_transaction()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.PER_TRANSACTION_AMOUNT
        ):
            return per_transaction_amount()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.PER_TRANSACTION_PERCENTAGE
        ):
            return per_transaction_percentage()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.QUARTERLY
        ):
            return quarterly()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.SIX_MONTHLY
        ):
            return six_monthly()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.STATEMENT_MONTHLY
        ):
            return statement_monthly()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.WEEKLY
        ):
            return weekly()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency.YEARLY
        ):
            return yearly()
