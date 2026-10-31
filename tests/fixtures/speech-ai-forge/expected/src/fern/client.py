

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .forge_v2.client import AsyncForgeV2Client, ForgeV2Client
    from .google_api.client import AsyncGoogleApiClient, GoogleApiClient
    from .models.client import AsyncModelsClient, ModelsClient
    from .open_ai_api.client import AsyncOpenAiApiClient, OpenAiApiClient
    from .speaker.client import AsyncSpeakerClient, SpeakerClient
    from .ssml.client import AsyncSsmlClient, SsmlClient
    from .stt.client import AsyncSttClient, SttClient
    from .style.client import AsyncStyleClient, StyleClient
    from .system.client import AsyncSystemClient, SystemClient
    from .text.client import AsyncTextClient, TextClient
    from .tts.client import AsyncTtsClient, TtsClient
    from .voice_clone.client import AsyncVoiceCloneClient, VoiceCloneClient
    from .xtts.client import AsyncXttsClient, XttsClient


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
        self._system: typing.Optional[SystemClient] = None
        self._models: typing.Optional[ModelsClient] = None
        self._style: typing.Optional[StyleClient] = None
        self._speaker: typing.Optional[SpeakerClient] = None
        self._tts: typing.Optional[TtsClient] = None
        self._ssml: typing.Optional[SsmlClient] = None
        self._google_api: typing.Optional[GoogleApiClient] = None
        self._open_ai_api: typing.Optional[OpenAiApiClient] = None
        self._text: typing.Optional[TextClient] = None
        self._xtts: typing.Optional[XttsClient] = None
        self._stt: typing.Optional[SttClient] = None
        self._voice_clone: typing.Optional[VoiceCloneClient] = None
        self._forge_v2: typing.Optional[ForgeV2Client] = None

    @property
    def system(self):
        if self._system is None:
            from .system.client import SystemClient

            self._system = SystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def models(self):
        if self._models is None:
            from .models.client import ModelsClient

            self._models = ModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def style(self):
        if self._style is None:
            from .style.client import StyleClient

            self._style = StyleClient(client_wrapper=self._client_wrapper)
        return self._style

    @property
    def speaker(self):
        if self._speaker is None:
            from .speaker.client import SpeakerClient

            self._speaker = SpeakerClient(client_wrapper=self._client_wrapper)
        return self._speaker

    @property
    def tts(self):
        if self._tts is None:
            from .tts.client import TtsClient

            self._tts = TtsClient(client_wrapper=self._client_wrapper)
        return self._tts

    @property
    def ssml(self):
        if self._ssml is None:
            from .ssml.client import SsmlClient

            self._ssml = SsmlClient(client_wrapper=self._client_wrapper)
        return self._ssml

    @property
    def google_api(self):
        if self._google_api is None:
            from .google_api.client import GoogleApiClient

            self._google_api = GoogleApiClient(client_wrapper=self._client_wrapper)
        return self._google_api

    @property
    def open_ai_api(self):
        if self._open_ai_api is None:
            from .open_ai_api.client import OpenAiApiClient

            self._open_ai_api = OpenAiApiClient(client_wrapper=self._client_wrapper)
        return self._open_ai_api

    @property
    def text(self):
        if self._text is None:
            from .text.client import TextClient

            self._text = TextClient(client_wrapper=self._client_wrapper)
        return self._text

    @property
    def xtts(self):
        if self._xtts is None:
            from .xtts.client import XttsClient

            self._xtts = XttsClient(client_wrapper=self._client_wrapper)
        return self._xtts

    @property
    def stt(self):
        if self._stt is None:
            from .stt.client import SttClient

            self._stt = SttClient(client_wrapper=self._client_wrapper)
        return self._stt

    @property
    def voice_clone(self):
        if self._voice_clone is None:
            from .voice_clone.client import VoiceCloneClient

            self._voice_clone = VoiceCloneClient(client_wrapper=self._client_wrapper)
        return self._voice_clone

    @property
    def forge_v2(self):
        if self._forge_v2 is None:
            from .forge_v2.client import ForgeV2Client

            self._forge_v2 = ForgeV2Client(client_wrapper=self._client_wrapper)
        return self._forge_v2


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
        self._system: typing.Optional[AsyncSystemClient] = None
        self._models: typing.Optional[AsyncModelsClient] = None
        self._style: typing.Optional[AsyncStyleClient] = None
        self._speaker: typing.Optional[AsyncSpeakerClient] = None
        self._tts: typing.Optional[AsyncTtsClient] = None
        self._ssml: typing.Optional[AsyncSsmlClient] = None
        self._google_api: typing.Optional[AsyncGoogleApiClient] = None
        self._open_ai_api: typing.Optional[AsyncOpenAiApiClient] = None
        self._text: typing.Optional[AsyncTextClient] = None
        self._xtts: typing.Optional[AsyncXttsClient] = None
        self._stt: typing.Optional[AsyncSttClient] = None
        self._voice_clone: typing.Optional[AsyncVoiceCloneClient] = None
        self._forge_v2: typing.Optional[AsyncForgeV2Client] = None

    @property
    def system(self):
        if self._system is None:
            from .system.client import AsyncSystemClient

            self._system = AsyncSystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def models(self):
        if self._models is None:
            from .models.client import AsyncModelsClient

            self._models = AsyncModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def style(self):
        if self._style is None:
            from .style.client import AsyncStyleClient

            self._style = AsyncStyleClient(client_wrapper=self._client_wrapper)
        return self._style

    @property
    def speaker(self):
        if self._speaker is None:
            from .speaker.client import AsyncSpeakerClient

            self._speaker = AsyncSpeakerClient(client_wrapper=self._client_wrapper)
        return self._speaker

    @property
    def tts(self):
        if self._tts is None:
            from .tts.client import AsyncTtsClient

            self._tts = AsyncTtsClient(client_wrapper=self._client_wrapper)
        return self._tts

    @property
    def ssml(self):
        if self._ssml is None:
            from .ssml.client import AsyncSsmlClient

            self._ssml = AsyncSsmlClient(client_wrapper=self._client_wrapper)
        return self._ssml

    @property
    def google_api(self):
        if self._google_api is None:
            from .google_api.client import AsyncGoogleApiClient

            self._google_api = AsyncGoogleApiClient(client_wrapper=self._client_wrapper)
        return self._google_api

    @property
    def open_ai_api(self):
        if self._open_ai_api is None:
            from .open_ai_api.client import AsyncOpenAiApiClient

            self._open_ai_api = AsyncOpenAiApiClient(client_wrapper=self._client_wrapper)
        return self._open_ai_api

    @property
    def text(self):
        if self._text is None:
            from .text.client import AsyncTextClient

            self._text = AsyncTextClient(client_wrapper=self._client_wrapper)
        return self._text

    @property
    def xtts(self):
        if self._xtts is None:
            from .xtts.client import AsyncXttsClient

            self._xtts = AsyncXttsClient(client_wrapper=self._client_wrapper)
        return self._xtts

    @property
    def stt(self):
        if self._stt is None:
            from .stt.client import AsyncSttClient

            self._stt = AsyncSttClient(client_wrapper=self._client_wrapper)
        return self._stt

    @property
    def voice_clone(self):
        if self._voice_clone is None:
            from .voice_clone.client import AsyncVoiceCloneClient

            self._voice_clone = AsyncVoiceCloneClient(client_wrapper=self._client_wrapper)
        return self._voice_clone

    @property
    def forge_v2(self):
        if self._forge_v2 is None:
            from .forge_v2.client import AsyncForgeV2Client

            self._forge_v2 = AsyncForgeV2Client(client_wrapper=self._client_wrapper)
        return self._forge_v2


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
