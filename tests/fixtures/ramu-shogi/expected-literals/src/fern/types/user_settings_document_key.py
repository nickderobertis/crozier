

import typing

UserSettingsDocumentKey = typing.Union[
    typing.Literal[
        "match.time-settings", "match.display-settings", "match.analysis-settings", "match.pass-rights-settings"
    ],
    typing.Any,
]
