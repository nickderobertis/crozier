

import typing

AdminListUsersRequestOrder = typing.Union[
    typing.Literal[
        "created",
        "last_emailed",
        "seen",
        "username",
        "email",
        "trust_level",
        "days_visited",
        "posts_read",
        "topics_viewed",
        "posts",
        "read_time",
    ],
    typing.Any,
]
