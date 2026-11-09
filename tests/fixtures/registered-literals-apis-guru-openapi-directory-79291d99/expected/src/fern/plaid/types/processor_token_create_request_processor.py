

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ProcessorTokenCreateRequestProcessor(enum.StrEnum):
    """
    The processor you are integrating with.
    """

    DWOLLA = "dwolla"
    GALILEO = "galileo"
    MODERN_TREASURY = "modern_treasury"
    OCROLUS = "ocrolus"
    PRIME_TRUST = "prime_trust"
    VESTA = "vesta"
    DRIVEWEALTH = "drivewealth"
    VOPAY = "vopay"
    ACHQ = "achq"
    CHECK = "check"
    CHECKBOOK = "checkbook"
    CIRCLE = "circle"
    SILA_MONEY = "sila_money"
    RIZE = "rize"
    SVB_API = "svb_api"
    UNIT = "unit"
    WYRE = "wyre"
    LITHIC = "lithic"
    ALPACA = "alpaca"
    ASTRA = "astra"
    MOOV = "moov"
    TREASURY_PRIME = "treasury_prime"
    MARQETA = "marqeta"
    CHECKOUT = "checkout"
    SOLID = "solid"
    HIGHNOTE = "highnote"
    APEX_CLEARING = "apex_clearing"
    GUSTO = "gusto"
    ADYEN = "adyen"
    ATOMIC = "atomic"
    I2C = "i2c"
    WEPAY = "wepay"
    RISKIFIED = "riskified"
    UTB = "utb"
    ADP_ROLL = "adp_roll"
    FORTRESS_TRUST = "fortress_trust"

    def visit(
        self,
        dwolla: typing.Callable[[], T_Result],
        galileo: typing.Callable[[], T_Result],
        modern_treasury: typing.Callable[[], T_Result],
        ocrolus: typing.Callable[[], T_Result],
        prime_trust: typing.Callable[[], T_Result],
        vesta: typing.Callable[[], T_Result],
        drivewealth: typing.Callable[[], T_Result],
        vopay: typing.Callable[[], T_Result],
        achq: typing.Callable[[], T_Result],
        check: typing.Callable[[], T_Result],
        checkbook: typing.Callable[[], T_Result],
        circle: typing.Callable[[], T_Result],
        sila_money: typing.Callable[[], T_Result],
        rize: typing.Callable[[], T_Result],
        svb_api: typing.Callable[[], T_Result],
        unit: typing.Callable[[], T_Result],
        wyre: typing.Callable[[], T_Result],
        lithic: typing.Callable[[], T_Result],
        alpaca: typing.Callable[[], T_Result],
        astra: typing.Callable[[], T_Result],
        moov: typing.Callable[[], T_Result],
        treasury_prime: typing.Callable[[], T_Result],
        marqeta: typing.Callable[[], T_Result],
        checkout: typing.Callable[[], T_Result],
        solid: typing.Callable[[], T_Result],
        highnote: typing.Callable[[], T_Result],
        apex_clearing: typing.Callable[[], T_Result],
        gusto: typing.Callable[[], T_Result],
        adyen: typing.Callable[[], T_Result],
        atomic: typing.Callable[[], T_Result],
        i2c: typing.Callable[[], T_Result],
        wepay: typing.Callable[[], T_Result],
        riskified: typing.Callable[[], T_Result],
        utb: typing.Callable[[], T_Result],
        adp_roll: typing.Callable[[], T_Result],
        fortress_trust: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProcessorTokenCreateRequestProcessor.DWOLLA:
            return dwolla()
        if self is ProcessorTokenCreateRequestProcessor.GALILEO:
            return galileo()
        if self is ProcessorTokenCreateRequestProcessor.MODERN_TREASURY:
            return modern_treasury()
        if self is ProcessorTokenCreateRequestProcessor.OCROLUS:
            return ocrolus()
        if self is ProcessorTokenCreateRequestProcessor.PRIME_TRUST:
            return prime_trust()
        if self is ProcessorTokenCreateRequestProcessor.VESTA:
            return vesta()
        if self is ProcessorTokenCreateRequestProcessor.DRIVEWEALTH:
            return drivewealth()
        if self is ProcessorTokenCreateRequestProcessor.VOPAY:
            return vopay()
        if self is ProcessorTokenCreateRequestProcessor.ACHQ:
            return achq()
        if self is ProcessorTokenCreateRequestProcessor.CHECK:
            return check()
        if self is ProcessorTokenCreateRequestProcessor.CHECKBOOK:
            return checkbook()
        if self is ProcessorTokenCreateRequestProcessor.CIRCLE:
            return circle()
        if self is ProcessorTokenCreateRequestProcessor.SILA_MONEY:
            return sila_money()
        if self is ProcessorTokenCreateRequestProcessor.RIZE:
            return rize()
        if self is ProcessorTokenCreateRequestProcessor.SVB_API:
            return svb_api()
        if self is ProcessorTokenCreateRequestProcessor.UNIT:
            return unit()
        if self is ProcessorTokenCreateRequestProcessor.WYRE:
            return wyre()
        if self is ProcessorTokenCreateRequestProcessor.LITHIC:
            return lithic()
        if self is ProcessorTokenCreateRequestProcessor.ALPACA:
            return alpaca()
        if self is ProcessorTokenCreateRequestProcessor.ASTRA:
            return astra()
        if self is ProcessorTokenCreateRequestProcessor.MOOV:
            return moov()
        if self is ProcessorTokenCreateRequestProcessor.TREASURY_PRIME:
            return treasury_prime()
        if self is ProcessorTokenCreateRequestProcessor.MARQETA:
            return marqeta()
        if self is ProcessorTokenCreateRequestProcessor.CHECKOUT:
            return checkout()
        if self is ProcessorTokenCreateRequestProcessor.SOLID:
            return solid()
        if self is ProcessorTokenCreateRequestProcessor.HIGHNOTE:
            return highnote()
        if self is ProcessorTokenCreateRequestProcessor.APEX_CLEARING:
            return apex_clearing()
        if self is ProcessorTokenCreateRequestProcessor.GUSTO:
            return gusto()
        if self is ProcessorTokenCreateRequestProcessor.ADYEN:
            return adyen()
        if self is ProcessorTokenCreateRequestProcessor.ATOMIC:
            return atomic()
        if self is ProcessorTokenCreateRequestProcessor.I2C:
            return i2c()
        if self is ProcessorTokenCreateRequestProcessor.WEPAY:
            return wepay()
        if self is ProcessorTokenCreateRequestProcessor.RISKIFIED:
            return riskified()
        if self is ProcessorTokenCreateRequestProcessor.UTB:
            return utb()
        if self is ProcessorTokenCreateRequestProcessor.ADP_ROLL:
            return adp_roll()
        if self is ProcessorTokenCreateRequestProcessor.FORTRESS_TRUST:
            return fortress_trust()
