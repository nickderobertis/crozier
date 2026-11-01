

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeviceDebugInfo(UniversalBaseModel):
    system_ready: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if the system is ready
    """

    slave_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if the device is a slave in multiroom mode
    """

    slave_playing: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if the slave device is currently playing audio in multiroom mode
    """

    slave_num: typing.Optional[str] = pydantic.Field(default=None)
    """
    Number of slave devices in multiroom mode
    """

    slave_latency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Latency for slave devices in multiroom mode
    """

    slave_default_latency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default latency for slave devices in multiroom mode
    """

    connecting_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates the type of connection for the device
    """

    play_mode: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current play mode of the device
    """

    plm_notify_flag: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if there is a PLM notification
    """

    play_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current play status of the device
    """

    bt_play_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Bluetooth play status
    """

    spotify_play_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Spotify play status
    """

    capture_play_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Capture play status
    """

    time_sync_ready: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if time synchronization is ready
    """

    asr_ongoing: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if ASR is ongoing
    """

    asr_ready: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if ASR is ready
    """

    asr_region: typing.Optional[str] = pydantic.Field(default=None)
    """
    ASR region setting
    """

    asr_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    ASR language setting
    """

    asr_pause_request: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if there is a request to pause ASR
    """

    alexa_response_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Status of the response from Alexa
    """

    pause_flag_for_alexa: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if there is a pause flag for Alexa
    """

    priv_languages: typing.Optional[str] = pydantic.Field(default=None)
    """
    Supported languages for private use, bit mask
    """

    retail_mode: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if the device is in retail mode
    """

    ezlink_active: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if EZLink is active
    """

    device_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device status
    """

    a01controller_crash: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if there has been a crash in the A01 controller
    """

    asr_tts_crash: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if there has been a crash in ASR or TTS
    """

    mcu_crash: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if there has been a crash in the MCU
    """

    process_deadlock: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if there has been a deadlock in any process
    """

    power_ticks: typing.Optional[str] = pydantic.Field(default=None)
    """
    Number of power ticks
    """

    gapless: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if gapless playback is enabled
    """

    imuzop_pid: typing.Optional[str] = pydantic.Field(default=None)
    """
    PID for IMUZOP process
    """

    slave: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if the device is a slave in multiroom mode
    """

    upnp_action_total0: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total UPnP actions for zone 0
    """

    upnp_action_remain0: typing.Optional[str] = pydantic.Field(default=None)
    """
    Remaining UPnP actions for zone 0
    """

    upnp_action_lost0: typing.Optional[str] = pydantic.Field(default=None)
    """
    Lost UPnP actions for zone 0
    """

    upnp_action_total1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total UPnP actions for zone 1
    """

    upnp_action_remain1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Remaining UPnP actions for zone 1
    """

    upnp_action_lost1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Lost UPnP actions for zone 1
    """

    upnp_action_total2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total UPnP actions for zone 2
    """

    upnp_action_remain2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Remaining UPnP actions for zone 2
    """

    upnp_action_lost2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Lost UPnP actions for zone 2
    """

    upnp_action_total3: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total UPnP actions for zone 3
    """

    upnp_action_remain3: typing.Optional[str] = pydantic.Field(default=None)
    """
    Remaining UPnP actions for zone 3
    """

    upnp_action_lost3: typing.Optional[str] = pydantic.Field(default=None)
    """
    Lost UPnP actions for zone 3
    """

    wifi_abort_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date of the last WiFi abort
    """

    smplay_skip_silence: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if skip silence is enabled for SMPlay
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
