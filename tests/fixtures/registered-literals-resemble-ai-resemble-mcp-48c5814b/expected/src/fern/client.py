

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .account.client import AccountClient, AsyncAccountClient
    from .agent_knowledge_base.client import AgentKnowledgeBaseClient, AsyncAgentKnowledgeBaseClient
    from .agent_phone_numbers.client import AgentPhoneNumbersClient, AsyncAgentPhoneNumbersClient
    from .agent_tools.client import AgentToolsClient, AsyncAgentToolsClient
    from .agent_webhooks.client import AgentWebhooksClient, AsyncAgentWebhooksClient
    from .agents.client import AgentsClient, AsyncAgentsClient
    from .audio_edit.client import AsyncAudioEditClient, AudioEditClient
    from .audio_enhancement.client import AsyncAudioEnhancementClient, AudioEnhancementClient
    from .audio_source_tracing.client import AsyncAudioSourceTracingClient, AudioSourceTracingClient
    from .clips.client import AsyncClipsClient, ClipsClient
    from .custom_pronunciations.client import AsyncCustomPronunciationsClient, CustomPronunciationsClient
    from .deepfake_detection.client import AsyncDeepfakeDetectionClient, DeepfakeDetectionClient
    from .detect_intelligence.client import AsyncDetectIntelligenceClient, DetectIntelligenceClient
    from .duets.client import AsyncDuetsClient, DuetsClient
    from .identity.client import AsyncIdentityClient, IdentityClient
    from .intelligence.client import AsyncIntelligenceClient, IntelligenceClient
    from .projects.client import AsyncProjectsClient, ProjectsClient
    from .recordings.client import AsyncRecordingsClient, RecordingsClient
    from .speech_to_text.client import AsyncSpeechToTextClient, SpeechToTextClient
    from .term_substitutions.client import AsyncTermSubstitutionsClient, TermSubstitutionsClient
    from .text_to_speech.client import AsyncTextToSpeechClient, TextToSpeechClient
    from .voice_design.client import AsyncVoiceDesignClient, VoiceDesignClient
    from .voice_settings_presets.client import AsyncVoiceSettingsPresetsClient, VoiceSettingsPresetsClient
    from .voices.client import AsyncVoicesClient, VoicesClient
    from .watermark.client import AsyncWatermarkClient, WatermarkClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



    token : typing.Union[str, typing.Callable[[], str]]
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

    client = FernApi(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
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
            environment=environment,
            token=token,
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
        self._text_to_speech: typing.Optional[TextToSpeechClient] = None
        self._speech_to_text: typing.Optional[SpeechToTextClient] = None
        self._audio_edit: typing.Optional[AudioEditClient] = None
        self._audio_enhancement: typing.Optional[AudioEnhancementClient] = None
        self._agents: typing.Optional[AgentsClient] = None
        self._agent_tools: typing.Optional[AgentToolsClient] = None
        self._agent_webhooks: typing.Optional[AgentWebhooksClient] = None
        self._agent_phone_numbers: typing.Optional[AgentPhoneNumbersClient] = None
        self._agent_knowledge_base: typing.Optional[AgentKnowledgeBaseClient] = None
        self._deepfake_detection: typing.Optional[DeepfakeDetectionClient] = None
        self._intelligence: typing.Optional[IntelligenceClient] = None
        self._detect_intelligence: typing.Optional[DetectIntelligenceClient] = None
        self._audio_source_tracing: typing.Optional[AudioSourceTracingClient] = None
        self._identity: typing.Optional[IdentityClient] = None
        self._watermark: typing.Optional[WatermarkClient] = None
        self._voices: typing.Optional[VoicesClient] = None
        self._voice_design: typing.Optional[VoiceDesignClient] = None
        self._recordings: typing.Optional[RecordingsClient] = None
        self._term_substitutions: typing.Optional[TermSubstitutionsClient] = None
        self._custom_pronunciations: typing.Optional[CustomPronunciationsClient] = None
        self._voice_settings_presets: typing.Optional[VoiceSettingsPresetsClient] = None
        self._projects: typing.Optional[ProjectsClient] = None
        self._clips: typing.Optional[ClipsClient] = None
        self._account: typing.Optional[AccountClient] = None
        self._duets: typing.Optional[DuetsClient] = None

    @property
    def text_to_speech(self):
        if self._text_to_speech is None:
            from .text_to_speech.client import TextToSpeechClient

            self._text_to_speech = TextToSpeechClient(client_wrapper=self._client_wrapper)
        return self._text_to_speech

    @property
    def speech_to_text(self):
        if self._speech_to_text is None:
            from .speech_to_text.client import SpeechToTextClient

            self._speech_to_text = SpeechToTextClient(client_wrapper=self._client_wrapper)
        return self._speech_to_text

    @property
    def audio_edit(self):
        if self._audio_edit is None:
            from .audio_edit.client import AudioEditClient

            self._audio_edit = AudioEditClient(client_wrapper=self._client_wrapper)
        return self._audio_edit

    @property
    def audio_enhancement(self):
        if self._audio_enhancement is None:
            from .audio_enhancement.client import AudioEnhancementClient

            self._audio_enhancement = AudioEnhancementClient(client_wrapper=self._client_wrapper)
        return self._audio_enhancement

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AgentsClient

            self._agents = AgentsClient(client_wrapper=self._client_wrapper)
        return self._agents

    @property
    def agent_tools(self):
        if self._agent_tools is None:
            from .agent_tools.client import AgentToolsClient

            self._agent_tools = AgentToolsClient(client_wrapper=self._client_wrapper)
        return self._agent_tools

    @property
    def agent_webhooks(self):
        if self._agent_webhooks is None:
            from .agent_webhooks.client import AgentWebhooksClient

            self._agent_webhooks = AgentWebhooksClient(client_wrapper=self._client_wrapper)
        return self._agent_webhooks

    @property
    def agent_phone_numbers(self):
        if self._agent_phone_numbers is None:
            from .agent_phone_numbers.client import AgentPhoneNumbersClient

            self._agent_phone_numbers = AgentPhoneNumbersClient(client_wrapper=self._client_wrapper)
        return self._agent_phone_numbers

    @property
    def agent_knowledge_base(self):
        if self._agent_knowledge_base is None:
            from .agent_knowledge_base.client import AgentKnowledgeBaseClient

            self._agent_knowledge_base = AgentKnowledgeBaseClient(client_wrapper=self._client_wrapper)
        return self._agent_knowledge_base

    @property
    def deepfake_detection(self):
        if self._deepfake_detection is None:
            from .deepfake_detection.client import DeepfakeDetectionClient

            self._deepfake_detection = DeepfakeDetectionClient(client_wrapper=self._client_wrapper)
        return self._deepfake_detection

    @property
    def intelligence(self):
        if self._intelligence is None:
            from .intelligence.client import IntelligenceClient

            self._intelligence = IntelligenceClient(client_wrapper=self._client_wrapper)
        return self._intelligence

    @property
    def detect_intelligence(self):
        if self._detect_intelligence is None:
            from .detect_intelligence.client import DetectIntelligenceClient

            self._detect_intelligence = DetectIntelligenceClient(client_wrapper=self._client_wrapper)
        return self._detect_intelligence

    @property
    def audio_source_tracing(self):
        if self._audio_source_tracing is None:
            from .audio_source_tracing.client import AudioSourceTracingClient

            self._audio_source_tracing = AudioSourceTracingClient(client_wrapper=self._client_wrapper)
        return self._audio_source_tracing

    @property
    def identity(self):
        if self._identity is None:
            from .identity.client import IdentityClient

            self._identity = IdentityClient(client_wrapper=self._client_wrapper)
        return self._identity

    @property
    def watermark(self):
        if self._watermark is None:
            from .watermark.client import WatermarkClient

            self._watermark = WatermarkClient(client_wrapper=self._client_wrapper)
        return self._watermark

    @property
    def voices(self):
        if self._voices is None:
            from .voices.client import VoicesClient

            self._voices = VoicesClient(client_wrapper=self._client_wrapper)
        return self._voices

    @property
    def voice_design(self):
        if self._voice_design is None:
            from .voice_design.client import VoiceDesignClient

            self._voice_design = VoiceDesignClient(client_wrapper=self._client_wrapper)
        return self._voice_design

    @property
    def recordings(self):
        if self._recordings is None:
            from .recordings.client import RecordingsClient

            self._recordings = RecordingsClient(client_wrapper=self._client_wrapper)
        return self._recordings

    @property
    def term_substitutions(self):
        if self._term_substitutions is None:
            from .term_substitutions.client import TermSubstitutionsClient

            self._term_substitutions = TermSubstitutionsClient(client_wrapper=self._client_wrapper)
        return self._term_substitutions

    @property
    def custom_pronunciations(self):
        if self._custom_pronunciations is None:
            from .custom_pronunciations.client import CustomPronunciationsClient

            self._custom_pronunciations = CustomPronunciationsClient(client_wrapper=self._client_wrapper)
        return self._custom_pronunciations

    @property
    def voice_settings_presets(self):
        if self._voice_settings_presets is None:
            from .voice_settings_presets.client import VoiceSettingsPresetsClient

            self._voice_settings_presets = VoiceSettingsPresetsClient(client_wrapper=self._client_wrapper)
        return self._voice_settings_presets

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import ProjectsClient

            self._projects = ProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def clips(self):
        if self._clips is None:
            from .clips.client import ClipsClient

            self._clips = ClipsClient(client_wrapper=self._client_wrapper)
        return self._clips

    @property
    def account(self):
        if self._account is None:
            from .account.client import AccountClient

            self._account = AccountClient(client_wrapper=self._client_wrapper)
        return self._account

    @property
    def duets(self):
        if self._duets is None:
            from .duets.client import DuetsClient

            self._duets = DuetsClient(client_wrapper=self._client_wrapper)
        return self._duets


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
    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



    token : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

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

    client = AsyncFernApi(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
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
            environment=environment,
            token=token,
            headers=headers,
            async_token=async_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._text_to_speech: typing.Optional[AsyncTextToSpeechClient] = None
        self._speech_to_text: typing.Optional[AsyncSpeechToTextClient] = None
        self._audio_edit: typing.Optional[AsyncAudioEditClient] = None
        self._audio_enhancement: typing.Optional[AsyncAudioEnhancementClient] = None
        self._agents: typing.Optional[AsyncAgentsClient] = None
        self._agent_tools: typing.Optional[AsyncAgentToolsClient] = None
        self._agent_webhooks: typing.Optional[AsyncAgentWebhooksClient] = None
        self._agent_phone_numbers: typing.Optional[AsyncAgentPhoneNumbersClient] = None
        self._agent_knowledge_base: typing.Optional[AsyncAgentKnowledgeBaseClient] = None
        self._deepfake_detection: typing.Optional[AsyncDeepfakeDetectionClient] = None
        self._intelligence: typing.Optional[AsyncIntelligenceClient] = None
        self._detect_intelligence: typing.Optional[AsyncDetectIntelligenceClient] = None
        self._audio_source_tracing: typing.Optional[AsyncAudioSourceTracingClient] = None
        self._identity: typing.Optional[AsyncIdentityClient] = None
        self._watermark: typing.Optional[AsyncWatermarkClient] = None
        self._voices: typing.Optional[AsyncVoicesClient] = None
        self._voice_design: typing.Optional[AsyncVoiceDesignClient] = None
        self._recordings: typing.Optional[AsyncRecordingsClient] = None
        self._term_substitutions: typing.Optional[AsyncTermSubstitutionsClient] = None
        self._custom_pronunciations: typing.Optional[AsyncCustomPronunciationsClient] = None
        self._voice_settings_presets: typing.Optional[AsyncVoiceSettingsPresetsClient] = None
        self._projects: typing.Optional[AsyncProjectsClient] = None
        self._clips: typing.Optional[AsyncClipsClient] = None
        self._account: typing.Optional[AsyncAccountClient] = None
        self._duets: typing.Optional[AsyncDuetsClient] = None

    @property
    def text_to_speech(self):
        if self._text_to_speech is None:
            from .text_to_speech.client import AsyncTextToSpeechClient

            self._text_to_speech = AsyncTextToSpeechClient(client_wrapper=self._client_wrapper)
        return self._text_to_speech

    @property
    def speech_to_text(self):
        if self._speech_to_text is None:
            from .speech_to_text.client import AsyncSpeechToTextClient

            self._speech_to_text = AsyncSpeechToTextClient(client_wrapper=self._client_wrapper)
        return self._speech_to_text

    @property
    def audio_edit(self):
        if self._audio_edit is None:
            from .audio_edit.client import AsyncAudioEditClient

            self._audio_edit = AsyncAudioEditClient(client_wrapper=self._client_wrapper)
        return self._audio_edit

    @property
    def audio_enhancement(self):
        if self._audio_enhancement is None:
            from .audio_enhancement.client import AsyncAudioEnhancementClient

            self._audio_enhancement = AsyncAudioEnhancementClient(client_wrapper=self._client_wrapper)
        return self._audio_enhancement

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AsyncAgentsClient

            self._agents = AsyncAgentsClient(client_wrapper=self._client_wrapper)
        return self._agents

    @property
    def agent_tools(self):
        if self._agent_tools is None:
            from .agent_tools.client import AsyncAgentToolsClient

            self._agent_tools = AsyncAgentToolsClient(client_wrapper=self._client_wrapper)
        return self._agent_tools

    @property
    def agent_webhooks(self):
        if self._agent_webhooks is None:
            from .agent_webhooks.client import AsyncAgentWebhooksClient

            self._agent_webhooks = AsyncAgentWebhooksClient(client_wrapper=self._client_wrapper)
        return self._agent_webhooks

    @property
    def agent_phone_numbers(self):
        if self._agent_phone_numbers is None:
            from .agent_phone_numbers.client import AsyncAgentPhoneNumbersClient

            self._agent_phone_numbers = AsyncAgentPhoneNumbersClient(client_wrapper=self._client_wrapper)
        return self._agent_phone_numbers

    @property
    def agent_knowledge_base(self):
        if self._agent_knowledge_base is None:
            from .agent_knowledge_base.client import AsyncAgentKnowledgeBaseClient

            self._agent_knowledge_base = AsyncAgentKnowledgeBaseClient(client_wrapper=self._client_wrapper)
        return self._agent_knowledge_base

    @property
    def deepfake_detection(self):
        if self._deepfake_detection is None:
            from .deepfake_detection.client import AsyncDeepfakeDetectionClient

            self._deepfake_detection = AsyncDeepfakeDetectionClient(client_wrapper=self._client_wrapper)
        return self._deepfake_detection

    @property
    def intelligence(self):
        if self._intelligence is None:
            from .intelligence.client import AsyncIntelligenceClient

            self._intelligence = AsyncIntelligenceClient(client_wrapper=self._client_wrapper)
        return self._intelligence

    @property
    def detect_intelligence(self):
        if self._detect_intelligence is None:
            from .detect_intelligence.client import AsyncDetectIntelligenceClient

            self._detect_intelligence = AsyncDetectIntelligenceClient(client_wrapper=self._client_wrapper)
        return self._detect_intelligence

    @property
    def audio_source_tracing(self):
        if self._audio_source_tracing is None:
            from .audio_source_tracing.client import AsyncAudioSourceTracingClient

            self._audio_source_tracing = AsyncAudioSourceTracingClient(client_wrapper=self._client_wrapper)
        return self._audio_source_tracing

    @property
    def identity(self):
        if self._identity is None:
            from .identity.client import AsyncIdentityClient

            self._identity = AsyncIdentityClient(client_wrapper=self._client_wrapper)
        return self._identity

    @property
    def watermark(self):
        if self._watermark is None:
            from .watermark.client import AsyncWatermarkClient

            self._watermark = AsyncWatermarkClient(client_wrapper=self._client_wrapper)
        return self._watermark

    @property
    def voices(self):
        if self._voices is None:
            from .voices.client import AsyncVoicesClient

            self._voices = AsyncVoicesClient(client_wrapper=self._client_wrapper)
        return self._voices

    @property
    def voice_design(self):
        if self._voice_design is None:
            from .voice_design.client import AsyncVoiceDesignClient

            self._voice_design = AsyncVoiceDesignClient(client_wrapper=self._client_wrapper)
        return self._voice_design

    @property
    def recordings(self):
        if self._recordings is None:
            from .recordings.client import AsyncRecordingsClient

            self._recordings = AsyncRecordingsClient(client_wrapper=self._client_wrapper)
        return self._recordings

    @property
    def term_substitutions(self):
        if self._term_substitutions is None:
            from .term_substitutions.client import AsyncTermSubstitutionsClient

            self._term_substitutions = AsyncTermSubstitutionsClient(client_wrapper=self._client_wrapper)
        return self._term_substitutions

    @property
    def custom_pronunciations(self):
        if self._custom_pronunciations is None:
            from .custom_pronunciations.client import AsyncCustomPronunciationsClient

            self._custom_pronunciations = AsyncCustomPronunciationsClient(client_wrapper=self._client_wrapper)
        return self._custom_pronunciations

    @property
    def voice_settings_presets(self):
        if self._voice_settings_presets is None:
            from .voice_settings_presets.client import AsyncVoiceSettingsPresetsClient

            self._voice_settings_presets = AsyncVoiceSettingsPresetsClient(client_wrapper=self._client_wrapper)
        return self._voice_settings_presets

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import AsyncProjectsClient

            self._projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def clips(self):
        if self._clips is None:
            from .clips.client import AsyncClipsClient

            self._clips = AsyncClipsClient(client_wrapper=self._client_wrapper)
        return self._clips

    @property
    def account(self):
        if self._account is None:
            from .account.client import AsyncAccountClient

            self._account = AsyncAccountClient(client_wrapper=self._client_wrapper)
        return self._account

    @property
    def duets(self):
        if self._duets is None:
            from .duets.client import AsyncDuetsClient

            self._duets = AsyncDuetsClient(client_wrapper=self._client_wrapper)
        return self._duets
