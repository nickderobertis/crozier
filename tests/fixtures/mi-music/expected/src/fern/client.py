

import typing

import httpx
from . import core
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.cmd_status_resp import CmdStatusResp
from .types.download_json_resp import DownloadJsonResp
from .types.latest_version_resp import LatestVersionResp
from .types.music_info_item import MusicInfoItem
from .types.music_info_resp import MusicInfoResp
from .types.playing_music_resp import PlayingMusicResp
from .types.playlist_musics_resp import PlaylistMusicsResp
from .types.playlist_names_resp import PlaylistNamesResp
from .types.ret_msg import RetMsg
from .types.set_volume_resp import SetVolumeResp
from .types.upload_cookie_resp import UploadCookieResp
from .types.version_resp import VersionResp
from .types.volume_resp import VolumeResp
from .types.ws_token_resp import WsTokenResp


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            base_url=base_url,
            username=username,
            password=password,
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
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def thdaction_thdaction_post(
        self, *, action: str, args: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        action : str

        args : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.thdaction_thdaction_post(
            action="action",
            args="args",
        )
        """
        _response = self._raw_client.thdaction_thdaction_post(action=action, args=args, request_options=request_options)
        return _response.data

    def read_index_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.read_index_get()
        """
        _response = self._raw_client.read_index_get(request_options=request_options)
        return _response.data

    def getversion_getversion_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionResp:
        """
        获取当前运行的xiaomusic版本号

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionResp
            版本信息

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.getversion_getversion_get()
        """
        _response = self._raw_client.getversion_getversion_get(request_options=request_options)
        return _response.data

    def getvolume_getvolume_get(
        self, *, did: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> VolumeResp:
        """
        获取指定设备的当前音量值（0-100）

        Parameters
        ----------
        did : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VolumeResp
            音量信息

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.getvolume_getvolume_get()
        """
        _response = self._raw_client.getvolume_getvolume_get(did=did, request_options=request_options)
        return _response.data

    def setvolume_setvolume_post(
        self, *, did: str, volume: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SetVolumeResp:
        """
        设置指定设备的音量值（0-100）

        Parameters
        ----------
        did : str
            设备ID

        volume : typing.Optional[int]
            音量大小 (0-100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetVolumeResp
            设置结果和当前音量

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.setvolume_setvolume_post(
            did="did",
        )
        """
        _response = self._raw_client.setvolume_setvolume_post(did=did, volume=volume, request_options=request_options)
        return _response.data

    def searchmusic_searchmusic_get(
        self, *, name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        根据关键词搜索音乐，返回匹配的歌曲名称列表

        Parameters
        ----------
        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            匹配的歌曲名称列表

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.searchmusic_searchmusic_get()
        """
        _response = self._raw_client.searchmusic_searchmusic_get(name=name, request_options=request_options)
        return _response.data

    def playingmusic_playingmusic_get(
        self, *, did: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> PlayingMusicResp:
        """
        获取指定设备的当前播放状态，包括是否正在播放、当前歌曲、当前歌单、播放进度等信息

        Parameters
        ----------
        did : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlayingMusicResp
            播放状态信息

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playingmusic_playingmusic_get()
        """
        _response = self._raw_client.playingmusic_playingmusic_get(did=did, request_options=request_options)
        return _response.data

    def do_cmd_cmd_post(self, *, did: str, cmd: str, request_options: typing.Optional[RequestOptions] = None) -> RetMsg:
        """
        向指定设备发送语音命令，系统会根据配置的关键词匹配执行相应操作

        Parameters
        ----------
        did : str
            设备ID

        cmd : str
            命令内容

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            命令执行结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.do_cmd_cmd_post(
            did="did",
            cmd="cmd",
        )
        """
        _response = self._raw_client.do_cmd_cmd_post(did=did, cmd=cmd, request_options=request_options)
        return _response.data

    def cmd_status_cmdstatus_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> CmdStatusResp:
        """
        查询最近一次命令的执行状态，返回finish（已完成）或running（执行中）

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CmdStatusResp
            命令执行状态

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cmd_status_cmdstatus_get()
        """
        _response = self._raw_client.cmd_status_cmdstatus_get(request_options=request_options)
        return _response.data

    def getsetting_getsetting_get(
        self, *, need_device_list: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        need_device_list : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            系统配置信息

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.getsetting_getsetting_get()
        """
        _response = self._raw_client.getsetting_getsetting_get(
            need_device_list=need_device_list, request_options=request_options
        )
        return _response.data

    def savesetting_savesetting_post(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        保存系统配置，密码字段如果为******或空则保持原值不变

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            保存结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.savesetting_savesetting_post()
        """
        _response = self._raw_client.savesetting_savesetting_post(request_options=request_options)
        return _response.data

    def musiclist_musiclist_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            所有歌单及其包含的歌曲列表

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.musiclist_musiclist_get()
        """
        _response = self._raw_client.musiclist_musiclist_get(request_options=request_options)
        return _response.data

    def musicinfo_musicinfo_get(
        self,
        *,
        name: str,
        musictag: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MusicInfoResp:
        """
        获取单首歌曲的详细信息，包括播放URL和可选的标签信息（标题、艺术家、专辑等）

        Parameters
        ----------
        name : str

        musictag : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicInfoResp
            歌曲信息

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.musicinfo_musicinfo_get(
            name="name",
        )
        """
        _response = self._raw_client.musicinfo_musicinfo_get(
            name=name, musictag=musictag, request_options=request_options
        )
        return _response.data

    def musicinfos_musicinfos_get(
        self,
        *,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        musictag: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MusicInfoItem]:
        """
        批量获取多首歌曲的详细信息，包括URL和可选的标签信息

        Parameters
        ----------
        name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        musictag : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MusicInfoItem]
            歌曲信息列表

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.musicinfos_musicinfos_get()
        """
        _response = self._raw_client.musicinfos_musicinfos_get(
            name=name, musictag=musictag, request_options=request_options
        )
        return _response.data

    def setmusictag_setmusictag_post(
        self,
        *,
        musicname: str,
        title: typing.Optional[str] = OMIT,
        artist: typing.Optional[str] = OMIT,
        album: typing.Optional[str] = OMIT,
        year: typing.Optional[str] = OMIT,
        genre: typing.Optional[str] = OMIT,
        lyrics: typing.Optional[str] = OMIT,
        picture: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        设置歌曲的ID3标签信息，包括标题、艺术家、专辑、年份、流派、歌词和封面图片

        Parameters
        ----------
        musicname : str
            歌曲文件名

        title : typing.Optional[str]
            标题

        artist : typing.Optional[str]
            艺术家

        album : typing.Optional[str]
            专辑

        year : typing.Optional[str]
            年份

        genre : typing.Optional[str]
            流派

        lyrics : typing.Optional[str]
            歌词

        picture : typing.Optional[str]
            封面图片(Base64)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            设置结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.setmusictag_setmusictag_post(
            musicname="musicname",
        )
        """
        _response = self._raw_client.setmusictag_setmusictag_post(
            musicname=musicname,
            title=title,
            artist=artist,
            album=album,
            year=year,
            genre=genre,
            lyrics=lyrics,
            picture=picture,
            request_options=request_options,
        )
        return _response.data

    def curplaylist_curplaylist_get(
        self, *, did: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        获取指定设备当前正在播放的歌单名称

        Parameters
        ----------
        did : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            当前播放列表名称，如果设备不存在则返回空字符串

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.curplaylist_curplaylist_get()
        """
        _response = self._raw_client.curplaylist_curplaylist_get(did=did, request_options=request_options)
        return _response.data

    def delmusic_delmusic_post(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        从音乐库中删除指定的歌曲文件

        Parameters
        ----------
        name : str
            歌曲文件名

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            删除操作结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delmusic_delmusic_post(
            name="name",
        )
        """
        _response = self._raw_client.delmusic_delmusic_post(name=name, request_options=request_options)
        return _response.data

    def playmusic_playmusic_post(
        self,
        *,
        did: str,
        musicname: typing.Optional[str] = OMIT,
        searchkey: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        在指定设备上播放歌曲，可通过歌曲名或搜索关键字播放

        Parameters
        ----------
        did : str
            设备ID

        musicname : typing.Optional[str]
            歌曲名

        searchkey : typing.Optional[str]
            搜索关键字

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            播放操作结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playmusic_playmusic_post(
            did="did",
        )
        """
        _response = self._raw_client.playmusic_playmusic_post(
            did=did, musicname=musicname, searchkey=searchkey, request_options=request_options
        )
        return _response.data

    def playmusiclist_playmusiclist_post(
        self,
        *,
        did: str,
        listname: typing.Optional[str] = OMIT,
        musicname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        在指定设备上播放指定歌单，可指定从歌单中的某首歌曲开始播放

        Parameters
        ----------
        did : str
            设备ID

        listname : typing.Optional[str]
            歌单名称

        musicname : typing.Optional[str]
            歌曲名称(可选)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            播放操作结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playmusiclist_playmusiclist_post(
            did="did",
        )
        """
        _response = self._raw_client.playmusiclist_playmusiclist_post(
            did=did, listname=listname, musicname=musicname, request_options=request_options
        )
        return _response.data

    def downloadjson_downloadjson_post(
        self, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DownloadJsonResp:
        """
        从指定URL下载JSON文件内容

        Parameters
        ----------
        url : str
            文件URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DownloadJsonResp
            下载结果和文件内容

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.downloadjson_downloadjson_post(
            url="url",
        )
        """
        _response = self._raw_client.downloadjson_downloadjson_post(url=url, request_options=request_options)
        return _response.data

    def downloadlog_downloadlog_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            日志文件内容（文本格式）

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.downloadlog_downloadlog_get()
        """
        _response = self._raw_client.downloadlog_downloadlog_get(request_options=request_options)
        return _response.data

    def playurl_playurl_get(
        self, *, did: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        did : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            播放结果列表

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playurl_playurl_get(
            did="did",
            url="url",
        )
        """
        _response = self._raw_client.playurl_playurl_get(did=did, url=url, request_options=request_options)
        return _response.data

    def playtts_playtts_get(
        self, *, did: str, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        在指定设备上播放文本转语音（TTS），设备会朗读指定的文本内容

        Parameters
        ----------
        did : str

        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            TTS播放结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playtts_playtts_get(
            did="did",
            text="text",
        )
        """
        _response = self._raw_client.playtts_playtts_get(did=did, text=text, request_options=request_options)
        return _response.data

    def refreshmusictag_refreshmusictag_post(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        清除并重新加载所有音乐文件的标签信息缓存

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            刷新操作结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.refreshmusictag_refreshmusictag_post()
        """
        _response = self._raw_client.refreshmusictag_refreshmusictag_post(request_options=request_options)
        return _response.data

    def debug_play_by_music_url_debug_play_by_music_url_post(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            播放结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.debug_play_by_music_url_debug_play_by_music_url_post()
        """
        _response = self._raw_client.debug_play_by_music_url_debug_play_by_music_url_post(
            request_options=request_options
        )
        return _response.data

    def latest_version_latestversion_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LatestVersionResp:
        """
        从远程仓库获取xiaomusic的最新版本号

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LatestVersionResp
            版本信息

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.latest_version_latestversion_get()
        """
        _response = self._raw_client.latest_version_latestversion_get(request_options=request_options)
        return _response.data

    def downloadplaylist_downloadplaylist_post(
        self, *, dirname: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        从URL下载歌单或B站收藏夹，支持自动创建目录并整理文件

        Parameters
        ----------
        dirname : str
            下载到的目录名称

        url : str
            歌单或视频的URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            下载操作结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.downloadplaylist_downloadplaylist_post(
            dirname="dirname",
            url="url",
        )
        """
        _response = self._raw_client.downloadplaylist_downloadplaylist_post(
            dirname=dirname, url=url, request_options=request_options
        )
        return _response.data

    def downloadonemusic_downloadonemusic_post(
        self, *, url: str, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        从URL下载单首歌曲或视频，支持自动命名或指定文件名

        Parameters
        ----------
        url : str
            歌曲或视频的URL

        name : typing.Optional[str]
            保存的文件名，留空则自动获取

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            下载操作结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.downloadonemusic_downloadonemusic_post(
            url="url",
        )
        """
        _response = self._raw_client.downloadonemusic_downloadonemusic_post(
            url=url, name=name, request_options=request_options
        )
        return _response.data

    def upload_yt_dlp_cookie_uploadytdlpcookie_post(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadCookieResp:
        """
        上传yt-dlp所需的cookies文件，用于访问需要登录的视频网站

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadCookieResp
            上传结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.upload_yt_dlp_cookie_uploadytdlpcookie_post()
        """
        _response = self._raw_client.upload_yt_dlp_cookie_uploadytdlpcookie_post(
            file=file, request_options=request_options
        )
        return _response.data

    def playlistadd_playlistadd_post(
        self, *, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        创建一个新的自定义歌单

        Parameters
        ----------
        name : typing.Optional[str]
            歌单名称

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            创建结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playlistadd_playlistadd_post()
        """
        _response = self._raw_client.playlistadd_playlistadd_post(name=name, request_options=request_options)
        return _response.data

    def playlistdel_playlistdel_post(
        self, *, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        删除指定的自定义歌单

        Parameters
        ----------
        name : typing.Optional[str]
            歌单名称

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            删除结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playlistdel_playlistdel_post()
        """
        _response = self._raw_client.playlistdel_playlistdel_post(name=name, request_options=request_options)
        return _response.data

    def playlistupdatename_playlistupdatename_post(
        self, *, oldname: str, newname: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        重命名指定的自定义歌单

        Parameters
        ----------
        oldname : str
            旧歌单名

        newname : str
            新歌单名

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            重命名结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playlistupdatename_playlistupdatename_post(
            oldname="oldname",
            newname="newname",
        )
        """
        _response = self._raw_client.playlistupdatename_playlistupdatename_post(
            oldname=oldname, newname=newname, request_options=request_options
        )
        return _response.data

    def getplaylistnames_playlistnames_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaylistNamesResp:
        """
        获取所有用户创建的自定义歌单名称列表

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaylistNamesResp
            歌单名称列表

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.getplaylistnames_playlistnames_get()
        """
        _response = self._raw_client.getplaylistnames_playlistnames_get(request_options=request_options)
        return _response.data

    def playlistaddmusic_playlistaddmusic_post(
        self,
        *,
        music_list: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        向指定歌单中添加一首或多首歌曲

        Parameters
        ----------
        music_list : typing.Sequence[str]
            歌曲名称列表

        name : typing.Optional[str]
            歌单名称

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            添加结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playlistaddmusic_playlistaddmusic_post(
            music_list=["music_list"],
        )
        """
        _response = self._raw_client.playlistaddmusic_playlistaddmusic_post(
            music_list=music_list, name=name, request_options=request_options
        )
        return _response.data

    def playlistdelmusic_playlistdelmusic_post(
        self,
        *,
        music_list: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        从指定歌单中移除一首或多首歌曲

        Parameters
        ----------
        music_list : typing.Sequence[str]
            歌曲名称列表

        name : typing.Optional[str]
            歌单名称

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            移除结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playlistdelmusic_playlistdelmusic_post(
            music_list=["music_list"],
        )
        """
        _response = self._raw_client.playlistdelmusic_playlistdelmusic_post(
            music_list=music_list, name=name, request_options=request_options
        )
        return _response.data

    def playlistupdatemusic_playlistupdatemusic_post(
        self,
        *,
        music_list: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        用新的歌曲列表完全替换指定歌单中的所有歌曲

        Parameters
        ----------
        music_list : typing.Sequence[str]
            歌曲名称列表

        name : typing.Optional[str]
            歌单名称

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            更新结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.playlistupdatemusic_playlistupdatemusic_post(
            music_list=["music_list"],
        )
        """
        _response = self._raw_client.playlistupdatemusic_playlistupdatemusic_post(
            music_list=music_list, name=name, request_options=request_options
        )
        return _response.data

    def getplaylist_playlistmusics_get(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaylistMusicsResp:
        """
        获取指定歌单中包含的所有歌曲名称列表

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaylistMusicsResp
            歌单中的歌曲列表

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.getplaylist_playlistmusics_get(
            name="name",
        )
        """
        _response = self._raw_client.getplaylist_playlistmusics_get(name=name, request_options=request_options)
        return _response.data

    def updateversion_updateversion_post(
        self,
        *,
        version: typing.Optional[str] = None,
        lite: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        更新系统到指定版本，更新完成后会自动重启服务

        Parameters
        ----------
        version : typing.Optional[str]

        lite : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            更新操作结果

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.updateversion_updateversion_post()
        """
        _response = self._raw_client.updateversion_updateversion_post(
            version=version, lite=lite, request_options=request_options
        )
        return _response.data

    def music_file_music_file_path_get(
        self,
        file_path: str,
        *,
        key: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        file_path : str

        key : typing.Optional[str]

        code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            音乐文件流（支持Range请求，用于音频播放）

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.music_file_music_file_path_get(
            file_path="file_path",
        )
        """
        with self._raw_client.music_file_music_file_path_get(
            file_path, key=key, code=code, request_options=request_options
        ) as r:
            yield from r.data

    def get_picture_picture_file_path_get(
        self,
        file_path: str,
        *,
        key: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        file_path : str

        key : typing.Optional[str]

        code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            图片文件流

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_picture_picture_file_path_get(
            file_path="file_path",
        )
        """
        with self._raw_client.get_picture_picture_file_path_get(
            file_path, key=key, code=code, request_options=request_options
        ) as r:
            yield from r.data

    def proxy_proxy_get(
        self, *, urlb64: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        通过Base64编码的URL代理下载文件，支持流式传输

        Parameters
        ----------
        urlb64 : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            文件流（根据URL返回对应的Content-Type）

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.proxy_proxy_get(
            urlb64="urlb64",
        )
        """
        with self._raw_client.proxy_proxy_get(urlb64=urlb64, request_options=request_options) as r:
            yield from r.data

    def generate_ws_token_generate_ws_token_get(
        self, *, did: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WsTokenResp:
        """
        生成用于WebSocket连接的JWT token，token有效期为5分钟

        Parameters
        ----------
        did : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WsTokenResp
            Token信息

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.generate_ws_token_generate_ws_token_get(
            did="did",
        )
        """
        _response = self._raw_client.generate_ws_token_generate_ws_token_get(did=did, request_options=request_options)
        return _response.data


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
    base_url : str
        The base url to use for requests from the client.

    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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

    client = AsyncFernApi(
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            base_url=base_url,
            username=username,
            password=password,
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
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def thdaction_thdaction_post(
        self, *, action: str, args: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        action : str

        args : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.thdaction_thdaction_post(
                action="action",
                args="args",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.thdaction_thdaction_post(
            action=action, args=args, request_options=request_options
        )
        return _response.data

    async def read_index_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.read_index_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_index_get(request_options=request_options)
        return _response.data

    async def getversion_getversion_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VersionResp:
        """
        获取当前运行的xiaomusic版本号

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionResp
            版本信息

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.getversion_getversion_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.getversion_getversion_get(request_options=request_options)
        return _response.data

    async def getvolume_getvolume_get(
        self, *, did: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> VolumeResp:
        """
        获取指定设备的当前音量值（0-100）

        Parameters
        ----------
        did : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VolumeResp
            音量信息

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.getvolume_getvolume_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.getvolume_getvolume_get(did=did, request_options=request_options)
        return _response.data

    async def setvolume_setvolume_post(
        self, *, did: str, volume: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SetVolumeResp:
        """
        设置指定设备的音量值（0-100）

        Parameters
        ----------
        did : str
            设备ID

        volume : typing.Optional[int]
            音量大小 (0-100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetVolumeResp
            设置结果和当前音量

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.setvolume_setvolume_post(
                did="did",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.setvolume_setvolume_post(
            did=did, volume=volume, request_options=request_options
        )
        return _response.data

    async def searchmusic_searchmusic_get(
        self, *, name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        根据关键词搜索音乐，返回匹配的歌曲名称列表

        Parameters
        ----------
        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            匹配的歌曲名称列表

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.searchmusic_searchmusic_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.searchmusic_searchmusic_get(name=name, request_options=request_options)
        return _response.data

    async def playingmusic_playingmusic_get(
        self, *, did: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> PlayingMusicResp:
        """
        获取指定设备的当前播放状态，包括是否正在播放、当前歌曲、当前歌单、播放进度等信息

        Parameters
        ----------
        did : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlayingMusicResp
            播放状态信息

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playingmusic_playingmusic_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.playingmusic_playingmusic_get(did=did, request_options=request_options)
        return _response.data

    async def do_cmd_cmd_post(
        self, *, did: str, cmd: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        向指定设备发送语音命令，系统会根据配置的关键词匹配执行相应操作

        Parameters
        ----------
        did : str
            设备ID

        cmd : str
            命令内容

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            命令执行结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.do_cmd_cmd_post(
                did="did",
                cmd="cmd",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.do_cmd_cmd_post(did=did, cmd=cmd, request_options=request_options)
        return _response.data

    async def cmd_status_cmdstatus_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CmdStatusResp:
        """
        查询最近一次命令的执行状态，返回finish（已完成）或running（执行中）

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CmdStatusResp
            命令执行状态

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cmd_status_cmdstatus_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.cmd_status_cmdstatus_get(request_options=request_options)
        return _response.data

    async def getsetting_getsetting_get(
        self, *, need_device_list: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        need_device_list : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            系统配置信息

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.getsetting_getsetting_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.getsetting_getsetting_get(
            need_device_list=need_device_list, request_options=request_options
        )
        return _response.data

    async def savesetting_savesetting_post(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        保存系统配置，密码字段如果为******或空则保持原值不变

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            保存结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.savesetting_savesetting_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.savesetting_savesetting_post(request_options=request_options)
        return _response.data

    async def musiclist_musiclist_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            所有歌单及其包含的歌曲列表

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.musiclist_musiclist_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.musiclist_musiclist_get(request_options=request_options)
        return _response.data

    async def musicinfo_musicinfo_get(
        self,
        *,
        name: str,
        musictag: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MusicInfoResp:
        """
        获取单首歌曲的详细信息，包括播放URL和可选的标签信息（标题、艺术家、专辑等）

        Parameters
        ----------
        name : str

        musictag : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicInfoResp
            歌曲信息

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.musicinfo_musicinfo_get(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.musicinfo_musicinfo_get(
            name=name, musictag=musictag, request_options=request_options
        )
        return _response.data

    async def musicinfos_musicinfos_get(
        self,
        *,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        musictag: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MusicInfoItem]:
        """
        批量获取多首歌曲的详细信息，包括URL和可选的标签信息

        Parameters
        ----------
        name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        musictag : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MusicInfoItem]
            歌曲信息列表

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.musicinfos_musicinfos_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.musicinfos_musicinfos_get(
            name=name, musictag=musictag, request_options=request_options
        )
        return _response.data

    async def setmusictag_setmusictag_post(
        self,
        *,
        musicname: str,
        title: typing.Optional[str] = OMIT,
        artist: typing.Optional[str] = OMIT,
        album: typing.Optional[str] = OMIT,
        year: typing.Optional[str] = OMIT,
        genre: typing.Optional[str] = OMIT,
        lyrics: typing.Optional[str] = OMIT,
        picture: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        设置歌曲的ID3标签信息，包括标题、艺术家、专辑、年份、流派、歌词和封面图片

        Parameters
        ----------
        musicname : str
            歌曲文件名

        title : typing.Optional[str]
            标题

        artist : typing.Optional[str]
            艺术家

        album : typing.Optional[str]
            专辑

        year : typing.Optional[str]
            年份

        genre : typing.Optional[str]
            流派

        lyrics : typing.Optional[str]
            歌词

        picture : typing.Optional[str]
            封面图片(Base64)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            设置结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.setmusictag_setmusictag_post(
                musicname="musicname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.setmusictag_setmusictag_post(
            musicname=musicname,
            title=title,
            artist=artist,
            album=album,
            year=year,
            genre=genre,
            lyrics=lyrics,
            picture=picture,
            request_options=request_options,
        )
        return _response.data

    async def curplaylist_curplaylist_get(
        self, *, did: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        获取指定设备当前正在播放的歌单名称

        Parameters
        ----------
        did : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            当前播放列表名称，如果设备不存在则返回空字符串

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.curplaylist_curplaylist_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.curplaylist_curplaylist_get(did=did, request_options=request_options)
        return _response.data

    async def delmusic_delmusic_post(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        从音乐库中删除指定的歌曲文件

        Parameters
        ----------
        name : str
            歌曲文件名

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            删除操作结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delmusic_delmusic_post(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delmusic_delmusic_post(name=name, request_options=request_options)
        return _response.data

    async def playmusic_playmusic_post(
        self,
        *,
        did: str,
        musicname: typing.Optional[str] = OMIT,
        searchkey: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        在指定设备上播放歌曲，可通过歌曲名或搜索关键字播放

        Parameters
        ----------
        did : str
            设备ID

        musicname : typing.Optional[str]
            歌曲名

        searchkey : typing.Optional[str]
            搜索关键字

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            播放操作结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playmusic_playmusic_post(
                did="did",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.playmusic_playmusic_post(
            did=did, musicname=musicname, searchkey=searchkey, request_options=request_options
        )
        return _response.data

    async def playmusiclist_playmusiclist_post(
        self,
        *,
        did: str,
        listname: typing.Optional[str] = OMIT,
        musicname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        在指定设备上播放指定歌单，可指定从歌单中的某首歌曲开始播放

        Parameters
        ----------
        did : str
            设备ID

        listname : typing.Optional[str]
            歌单名称

        musicname : typing.Optional[str]
            歌曲名称(可选)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            播放操作结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playmusiclist_playmusiclist_post(
                did="did",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.playmusiclist_playmusiclist_post(
            did=did, listname=listname, musicname=musicname, request_options=request_options
        )
        return _response.data

    async def downloadjson_downloadjson_post(
        self, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DownloadJsonResp:
        """
        从指定URL下载JSON文件内容

        Parameters
        ----------
        url : str
            文件URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DownloadJsonResp
            下载结果和文件内容

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.downloadjson_downloadjson_post(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.downloadjson_downloadjson_post(url=url, request_options=request_options)
        return _response.data

    async def downloadlog_downloadlog_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            日志文件内容（文本格式）

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.downloadlog_downloadlog_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.downloadlog_downloadlog_get(request_options=request_options)
        return _response.data

    async def playurl_playurl_get(
        self, *, did: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        did : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            播放结果列表

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playurl_playurl_get(
                did="did",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.playurl_playurl_get(did=did, url=url, request_options=request_options)
        return _response.data

    async def playtts_playtts_get(
        self, *, did: str, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        在指定设备上播放文本转语音（TTS），设备会朗读指定的文本内容

        Parameters
        ----------
        did : str

        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            TTS播放结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playtts_playtts_get(
                did="did",
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.playtts_playtts_get(did=did, text=text, request_options=request_options)
        return _response.data

    async def refreshmusictag_refreshmusictag_post(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        清除并重新加载所有音乐文件的标签信息缓存

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            刷新操作结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.refreshmusictag_refreshmusictag_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.refreshmusictag_refreshmusictag_post(request_options=request_options)
        return _response.data

    async def debug_play_by_music_url_debug_play_by_music_url_post(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            播放结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.debug_play_by_music_url_debug_play_by_music_url_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.debug_play_by_music_url_debug_play_by_music_url_post(
            request_options=request_options
        )
        return _response.data

    async def latest_version_latestversion_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LatestVersionResp:
        """
        从远程仓库获取xiaomusic的最新版本号

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LatestVersionResp
            版本信息

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.latest_version_latestversion_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.latest_version_latestversion_get(request_options=request_options)
        return _response.data

    async def downloadplaylist_downloadplaylist_post(
        self, *, dirname: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        从URL下载歌单或B站收藏夹，支持自动创建目录并整理文件

        Parameters
        ----------
        dirname : str
            下载到的目录名称

        url : str
            歌单或视频的URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            下载操作结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.downloadplaylist_downloadplaylist_post(
                dirname="dirname",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.downloadplaylist_downloadplaylist_post(
            dirname=dirname, url=url, request_options=request_options
        )
        return _response.data

    async def downloadonemusic_downloadonemusic_post(
        self, *, url: str, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        从URL下载单首歌曲或视频，支持自动命名或指定文件名

        Parameters
        ----------
        url : str
            歌曲或视频的URL

        name : typing.Optional[str]
            保存的文件名，留空则自动获取

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            下载操作结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.downloadonemusic_downloadonemusic_post(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.downloadonemusic_downloadonemusic_post(
            url=url, name=name, request_options=request_options
        )
        return _response.data

    async def upload_yt_dlp_cookie_uploadytdlpcookie_post(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadCookieResp:
        """
        上传yt-dlp所需的cookies文件，用于访问需要登录的视频网站

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadCookieResp
            上传结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.upload_yt_dlp_cookie_uploadytdlpcookie_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_yt_dlp_cookie_uploadytdlpcookie_post(
            file=file, request_options=request_options
        )
        return _response.data

    async def playlistadd_playlistadd_post(
        self, *, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        创建一个新的自定义歌单

        Parameters
        ----------
        name : typing.Optional[str]
            歌单名称

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            创建结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playlistadd_playlistadd_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.playlistadd_playlistadd_post(name=name, request_options=request_options)
        return _response.data

    async def playlistdel_playlistdel_post(
        self, *, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        删除指定的自定义歌单

        Parameters
        ----------
        name : typing.Optional[str]
            歌单名称

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            删除结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playlistdel_playlistdel_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.playlistdel_playlistdel_post(name=name, request_options=request_options)
        return _response.data

    async def playlistupdatename_playlistupdatename_post(
        self, *, oldname: str, newname: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetMsg:
        """
        重命名指定的自定义歌单

        Parameters
        ----------
        oldname : str
            旧歌单名

        newname : str
            新歌单名

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            重命名结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playlistupdatename_playlistupdatename_post(
                oldname="oldname",
                newname="newname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.playlistupdatename_playlistupdatename_post(
            oldname=oldname, newname=newname, request_options=request_options
        )
        return _response.data

    async def getplaylistnames_playlistnames_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaylistNamesResp:
        """
        获取所有用户创建的自定义歌单名称列表

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaylistNamesResp
            歌单名称列表

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.getplaylistnames_playlistnames_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.getplaylistnames_playlistnames_get(request_options=request_options)
        return _response.data

    async def playlistaddmusic_playlistaddmusic_post(
        self,
        *,
        music_list: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        向指定歌单中添加一首或多首歌曲

        Parameters
        ----------
        music_list : typing.Sequence[str]
            歌曲名称列表

        name : typing.Optional[str]
            歌单名称

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            添加结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playlistaddmusic_playlistaddmusic_post(
                music_list=["music_list"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.playlistaddmusic_playlistaddmusic_post(
            music_list=music_list, name=name, request_options=request_options
        )
        return _response.data

    async def playlistdelmusic_playlistdelmusic_post(
        self,
        *,
        music_list: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        从指定歌单中移除一首或多首歌曲

        Parameters
        ----------
        music_list : typing.Sequence[str]
            歌曲名称列表

        name : typing.Optional[str]
            歌单名称

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            移除结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playlistdelmusic_playlistdelmusic_post(
                music_list=["music_list"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.playlistdelmusic_playlistdelmusic_post(
            music_list=music_list, name=name, request_options=request_options
        )
        return _response.data

    async def playlistupdatemusic_playlistupdatemusic_post(
        self,
        *,
        music_list: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        用新的歌曲列表完全替换指定歌单中的所有歌曲

        Parameters
        ----------
        music_list : typing.Sequence[str]
            歌曲名称列表

        name : typing.Optional[str]
            歌单名称

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            更新结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.playlistupdatemusic_playlistupdatemusic_post(
                music_list=["music_list"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.playlistupdatemusic_playlistupdatemusic_post(
            music_list=music_list, name=name, request_options=request_options
        )
        return _response.data

    async def getplaylist_playlistmusics_get(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaylistMusicsResp:
        """
        获取指定歌单中包含的所有歌曲名称列表

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaylistMusicsResp
            歌单中的歌曲列表

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.getplaylist_playlistmusics_get(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getplaylist_playlistmusics_get(name=name, request_options=request_options)
        return _response.data

    async def updateversion_updateversion_post(
        self,
        *,
        version: typing.Optional[str] = None,
        lite: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetMsg:
        """
        更新系统到指定版本，更新完成后会自动重启服务

        Parameters
        ----------
        version : typing.Optional[str]

        lite : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetMsg
            更新操作结果

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.updateversion_updateversion_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.updateversion_updateversion_post(
            version=version, lite=lite, request_options=request_options
        )
        return _response.data

    async def music_file_music_file_path_get(
        self,
        file_path: str,
        *,
        key: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        file_path : str

        key : typing.Optional[str]

        code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            音乐文件流（支持Range请求，用于音频播放）

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.music_file_music_file_path_get(
                file_path="file_path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.music_file_music_file_path_get(
            file_path, key=key, code=code, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_picture_picture_file_path_get(
        self,
        file_path: str,
        *,
        key: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        file_path : str

        key : typing.Optional[str]

        code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            图片文件流

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_picture_picture_file_path_get(
                file_path="file_path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_picture_picture_file_path_get(
            file_path, key=key, code=code, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def proxy_proxy_get(
        self, *, urlb64: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        通过Base64编码的URL代理下载文件，支持流式传输

        Parameters
        ----------
        urlb64 : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            文件流（根据URL返回对应的Content-Type）

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.proxy_proxy_get(
                urlb64="urlb64",
            )


        asyncio.run(main())
        """
        async with self._raw_client.proxy_proxy_get(urlb64=urlb64, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def generate_ws_token_generate_ws_token_get(
        self, *, did: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WsTokenResp:
        """
        生成用于WebSocket连接的JWT token，token有效期为5分钟

        Parameters
        ----------
        did : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WsTokenResp
            Token信息

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generate_ws_token_generate_ws_token_get(
                did="did",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_ws_token_generate_ws_token_get(
            did=did, request_options=request_options
        )
        return _response.data
