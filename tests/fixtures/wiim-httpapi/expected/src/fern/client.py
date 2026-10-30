

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .alarm_clock.client import AlarmClockClient, AsyncAlarmClockClient
    from .alexa.client import AlexaClient, AsyncAlexaClient
    from .amazon_music.client import AmazonMusicClient, AsyncAmazonMusicClient
    from .audio_output_control.client import AsyncAudioOutputControlClient, AudioOutputControlClient
    from .bluetooth.client import AsyncBluetoothClient, BluetoothClient
    from .device_control.client import AsyncDeviceControlClient, DeviceControlClient
    from .device_information.client import AsyncDeviceInformationClient, DeviceInformationClient
    from .equalizer.client import AsyncEqualizerClient, EqualizerClient
    from .generic.client import AsyncGenericClient, GenericClient
    from .multiroom.client import AsyncMultiroomClient, MultiroomClient
    from .network.client import AsyncNetworkClient, NetworkClient
    from .other.client import AsyncOtherClient, OtherClient
    from .playback_control.client import AsyncPlaybackControlClient, PlaybackControlClient
    from .presets.client import AsyncPresetsClient, PresetsClient
    from .room_correction.client import AsyncRoomCorrectionClient, RoomCorrectionClient
    from .source_input_switch.client import AsyncSourceInputSwitchClient, SourceInputSwitchClient
    from .track_metadata.client import AsyncTrackMetadataClient, TrackMetadataClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._generic: typing.Optional[GenericClient] = None
        self._device_information: typing.Optional[DeviceInformationClient] = None
        self._track_metadata: typing.Optional[TrackMetadataClient] = None
        self._playback_control: typing.Optional[PlaybackControlClient] = None
        self._network: typing.Optional[NetworkClient] = None
        self._equalizer: typing.Optional[EqualizerClient] = None
        self._device_control: typing.Optional[DeviceControlClient] = None
        self._alarm_clock: typing.Optional[AlarmClockClient] = None
        self._source_input_switch: typing.Optional[SourceInputSwitchClient] = None
        self._presets: typing.Optional[PresetsClient] = None
        self._audio_output_control: typing.Optional[AudioOutputControlClient] = None
        self._bluetooth: typing.Optional[BluetoothClient] = None
        self._room_correction: typing.Optional[RoomCorrectionClient] = None
        self._alexa: typing.Optional[AlexaClient] = None
        self._amazon_music: typing.Optional[AmazonMusicClient] = None
        self._multiroom: typing.Optional[MultiroomClient] = None
        self._other: typing.Optional[OtherClient] = None

    @property
    def generic(self):
        if self._generic is None:
            from .generic.client import GenericClient

            self._generic = GenericClient(client_wrapper=self._client_wrapper)
        return self._generic

    @property
    def device_information(self):
        if self._device_information is None:
            from .device_information.client import DeviceInformationClient

            self._device_information = DeviceInformationClient(client_wrapper=self._client_wrapper)
        return self._device_information

    @property
    def track_metadata(self):
        if self._track_metadata is None:
            from .track_metadata.client import TrackMetadataClient

            self._track_metadata = TrackMetadataClient(client_wrapper=self._client_wrapper)
        return self._track_metadata

    @property
    def playback_control(self):
        if self._playback_control is None:
            from .playback_control.client import PlaybackControlClient

            self._playback_control = PlaybackControlClient(client_wrapper=self._client_wrapper)
        return self._playback_control

    @property
    def network(self):
        if self._network is None:
            from .network.client import NetworkClient

            self._network = NetworkClient(client_wrapper=self._client_wrapper)
        return self._network

    @property
    def equalizer(self):
        if self._equalizer is None:
            from .equalizer.client import EqualizerClient

            self._equalizer = EqualizerClient(client_wrapper=self._client_wrapper)
        return self._equalizer

    @property
    def device_control(self):
        if self._device_control is None:
            from .device_control.client import DeviceControlClient

            self._device_control = DeviceControlClient(client_wrapper=self._client_wrapper)
        return self._device_control

    @property
    def alarm_clock(self):
        if self._alarm_clock is None:
            from .alarm_clock.client import AlarmClockClient

            self._alarm_clock = AlarmClockClient(client_wrapper=self._client_wrapper)
        return self._alarm_clock

    @property
    def source_input_switch(self):
        if self._source_input_switch is None:
            from .source_input_switch.client import SourceInputSwitchClient

            self._source_input_switch = SourceInputSwitchClient(client_wrapper=self._client_wrapper)
        return self._source_input_switch

    @property
    def presets(self):
        if self._presets is None:
            from .presets.client import PresetsClient

            self._presets = PresetsClient(client_wrapper=self._client_wrapper)
        return self._presets

    @property
    def audio_output_control(self):
        if self._audio_output_control is None:
            from .audio_output_control.client import AudioOutputControlClient

            self._audio_output_control = AudioOutputControlClient(client_wrapper=self._client_wrapper)
        return self._audio_output_control

    @property
    def bluetooth(self):
        if self._bluetooth is None:
            from .bluetooth.client import BluetoothClient

            self._bluetooth = BluetoothClient(client_wrapper=self._client_wrapper)
        return self._bluetooth

    @property
    def room_correction(self):
        if self._room_correction is None:
            from .room_correction.client import RoomCorrectionClient

            self._room_correction = RoomCorrectionClient(client_wrapper=self._client_wrapper)
        return self._room_correction

    @property
    def alexa(self):
        if self._alexa is None:
            from .alexa.client import AlexaClient

            self._alexa = AlexaClient(client_wrapper=self._client_wrapper)
        return self._alexa

    @property
    def amazon_music(self):
        if self._amazon_music is None:
            from .amazon_music.client import AmazonMusicClient

            self._amazon_music = AmazonMusicClient(client_wrapper=self._client_wrapper)
        return self._amazon_music

    @property
    def multiroom(self):
        if self._multiroom is None:
            from .multiroom.client import MultiroomClient

            self._multiroom = MultiroomClient(client_wrapper=self._client_wrapper)
        return self._multiroom

    @property
    def other(self):
        if self._other is None:
            from .other.client import OtherClient

            self._other = OtherClient(client_wrapper=self._client_wrapper)
        return self._other


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._generic: typing.Optional[AsyncGenericClient] = None
        self._device_information: typing.Optional[AsyncDeviceInformationClient] = None
        self._track_metadata: typing.Optional[AsyncTrackMetadataClient] = None
        self._playback_control: typing.Optional[AsyncPlaybackControlClient] = None
        self._network: typing.Optional[AsyncNetworkClient] = None
        self._equalizer: typing.Optional[AsyncEqualizerClient] = None
        self._device_control: typing.Optional[AsyncDeviceControlClient] = None
        self._alarm_clock: typing.Optional[AsyncAlarmClockClient] = None
        self._source_input_switch: typing.Optional[AsyncSourceInputSwitchClient] = None
        self._presets: typing.Optional[AsyncPresetsClient] = None
        self._audio_output_control: typing.Optional[AsyncAudioOutputControlClient] = None
        self._bluetooth: typing.Optional[AsyncBluetoothClient] = None
        self._room_correction: typing.Optional[AsyncRoomCorrectionClient] = None
        self._alexa: typing.Optional[AsyncAlexaClient] = None
        self._amazon_music: typing.Optional[AsyncAmazonMusicClient] = None
        self._multiroom: typing.Optional[AsyncMultiroomClient] = None
        self._other: typing.Optional[AsyncOtherClient] = None

    @property
    def generic(self):
        if self._generic is None:
            from .generic.client import AsyncGenericClient

            self._generic = AsyncGenericClient(client_wrapper=self._client_wrapper)
        return self._generic

    @property
    def device_information(self):
        if self._device_information is None:
            from .device_information.client import AsyncDeviceInformationClient

            self._device_information = AsyncDeviceInformationClient(client_wrapper=self._client_wrapper)
        return self._device_information

    @property
    def track_metadata(self):
        if self._track_metadata is None:
            from .track_metadata.client import AsyncTrackMetadataClient

            self._track_metadata = AsyncTrackMetadataClient(client_wrapper=self._client_wrapper)
        return self._track_metadata

    @property
    def playback_control(self):
        if self._playback_control is None:
            from .playback_control.client import AsyncPlaybackControlClient

            self._playback_control = AsyncPlaybackControlClient(client_wrapper=self._client_wrapper)
        return self._playback_control

    @property
    def network(self):
        if self._network is None:
            from .network.client import AsyncNetworkClient

            self._network = AsyncNetworkClient(client_wrapper=self._client_wrapper)
        return self._network

    @property
    def equalizer(self):
        if self._equalizer is None:
            from .equalizer.client import AsyncEqualizerClient

            self._equalizer = AsyncEqualizerClient(client_wrapper=self._client_wrapper)
        return self._equalizer

    @property
    def device_control(self):
        if self._device_control is None:
            from .device_control.client import AsyncDeviceControlClient

            self._device_control = AsyncDeviceControlClient(client_wrapper=self._client_wrapper)
        return self._device_control

    @property
    def alarm_clock(self):
        if self._alarm_clock is None:
            from .alarm_clock.client import AsyncAlarmClockClient

            self._alarm_clock = AsyncAlarmClockClient(client_wrapper=self._client_wrapper)
        return self._alarm_clock

    @property
    def source_input_switch(self):
        if self._source_input_switch is None:
            from .source_input_switch.client import AsyncSourceInputSwitchClient

            self._source_input_switch = AsyncSourceInputSwitchClient(client_wrapper=self._client_wrapper)
        return self._source_input_switch

    @property
    def presets(self):
        if self._presets is None:
            from .presets.client import AsyncPresetsClient

            self._presets = AsyncPresetsClient(client_wrapper=self._client_wrapper)
        return self._presets

    @property
    def audio_output_control(self):
        if self._audio_output_control is None:
            from .audio_output_control.client import AsyncAudioOutputControlClient

            self._audio_output_control = AsyncAudioOutputControlClient(client_wrapper=self._client_wrapper)
        return self._audio_output_control

    @property
    def bluetooth(self):
        if self._bluetooth is None:
            from .bluetooth.client import AsyncBluetoothClient

            self._bluetooth = AsyncBluetoothClient(client_wrapper=self._client_wrapper)
        return self._bluetooth

    @property
    def room_correction(self):
        if self._room_correction is None:
            from .room_correction.client import AsyncRoomCorrectionClient

            self._room_correction = AsyncRoomCorrectionClient(client_wrapper=self._client_wrapper)
        return self._room_correction

    @property
    def alexa(self):
        if self._alexa is None:
            from .alexa.client import AsyncAlexaClient

            self._alexa = AsyncAlexaClient(client_wrapper=self._client_wrapper)
        return self._alexa

    @property
    def amazon_music(self):
        if self._amazon_music is None:
            from .amazon_music.client import AsyncAmazonMusicClient

            self._amazon_music = AsyncAmazonMusicClient(client_wrapper=self._client_wrapper)
        return self._amazon_music

    @property
    def multiroom(self):
        if self._multiroom is None:
            from .multiroom.client import AsyncMultiroomClient

            self._multiroom = AsyncMultiroomClient(client_wrapper=self._client_wrapper)
        return self._multiroom

    @property
    def other(self):
        if self._other is None:
            from .other.client import AsyncOtherClient

            self._other = AsyncOtherClient(client_wrapper=self._client_wrapper)
        return self._other


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
