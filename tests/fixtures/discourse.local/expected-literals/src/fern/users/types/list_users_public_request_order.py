

import typing

ListUsersPublicRequestOrder = typing.Union[
    typing.Literal[
        "likes_received", "likes_given", "topic_count", "post_count", "topics_entered", "posts_read", "days_visited"
    ],
    typing.Any,
]
