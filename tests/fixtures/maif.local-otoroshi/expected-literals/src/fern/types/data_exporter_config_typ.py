

import typing

DataExporterConfigTyp = typing.Union[
    typing.Literal["kafka", "pulsar", "file", "mailer", "elastic", "console", "custom"], typing.Any
]
