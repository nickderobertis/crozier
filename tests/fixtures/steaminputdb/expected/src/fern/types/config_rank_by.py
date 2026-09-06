

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfigRankBy(enum.StrEnum):
    """
    Criterion to rank search results by
    """

    VOTE = "vote"
    PUBLICATION = "publication"
    TREND = "trend"
    SUBSCRIPTIONS = "subscriptions"
    VOTES_ASC = "votes_asc"
    VOTES_UP = "votes_up"
    TEXT_SEARCH = "text_search"
    PLAYTIME_TREND = "playtime_trend"
    TOTAL_PLAYTIME = "total_playtime"
    AVG_PLAYTIME_TREND = "avg_playtime_trend"
    LIFETIME_AVG_PLAYTIME = "lifetime_avg_playtime"
    PLAYTIME_SESSIONS_TREND = "playtime_sessions_trend"
    LIFETIME_PLAYTIME_SESSIONS = "lifetime_playtime_sessions"
    UPDATED = "updated"

    def visit(
        self,
        vote: typing.Callable[[], T_Result],
        publication: typing.Callable[[], T_Result],
        trend: typing.Callable[[], T_Result],
        subscriptions: typing.Callable[[], T_Result],
        votes_asc: typing.Callable[[], T_Result],
        votes_up: typing.Callable[[], T_Result],
        text_search: typing.Callable[[], T_Result],
        playtime_trend: typing.Callable[[], T_Result],
        total_playtime: typing.Callable[[], T_Result],
        avg_playtime_trend: typing.Callable[[], T_Result],
        lifetime_avg_playtime: typing.Callable[[], T_Result],
        playtime_sessions_trend: typing.Callable[[], T_Result],
        lifetime_playtime_sessions: typing.Callable[[], T_Result],
        updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConfigRankBy.VOTE:
            return vote()
        if self is ConfigRankBy.PUBLICATION:
            return publication()
        if self is ConfigRankBy.TREND:
            return trend()
        if self is ConfigRankBy.SUBSCRIPTIONS:
            return subscriptions()
        if self is ConfigRankBy.VOTES_ASC:
            return votes_asc()
        if self is ConfigRankBy.VOTES_UP:
            return votes_up()
        if self is ConfigRankBy.TEXT_SEARCH:
            return text_search()
        if self is ConfigRankBy.PLAYTIME_TREND:
            return playtime_trend()
        if self is ConfigRankBy.TOTAL_PLAYTIME:
            return total_playtime()
        if self is ConfigRankBy.AVG_PLAYTIME_TREND:
            return avg_playtime_trend()
        if self is ConfigRankBy.LIFETIME_AVG_PLAYTIME:
            return lifetime_avg_playtime()
        if self is ConfigRankBy.PLAYTIME_SESSIONS_TREND:
            return playtime_sessions_trend()
        if self is ConfigRankBy.LIFETIME_PLAYTIME_SESSIONS:
            return lifetime_playtime_sessions()
        if self is ConfigRankBy.UPDATED:
            return updated()
