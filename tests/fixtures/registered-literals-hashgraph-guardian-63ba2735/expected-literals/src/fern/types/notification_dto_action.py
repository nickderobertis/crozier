

import typing

NotificationDtoAction = typing.Union[
    typing.Literal[
        "POLICY_CONFIGURATION", "POLICY_VIEW", "POLICIES_PAGE", "SCHEMAS_PAGE", "TOKENS_PAGE", "PROFILE_PAGE"
    ],
    typing.Any,
]
