

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenTutorialRequestTutorialIdZero(enum.StrEnum):
    DATAFLOW = "dataflow"
    EXTERNAL_DEPENDENCIES = "external-dependencies"
    FILEFORMAT = "fileformat"
    FOR_JUPYTER_USERS = "for-jupyter-users"
    INTRO = "intro"
    LAYOUT = "layout"
    MARKDOWN = "markdown"
    PLOTS = "plots"
    SQL = "sql"
    UI = "ui"

    def visit(
        self,
        dataflow: typing.Callable[[], T_Result],
        external_dependencies: typing.Callable[[], T_Result],
        fileformat: typing.Callable[[], T_Result],
        for_jupyter_users: typing.Callable[[], T_Result],
        intro: typing.Callable[[], T_Result],
        layout: typing.Callable[[], T_Result],
        markdown: typing.Callable[[], T_Result],
        plots: typing.Callable[[], T_Result],
        sql: typing.Callable[[], T_Result],
        ui: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OpenTutorialRequestTutorialIdZero.DATAFLOW:
            return dataflow()
        if self is OpenTutorialRequestTutorialIdZero.EXTERNAL_DEPENDENCIES:
            return external_dependencies()
        if self is OpenTutorialRequestTutorialIdZero.FILEFORMAT:
            return fileformat()
        if self is OpenTutorialRequestTutorialIdZero.FOR_JUPYTER_USERS:
            return for_jupyter_users()
        if self is OpenTutorialRequestTutorialIdZero.INTRO:
            return intro()
        if self is OpenTutorialRequestTutorialIdZero.LAYOUT:
            return layout()
        if self is OpenTutorialRequestTutorialIdZero.MARKDOWN:
            return markdown()
        if self is OpenTutorialRequestTutorialIdZero.PLOTS:
            return plots()
        if self is OpenTutorialRequestTutorialIdZero.SQL:
            return sql()
        if self is OpenTutorialRequestTutorialIdZero.UI:
            return ui()
