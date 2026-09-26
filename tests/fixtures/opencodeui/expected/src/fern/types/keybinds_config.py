

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class KeybindsConfig(UniversalBaseModel):
    """
    Custom keybind configurations
    """

    leader: typing.Optional[str] = pydantic.Field(default=None)
    """
    Leader key for keybind combinations
    """

    app_exit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Exit the application
    """

    editor_open: typing.Optional[str] = pydantic.Field(default=None)
    """
    Open external editor
    """

    theme_list: typing.Optional[str] = pydantic.Field(default=None)
    """
    List available themes
    """

    sidebar_toggle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Toggle sidebar
    """

    scrollbar_toggle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Toggle session scrollbar
    """

    username_toggle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Toggle username visibility
    """

    status_view: typing.Optional[str] = pydantic.Field(default=None)
    """
    View status
    """

    session_export: typing.Optional[str] = pydantic.Field(default=None)
    """
    Export session to editor
    """

    session_new: typing.Optional[str] = pydantic.Field(default=None)
    """
    Create a new session
    """

    session_list: typing.Optional[str] = pydantic.Field(default=None)
    """
    List all sessions
    """

    session_timeline: typing.Optional[str] = pydantic.Field(default=None)
    """
    Show session timeline
    """

    session_fork: typing.Optional[str] = pydantic.Field(default=None)
    """
    Fork session from message
    """

    session_rename: typing.Optional[str] = pydantic.Field(default=None)
    """
    Rename session
    """

    session_delete: typing.Optional[str] = pydantic.Field(default=None)
    """
    Delete session
    """

    stash_delete: typing.Optional[str] = pydantic.Field(default=None)
    """
    Delete stash entry
    """

    model_provider_list: typing.Optional[str] = pydantic.Field(default=None)
    """
    Open provider list from model dialog
    """

    model_favorite_toggle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Toggle model favorite status
    """

    session_share: typing.Optional[str] = pydantic.Field(default=None)
    """
    Share current session
    """

    session_unshare: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unshare current session
    """

    session_interrupt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Interrupt current session
    """

    session_compact: typing.Optional[str] = pydantic.Field(default=None)
    """
    Compact the session
    """

    messages_page_up: typing.Optional[str] = pydantic.Field(default=None)
    """
    Scroll messages up by one page
    """

    messages_page_down: typing.Optional[str] = pydantic.Field(default=None)
    """
    Scroll messages down by one page
    """

    messages_line_up: typing.Optional[str] = pydantic.Field(default=None)
    """
    Scroll messages up by one line
    """

    messages_line_down: typing.Optional[str] = pydantic.Field(default=None)
    """
    Scroll messages down by one line
    """

    messages_half_page_up: typing.Optional[str] = pydantic.Field(default=None)
    """
    Scroll messages up by half page
    """

    messages_half_page_down: typing.Optional[str] = pydantic.Field(default=None)
    """
    Scroll messages down by half page
    """

    messages_first: typing.Optional[str] = pydantic.Field(default=None)
    """
    Navigate to first message
    """

    messages_last: typing.Optional[str] = pydantic.Field(default=None)
    """
    Navigate to last message
    """

    messages_next: typing.Optional[str] = pydantic.Field(default=None)
    """
    Navigate to next message
    """

    messages_previous: typing.Optional[str] = pydantic.Field(default=None)
    """
    Navigate to previous message
    """

    messages_last_user: typing.Optional[str] = pydantic.Field(default=None)
    """
    Navigate to last user message
    """

    messages_copy: typing.Optional[str] = pydantic.Field(default=None)
    """
    Copy message
    """

    messages_undo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Undo message
    """

    messages_redo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Redo message
    """

    messages_toggle_conceal: typing.Optional[str] = pydantic.Field(default=None)
    """
    Toggle code block concealment in messages
    """

    tool_details: typing.Optional[str] = pydantic.Field(default=None)
    """
    Toggle tool details visibility
    """

    model_list: typing.Optional[str] = pydantic.Field(default=None)
    """
    List available models
    """

    model_cycle_recent: typing.Optional[str] = pydantic.Field(default=None)
    """
    Next recently used model
    """

    model_cycle_recent_reverse: typing.Optional[str] = pydantic.Field(default=None)
    """
    Previous recently used model
    """

    model_cycle_favorite: typing.Optional[str] = pydantic.Field(default=None)
    """
    Next favorite model
    """

    model_cycle_favorite_reverse: typing.Optional[str] = pydantic.Field(default=None)
    """
    Previous favorite model
    """

    command_list: typing.Optional[str] = pydantic.Field(default=None)
    """
    List available commands
    """

    agent_list: typing.Optional[str] = pydantic.Field(default=None)
    """
    List agents
    """

    agent_cycle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Next agent
    """

    agent_cycle_reverse: typing.Optional[str] = pydantic.Field(default=None)
    """
    Previous agent
    """

    variant_cycle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cycle model variants
    """

    input_clear: typing.Optional[str] = pydantic.Field(default=None)
    """
    Clear input field
    """

    input_paste: typing.Optional[str] = pydantic.Field(default=None)
    """
    Paste from clipboard
    """

    input_submit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Submit input
    """

    input_newline: typing.Optional[str] = pydantic.Field(default=None)
    """
    Insert newline in input
    """

    input_move_left: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move cursor left in input
    """

    input_move_right: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move cursor right in input
    """

    input_move_up: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move cursor up in input
    """

    input_move_down: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move cursor down in input
    """

    input_select_left: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select left in input
    """

    input_select_right: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select right in input
    """

    input_select_up: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select up in input
    """

    input_select_down: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select down in input
    """

    input_line_home: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move to start of line in input
    """

    input_line_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move to end of line in input
    """

    input_select_line_home: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select to start of line in input
    """

    input_select_line_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select to end of line in input
    """

    input_visual_line_home: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move to start of visual line in input
    """

    input_visual_line_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move to end of visual line in input
    """

    input_select_visual_line_home: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select to start of visual line in input
    """

    input_select_visual_line_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select to end of visual line in input
    """

    input_buffer_home: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move to start of buffer in input
    """

    input_buffer_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move to end of buffer in input
    """

    input_select_buffer_home: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select to start of buffer in input
    """

    input_select_buffer_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select to end of buffer in input
    """

    input_delete_line: typing.Optional[str] = pydantic.Field(default=None)
    """
    Delete line in input
    """

    input_delete_to_line_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    Delete to end of line in input
    """

    input_delete_to_line_start: typing.Optional[str] = pydantic.Field(default=None)
    """
    Delete to start of line in input
    """

    input_backspace: typing.Optional[str] = pydantic.Field(default=None)
    """
    Backspace in input
    """

    input_delete: typing.Optional[str] = pydantic.Field(default=None)
    """
    Delete character in input
    """

    input_undo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Undo in input
    """

    input_redo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Redo in input
    """

    input_word_forward: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move word forward in input
    """

    input_word_backward: typing.Optional[str] = pydantic.Field(default=None)
    """
    Move word backward in input
    """

    input_select_word_forward: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select word forward in input
    """

    input_select_word_backward: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select word backward in input
    """

    input_delete_word_forward: typing.Optional[str] = pydantic.Field(default=None)
    """
    Delete word forward in input
    """

    input_delete_word_backward: typing.Optional[str] = pydantic.Field(default=None)
    """
    Delete word backward in input
    """

    history_previous: typing.Optional[str] = pydantic.Field(default=None)
    """
    Previous history item
    """

    history_next: typing.Optional[str] = pydantic.Field(default=None)
    """
    Next history item
    """

    session_child_cycle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Next child session
    """

    session_child_cycle_reverse: typing.Optional[str] = pydantic.Field(default=None)
    """
    Previous child session
    """

    session_parent: typing.Optional[str] = pydantic.Field(default=None)
    """
    Go to parent session
    """

    terminal_suspend: typing.Optional[str] = pydantic.Field(default=None)
    """
    Suspend terminal
    """

    terminal_title_toggle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Toggle terminal title
    """

    tips_toggle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Toggle tips on home screen
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
