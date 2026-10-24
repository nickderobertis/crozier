

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdsAdapterStatusReasonCodesItem(enum.StrEnum):
    NO_AMAZON_ADS_ACCOUNT = "no_amazon_ads_account"
    NO_CAPABILITY_GATE = "no_capability_gate"
    GATE_NOT_PASSED = "gate_not_passed"
    REQUIRED_CAPABILITIES_MISSING = "required_capabilities_missing"
    GATE_ACCOUNT_CONFIG_MISMATCH = "gate_account_config_mismatch"
    GATE_NOT_CHECKED = "gate_not_checked"
    GATE_STALE_ACCOUNT_CHANGED = "gate_stale_account_changed"
    GATE_EXPIRED = "gate_expired"
    GATE_CHECKED_IN_FUTURE = "gate_checked_in_future"
    ADAPTER_NOT_INSTALLED = "adapter_not_installed"
    WRITE_SURFACE_DISABLED = "write_surface_disabled"

    def visit(
        self,
        no_amazon_ads_account: typing.Callable[[], T_Result],
        no_capability_gate: typing.Callable[[], T_Result],
        gate_not_passed: typing.Callable[[], T_Result],
        required_capabilities_missing: typing.Callable[[], T_Result],
        gate_account_config_mismatch: typing.Callable[[], T_Result],
        gate_not_checked: typing.Callable[[], T_Result],
        gate_stale_account_changed: typing.Callable[[], T_Result],
        gate_expired: typing.Callable[[], T_Result],
        gate_checked_in_future: typing.Callable[[], T_Result],
        adapter_not_installed: typing.Callable[[], T_Result],
        write_surface_disabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdsAdapterStatusReasonCodesItem.NO_AMAZON_ADS_ACCOUNT:
            return no_amazon_ads_account()
        if self is AdsAdapterStatusReasonCodesItem.NO_CAPABILITY_GATE:
            return no_capability_gate()
        if self is AdsAdapterStatusReasonCodesItem.GATE_NOT_PASSED:
            return gate_not_passed()
        if self is AdsAdapterStatusReasonCodesItem.REQUIRED_CAPABILITIES_MISSING:
            return required_capabilities_missing()
        if self is AdsAdapterStatusReasonCodesItem.GATE_ACCOUNT_CONFIG_MISMATCH:
            return gate_account_config_mismatch()
        if self is AdsAdapterStatusReasonCodesItem.GATE_NOT_CHECKED:
            return gate_not_checked()
        if self is AdsAdapterStatusReasonCodesItem.GATE_STALE_ACCOUNT_CHANGED:
            return gate_stale_account_changed()
        if self is AdsAdapterStatusReasonCodesItem.GATE_EXPIRED:
            return gate_expired()
        if self is AdsAdapterStatusReasonCodesItem.GATE_CHECKED_IN_FUTURE:
            return gate_checked_in_future()
        if self is AdsAdapterStatusReasonCodesItem.ADAPTER_NOT_INSTALLED:
            return adapter_not_installed()
        if self is AdsAdapterStatusReasonCodesItem.WRITE_SURFACE_DISABLED:
            return write_surface_disabled()
