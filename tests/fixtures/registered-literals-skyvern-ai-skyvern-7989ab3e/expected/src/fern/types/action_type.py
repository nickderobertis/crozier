

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionType(enum.StrEnum):
    CLICK = "click"
    INPUT_TEXT = "input_text"
    PASTE_TEXT = "paste_text"
    UPLOAD_FILE = "upload_file"
    DOWNLOAD_FILE = "download_file"
    SELECT_OPTION = "select_option"
    CHECKBOX = "checkbox"
    WAIT = "wait"
    HOVER = "hover"
    NULL_ACTION = "null_action"
    SOLVE_CAPTCHA = "solve_captcha"
    TERMINATE = "terminate"
    COMPLETE = "complete"
    RELOAD_PAGE = "reload_page"
    CLOSE_PAGE = "close_page"
    NEW_TAB = "new_tab"
    SWITCH_TAB = "switch_tab"
    EXTRACT = "extract"
    VERIFICATION_CODE = "verification_code"
    GOTO_URL = "goto_url"
    GO_BACK = "go_back"
    GO_FORWARD = "go_forward"
    SCROLL = "scroll"
    KEYPRESS = "keypress"
    MOVE = "move"
    DRAG = "drag"
    LEFT_MOUSE = "left_mouse"
    EXECUTE_JS = "execute_js"

    def visit(
        self,
        click: typing.Callable[[], T_Result],
        input_text: typing.Callable[[], T_Result],
        paste_text: typing.Callable[[], T_Result],
        upload_file: typing.Callable[[], T_Result],
        download_file: typing.Callable[[], T_Result],
        select_option: typing.Callable[[], T_Result],
        checkbox: typing.Callable[[], T_Result],
        wait: typing.Callable[[], T_Result],
        hover: typing.Callable[[], T_Result],
        null_action: typing.Callable[[], T_Result],
        solve_captcha: typing.Callable[[], T_Result],
        terminate: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        reload_page: typing.Callable[[], T_Result],
        close_page: typing.Callable[[], T_Result],
        new_tab: typing.Callable[[], T_Result],
        switch_tab: typing.Callable[[], T_Result],
        extract: typing.Callable[[], T_Result],
        verification_code: typing.Callable[[], T_Result],
        goto_url: typing.Callable[[], T_Result],
        go_back: typing.Callable[[], T_Result],
        go_forward: typing.Callable[[], T_Result],
        scroll: typing.Callable[[], T_Result],
        keypress: typing.Callable[[], T_Result],
        move: typing.Callable[[], T_Result],
        drag: typing.Callable[[], T_Result],
        left_mouse: typing.Callable[[], T_Result],
        execute_js: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActionType.CLICK:
            return click()
        if self is ActionType.INPUT_TEXT:
            return input_text()
        if self is ActionType.PASTE_TEXT:
            return paste_text()
        if self is ActionType.UPLOAD_FILE:
            return upload_file()
        if self is ActionType.DOWNLOAD_FILE:
            return download_file()
        if self is ActionType.SELECT_OPTION:
            return select_option()
        if self is ActionType.CHECKBOX:
            return checkbox()
        if self is ActionType.WAIT:
            return wait()
        if self is ActionType.HOVER:
            return hover()
        if self is ActionType.NULL_ACTION:
            return null_action()
        if self is ActionType.SOLVE_CAPTCHA:
            return solve_captcha()
        if self is ActionType.TERMINATE:
            return terminate()
        if self is ActionType.COMPLETE:
            return complete()
        if self is ActionType.RELOAD_PAGE:
            return reload_page()
        if self is ActionType.CLOSE_PAGE:
            return close_page()
        if self is ActionType.NEW_TAB:
            return new_tab()
        if self is ActionType.SWITCH_TAB:
            return switch_tab()
        if self is ActionType.EXTRACT:
            return extract()
        if self is ActionType.VERIFICATION_CODE:
            return verification_code()
        if self is ActionType.GOTO_URL:
            return goto_url()
        if self is ActionType.GO_BACK:
            return go_back()
        if self is ActionType.GO_FORWARD:
            return go_forward()
        if self is ActionType.SCROLL:
            return scroll()
        if self is ActionType.KEYPRESS:
            return keypress()
        if self is ActionType.MOVE:
            return move()
        if self is ActionType.DRAG:
            return drag()
        if self is ActionType.LEFT_MOUSE:
            return left_mouse()
        if self is ActionType.EXECUTE_JS:
            return execute_js()
