

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .character_data.client import AsyncCharacterDataClient, CharacterDataClient
    from .class_.client import AsyncClassClient, ClassClient
    from .class_levels.client import AsyncClassLevelsClient, ClassLevelsClient
    from .class_resource_lists.client import AsyncClassResourceListsClient, ClassResourceListsClient
    from .common.client import AsyncCommonClient, CommonClient
    from .equipment.client import AsyncEquipmentClient, EquipmentClient
    from .feats.client import AsyncFeatsClient, FeatsClient
    from .features.client import AsyncFeaturesClient, FeaturesClient
    from .game_mechanics.client import AsyncGameMechanicsClient, GameMechanicsClient
    from .monsters.client import AsyncMonstersClient, MonstersClient
    from .races.client import AsyncRacesClient, RacesClient
    from .rules.client import AsyncRulesClient, RulesClient
    from .spells.client import AsyncSpellsClient, SpellsClient
    from .subclasses.client import AsyncSubclassesClient, SubclassesClient
    from .subraces.client import AsyncSubracesClient, SubracesClient
    from .traits.client import AsyncTraitsClient, TraitsClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



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
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
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
        self._common: typing.Optional[CommonClient] = None
        self._character_data: typing.Optional[CharacterDataClient] = None
        self._class_: typing.Optional[ClassClient] = None
        self._class_resource_lists: typing.Optional[ClassResourceListsClient] = None
        self._class_levels: typing.Optional[ClassLevelsClient] = None
        self._game_mechanics: typing.Optional[GameMechanicsClient] = None
        self._equipment: typing.Optional[EquipmentClient] = None
        self._feats: typing.Optional[FeatsClient] = None
        self._features: typing.Optional[FeaturesClient] = None
        self._monsters: typing.Optional[MonstersClient] = None
        self._races: typing.Optional[RacesClient] = None
        self._rules: typing.Optional[RulesClient] = None
        self._spells: typing.Optional[SpellsClient] = None
        self._subclasses: typing.Optional[SubclassesClient] = None
        self._subraces: typing.Optional[SubracesClient] = None
        self._traits: typing.Optional[TraitsClient] = None

    @property
    def common(self):
        if self._common is None:
            from .common.client import CommonClient

            self._common = CommonClient(client_wrapper=self._client_wrapper)
        return self._common

    @property
    def character_data(self):
        if self._character_data is None:
            from .character_data.client import CharacterDataClient

            self._character_data = CharacterDataClient(client_wrapper=self._client_wrapper)
        return self._character_data

    @property
    def class_(self):
        if self._class_ is None:
            from .class_.client import ClassClient

            self._class_ = ClassClient(client_wrapper=self._client_wrapper)
        return self._class_

    @property
    def class_resource_lists(self):
        if self._class_resource_lists is None:
            from .class_resource_lists.client import ClassResourceListsClient

            self._class_resource_lists = ClassResourceListsClient(client_wrapper=self._client_wrapper)
        return self._class_resource_lists

    @property
    def class_levels(self):
        if self._class_levels is None:
            from .class_levels.client import ClassLevelsClient

            self._class_levels = ClassLevelsClient(client_wrapper=self._client_wrapper)
        return self._class_levels

    @property
    def game_mechanics(self):
        if self._game_mechanics is None:
            from .game_mechanics.client import GameMechanicsClient

            self._game_mechanics = GameMechanicsClient(client_wrapper=self._client_wrapper)
        return self._game_mechanics

    @property
    def equipment(self):
        if self._equipment is None:
            from .equipment.client import EquipmentClient

            self._equipment = EquipmentClient(client_wrapper=self._client_wrapper)
        return self._equipment

    @property
    def feats(self):
        if self._feats is None:
            from .feats.client import FeatsClient

            self._feats = FeatsClient(client_wrapper=self._client_wrapper)
        return self._feats

    @property
    def features(self):
        if self._features is None:
            from .features.client import FeaturesClient

            self._features = FeaturesClient(client_wrapper=self._client_wrapper)
        return self._features

    @property
    def monsters(self):
        if self._monsters is None:
            from .monsters.client import MonstersClient

            self._monsters = MonstersClient(client_wrapper=self._client_wrapper)
        return self._monsters

    @property
    def races(self):
        if self._races is None:
            from .races.client import RacesClient

            self._races = RacesClient(client_wrapper=self._client_wrapper)
        return self._races

    @property
    def rules(self):
        if self._rules is None:
            from .rules.client import RulesClient

            self._rules = RulesClient(client_wrapper=self._client_wrapper)
        return self._rules

    @property
    def spells(self):
        if self._spells is None:
            from .spells.client import SpellsClient

            self._spells = SpellsClient(client_wrapper=self._client_wrapper)
        return self._spells

    @property
    def subclasses(self):
        if self._subclasses is None:
            from .subclasses.client import SubclassesClient

            self._subclasses = SubclassesClient(client_wrapper=self._client_wrapper)
        return self._subclasses

    @property
    def subraces(self):
        if self._subraces is None:
            from .subraces.client import SubracesClient

            self._subraces = SubracesClient(client_wrapper=self._client_wrapper)
        return self._subraces

    @property
    def traits(self):
        if self._traits is None:
            from .traits.client import TraitsClient

            self._traits = TraitsClient(client_wrapper=self._client_wrapper)
        return self._traits


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



        Defaults to FernApiEnvironment.PRODUCTION



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
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
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
        self._common: typing.Optional[AsyncCommonClient] = None
        self._character_data: typing.Optional[AsyncCharacterDataClient] = None
        self._class_: typing.Optional[AsyncClassClient] = None
        self._class_resource_lists: typing.Optional[AsyncClassResourceListsClient] = None
        self._class_levels: typing.Optional[AsyncClassLevelsClient] = None
        self._game_mechanics: typing.Optional[AsyncGameMechanicsClient] = None
        self._equipment: typing.Optional[AsyncEquipmentClient] = None
        self._feats: typing.Optional[AsyncFeatsClient] = None
        self._features: typing.Optional[AsyncFeaturesClient] = None
        self._monsters: typing.Optional[AsyncMonstersClient] = None
        self._races: typing.Optional[AsyncRacesClient] = None
        self._rules: typing.Optional[AsyncRulesClient] = None
        self._spells: typing.Optional[AsyncSpellsClient] = None
        self._subclasses: typing.Optional[AsyncSubclassesClient] = None
        self._subraces: typing.Optional[AsyncSubracesClient] = None
        self._traits: typing.Optional[AsyncTraitsClient] = None

    @property
    def common(self):
        if self._common is None:
            from .common.client import AsyncCommonClient

            self._common = AsyncCommonClient(client_wrapper=self._client_wrapper)
        return self._common

    @property
    def character_data(self):
        if self._character_data is None:
            from .character_data.client import AsyncCharacterDataClient

            self._character_data = AsyncCharacterDataClient(client_wrapper=self._client_wrapper)
        return self._character_data

    @property
    def class_(self):
        if self._class_ is None:
            from .class_.client import AsyncClassClient

            self._class_ = AsyncClassClient(client_wrapper=self._client_wrapper)
        return self._class_

    @property
    def class_resource_lists(self):
        if self._class_resource_lists is None:
            from .class_resource_lists.client import AsyncClassResourceListsClient

            self._class_resource_lists = AsyncClassResourceListsClient(client_wrapper=self._client_wrapper)
        return self._class_resource_lists

    @property
    def class_levels(self):
        if self._class_levels is None:
            from .class_levels.client import AsyncClassLevelsClient

            self._class_levels = AsyncClassLevelsClient(client_wrapper=self._client_wrapper)
        return self._class_levels

    @property
    def game_mechanics(self):
        if self._game_mechanics is None:
            from .game_mechanics.client import AsyncGameMechanicsClient

            self._game_mechanics = AsyncGameMechanicsClient(client_wrapper=self._client_wrapper)
        return self._game_mechanics

    @property
    def equipment(self):
        if self._equipment is None:
            from .equipment.client import AsyncEquipmentClient

            self._equipment = AsyncEquipmentClient(client_wrapper=self._client_wrapper)
        return self._equipment

    @property
    def feats(self):
        if self._feats is None:
            from .feats.client import AsyncFeatsClient

            self._feats = AsyncFeatsClient(client_wrapper=self._client_wrapper)
        return self._feats

    @property
    def features(self):
        if self._features is None:
            from .features.client import AsyncFeaturesClient

            self._features = AsyncFeaturesClient(client_wrapper=self._client_wrapper)
        return self._features

    @property
    def monsters(self):
        if self._monsters is None:
            from .monsters.client import AsyncMonstersClient

            self._monsters = AsyncMonstersClient(client_wrapper=self._client_wrapper)
        return self._monsters

    @property
    def races(self):
        if self._races is None:
            from .races.client import AsyncRacesClient

            self._races = AsyncRacesClient(client_wrapper=self._client_wrapper)
        return self._races

    @property
    def rules(self):
        if self._rules is None:
            from .rules.client import AsyncRulesClient

            self._rules = AsyncRulesClient(client_wrapper=self._client_wrapper)
        return self._rules

    @property
    def spells(self):
        if self._spells is None:
            from .spells.client import AsyncSpellsClient

            self._spells = AsyncSpellsClient(client_wrapper=self._client_wrapper)
        return self._spells

    @property
    def subclasses(self):
        if self._subclasses is None:
            from .subclasses.client import AsyncSubclassesClient

            self._subclasses = AsyncSubclassesClient(client_wrapper=self._client_wrapper)
        return self._subclasses

    @property
    def subraces(self):
        if self._subraces is None:
            from .subraces.client import AsyncSubracesClient

            self._subraces = AsyncSubracesClient(client_wrapper=self._client_wrapper)
        return self._subraces

    @property
    def traits(self):
        if self._traits is None:
            from .traits.client import AsyncTraitsClient

            self._traits = AsyncTraitsClient(client_wrapper=self._client_wrapper)
        return self._traits


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
