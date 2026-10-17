

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApplyProjectAddonBodyAddonType(enum.StrEnum):
    CUSTOM_DOMAIN = "custom_domain"
    COMPUTE_INSTANCE = "compute_instance"
    PITR = "pitr"
    IPV4 = "ipv4"
    AUTH_MFA_PHONE = "auth_mfa_phone"
    AUTH_MFA_WEB_AUTHN = "auth_mfa_web_authn"
    LOG_DRAIN = "log_drain"
    ETL_PIPELINE = "etl_pipeline"

    def visit(
        self,
        custom_domain: typing.Callable[[], T_Result],
        compute_instance: typing.Callable[[], T_Result],
        pitr: typing.Callable[[], T_Result],
        ipv4: typing.Callable[[], T_Result],
        auth_mfa_phone: typing.Callable[[], T_Result],
        auth_mfa_web_authn: typing.Callable[[], T_Result],
        log_drain: typing.Callable[[], T_Result],
        etl_pipeline: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApplyProjectAddonBodyAddonType.CUSTOM_DOMAIN:
            return custom_domain()
        if self is ApplyProjectAddonBodyAddonType.COMPUTE_INSTANCE:
            return compute_instance()
        if self is ApplyProjectAddonBodyAddonType.PITR:
            return pitr()
        if self is ApplyProjectAddonBodyAddonType.IPV4:
            return ipv4()
        if self is ApplyProjectAddonBodyAddonType.AUTH_MFA_PHONE:
            return auth_mfa_phone()
        if self is ApplyProjectAddonBodyAddonType.AUTH_MFA_WEB_AUTHN:
            return auth_mfa_web_authn()
        if self is ApplyProjectAddonBodyAddonType.LOG_DRAIN:
            return log_drain()
        if self is ApplyProjectAddonBodyAddonType.ETL_PIPELINE:
            return etl_pipeline()
