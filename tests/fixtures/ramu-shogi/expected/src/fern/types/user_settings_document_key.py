

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserSettingsDocumentKey(enum.StrEnum):
    MATCH_TIME_SETTINGS = "match.time-settings"
    MATCH_DISPLAY_SETTINGS = "match.display-settings"
    MATCH_ANALYSIS_SETTINGS = "match.analysis-settings"
    MATCH_PASS_RIGHTS_SETTINGS = "match.pass-rights-settings"

    def visit(
        self,
        match_time_settings: typing.Callable[[], T_Result],
        match_display_settings: typing.Callable[[], T_Result],
        match_analysis_settings: typing.Callable[[], T_Result],
        match_pass_rights_settings: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserSettingsDocumentKey.MATCH_TIME_SETTINGS:
            return match_time_settings()
        if self is UserSettingsDocumentKey.MATCH_DISPLAY_SETTINGS:
            return match_display_settings()
        if self is UserSettingsDocumentKey.MATCH_ANALYSIS_SETTINGS:
            return match_analysis_settings()
        if self is UserSettingsDocumentKey.MATCH_PASS_RIGHTS_SETTINGS:
            return match_pass_rights_settings()
