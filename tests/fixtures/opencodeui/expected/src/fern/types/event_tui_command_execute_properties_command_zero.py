

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventTuiCommandExecutePropertiesCommandZero(enum.StrEnum):
    SESSION_LIST = "session.list"
    SESSION_NEW = "session.new"
    SESSION_SHARE = "session.share"
    SESSION_INTERRUPT = "session.interrupt"
    SESSION_COMPACT = "session.compact"
    SESSION_PAGE_UP = "session.page.up"
    SESSION_PAGE_DOWN = "session.page.down"
    SESSION_LINE_UP = "session.line.up"
    SESSION_LINE_DOWN = "session.line.down"
    SESSION_HALF_PAGE_UP = "session.half.page.up"
    SESSION_HALF_PAGE_DOWN = "session.half.page.down"
    SESSION_FIRST = "session.first"
    SESSION_LAST = "session.last"
    PROMPT_CLEAR = "prompt.clear"
    PROMPT_SUBMIT = "prompt.submit"
    AGENT_CYCLE = "agent.cycle"

    def visit(
        self,
        session_list: typing.Callable[[], T_Result],
        session_new: typing.Callable[[], T_Result],
        session_share: typing.Callable[[], T_Result],
        session_interrupt: typing.Callable[[], T_Result],
        session_compact: typing.Callable[[], T_Result],
        session_page_up: typing.Callable[[], T_Result],
        session_page_down: typing.Callable[[], T_Result],
        session_line_up: typing.Callable[[], T_Result],
        session_line_down: typing.Callable[[], T_Result],
        session_half_page_up: typing.Callable[[], T_Result],
        session_half_page_down: typing.Callable[[], T_Result],
        session_first: typing.Callable[[], T_Result],
        session_last: typing.Callable[[], T_Result],
        prompt_clear: typing.Callable[[], T_Result],
        prompt_submit: typing.Callable[[], T_Result],
        agent_cycle: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_LIST:
            return session_list()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_NEW:
            return session_new()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_SHARE:
            return session_share()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_INTERRUPT:
            return session_interrupt()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_COMPACT:
            return session_compact()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_PAGE_UP:
            return session_page_up()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_PAGE_DOWN:
            return session_page_down()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_LINE_UP:
            return session_line_up()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_LINE_DOWN:
            return session_line_down()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_HALF_PAGE_UP:
            return session_half_page_up()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_HALF_PAGE_DOWN:
            return session_half_page_down()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_FIRST:
            return session_first()
        if self is EventTuiCommandExecutePropertiesCommandZero.SESSION_LAST:
            return session_last()
        if self is EventTuiCommandExecutePropertiesCommandZero.PROMPT_CLEAR:
            return prompt_clear()
        if self is EventTuiCommandExecutePropertiesCommandZero.PROMPT_SUBMIT:
            return prompt_submit()
        if self is EventTuiCommandExecutePropertiesCommandZero.AGENT_CYCLE:
            return agent_cycle()
