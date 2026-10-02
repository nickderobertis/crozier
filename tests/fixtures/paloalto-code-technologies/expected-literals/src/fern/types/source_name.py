

import typing

SourceName = typing.Union[
    typing.Literal[
        "VCS Webhooks",
        "VCS App",
        "VCS DeployKey",
        "CI Credentials",
        "CI Plugins",
        "CI Files",
        "VCS Credentials",
        "Pipeline Configurations",
        "Pipeline Tools",
        "Integrations",
    ],
    typing.Any,
]
