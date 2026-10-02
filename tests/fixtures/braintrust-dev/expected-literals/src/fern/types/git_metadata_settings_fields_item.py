

import typing

GitMetadataSettingsFieldsItem = typing.Union[
    typing.Literal[
        "commit", "branch", "tag", "dirty", "author_name", "author_email", "commit_message", "commit_time", "git_diff"
    ],
    typing.Any,
]
