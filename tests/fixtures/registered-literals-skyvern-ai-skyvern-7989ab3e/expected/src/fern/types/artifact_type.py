

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ArtifactType(enum.StrEnum):
    RECORDING = "recording"
    AUDIO = "audio"
    SESSION_REPLAY = "session_replay"
    EVAL_SCORE = "eval_score"
    EVAL_TRAJECTORY = "eval_trajectory"
    EVAL_RUBRICS = "eval_rubrics"
    BROWSER_CONSOLE_LOG = "browser_console_log"
    BROWSER_SESSION_ACTION_LOG = "browser_session_action_log"
    SKYVERN_LOG = "skyvern_log"
    SKYVERN_LOG_RAW = "skyvern_log_raw"
    SCREENSHOT = "screenshot"
    SCREENSHOT_LLM = "screenshot_llm"
    SCREENSHOT_ACTION = "screenshot_action"
    SCREENSHOT_FINAL = "screenshot_final"
    SCREENSHOT_PROXY = "screenshot_proxy"
    SCREENSHOT_PRE_SUBMIT = "screenshot_pre_submit"
    LLM_PROMPT = "llm_prompt"
    LLM_REQUEST = "llm_request"
    LLM_RESPONSE = "llm_response"
    LLM_RESPONSE_PARSED = "llm_response_parsed"
    LLM_RESPONSE_RENDERED = "llm_response_rendered"
    VISIBLE_ELEMENTS_ID_CSS_MAP = "visible_elements_id_css_map"
    VISIBLE_ELEMENTS_ID_FRAME_MAP = "visible_elements_id_frame_map"
    VISIBLE_ELEMENTS_TREE = "visible_elements_tree"
    VISIBLE_ELEMENTS_TREE_TRIMMED = "visible_elements_tree_trimmed"
    VISIBLE_ELEMENTS_TREE_IN_PROMPT = "visible_elements_tree_in_prompt"
    HASHED_HREF_MAP = "hashed_href_map"
    VISIBLE_ELEMENTS_ID_XPATH_MAP = "visible_elements_id_xpath_map"
    HTML = "html"
    HTML_SCRAPE = "html_scrape"
    HTML_ACTION = "html_action"
    HTML_PRE_SUBMIT = "html_pre_submit"
    TRACE = "trace"
    HAR = "har"
    SCRIPT_FILE = "script_file"
    PDF = "pdf"
    STEP_ARCHIVE = "step_archive"
    TASK_ARCHIVE = "task_archive"
    DOWNLOAD = "download"
    UNKNOWN = "unknown"

    def visit(
        self,
        recording: typing.Callable[[], T_Result],
        audio: typing.Callable[[], T_Result],
        session_replay: typing.Callable[[], T_Result],
        eval_score: typing.Callable[[], T_Result],
        eval_trajectory: typing.Callable[[], T_Result],
        eval_rubrics: typing.Callable[[], T_Result],
        browser_console_log: typing.Callable[[], T_Result],
        browser_session_action_log: typing.Callable[[], T_Result],
        skyvern_log: typing.Callable[[], T_Result],
        skyvern_log_raw: typing.Callable[[], T_Result],
        screenshot: typing.Callable[[], T_Result],
        screenshot_llm: typing.Callable[[], T_Result],
        screenshot_action: typing.Callable[[], T_Result],
        screenshot_final: typing.Callable[[], T_Result],
        screenshot_proxy: typing.Callable[[], T_Result],
        screenshot_pre_submit: typing.Callable[[], T_Result],
        llm_prompt: typing.Callable[[], T_Result],
        llm_request: typing.Callable[[], T_Result],
        llm_response: typing.Callable[[], T_Result],
        llm_response_parsed: typing.Callable[[], T_Result],
        llm_response_rendered: typing.Callable[[], T_Result],
        visible_elements_id_css_map: typing.Callable[[], T_Result],
        visible_elements_id_frame_map: typing.Callable[[], T_Result],
        visible_elements_tree: typing.Callable[[], T_Result],
        visible_elements_tree_trimmed: typing.Callable[[], T_Result],
        visible_elements_tree_in_prompt: typing.Callable[[], T_Result],
        hashed_href_map: typing.Callable[[], T_Result],
        visible_elements_id_xpath_map: typing.Callable[[], T_Result],
        html: typing.Callable[[], T_Result],
        html_scrape: typing.Callable[[], T_Result],
        html_action: typing.Callable[[], T_Result],
        html_pre_submit: typing.Callable[[], T_Result],
        trace: typing.Callable[[], T_Result],
        har: typing.Callable[[], T_Result],
        script_file: typing.Callable[[], T_Result],
        pdf: typing.Callable[[], T_Result],
        step_archive: typing.Callable[[], T_Result],
        task_archive: typing.Callable[[], T_Result],
        download: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ArtifactType.RECORDING:
            return recording()
        if self is ArtifactType.AUDIO:
            return audio()
        if self is ArtifactType.SESSION_REPLAY:
            return session_replay()
        if self is ArtifactType.EVAL_SCORE:
            return eval_score()
        if self is ArtifactType.EVAL_TRAJECTORY:
            return eval_trajectory()
        if self is ArtifactType.EVAL_RUBRICS:
            return eval_rubrics()
        if self is ArtifactType.BROWSER_CONSOLE_LOG:
            return browser_console_log()
        if self is ArtifactType.BROWSER_SESSION_ACTION_LOG:
            return browser_session_action_log()
        if self is ArtifactType.SKYVERN_LOG:
            return skyvern_log()
        if self is ArtifactType.SKYVERN_LOG_RAW:
            return skyvern_log_raw()
        if self is ArtifactType.SCREENSHOT:
            return screenshot()
        if self is ArtifactType.SCREENSHOT_LLM:
            return screenshot_llm()
        if self is ArtifactType.SCREENSHOT_ACTION:
            return screenshot_action()
        if self is ArtifactType.SCREENSHOT_FINAL:
            return screenshot_final()
        if self is ArtifactType.SCREENSHOT_PROXY:
            return screenshot_proxy()
        if self is ArtifactType.SCREENSHOT_PRE_SUBMIT:
            return screenshot_pre_submit()
        if self is ArtifactType.LLM_PROMPT:
            return llm_prompt()
        if self is ArtifactType.LLM_REQUEST:
            return llm_request()
        if self is ArtifactType.LLM_RESPONSE:
            return llm_response()
        if self is ArtifactType.LLM_RESPONSE_PARSED:
            return llm_response_parsed()
        if self is ArtifactType.LLM_RESPONSE_RENDERED:
            return llm_response_rendered()
        if self is ArtifactType.VISIBLE_ELEMENTS_ID_CSS_MAP:
            return visible_elements_id_css_map()
        if self is ArtifactType.VISIBLE_ELEMENTS_ID_FRAME_MAP:
            return visible_elements_id_frame_map()
        if self is ArtifactType.VISIBLE_ELEMENTS_TREE:
            return visible_elements_tree()
        if self is ArtifactType.VISIBLE_ELEMENTS_TREE_TRIMMED:
            return visible_elements_tree_trimmed()
        if self is ArtifactType.VISIBLE_ELEMENTS_TREE_IN_PROMPT:
            return visible_elements_tree_in_prompt()
        if self is ArtifactType.HASHED_HREF_MAP:
            return hashed_href_map()
        if self is ArtifactType.VISIBLE_ELEMENTS_ID_XPATH_MAP:
            return visible_elements_id_xpath_map()
        if self is ArtifactType.HTML:
            return html()
        if self is ArtifactType.HTML_SCRAPE:
            return html_scrape()
        if self is ArtifactType.HTML_ACTION:
            return html_action()
        if self is ArtifactType.HTML_PRE_SUBMIT:
            return html_pre_submit()
        if self is ArtifactType.TRACE:
            return trace()
        if self is ArtifactType.HAR:
            return har()
        if self is ArtifactType.SCRIPT_FILE:
            return script_file()
        if self is ArtifactType.PDF:
            return pdf()
        if self is ArtifactType.STEP_ARCHIVE:
            return step_archive()
        if self is ArtifactType.TASK_ARCHIVE:
            return task_archive()
        if self is ArtifactType.DOWNLOAD:
            return download()
        if self is ArtifactType.UNKNOWN:
            return unknown()
