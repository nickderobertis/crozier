

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GiftCardActivityType(str, enum.Enum):
    """ """

    ACTIVATE = "ACTIVATE"
    LOAD = "LOAD"
    REDEEM = "REDEEM"
    CLEAR_BALANCE = "CLEAR_BALANCE"
    DEACTIVATE = "DEACTIVATE"
    ADJUST_INCREMENT = "ADJUST_INCREMENT"
    ADJUST_DECREMENT = "ADJUST_DECREMENT"
    REFUND = "REFUND"
    UNLINKED_ACTIVITY_REFUND = "UNLINKED_ACTIVITY_REFUND"
    IMPORT = "IMPORT"
    BLOCK = "BLOCK"
    UNBLOCK = "UNBLOCK"
    IMPORT_REVERSAL = "IMPORT_REVERSAL"

    def visit(
        self,
        activate: typing.Callable[[], T_Result],
        load: typing.Callable[[], T_Result],
        redeem: typing.Callable[[], T_Result],
        clear_balance: typing.Callable[[], T_Result],
        deactivate: typing.Callable[[], T_Result],
        adjust_increment: typing.Callable[[], T_Result],
        adjust_decrement: typing.Callable[[], T_Result],
        refund: typing.Callable[[], T_Result],
        unlinked_activity_refund: typing.Callable[[], T_Result],
        import_: typing.Callable[[], T_Result],
        block: typing.Callable[[], T_Result],
        unblock: typing.Callable[[], T_Result],
        import_reversal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GiftCardActivityType.ACTIVATE:
            return activate()
        if self is GiftCardActivityType.LOAD:
            return load()
        if self is GiftCardActivityType.REDEEM:
            return redeem()
        if self is GiftCardActivityType.CLEAR_BALANCE:
            return clear_balance()
        if self is GiftCardActivityType.DEACTIVATE:
            return deactivate()
        if self is GiftCardActivityType.ADJUST_INCREMENT:
            return adjust_increment()
        if self is GiftCardActivityType.ADJUST_DECREMENT:
            return adjust_decrement()
        if self is GiftCardActivityType.REFUND:
            return refund()
        if self is GiftCardActivityType.UNLINKED_ACTIVITY_REFUND:
            return unlinked_activity_refund()
        if self is GiftCardActivityType.IMPORT:
            return import_()
        if self is GiftCardActivityType.BLOCK:
            return block()
        if self is GiftCardActivityType.UNBLOCK:
            return unblock()
        if self is GiftCardActivityType.IMPORT_REVERSAL:
            return import_reversal()
