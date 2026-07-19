

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .compaction_settings_input_mode import CompactionSettingsInputMode
from .compaction_settings_input_model_settings import CompactionSettingsInputModelSettings


class CompactionSettingsInput(UniversalBaseModel):
    """
    Configuration for conversation compaction / summarization.

    ``model`` is the only required user-facing field – it specifies the summarizer
    model handle (e.g. ``"openai/gpt-4o-mini"``). Per-model settings (temperature,
    max tokens, etc.) are derived from the default configuration for that handle.
    """

    model: str = pydantic.Field()
    """
    Model handle to use for summarization (format: provider/model-name).
    """

    model_settings: typing.Optional[CompactionSettingsInputModelSettings] = pydantic.Field(default=None)
    """
    Optional model settings used to override defaults for the summarizer model.
    """

    prompt: typing.Optional[str] = pydantic.Field(default=None)
    """
    The prompt to use for summarization.
    """

    prompt_acknowledgement: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to include an acknowledgement post-prompt (helps prevent non-summary outputs).
    """

    clip_chars: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum length of the summary in characters. If none, no clipping is performed.
    """

    mode: typing.Optional[CompactionSettingsInputMode] = pydantic.Field(default=None)
    """
    The type of summarization technique use.
    """

    sliding_window_percentage: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percentage of the context window to keep post-summarization (only used in sliding window mode).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
