

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvestmentTransactionSubtype(enum.StrEnum):
    """
    For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema).
    """

    ACCOUNT_FEE = "account fee"
    ADJUSTMENT = "adjustment"
    ASSIGNMENT = "assignment"
    BUY = "buy"
    BUY_TO_COVER = "buy to cover"
    CONTRIBUTION = "contribution"
    DEPOSIT = "deposit"
    DISTRIBUTION = "distribution"
    DIVIDEND = "dividend"
    DIVIDEND_REINVESTMENT = "dividend reinvestment"
    EXERCISE = "exercise"
    EXPIRE = "expire"
    FUND_FEE = "fund fee"
    INTEREST = "interest"
    INTEREST_RECEIVABLE = "interest receivable"
    INTEREST_REINVESTMENT = "interest reinvestment"
    LEGAL_FEE = "legal fee"
    LOAN_PAYMENT = "loan payment"
    LONG_TERM_CAPITAL_GAIN = "long-term capital gain"
    LONG_TERM_CAPITAL_GAIN_REINVESTMENT = "long-term capital gain reinvestment"
    MANAGEMENT_FEE = "management fee"
    MARGIN_EXPENSE = "margin expense"
    MERGER = "merger"
    MISCELLANEOUS_FEE = "miscellaneous fee"
    NON_QUALIFIED_DIVIDEND = "non-qualified dividend"
    NON_RESIDENT_TAX = "non-resident tax"
    PENDING_CREDIT = "pending credit"
    PENDING_DEBIT = "pending debit"
    QUALIFIED_DIVIDEND = "qualified dividend"
    REBALANCE = "rebalance"
    RETURN_OF_PRINCIPAL = "return of principal"
    REQUEST = "request"
    SELL = "sell"
    SELL_SHORT = "sell short"
    SEND = "send"
    SHORT_TERM_CAPITAL_GAIN = "short-term capital gain"
    SHORT_TERM_CAPITAL_GAIN_REINVESTMENT = "short-term capital gain reinvestment"
    SPIN_OFF = "spin off"
    SPLIT = "split"
    STOCK_DISTRIBUTION = "stock distribution"
    TAX = "tax"
    TAX_WITHHELD = "tax withheld"
    TRADE = "trade"
    TRANSFER = "transfer"
    TRANSFER_FEE = "transfer fee"
    TRUST_FEE = "trust fee"
    UNQUALIFIED_GAIN = "unqualified gain"
    WITHDRAWAL = "withdrawal"

    def visit(
        self,
        account_fee: typing.Callable[[], T_Result],
        adjustment: typing.Callable[[], T_Result],
        assignment: typing.Callable[[], T_Result],
        buy: typing.Callable[[], T_Result],
        buy_to_cover: typing.Callable[[], T_Result],
        contribution: typing.Callable[[], T_Result],
        deposit: typing.Callable[[], T_Result],
        distribution: typing.Callable[[], T_Result],
        dividend: typing.Callable[[], T_Result],
        dividend_reinvestment: typing.Callable[[], T_Result],
        exercise: typing.Callable[[], T_Result],
        expire: typing.Callable[[], T_Result],
        fund_fee: typing.Callable[[], T_Result],
        interest: typing.Callable[[], T_Result],
        interest_receivable: typing.Callable[[], T_Result],
        interest_reinvestment: typing.Callable[[], T_Result],
        legal_fee: typing.Callable[[], T_Result],
        loan_payment: typing.Callable[[], T_Result],
        long_term_capital_gain: typing.Callable[[], T_Result],
        long_term_capital_gain_reinvestment: typing.Callable[[], T_Result],
        management_fee: typing.Callable[[], T_Result],
        margin_expense: typing.Callable[[], T_Result],
        merger: typing.Callable[[], T_Result],
        miscellaneous_fee: typing.Callable[[], T_Result],
        non_qualified_dividend: typing.Callable[[], T_Result],
        non_resident_tax: typing.Callable[[], T_Result],
        pending_credit: typing.Callable[[], T_Result],
        pending_debit: typing.Callable[[], T_Result],
        qualified_dividend: typing.Callable[[], T_Result],
        rebalance: typing.Callable[[], T_Result],
        return_of_principal: typing.Callable[[], T_Result],
        request: typing.Callable[[], T_Result],
        sell: typing.Callable[[], T_Result],
        sell_short: typing.Callable[[], T_Result],
        send: typing.Callable[[], T_Result],
        short_term_capital_gain: typing.Callable[[], T_Result],
        short_term_capital_gain_reinvestment: typing.Callable[[], T_Result],
        spin_off: typing.Callable[[], T_Result],
        split: typing.Callable[[], T_Result],
        stock_distribution: typing.Callable[[], T_Result],
        tax: typing.Callable[[], T_Result],
        tax_withheld: typing.Callable[[], T_Result],
        trade: typing.Callable[[], T_Result],
        transfer: typing.Callable[[], T_Result],
        transfer_fee: typing.Callable[[], T_Result],
        trust_fee: typing.Callable[[], T_Result],
        unqualified_gain: typing.Callable[[], T_Result],
        withdrawal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvestmentTransactionSubtype.ACCOUNT_FEE:
            return account_fee()
        if self is InvestmentTransactionSubtype.ADJUSTMENT:
            return adjustment()
        if self is InvestmentTransactionSubtype.ASSIGNMENT:
            return assignment()
        if self is InvestmentTransactionSubtype.BUY:
            return buy()
        if self is InvestmentTransactionSubtype.BUY_TO_COVER:
            return buy_to_cover()
        if self is InvestmentTransactionSubtype.CONTRIBUTION:
            return contribution()
        if self is InvestmentTransactionSubtype.DEPOSIT:
            return deposit()
        if self is InvestmentTransactionSubtype.DISTRIBUTION:
            return distribution()
        if self is InvestmentTransactionSubtype.DIVIDEND:
            return dividend()
        if self is InvestmentTransactionSubtype.DIVIDEND_REINVESTMENT:
            return dividend_reinvestment()
        if self is InvestmentTransactionSubtype.EXERCISE:
            return exercise()
        if self is InvestmentTransactionSubtype.EXPIRE:
            return expire()
        if self is InvestmentTransactionSubtype.FUND_FEE:
            return fund_fee()
        if self is InvestmentTransactionSubtype.INTEREST:
            return interest()
        if self is InvestmentTransactionSubtype.INTEREST_RECEIVABLE:
            return interest_receivable()
        if self is InvestmentTransactionSubtype.INTEREST_REINVESTMENT:
            return interest_reinvestment()
        if self is InvestmentTransactionSubtype.LEGAL_FEE:
            return legal_fee()
        if self is InvestmentTransactionSubtype.LOAN_PAYMENT:
            return loan_payment()
        if self is InvestmentTransactionSubtype.LONG_TERM_CAPITAL_GAIN:
            return long_term_capital_gain()
        if self is InvestmentTransactionSubtype.LONG_TERM_CAPITAL_GAIN_REINVESTMENT:
            return long_term_capital_gain_reinvestment()
        if self is InvestmentTransactionSubtype.MANAGEMENT_FEE:
            return management_fee()
        if self is InvestmentTransactionSubtype.MARGIN_EXPENSE:
            return margin_expense()
        if self is InvestmentTransactionSubtype.MERGER:
            return merger()
        if self is InvestmentTransactionSubtype.MISCELLANEOUS_FEE:
            return miscellaneous_fee()
        if self is InvestmentTransactionSubtype.NON_QUALIFIED_DIVIDEND:
            return non_qualified_dividend()
        if self is InvestmentTransactionSubtype.NON_RESIDENT_TAX:
            return non_resident_tax()
        if self is InvestmentTransactionSubtype.PENDING_CREDIT:
            return pending_credit()
        if self is InvestmentTransactionSubtype.PENDING_DEBIT:
            return pending_debit()
        if self is InvestmentTransactionSubtype.QUALIFIED_DIVIDEND:
            return qualified_dividend()
        if self is InvestmentTransactionSubtype.REBALANCE:
            return rebalance()
        if self is InvestmentTransactionSubtype.RETURN_OF_PRINCIPAL:
            return return_of_principal()
        if self is InvestmentTransactionSubtype.REQUEST:
            return request()
        if self is InvestmentTransactionSubtype.SELL:
            return sell()
        if self is InvestmentTransactionSubtype.SELL_SHORT:
            return sell_short()
        if self is InvestmentTransactionSubtype.SEND:
            return send()
        if self is InvestmentTransactionSubtype.SHORT_TERM_CAPITAL_GAIN:
            return short_term_capital_gain()
        if self is InvestmentTransactionSubtype.SHORT_TERM_CAPITAL_GAIN_REINVESTMENT:
            return short_term_capital_gain_reinvestment()
        if self is InvestmentTransactionSubtype.SPIN_OFF:
            return spin_off()
        if self is InvestmentTransactionSubtype.SPLIT:
            return split()
        if self is InvestmentTransactionSubtype.STOCK_DISTRIBUTION:
            return stock_distribution()
        if self is InvestmentTransactionSubtype.TAX:
            return tax()
        if self is InvestmentTransactionSubtype.TAX_WITHHELD:
            return tax_withheld()
        if self is InvestmentTransactionSubtype.TRADE:
            return trade()
        if self is InvestmentTransactionSubtype.TRANSFER:
            return transfer()
        if self is InvestmentTransactionSubtype.TRANSFER_FEE:
            return transfer_fee()
        if self is InvestmentTransactionSubtype.TRUST_FEE:
            return trust_fee()
        if self is InvestmentTransactionSubtype.UNQUALIFIED_GAIN:
            return unqualified_gain()
        if self is InvestmentTransactionSubtype.WITHDRAWAL:
            return withdrawal()
