

import typing

TestWebhookRequestNotificationType = typing.Union[
    typing.Literal["tag_update", "analysis_update", "vuln_update", "policy_eval"], typing.Any
]
