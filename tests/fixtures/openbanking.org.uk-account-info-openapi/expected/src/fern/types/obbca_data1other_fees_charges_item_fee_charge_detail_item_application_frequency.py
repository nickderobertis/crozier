

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency(str, enum.Enum):
    """
    How frequently the fee/charge is applied to the account
    """

    ON_CLOSING = "OnClosing"
    ON_OPENING = "OnOpening"
    CHARGING_PERIOD = "ChargingPeriod"
    DAILY = "Daily"
    PER_ITEM = "PerItem"
    MONTHLY = "Monthly"
    ON_ANNIVERSARY = "OnAnniversary"
    OTHER = "Other"
    PER_HUNDRED_POUNDS = "PerHundredPounds"
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
        on_closing: typing.Callable[[], T_Result],
        on_opening: typing.Callable[[], T_Result],
        charging_period: typing.Callable[[], T_Result],
        daily: typing.Callable[[], T_Result],
        per_item: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        on_anniversary: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        per_hundred_pounds: typing.Callable[[], T_Result],
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
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.ON_CLOSING:
            return on_closing()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.ON_OPENING:
            return on_opening()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.CHARGING_PERIOD:
            return charging_period()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.DAILY:
            return daily()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.PER_ITEM:
            return per_item()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.MONTHLY:
            return monthly()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.ON_ANNIVERSARY:
            return on_anniversary()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.OTHER:
            return other()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.PER_HUNDRED_POUNDS:
            return per_hundred_pounds()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.PER_HOUR:
            return per_hour()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.PER_OCCURRENCE:
            return per_occurrence()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.PER_SHEET:
            return per_sheet()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.PER_TRANSACTION:
            return per_transaction()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.PER_TRANSACTION_AMOUNT:
            return per_transaction_amount()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.PER_TRANSACTION_PERCENTAGE:
            return per_transaction_percentage()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.QUARTERLY:
            return quarterly()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.SIX_MONTHLY:
            return six_monthly()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.STATEMENT_MONTHLY:
            return statement_monthly()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.WEEKLY:
            return weekly()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency.YEARLY:
            return yearly()
