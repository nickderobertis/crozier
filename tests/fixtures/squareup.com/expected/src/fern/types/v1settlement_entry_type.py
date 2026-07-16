

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1SettlementEntryType(enum.StrEnum):
    """ """

    ADJUSTMENT = "ADJUSTMENT"
    BALANCE_CHARGE = "BALANCE_CHARGE"
    CHARGE = "CHARGE"
    FREE_PROCESSING = "FREE_PROCESSING"
    HOLD_ADJUSTMENT = "HOLD_ADJUSTMENT"
    PAID_SERVICE_FEE = "PAID_SERVICE_FEE"
    PAID_SERVICE_FEE_REFUND = "PAID_SERVICE_FEE_REFUND"
    REDEMPTION_CODE = "REDEMPTION_CODE"
    REFUND = "REFUND"
    RETURNED_PAYOUT = "RETURNED_PAYOUT"
    SQUARE_CAPITAL_ADVANCE = "SQUARE_CAPITAL_ADVANCE"
    SQUARE_CAPITAL_PAYMENT = "SQUARE_CAPITAL_PAYMENT"
    SQUARE_CAPITAL_REVERSED_PAYMENT = "SQUARE_CAPITAL_REVERSED_PAYMENT"
    SUBSCRIPTION_FEE = "SUBSCRIPTION_FEE"
    SUBSCRIPTION_FEE_REFUND = "SUBSCRIPTION_FEE_REFUND"
    OTHER = "OTHER"
    INCENTED_PAYMENT = "INCENTED_PAYMENT"
    RETURNED_ACH_ENTRY = "RETURNED_ACH_ENTRY"
    RETURNED_SQUARE275 = "RETURNED_SQUARE_275"
    SQUARE275 = "SQUARE_275"
    SQUARE_CARD = "SQUARE_CARD"

    def visit(
        self,
        adjustment: typing.Callable[[], T_Result],
        balance_charge: typing.Callable[[], T_Result],
        charge: typing.Callable[[], T_Result],
        free_processing: typing.Callable[[], T_Result],
        hold_adjustment: typing.Callable[[], T_Result],
        paid_service_fee: typing.Callable[[], T_Result],
        paid_service_fee_refund: typing.Callable[[], T_Result],
        redemption_code: typing.Callable[[], T_Result],
        refund: typing.Callable[[], T_Result],
        returned_payout: typing.Callable[[], T_Result],
        square_capital_advance: typing.Callable[[], T_Result],
        square_capital_payment: typing.Callable[[], T_Result],
        square_capital_reversed_payment: typing.Callable[[], T_Result],
        subscription_fee: typing.Callable[[], T_Result],
        subscription_fee_refund: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        incented_payment: typing.Callable[[], T_Result],
        returned_ach_entry: typing.Callable[[], T_Result],
        returned_square275: typing.Callable[[], T_Result],
        square275: typing.Callable[[], T_Result],
        square_card: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1SettlementEntryType.ADJUSTMENT:
            return adjustment()
        if self is V1SettlementEntryType.BALANCE_CHARGE:
            return balance_charge()
        if self is V1SettlementEntryType.CHARGE:
            return charge()
        if self is V1SettlementEntryType.FREE_PROCESSING:
            return free_processing()
        if self is V1SettlementEntryType.HOLD_ADJUSTMENT:
            return hold_adjustment()
        if self is V1SettlementEntryType.PAID_SERVICE_FEE:
            return paid_service_fee()
        if self is V1SettlementEntryType.PAID_SERVICE_FEE_REFUND:
            return paid_service_fee_refund()
        if self is V1SettlementEntryType.REDEMPTION_CODE:
            return redemption_code()
        if self is V1SettlementEntryType.REFUND:
            return refund()
        if self is V1SettlementEntryType.RETURNED_PAYOUT:
            return returned_payout()
        if self is V1SettlementEntryType.SQUARE_CAPITAL_ADVANCE:
            return square_capital_advance()
        if self is V1SettlementEntryType.SQUARE_CAPITAL_PAYMENT:
            return square_capital_payment()
        if self is V1SettlementEntryType.SQUARE_CAPITAL_REVERSED_PAYMENT:
            return square_capital_reversed_payment()
        if self is V1SettlementEntryType.SUBSCRIPTION_FEE:
            return subscription_fee()
        if self is V1SettlementEntryType.SUBSCRIPTION_FEE_REFUND:
            return subscription_fee_refund()
        if self is V1SettlementEntryType.OTHER:
            return other()
        if self is V1SettlementEntryType.INCENTED_PAYMENT:
            return incented_payment()
        if self is V1SettlementEntryType.RETURNED_ACH_ENTRY:
            return returned_ach_entry()
        if self is V1SettlementEntryType.RETURNED_SQUARE275:
            return returned_square275()
        if self is V1SettlementEntryType.SQUARE275:
            return square275()
        if self is V1SettlementEntryType.SQUARE_CARD:
            return square_card()
