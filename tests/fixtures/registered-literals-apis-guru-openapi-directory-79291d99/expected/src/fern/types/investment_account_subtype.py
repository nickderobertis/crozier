

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvestmentAccountSubtype(enum.StrEnum):
    """
    Valid account subtypes for investment accounts. For a list containing descriptions of each subtype, see [Account schemas](https://plaid.com/docs/api/accounts/#StandaloneAccountType-investment).
    """

    FIVE_HUNDRED_TWENTY_NINE = "529"
    FOUR_HUNDRED_ONE_A = "401a"
    FOUR_HUNDRED_ONE_K = "401k"
    FOUR_HUNDRED_THREE_B = "403B"
    FOUR_HUNDRED_FIFTY_SEVEN_B = "457b"
    BROKERAGE = "brokerage"
    CASH_ISA = "cash isa"
    CRYPTO_EXCHANGE = "crypto exchange"
    EDUCATION_SAVINGS_ACCOUNT = "education savings account"
    FIXED_ANNUITY = "fixed annuity"
    GIC = "gic"
    HEALTH_REIMBURSEMENT_ARRANGEMENT = "health reimbursement arrangement"
    HSA = "hsa"
    IRA = "ira"
    ISA = "isa"
    KEOGH = "keogh"
    LIF = "lif"
    LIFE_INSURANCE = "life insurance"
    LIRA = "lira"
    LRIF = "lrif"
    LRSP = "lrsp"
    MUTUAL_FUND = "mutual fund"
    NON_CUSTODIAL_WALLET = "non-custodial wallet"
    NON_TAXABLE_BROKERAGE_ACCOUNT = "non-taxable brokerage account"
    OTHER = "other"
    OTHER_ANNUITY = "other annuity"
    OTHER_INSURANCE = "other insurance"
    PENSION = "pension"
    PRIF = "prif"
    PROFIT_SHARING_PLAN = "profit sharing plan"
    QSHR = "qshr"
    RDSP = "rdsp"
    RESP = "resp"
    RETIREMENT = "retirement"
    RLIF = "rlif"
    ROTH = "roth"
    ROTH401K = "roth 401k"
    RRIF = "rrif"
    RRSP = "rrsp"
    SARSEP = "sarsep"
    SEP_IRA = "sep ira"
    SIMPLE_IRA = "simple ira"
    SIPP = "sipp"
    STOCK_PLAN = "stock plan"
    TFSA = "tfsa"
    TRUST = "trust"
    UGMA = "ugma"
    UTMA = "utma"
    VARIABLE_ANNUITY = "variable annuity"
    ALL = "all"

    def visit(
        self,
        five_hundred_twenty_nine: typing.Callable[[], T_Result],
        four_hundred_one_a: typing.Callable[[], T_Result],
        four_hundred_one_k: typing.Callable[[], T_Result],
        four_hundred_three_b: typing.Callable[[], T_Result],
        four_hundred_fifty_seven_b: typing.Callable[[], T_Result],
        brokerage: typing.Callable[[], T_Result],
        cash_isa: typing.Callable[[], T_Result],
        crypto_exchange: typing.Callable[[], T_Result],
        education_savings_account: typing.Callable[[], T_Result],
        fixed_annuity: typing.Callable[[], T_Result],
        gic: typing.Callable[[], T_Result],
        health_reimbursement_arrangement: typing.Callable[[], T_Result],
        hsa: typing.Callable[[], T_Result],
        ira: typing.Callable[[], T_Result],
        isa: typing.Callable[[], T_Result],
        keogh: typing.Callable[[], T_Result],
        lif: typing.Callable[[], T_Result],
        life_insurance: typing.Callable[[], T_Result],
        lira: typing.Callable[[], T_Result],
        lrif: typing.Callable[[], T_Result],
        lrsp: typing.Callable[[], T_Result],
        mutual_fund: typing.Callable[[], T_Result],
        non_custodial_wallet: typing.Callable[[], T_Result],
        non_taxable_brokerage_account: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        other_annuity: typing.Callable[[], T_Result],
        other_insurance: typing.Callable[[], T_Result],
        pension: typing.Callable[[], T_Result],
        prif: typing.Callable[[], T_Result],
        profit_sharing_plan: typing.Callable[[], T_Result],
        qshr: typing.Callable[[], T_Result],
        rdsp: typing.Callable[[], T_Result],
        resp: typing.Callable[[], T_Result],
        retirement: typing.Callable[[], T_Result],
        rlif: typing.Callable[[], T_Result],
        roth: typing.Callable[[], T_Result],
        roth401k: typing.Callable[[], T_Result],
        rrif: typing.Callable[[], T_Result],
        rrsp: typing.Callable[[], T_Result],
        sarsep: typing.Callable[[], T_Result],
        sep_ira: typing.Callable[[], T_Result],
        simple_ira: typing.Callable[[], T_Result],
        sipp: typing.Callable[[], T_Result],
        stock_plan: typing.Callable[[], T_Result],
        tfsa: typing.Callable[[], T_Result],
        trust: typing.Callable[[], T_Result],
        ugma: typing.Callable[[], T_Result],
        utma: typing.Callable[[], T_Result],
        variable_annuity: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvestmentAccountSubtype.FIVE_HUNDRED_TWENTY_NINE:
            return five_hundred_twenty_nine()
        if self is InvestmentAccountSubtype.FOUR_HUNDRED_ONE_A:
            return four_hundred_one_a()
        if self is InvestmentAccountSubtype.FOUR_HUNDRED_ONE_K:
            return four_hundred_one_k()
        if self is InvestmentAccountSubtype.FOUR_HUNDRED_THREE_B:
            return four_hundred_three_b()
        if self is InvestmentAccountSubtype.FOUR_HUNDRED_FIFTY_SEVEN_B:
            return four_hundred_fifty_seven_b()
        if self is InvestmentAccountSubtype.BROKERAGE:
            return brokerage()
        if self is InvestmentAccountSubtype.CASH_ISA:
            return cash_isa()
        if self is InvestmentAccountSubtype.CRYPTO_EXCHANGE:
            return crypto_exchange()
        if self is InvestmentAccountSubtype.EDUCATION_SAVINGS_ACCOUNT:
            return education_savings_account()
        if self is InvestmentAccountSubtype.FIXED_ANNUITY:
            return fixed_annuity()
        if self is InvestmentAccountSubtype.GIC:
            return gic()
        if self is InvestmentAccountSubtype.HEALTH_REIMBURSEMENT_ARRANGEMENT:
            return health_reimbursement_arrangement()
        if self is InvestmentAccountSubtype.HSA:
            return hsa()
        if self is InvestmentAccountSubtype.IRA:
            return ira()
        if self is InvestmentAccountSubtype.ISA:
            return isa()
        if self is InvestmentAccountSubtype.KEOGH:
            return keogh()
        if self is InvestmentAccountSubtype.LIF:
            return lif()
        if self is InvestmentAccountSubtype.LIFE_INSURANCE:
            return life_insurance()
        if self is InvestmentAccountSubtype.LIRA:
            return lira()
        if self is InvestmentAccountSubtype.LRIF:
            return lrif()
        if self is InvestmentAccountSubtype.LRSP:
            return lrsp()
        if self is InvestmentAccountSubtype.MUTUAL_FUND:
            return mutual_fund()
        if self is InvestmentAccountSubtype.NON_CUSTODIAL_WALLET:
            return non_custodial_wallet()
        if self is InvestmentAccountSubtype.NON_TAXABLE_BROKERAGE_ACCOUNT:
            return non_taxable_brokerage_account()
        if self is InvestmentAccountSubtype.OTHER:
            return other()
        if self is InvestmentAccountSubtype.OTHER_ANNUITY:
            return other_annuity()
        if self is InvestmentAccountSubtype.OTHER_INSURANCE:
            return other_insurance()
        if self is InvestmentAccountSubtype.PENSION:
            return pension()
        if self is InvestmentAccountSubtype.PRIF:
            return prif()
        if self is InvestmentAccountSubtype.PROFIT_SHARING_PLAN:
            return profit_sharing_plan()
        if self is InvestmentAccountSubtype.QSHR:
            return qshr()
        if self is InvestmentAccountSubtype.RDSP:
            return rdsp()
        if self is InvestmentAccountSubtype.RESP:
            return resp()
        if self is InvestmentAccountSubtype.RETIREMENT:
            return retirement()
        if self is InvestmentAccountSubtype.RLIF:
            return rlif()
        if self is InvestmentAccountSubtype.ROTH:
            return roth()
        if self is InvestmentAccountSubtype.ROTH401K:
            return roth401k()
        if self is InvestmentAccountSubtype.RRIF:
            return rrif()
        if self is InvestmentAccountSubtype.RRSP:
            return rrsp()
        if self is InvestmentAccountSubtype.SARSEP:
            return sarsep()
        if self is InvestmentAccountSubtype.SEP_IRA:
            return sep_ira()
        if self is InvestmentAccountSubtype.SIMPLE_IRA:
            return simple_ira()
        if self is InvestmentAccountSubtype.SIPP:
            return sipp()
        if self is InvestmentAccountSubtype.STOCK_PLAN:
            return stock_plan()
        if self is InvestmentAccountSubtype.TFSA:
            return tfsa()
        if self is InvestmentAccountSubtype.TRUST:
            return trust()
        if self is InvestmentAccountSubtype.UGMA:
            return ugma()
        if self is InvestmentAccountSubtype.UTMA:
            return utma()
        if self is InvestmentAccountSubtype.VARIABLE_ANNUITY:
            return variable_annuity()
        if self is InvestmentAccountSubtype.ALL:
            return all_()
