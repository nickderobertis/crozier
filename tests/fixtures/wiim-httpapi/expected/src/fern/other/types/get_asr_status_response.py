

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetAsrStatusResponse(UniversalBaseModel):
    times_talk_on: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    times_request_succeed: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    times_request_failed: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    times_vad_time_out: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    times_play_failed: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    open_failed: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    capture_failed: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    mode: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    score: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    volume: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    play_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    config_score: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    config_interval: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    trigger_test_mode: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    trigger_mis_test_mode: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    trigger_recording: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    have_prompt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    fallback_enable: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    profile: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    hands_free: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the ASR system, typically "ok"
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unknown
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
