

import typing

EntryLinkType = typing.Union[
    typing.Literal[
        "link",
        "user",
        "request",
        "entry",
        "stage_entry",
        "protocol",
        "workflow",
        "custom_entity",
        "aa_sequence",
        "dna_sequence",
        "batch",
        "box",
        "container",
        "location",
        "plate",
        "insights_dashboard",
        "folder",
        "sql_dashboard",
    ],
    typing.Any,
]
