

import typing

SubscriptionTriggerWritable = typing.Union[
    typing.Literal[
        "feature_baseline_to_newly",
        "feature_baseline_to_widely",
        "feature_browser_implementation_any_complete",
        "feature_baseline_regression_to_limited",
    ],
    typing.Any,
]
