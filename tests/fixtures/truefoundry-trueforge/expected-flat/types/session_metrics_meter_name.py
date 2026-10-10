

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionMetricsMeterName(enum.StrEnum):
    TOTAL_SESSIONS = "total_sessions"
    TOTAL_COST_IN_USD = "total_cost_in_usd"
    TOTAL_TURNS = "total_turns"
    COST_PER_SESSION_IN_USD = "cost_per_session_in_usd"
    AVG_TURNS_PER_SESSION = "avg_turns_per_session"
    MIN_TURNS_PER_SESSION = "min_turns_per_session"
    MAX_TURNS_PER_SESSION = "max_turns_per_session"
    MEDIAN_TURNS_PER_SESSION = "median_turns_per_session"
    MIN_SESSION_DURATION_MS = "min_session_duration_ms"
    MAX_SESSION_DURATION_MS = "max_session_duration_ms"
    MEDIAN_SESSION_DURATION_MS = "median_session_duration_ms"
    P95SESSION_DURATION_MS = "p95_session_duration_ms"

    def visit(
        self,
        total_sessions: typing.Callable[[], T_Result],
        total_cost_in_usd: typing.Callable[[], T_Result],
        total_turns: typing.Callable[[], T_Result],
        cost_per_session_in_usd: typing.Callable[[], T_Result],
        avg_turns_per_session: typing.Callable[[], T_Result],
        min_turns_per_session: typing.Callable[[], T_Result],
        max_turns_per_session: typing.Callable[[], T_Result],
        median_turns_per_session: typing.Callable[[], T_Result],
        min_session_duration_ms: typing.Callable[[], T_Result],
        max_session_duration_ms: typing.Callable[[], T_Result],
        median_session_duration_ms: typing.Callable[[], T_Result],
        p95session_duration_ms: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SessionMetricsMeterName.TOTAL_SESSIONS:
            return total_sessions()
        if self is SessionMetricsMeterName.TOTAL_COST_IN_USD:
            return total_cost_in_usd()
        if self is SessionMetricsMeterName.TOTAL_TURNS:
            return total_turns()
        if self is SessionMetricsMeterName.COST_PER_SESSION_IN_USD:
            return cost_per_session_in_usd()
        if self is SessionMetricsMeterName.AVG_TURNS_PER_SESSION:
            return avg_turns_per_session()
        if self is SessionMetricsMeterName.MIN_TURNS_PER_SESSION:
            return min_turns_per_session()
        if self is SessionMetricsMeterName.MAX_TURNS_PER_SESSION:
            return max_turns_per_session()
        if self is SessionMetricsMeterName.MEDIAN_TURNS_PER_SESSION:
            return median_turns_per_session()
        if self is SessionMetricsMeterName.MIN_SESSION_DURATION_MS:
            return min_session_duration_ms()
        if self is SessionMetricsMeterName.MAX_SESSION_DURATION_MS:
            return max_session_duration_ms()
        if self is SessionMetricsMeterName.MEDIAN_SESSION_DURATION_MS:
            return median_session_duration_ms()
        if self is SessionMetricsMeterName.P95SESSION_DURATION_MS:
            return p95session_duration_ms()
