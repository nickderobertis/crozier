

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdsCapabilityGateChecksItemName(enum.StrEnum):
    LWA = "lwa"
    PROFILES_READ = "profiles_read"
    TARGET_PROFILE = "target_profile"
    CAMPAIGNS_LIST_READ = "campaigns_list_read"
    EXTERNAL_ATTESTATION = "external_attestation"

    def visit(
        self,
        lwa: typing.Callable[[], T_Result],
        profiles_read: typing.Callable[[], T_Result],
        target_profile: typing.Callable[[], T_Result],
        campaigns_list_read: typing.Callable[[], T_Result],
        external_attestation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdsCapabilityGateChecksItemName.LWA:
            return lwa()
        if self is AdsCapabilityGateChecksItemName.PROFILES_READ:
            return profiles_read()
        if self is AdsCapabilityGateChecksItemName.TARGET_PROFILE:
            return target_profile()
        if self is AdsCapabilityGateChecksItemName.CAMPAIGNS_LIST_READ:
            return campaigns_list_read()
        if self is AdsCapabilityGateChecksItemName.EXTERNAL_ATTESTATION:
            return external_attestation()
