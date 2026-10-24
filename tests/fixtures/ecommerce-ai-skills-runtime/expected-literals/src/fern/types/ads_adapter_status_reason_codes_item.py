

import typing

AdsAdapterStatusReasonCodesItem = typing.Union[
    typing.Literal[
        "no_amazon_ads_account",
        "no_capability_gate",
        "gate_not_passed",
        "required_capabilities_missing",
        "gate_account_config_mismatch",
        "gate_not_checked",
        "gate_stale_account_changed",
        "gate_expired",
        "gate_checked_in_future",
        "adapter_not_installed",
        "write_surface_disabled",
    ],
    typing.Any,
]
