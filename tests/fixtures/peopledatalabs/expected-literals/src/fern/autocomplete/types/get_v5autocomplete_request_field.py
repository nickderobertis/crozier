

import typing

GetV5AutocompleteRequestField = typing.Union[
    typing.Literal[
        "company", "country", "industry", "location", "major", "region", "role", "school", "sub_role", "skill", "title"
    ],
    typing.Any,
]
