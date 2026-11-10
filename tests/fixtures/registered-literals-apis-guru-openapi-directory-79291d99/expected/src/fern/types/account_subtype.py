

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountSubtype(enum.StrEnum):
    """
    See the [Account type schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full listing of account types and corresponding subtypes.
    """

    FOUR_HUNDRED_ONE_A = "401a"
    FOUR_HUNDRED_ONE_K = "401k"
    FOUR_HUNDRED_THREE_B = "403B"
    FOUR_HUNDRED_FIFTY_SEVEN_B = "457b"
    FIVE_HUNDRED_TWENTY_NINE = "529"
    BROKERAGE = "brokerage"
    CASH_ISA = "cash isa"
    CRYPTO_EXCHANGE = "crypto exchange"
    EDUCATION_SAVINGS_ACCOUNT = "education savings account"
    EBT = "ebt"
    FIXED_ANNUITY = "fixed annuity"
    GIC = "gic"
    HEALTH_REIMBURSEMENT_ARRANGEMENT = "health reimbursement arrangement"
    HSA = "hsa"
    ISA = "isa"
    IRA = "ira"
    LIF = "lif"
    LIFE_INSURANCE = "life insurance"
    LIRA = "lira"
    LRIF = "lrif"
    LRSP = "lrsp"
    NON_CUSTODIAL_WALLET = "non-custodial wallet"
    NON_TAXABLE_BROKERAGE_ACCOUNT = "non-taxable brokerage account"
    OTHER = "other"
    OTHER_INSURANCE = "other insurance"
    OTHER_ANNUITY = "other annuity"
    PRIF = "prif"
    RDSP = "rdsp"
    RESP = "resp"
    RLIF = "rlif"
    RRIF = "rrif"
    PENSION = "pension"
    PROFIT_SHARING_PLAN = "profit sharing plan"
    RETIREMENT = "retirement"
    ROTH = "roth"
    ROTH401K = "roth 401k"
    RRSP = "rrsp"
    SEP_IRA = "sep ira"
    SIMPLE_IRA = "simple ira"
    SIPP = "sipp"
    STOCK_PLAN = "stock plan"
    THRIFT_SAVINGS_PLAN = "thrift savings plan"
    TFSA = "tfsa"
    TRUST = "trust"
    UGMA = "ugma"
    UTMA = "utma"
    VARIABLE_ANNUITY = "variable annuity"
    CREDIT_CARD = "credit card"
    PAYPAL = "paypal"
    CD = "cd"
    CHECKING = "checking"
    SAVINGS = "savings"
    MONEY_MARKET = "money market"
    PREPAID = "prepaid"
    AUTO = "auto"
    BUSINESS = "business"
    COMMERCIAL = "commercial"
    CONSTRUCTION = "construction"
    CONSUMER = "consumer"
    HOME_EQUITY = "home equity"
    LOAN = "loan"
    MORTGAGE = "mortgage"
    OVERDRAFT = "overdraft"
    LINE_OF_CREDIT = "line of credit"
    STUDENT = "student"
    CASH_MANAGEMENT = "cash management"
    KEOGH = "keogh"
    MUTUAL_FUND = "mutual fund"
    RECURRING = "recurring"
    REWARDS = "rewards"
    SAFE_DEPOSIT = "safe deposit"
    SARSEP = "sarsep"
    PAYROLL = "payroll"

    def visit(
        self,
        four_hundred_one_a: typing.Callable[[], T_Result],
        four_hundred_one_k: typing.Callable[[], T_Result],
        four_hundred_three_b: typing.Callable[[], T_Result],
        four_hundred_fifty_seven_b: typing.Callable[[], T_Result],
        five_hundred_twenty_nine: typing.Callable[[], T_Result],
        brokerage: typing.Callable[[], T_Result],
        cash_isa: typing.Callable[[], T_Result],
        crypto_exchange: typing.Callable[[], T_Result],
        education_savings_account: typing.Callable[[], T_Result],
        ebt: typing.Callable[[], T_Result],
        fixed_annuity: typing.Callable[[], T_Result],
        gic: typing.Callable[[], T_Result],
        health_reimbursement_arrangement: typing.Callable[[], T_Result],
        hsa: typing.Callable[[], T_Result],
        isa: typing.Callable[[], T_Result],
        ira: typing.Callable[[], T_Result],
        lif: typing.Callable[[], T_Result],
        life_insurance: typing.Callable[[], T_Result],
        lira: typing.Callable[[], T_Result],
        lrif: typing.Callable[[], T_Result],
        lrsp: typing.Callable[[], T_Result],
        non_custodial_wallet: typing.Callable[[], T_Result],
        non_taxable_brokerage_account: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        other_insurance: typing.Callable[[], T_Result],
        other_annuity: typing.Callable[[], T_Result],
        prif: typing.Callable[[], T_Result],
        rdsp: typing.Callable[[], T_Result],
        resp: typing.Callable[[], T_Result],
        rlif: typing.Callable[[], T_Result],
        rrif: typing.Callable[[], T_Result],
        pension: typing.Callable[[], T_Result],
        profit_sharing_plan: typing.Callable[[], T_Result],
        retirement: typing.Callable[[], T_Result],
        roth: typing.Callable[[], T_Result],
        roth401k: typing.Callable[[], T_Result],
        rrsp: typing.Callable[[], T_Result],
        sep_ira: typing.Callable[[], T_Result],
        simple_ira: typing.Callable[[], T_Result],
        sipp: typing.Callable[[], T_Result],
        stock_plan: typing.Callable[[], T_Result],
        thrift_savings_plan: typing.Callable[[], T_Result],
        tfsa: typing.Callable[[], T_Result],
        trust: typing.Callable[[], T_Result],
        ugma: typing.Callable[[], T_Result],
        utma: typing.Callable[[], T_Result],
        variable_annuity: typing.Callable[[], T_Result],
        credit_card: typing.Callable[[], T_Result],
        paypal: typing.Callable[[], T_Result],
        cd: typing.Callable[[], T_Result],
        checking: typing.Callable[[], T_Result],
        savings: typing.Callable[[], T_Result],
        money_market: typing.Callable[[], T_Result],
        prepaid: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
        commercial: typing.Callable[[], T_Result],
        construction: typing.Callable[[], T_Result],
        consumer: typing.Callable[[], T_Result],
        home_equity: typing.Callable[[], T_Result],
        loan: typing.Callable[[], T_Result],
        mortgage: typing.Callable[[], T_Result],
        overdraft: typing.Callable[[], T_Result],
        line_of_credit: typing.Callable[[], T_Result],
        student: typing.Callable[[], T_Result],
        cash_management: typing.Callable[[], T_Result],
        keogh: typing.Callable[[], T_Result],
        mutual_fund: typing.Callable[[], T_Result],
        recurring: typing.Callable[[], T_Result],
        rewards: typing.Callable[[], T_Result],
        safe_deposit: typing.Callable[[], T_Result],
        sarsep: typing.Callable[[], T_Result],
        payroll: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountSubtype.FOUR_HUNDRED_ONE_A:
            return four_hundred_one_a()
        if self is AccountSubtype.FOUR_HUNDRED_ONE_K:
            return four_hundred_one_k()
        if self is AccountSubtype.FOUR_HUNDRED_THREE_B:
            return four_hundred_three_b()
        if self is AccountSubtype.FOUR_HUNDRED_FIFTY_SEVEN_B:
            return four_hundred_fifty_seven_b()
        if self is AccountSubtype.FIVE_HUNDRED_TWENTY_NINE:
            return five_hundred_twenty_nine()
        if self is AccountSubtype.BROKERAGE:
            return brokerage()
        if self is AccountSubtype.CASH_ISA:
            return cash_isa()
        if self is AccountSubtype.CRYPTO_EXCHANGE:
            return crypto_exchange()
        if self is AccountSubtype.EDUCATION_SAVINGS_ACCOUNT:
            return education_savings_account()
        if self is AccountSubtype.EBT:
            return ebt()
        if self is AccountSubtype.FIXED_ANNUITY:
            return fixed_annuity()
        if self is AccountSubtype.GIC:
            return gic()
        if self is AccountSubtype.HEALTH_REIMBURSEMENT_ARRANGEMENT:
            return health_reimbursement_arrangement()
        if self is AccountSubtype.HSA:
            return hsa()
        if self is AccountSubtype.ISA:
            return isa()
        if self is AccountSubtype.IRA:
            return ira()
        if self is AccountSubtype.LIF:
            return lif()
        if self is AccountSubtype.LIFE_INSURANCE:
            return life_insurance()
        if self is AccountSubtype.LIRA:
            return lira()
        if self is AccountSubtype.LRIF:
            return lrif()
        if self is AccountSubtype.LRSP:
            return lrsp()
        if self is AccountSubtype.NON_CUSTODIAL_WALLET:
            return non_custodial_wallet()
        if self is AccountSubtype.NON_TAXABLE_BROKERAGE_ACCOUNT:
            return non_taxable_brokerage_account()
        if self is AccountSubtype.OTHER:
            return other()
        if self is AccountSubtype.OTHER_INSURANCE:
            return other_insurance()
        if self is AccountSubtype.OTHER_ANNUITY:
            return other_annuity()
        if self is AccountSubtype.PRIF:
            return prif()
        if self is AccountSubtype.RDSP:
            return rdsp()
        if self is AccountSubtype.RESP:
            return resp()
        if self is AccountSubtype.RLIF:
            return rlif()
        if self is AccountSubtype.RRIF:
            return rrif()
        if self is AccountSubtype.PENSION:
            return pension()
        if self is AccountSubtype.PROFIT_SHARING_PLAN:
            return profit_sharing_plan()
        if self is AccountSubtype.RETIREMENT:
            return retirement()
        if self is AccountSubtype.ROTH:
            return roth()
        if self is AccountSubtype.ROTH401K:
            return roth401k()
        if self is AccountSubtype.RRSP:
            return rrsp()
        if self is AccountSubtype.SEP_IRA:
            return sep_ira()
        if self is AccountSubtype.SIMPLE_IRA:
            return simple_ira()
        if self is AccountSubtype.SIPP:
            return sipp()
        if self is AccountSubtype.STOCK_PLAN:
            return stock_plan()
        if self is AccountSubtype.THRIFT_SAVINGS_PLAN:
            return thrift_savings_plan()
        if self is AccountSubtype.TFSA:
            return tfsa()
        if self is AccountSubtype.TRUST:
            return trust()
        if self is AccountSubtype.UGMA:
            return ugma()
        if self is AccountSubtype.UTMA:
            return utma()
        if self is AccountSubtype.VARIABLE_ANNUITY:
            return variable_annuity()
        if self is AccountSubtype.CREDIT_CARD:
            return credit_card()
        if self is AccountSubtype.PAYPAL:
            return paypal()
        if self is AccountSubtype.CD:
            return cd()
        if self is AccountSubtype.CHECKING:
            return checking()
        if self is AccountSubtype.SAVINGS:
            return savings()
        if self is AccountSubtype.MONEY_MARKET:
            return money_market()
        if self is AccountSubtype.PREPAID:
            return prepaid()
        if self is AccountSubtype.AUTO:
            return auto()
        if self is AccountSubtype.BUSINESS:
            return business()
        if self is AccountSubtype.COMMERCIAL:
            return commercial()
        if self is AccountSubtype.CONSTRUCTION:
            return construction()
        if self is AccountSubtype.CONSUMER:
            return consumer()
        if self is AccountSubtype.HOME_EQUITY:
            return home_equity()
        if self is AccountSubtype.LOAN:
            return loan()
        if self is AccountSubtype.MORTGAGE:
            return mortgage()
        if self is AccountSubtype.OVERDRAFT:
            return overdraft()
        if self is AccountSubtype.LINE_OF_CREDIT:
            return line_of_credit()
        if self is AccountSubtype.STUDENT:
            return student()
        if self is AccountSubtype.CASH_MANAGEMENT:
            return cash_management()
        if self is AccountSubtype.KEOGH:
            return keogh()
        if self is AccountSubtype.MUTUAL_FUND:
            return mutual_fund()
        if self is AccountSubtype.RECURRING:
            return recurring()
        if self is AccountSubtype.REWARDS:
            return rewards()
        if self is AccountSubtype.SAFE_DEPOSIT:
            return safe_deposit()
        if self is AccountSubtype.SARSEP:
            return sarsep()
        if self is AccountSubtype.PAYROLL:
            return payroll()
