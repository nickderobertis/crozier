

import typing

OtoroshiModelsWebhookType = typing.Union[
    typing.Literal["elastic", "webhook", "kafka", "pulsar", "file", "mailer", "custom", "console", "metrics"],
    typing.Any,
]
