

import typing

ConfigRankBy = typing.Union[
    typing.Literal[
        "vote",
        "publication",
        "trend",
        "subscriptions",
        "votes_asc",
        "votes_up",
        "text_search",
        "playtime_trend",
        "total_playtime",
        "avg_playtime_trend",
        "lifetime_avg_playtime",
        "playtime_sessions_trend",
        "lifetime_playtime_sessions",
        "updated",
    ],
    typing.Any,
]
