

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetMappingValuesKeyRequestKey(enum.StrEnum):
    ID_TYPE = "idType"
    EXCH_CODE = "exchCode"
    MIC_CODE = "micCode"
    CURRENCY = "currency"
    MARKET_SEC_DES = "marketSecDes"
    SECURITY_TYPE = "securityType"
    SECURITY_TYPE2 = "securityType2"

    def visit(
        self,
        id_type: typing.Callable[[], T_Result],
        exch_code: typing.Callable[[], T_Result],
        mic_code: typing.Callable[[], T_Result],
        currency: typing.Callable[[], T_Result],
        market_sec_des: typing.Callable[[], T_Result],
        security_type: typing.Callable[[], T_Result],
        security_type2: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetMappingValuesKeyRequestKey.ID_TYPE:
            return id_type()
        if self is GetMappingValuesKeyRequestKey.EXCH_CODE:
            return exch_code()
        if self is GetMappingValuesKeyRequestKey.MIC_CODE:
            return mic_code()
        if self is GetMappingValuesKeyRequestKey.CURRENCY:
            return currency()
        if self is GetMappingValuesKeyRequestKey.MARKET_SEC_DES:
            return market_sec_des()
        if self is GetMappingValuesKeyRequestKey.SECURITY_TYPE:
            return security_type()
        if self is GetMappingValuesKeyRequestKey.SECURITY_TYPE2:
            return security_type2()
