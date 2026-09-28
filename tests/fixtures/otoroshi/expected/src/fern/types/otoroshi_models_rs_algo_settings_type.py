

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtoroshiModelsRsAlgoSettingsType(enum.StrEnum):
    """
    the kind of algosettings
    """

    HS_ALGO_SETTINGS = "HSAlgoSettings"
    RS_ALGO_SETTINGS = "RSAlgoSettings"
    ES_ALGO_SETTINGS = "ESAlgoSettings"
    JWKS_ALGO_SETTINGS = "JWKSAlgoSettings"
    RSAKP_ALGO_SETTINGS = "RSAKPAlgoSettings"
    ESKP_ALGO_SETTINGS = "ESKPAlgoSettings"
    KID_ALGO_SETTINGS = "KidAlgoSettings"

    def visit(
        self,
        hs_algo_settings: typing.Callable[[], T_Result],
        rs_algo_settings: typing.Callable[[], T_Result],
        es_algo_settings: typing.Callable[[], T_Result],
        jwks_algo_settings: typing.Callable[[], T_Result],
        rsakp_algo_settings: typing.Callable[[], T_Result],
        eskp_algo_settings: typing.Callable[[], T_Result],
        kid_algo_settings: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OtoroshiModelsRsAlgoSettingsType.HS_ALGO_SETTINGS:
            return hs_algo_settings()
        if self is OtoroshiModelsRsAlgoSettingsType.RS_ALGO_SETTINGS:
            return rs_algo_settings()
        if self is OtoroshiModelsRsAlgoSettingsType.ES_ALGO_SETTINGS:
            return es_algo_settings()
        if self is OtoroshiModelsRsAlgoSettingsType.JWKS_ALGO_SETTINGS:
            return jwks_algo_settings()
        if self is OtoroshiModelsRsAlgoSettingsType.RSAKP_ALGO_SETTINGS:
            return rsakp_algo_settings()
        if self is OtoroshiModelsRsAlgoSettingsType.ESKP_ALGO_SETTINGS:
            return eskp_algo_settings()
        if self is OtoroshiModelsRsAlgoSettingsType.KID_ALGO_SETTINGS:
            return kid_algo_settings()
