

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_update_response import ConfigUpdateResponse
from ..types.log_search_response import LogSearchResponse
from ..types.log_tail_payload import LogTailPayload
from .raw_client import AsyncRawWebUiClient, RawWebUiClient
from .types.api_arr_open_item_request_kind import ApiArrOpenItemRequestKind
from .types.api_log_content_request_format import ApiLogContentRequestFormat
from .types.api_log_search_request_case import ApiLogSearchRequestCase
from .types.api_log_search_request_include_rotated import ApiLogSearchRequestIncludeRotated
from .types.api_log_search_request_regex import ApiLogSearchRequestRegex
from .types.web_arr_open_item_request_kind import WebArrOpenItemRequestKind
from .types.web_log_content_request_format import WebLogContentRequestFormat
from .types.web_log_search_request_case import WebLogSearchRequestCase
from .types.web_log_search_request_include_rotated import WebLogSearchRequestIncludeRotated
from .types.web_log_search_request_regex import WebLogSearchRequestRegex


OMIT = typing.cast(typing.Any, ...)


class WebUiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebUiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebUiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebUiClient
        """
        return self._raw_client

    def api_arr_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_arr_list()
        """
        _response = self._raw_client.api_arr_list(request_options=request_options)
        return _response.data

    def api_arr_rebuild(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_arr_rebuild()
        """
        _response = self._raw_client.api_arr_rebuild(request_options=request_options)
        return _response.data

    def api_arr_test_connection(
        self,
        *,
        api_key: typing.Optional[str] = OMIT,
        arr_type: typing.Optional[str] = OMIT,
        instance_key: typing.Optional[str] = OMIT,
        uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        api_key : typing.Optional[str]

        arr_type : typing.Optional[str]

        instance_key : typing.Optional[str]

        uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_arr_test_connection()
        """
        _response = self._raw_client.api_arr_test_connection(
            api_key=api_key, arr_type=arr_type, instance_key=instance_key, uri=uri, request_options=request_options
        )
        return _response.data

    def redirect_to_arr_ui_for_movie_series_artist_author_api(
        self, category: str, kind: str, entry_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        category : str

        kind : str

        entry_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.redirect_to_arr_ui_for_movie_series_artist_author_api(
            category="category",
            kind="kind",
            entry_id=1,
        )
        """
        _response = self._raw_client.redirect_to_arr_ui_for_movie_series_artist_author_api(
            category, kind, entry_id, request_options=request_options
        )
        return _response.data

    def api_arr_open_item(
        self,
        category: str,
        kind: ApiArrOpenItemRequestKind,
        entry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        category : str

        kind : ApiArrOpenItemRequestKind

        entry_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.web_ui import ApiArrOpenItemRequestKind

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_arr_open_item(
            category="category",
            kind=ApiArrOpenItemRequestKind.MOVIE,
            entry_id=1,
        )
        """
        _response = self._raw_client.api_arr_open_item(category, kind, entry_id, request_options=request_options)
        return _response.data

    def api_arr_restart(
        self, section: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        section : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_arr_restart(
            section="section",
        )
        """
        _response = self._raw_client.api_arr_restart(section, request_options=request_options)
        return _response.data

    def api_config_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_config_get()
        """
        _response = self._raw_client.api_config_get(request_options=request_options)
        return _response.data

    def api_config_post(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigUpdateResponse:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigUpdateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_config_post(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.api_config_post(request=request, request_options=request_options)
        return _response.data

    def api_config_schema_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Structured field registry (labels, kinds, reload hints)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_config_schema_get()
        """
        _response = self._raw_client.api_config_schema_get(request_options=request_options)
        return _response.data

    def api_download_update(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_download_update()
        """
        _response = self._raw_client.api_download_update(request_options=request_options)
        return _response.data

    def api_lidarr_albums(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_lidarr_albums(
            category="category",
        )
        """
        _response = self._raw_client.api_lidarr_albums(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def api_lidarr_artist_detail(
        self, category: str, artist_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        artist_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_lidarr_artist_detail(
            category="category",
            artist_id=1,
        )
        """
        _response = self._raw_client.api_lidarr_artist_detail(category, artist_id, request_options=request_options)
        return _response.data

    def api_lidarr_artist_thumbnail(
        self,
        category: str,
        artist_id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        category : str

        artist_id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Cached artist image bytes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_lidarr_artist_thumbnail(
            category="category",
            artist_id=1,
        )
        """
        with self._raw_client.api_lidarr_artist_thumbnail(
            category, artist_id, token=token, request_options=request_options
        ) as r:
            yield from r.data

    def api_lidarr_artists(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        monitored: typing.Optional[str] = None,
        missing: typing.Optional[bool] = None,
        reason: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        monitored : typing.Optional[str]

        missing : typing.Optional[bool]
            Restrict to artists with at least one monitored album whose file is missing.

        reason : typing.Optional[str]
            Restrict to artists with at least one album whose Reason matches. Accepts Missing, Quality, CustomFormat, Upgrade, or 'Not being searched' (also matches NULL).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_lidarr_artists(
            category="category",
        )
        """
        _response = self._raw_client.api_lidarr_artists(
            category,
            q=q,
            page=page,
            page_size=page_size,
            monitored=monitored,
            missing=missing,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    def lidarr_tracks_browse_api(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.lidarr_tracks_browse_api(
            category="category",
        )
        """
        _response = self._raw_client.lidarr_tracks_browse_api(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def api_loglevel(
        self, *, level: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        level : typing.Optional[str]
            CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG, TRACE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_loglevel()
        """
        _response = self._raw_client.api_loglevel(level=level, request_options=request_options)
        return _response.data

    def api_logs_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_logs_list()
        """
        _response = self._raw_client.api_logs_list(request_options=request_options)
        return _response.data

    def api_log_content(
        self,
        name: str,
        *,
        lines: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        since_bytes: typing.Optional[int] = None,
        inode: typing.Optional[int] = None,
        around_line: typing.Optional[int] = None,
        format: typing.Optional[ApiLogContentRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogTailPayload:
        """
        Parameters
        ----------
        name : str

        lines : typing.Optional[int]

        offset : typing.Optional[int]

        since_bytes : typing.Optional[int]
            Byte cursor for incremental delta

        inode : typing.Optional[int]
            Inode from prior response to detect rotation

        around_line : typing.Optional[int]
            Return a window around this 1-based line

        format : typing.Optional[ApiLogContentRequestFormat]
            Request JSON LogTailPayload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogTailPayload
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_log_content(
            name="name",
        )
        """
        _response = self._raw_client.api_log_content(
            name,
            lines=lines,
            offset=offset,
            since_bytes=since_bytes,
            inode=inode,
            around_line=around_line,
            format=format,
            request_options=request_options,
        )
        return _response.data

    def api_log_download(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            File download

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_log_download(
            name="name",
        )
        """
        with self._raw_client.api_log_download(name, request_options=request_options) as r:
            yield from r.data

    def api_log_search(
        self,
        name: str,
        *,
        q: str,
        case: typing.Optional[ApiLogSearchRequestCase] = None,
        regex: typing.Optional[ApiLogSearchRequestRegex] = None,
        max_matches: typing.Optional[int] = None,
        context: typing.Optional[int] = None,
        include_rotated: typing.Optional[ApiLogSearchRequestIncludeRotated] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogSearchResponse:
        """
        Parameters
        ----------
        name : str

        q : str

        case : typing.Optional[ApiLogSearchRequestCase]

        regex : typing.Optional[ApiLogSearchRequestRegex]

        max_matches : typing.Optional[int]

        context : typing.Optional[int]

        include_rotated : typing.Optional[ApiLogSearchRequestIncludeRotated]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_log_search(
            name="name",
            q="q",
        )
        """
        _response = self._raw_client.api_log_search(
            name,
            q=q,
            case=case,
            regex=regex,
            max_matches=max_matches,
            context=context,
            include_rotated=include_rotated,
            request_options=request_options,
        )
        return _response.data

    def api_log_stream(
        self,
        name: str,
        *,
        since_bytes: typing.Optional[int] = None,
        inode: typing.Optional[int] = None,
        lines: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        Server-Sent Events live tail. Prefer /web/* with session cookie for EventSource (cannot set Authorization).

        Parameters
        ----------
        name : str

        since_bytes : typing.Optional[int]

        inode : typing.Optional[int]

        lines : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            SSE stream (append/rotated/ping/reconnect events)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        response = client.web_ui.api_log_stream(
            name="name",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.api_log_stream(
            name, since_bytes=since_bytes, inode=inode, lines=lines, request_options=request_options
        ) as r:
            yield from r.data

    def api_meta(
        self, *, force: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_meta()
        """
        _response = self._raw_client.api_meta(force=force, request_options=request_options)
        return _response.data

    def api_processes(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_processes()
        """
        _response = self._raw_client.api_processes(request_options=request_options)
        return _response.data

    def api_processes_restart_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_processes_restart_all()
        """
        _response = self._raw_client.api_processes_restart_all(request_options=request_options)
        return _response.data

    def api_process_restart(
        self, category: str, kind: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        kind : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_process_restart(
            category="category",
            kind="kind",
        )
        """
        _response = self._raw_client.api_process_restart(category, kind, request_options=request_options)
        return _response.data

    def q_bittorrent_managed_categories_api(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.q_bittorrent_managed_categories_api()
        """
        _response = self._raw_client.q_bittorrent_managed_categories_api(request_options=request_options)
        return _response.data

    def api_radarr_movie_thumbnail(
        self,
        category: str,
        id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        category : str

        id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Cached movie poster image bytes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_radarr_movie_thumbnail(
            category="category",
            id=1,
        )
        """
        with self._raw_client.api_radarr_movie_thumbnail(
            category, id, token=token, request_options=request_options
        ) as r:
            yield from r.data

    def api_radarr_movies(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        year_min: typing.Optional[int] = None,
        year_max: typing.Optional[int] = None,
        monitored: typing.Optional[bool] = None,
        has_file: typing.Optional[bool] = None,
        quality_met: typing.Optional[bool] = None,
        is_request: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        year_min : typing.Optional[int]

        year_max : typing.Optional[int]

        monitored : typing.Optional[bool]

        has_file : typing.Optional[bool]

        quality_met : typing.Optional[bool]

        is_request : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_radarr_movies(
            category="category",
        )
        """
        _response = self._raw_client.api_radarr_movies(
            category,
            q=q,
            page=page,
            page_size=page_size,
            year_min=year_min,
            year_max=year_max,
            monitored=monitored,
            has_file=has_file,
            quality_met=quality_met,
            is_request=is_request,
            request_options=request_options,
        )
        return _response.data

    def readarr_author_detail_with_books_api(
        self, category: str, author_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        author_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.readarr_author_detail_with_books_api(
            category="category",
            author_id=1,
        )
        """
        _response = self._raw_client.readarr_author_detail_with_books_api(
            category, author_id, request_options=request_options
        )
        return _response.data

    def readarr_author_thumbnail_api(
        self, category: str, author_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        category : str

        author_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.readarr_author_thumbnail_api(
            category="category",
            author_id=1,
        )
        """
        _response = self._raw_client.readarr_author_thumbnail_api(category, author_id, request_options=request_options)
        return _response.data

    def readarr_authors_browse_api(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.readarr_authors_browse_api(
            category="category",
        )
        """
        _response = self._raw_client.readarr_authors_browse_api(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def api_sonarr_series(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_sonarr_series(
            category="category",
        )
        """
        _response = self._raw_client.api_sonarr_series(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def api_sonarr_series_thumbnail(
        self,
        category: str,
        id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        category : str

        id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Cached series poster image bytes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_sonarr_series_thumbnail(
            category="category",
            id=1,
        )
        """
        with self._raw_client.api_sonarr_series_thumbnail(
            category, id, token=token, request_options=request_options
        ) as r:
            yield from r.data

    def api_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_status()
        """
        _response = self._raw_client.api_status(request_options=request_options)
        return _response.data

    def api_torrents_distribution(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_torrents_distribution()
        """
        _response = self._raw_client.api_torrents_distribution(request_options=request_options)
        return _response.data

    def api_update(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.api_update()
        """
        _response = self._raw_client.api_update(request_options=request_options)
        return _response.data

    def web_arr_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_arr_list()
        """
        _response = self._raw_client.web_arr_list(request_options=request_options)
        return _response.data

    def web_arr_rebuild(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_arr_rebuild()
        """
        _response = self._raw_client.web_arr_rebuild(request_options=request_options)
        return _response.data

    def web_arr_test_connection(
        self,
        *,
        api_key: typing.Optional[str] = OMIT,
        arr_type: typing.Optional[str] = OMIT,
        instance_key: typing.Optional[str] = OMIT,
        uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        api_key : typing.Optional[str]

        arr_type : typing.Optional[str]

        instance_key : typing.Optional[str]

        uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_arr_test_connection()
        """
        _response = self._raw_client.web_arr_test_connection(
            api_key=api_key, arr_type=arr_type, instance_key=instance_key, uri=uri, request_options=request_options
        )
        return _response.data

    def redirect_to_arr_ui_for_movie_series_artist_author_web(
        self, category: str, kind: str, entry_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        category : str

        kind : str

        entry_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.redirect_to_arr_ui_for_movie_series_artist_author_web(
            category="category",
            kind="kind",
            entry_id=1,
        )
        """
        _response = self._raw_client.redirect_to_arr_ui_for_movie_series_artist_author_web(
            category, kind, entry_id, request_options=request_options
        )
        return _response.data

    def web_arr_open_item(
        self,
        category: str,
        kind: WebArrOpenItemRequestKind,
        entry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        category : str

        kind : WebArrOpenItemRequestKind

        entry_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.web_ui import WebArrOpenItemRequestKind

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_arr_open_item(
            category="category",
            kind=WebArrOpenItemRequestKind.MOVIE,
            entry_id=1,
        )
        """
        _response = self._raw_client.web_arr_open_item(category, kind, entry_id, request_options=request_options)
        return _response.data

    def web_arr_restart(
        self, section: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        section : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_arr_restart(
            section="section",
        )
        """
        _response = self._raw_client.web_arr_restart(section, request_options=request_options)
        return _response.data

    def web_config_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_config_get()
        """
        _response = self._raw_client.web_config_get(request_options=request_options)
        return _response.data

    def web_config_post(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigUpdateResponse:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigUpdateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_config_post(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.web_config_post(request=request, request_options=request_options)
        return _response.data

    def web_config_schema_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Structured field registry (labels, kinds, reload hints)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_config_schema_get()
        """
        _response = self._raw_client.web_config_schema_get(request_options=request_options)
        return _response.data

    def web_download_update(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_download_update()
        """
        _response = self._raw_client.web_download_update(request_options=request_options)
        return _response.data

    def web_lidarr_albums(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_lidarr_albums(
            category="category",
        )
        """
        _response = self._raw_client.web_lidarr_albums(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def web_lidarr_artist_detail(
        self, category: str, artist_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        artist_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_lidarr_artist_detail(
            category="category",
            artist_id=1,
        )
        """
        _response = self._raw_client.web_lidarr_artist_detail(category, artist_id, request_options=request_options)
        return _response.data

    def web_lidarr_artist_thumbnail(
        self,
        category: str,
        artist_id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        category : str

        artist_id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Cached artist image bytes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_lidarr_artist_thumbnail(
            category="category",
            artist_id=1,
        )
        """
        with self._raw_client.web_lidarr_artist_thumbnail(
            category, artist_id, token=token, request_options=request_options
        ) as r:
            yield from r.data

    def web_lidarr_artists(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        monitored: typing.Optional[str] = None,
        missing: typing.Optional[bool] = None,
        reason: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        monitored : typing.Optional[str]

        missing : typing.Optional[bool]
            Restrict to artists with at least one monitored album whose file is missing.

        reason : typing.Optional[str]
            Restrict to artists with at least one album whose Reason matches. Accepts Missing, Quality, CustomFormat, Upgrade, or 'Not being searched' (also matches NULL).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_lidarr_artists(
            category="category",
        )
        """
        _response = self._raw_client.web_lidarr_artists(
            category,
            q=q,
            page=page,
            page_size=page_size,
            monitored=monitored,
            missing=missing,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    def lidarr_tracks_browse_web(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.lidarr_tracks_browse_web(
            category="category",
        )
        """
        _response = self._raw_client.lidarr_tracks_browse_web(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def web_loglevel(
        self, *, level: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        level : typing.Optional[str]
            CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG, TRACE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_loglevel()
        """
        _response = self._raw_client.web_loglevel(level=level, request_options=request_options)
        return _response.data

    def web_logs_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_logs_list()
        """
        _response = self._raw_client.web_logs_list(request_options=request_options)
        return _response.data

    def web_log_content(
        self,
        name: str,
        *,
        lines: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        since_bytes: typing.Optional[int] = None,
        inode: typing.Optional[int] = None,
        around_line: typing.Optional[int] = None,
        format: typing.Optional[WebLogContentRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogTailPayload:
        """
        Parameters
        ----------
        name : str

        lines : typing.Optional[int]

        offset : typing.Optional[int]

        since_bytes : typing.Optional[int]
            Byte cursor for incremental delta

        inode : typing.Optional[int]
            Inode from prior response to detect rotation

        around_line : typing.Optional[int]
            Return a window around this 1-based line

        format : typing.Optional[WebLogContentRequestFormat]
            Request JSON LogTailPayload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogTailPayload
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_log_content(
            name="name",
        )
        """
        _response = self._raw_client.web_log_content(
            name,
            lines=lines,
            offset=offset,
            since_bytes=since_bytes,
            inode=inode,
            around_line=around_line,
            format=format,
            request_options=request_options,
        )
        return _response.data

    def web_log_download(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            File download

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_log_download(
            name="name",
        )
        """
        with self._raw_client.web_log_download(name, request_options=request_options) as r:
            yield from r.data

    def web_log_search(
        self,
        name: str,
        *,
        q: str,
        case: typing.Optional[WebLogSearchRequestCase] = None,
        regex: typing.Optional[WebLogSearchRequestRegex] = None,
        max_matches: typing.Optional[int] = None,
        context: typing.Optional[int] = None,
        include_rotated: typing.Optional[WebLogSearchRequestIncludeRotated] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogSearchResponse:
        """
        Parameters
        ----------
        name : str

        q : str

        case : typing.Optional[WebLogSearchRequestCase]

        regex : typing.Optional[WebLogSearchRequestRegex]

        max_matches : typing.Optional[int]

        context : typing.Optional[int]

        include_rotated : typing.Optional[WebLogSearchRequestIncludeRotated]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_log_search(
            name="name",
            q="q",
        )
        """
        _response = self._raw_client.web_log_search(
            name,
            q=q,
            case=case,
            regex=regex,
            max_matches=max_matches,
            context=context,
            include_rotated=include_rotated,
            request_options=request_options,
        )
        return _response.data

    def web_log_stream(
        self,
        name: str,
        *,
        since_bytes: typing.Optional[int] = None,
        inode: typing.Optional[int] = None,
        lines: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        Server-Sent Events live tail. Prefer /web/* with session cookie for EventSource (cannot set Authorization).

        Parameters
        ----------
        name : str

        since_bytes : typing.Optional[int]

        inode : typing.Optional[int]

        lines : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            SSE stream (append/rotated/ping/reconnect events)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        response = client.web_ui.web_log_stream(
            name="name",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.web_log_stream(
            name, since_bytes=since_bytes, inode=inode, lines=lines, request_options=request_options
        ) as r:
            yield from r.data

    def web_processes(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_processes()
        """
        _response = self._raw_client.web_processes(request_options=request_options)
        return _response.data

    def web_processes_restart_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_processes_restart_all()
        """
        _response = self._raw_client.web_processes_restart_all(request_options=request_options)
        return _response.data

    def web_process_restart(
        self, category: str, kind: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        kind : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_process_restart(
            category="category",
            kind="kind",
        )
        """
        _response = self._raw_client.web_process_restart(category, kind, request_options=request_options)
        return _response.data

    def web_qbit_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_qbit_categories()
        """
        _response = self._raw_client.web_qbit_categories(request_options=request_options)
        return _response.data

    def web_qbit_overview(
        self, *, instance: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        instance : typing.Optional[str]
            qBittorrent instance name, or omit/`all` for every instance

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_qbit_overview()
        """
        _response = self._raw_client.web_qbit_overview(instance=instance, request_options=request_options)
        return _response.data

    def web_radarr_movie_thumbnail(
        self,
        category: str,
        id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        category : str

        id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Cached movie poster image bytes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_radarr_movie_thumbnail(
            category="category",
            id=1,
        )
        """
        with self._raw_client.web_radarr_movie_thumbnail(
            category, id, token=token, request_options=request_options
        ) as r:
            yield from r.data

    def web_radarr_movies(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        year_min: typing.Optional[int] = None,
        year_max: typing.Optional[int] = None,
        monitored: typing.Optional[bool] = None,
        has_file: typing.Optional[bool] = None,
        quality_met: typing.Optional[bool] = None,
        is_request: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        year_min : typing.Optional[int]

        year_max : typing.Optional[int]

        monitored : typing.Optional[bool]

        has_file : typing.Optional[bool]

        quality_met : typing.Optional[bool]

        is_request : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_radarr_movies(
            category="category",
        )
        """
        _response = self._raw_client.web_radarr_movies(
            category,
            q=q,
            page=page,
            page_size=page_size,
            year_min=year_min,
            year_max=year_max,
            monitored=monitored,
            has_file=has_file,
            quality_met=quality_met,
            is_request=is_request,
            request_options=request_options,
        )
        return _response.data

    def readarr_author_detail_with_books_web(
        self, category: str, author_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        author_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.readarr_author_detail_with_books_web(
            category="category",
            author_id=1,
        )
        """
        _response = self._raw_client.readarr_author_detail_with_books_web(
            category, author_id, request_options=request_options
        )
        return _response.data

    def readarr_author_thumbnail_web(
        self, category: str, author_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        category : str

        author_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.readarr_author_thumbnail_web(
            category="category",
            author_id=1,
        )
        """
        _response = self._raw_client.readarr_author_thumbnail_web(category, author_id, request_options=request_options)
        return _response.data

    def readarr_authors_browse_web(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.readarr_authors_browse_web(
            category="category",
        )
        """
        _response = self._raw_client.readarr_authors_browse_web(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def web_sonarr_series(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_sonarr_series(
            category="category",
        )
        """
        _response = self._raw_client.web_sonarr_series(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def web_sonarr_series_thumbnail(
        self,
        category: str,
        id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        category : str

        id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Cached series poster image bytes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_sonarr_series_thumbnail(
            category="category",
            id=1,
        )
        """
        with self._raw_client.web_sonarr_series_thumbnail(
            category, id, token=token, request_options=request_options
        ) as r:
            yield from r.data

    def web_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_status()
        """
        _response = self._raw_client.web_status(request_options=request_options)
        return _response.data

    def torrent_distribution_by_category_web(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.torrent_distribution_by_category_web()
        """
        _response = self._raw_client.torrent_distribution_by_category_web(request_options=request_options)
        return _response.data

    def web_update(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_ui.web_update()
        """
        _response = self._raw_client.web_update(request_options=request_options)
        return _response.data


class AsyncWebUiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebUiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebUiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebUiClient
        """
        return self._raw_client

    async def api_arr_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_arr_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_arr_list(request_options=request_options)
        return _response.data

    async def api_arr_rebuild(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_arr_rebuild()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_arr_rebuild(request_options=request_options)
        return _response.data

    async def api_arr_test_connection(
        self,
        *,
        api_key: typing.Optional[str] = OMIT,
        arr_type: typing.Optional[str] = OMIT,
        instance_key: typing.Optional[str] = OMIT,
        uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        api_key : typing.Optional[str]

        arr_type : typing.Optional[str]

        instance_key : typing.Optional[str]

        uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_arr_test_connection()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_arr_test_connection(
            api_key=api_key, arr_type=arr_type, instance_key=instance_key, uri=uri, request_options=request_options
        )
        return _response.data

    async def redirect_to_arr_ui_for_movie_series_artist_author_api(
        self, category: str, kind: str, entry_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        category : str

        kind : str

        entry_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.redirect_to_arr_ui_for_movie_series_artist_author_api(
                category="category",
                kind="kind",
                entry_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.redirect_to_arr_ui_for_movie_series_artist_author_api(
            category, kind, entry_id, request_options=request_options
        )
        return _response.data

    async def api_arr_open_item(
        self,
        category: str,
        kind: ApiArrOpenItemRequestKind,
        entry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        category : str

        kind : ApiArrOpenItemRequestKind

        entry_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.web_ui import ApiArrOpenItemRequestKind

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_arr_open_item(
                category="category",
                kind=ApiArrOpenItemRequestKind.MOVIE,
                entry_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_arr_open_item(category, kind, entry_id, request_options=request_options)
        return _response.data

    async def api_arr_restart(
        self, section: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        section : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_arr_restart(
                section="section",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_arr_restart(section, request_options=request_options)
        return _response.data

    async def api_config_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_config_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_config_get(request_options=request_options)
        return _response.data

    async def api_config_post(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigUpdateResponse:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigUpdateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_config_post(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_config_post(request=request, request_options=request_options)
        return _response.data

    async def api_config_schema_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Structured field registry (labels, kinds, reload hints)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_config_schema_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_config_schema_get(request_options=request_options)
        return _response.data

    async def api_download_update(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_download_update()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_download_update(request_options=request_options)
        return _response.data

    async def api_lidarr_albums(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_lidarr_albums(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_lidarr_albums(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def api_lidarr_artist_detail(
        self, category: str, artist_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        artist_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_lidarr_artist_detail(
                category="category",
                artist_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_lidarr_artist_detail(
            category, artist_id, request_options=request_options
        )
        return _response.data

    async def api_lidarr_artist_thumbnail(
        self,
        category: str,
        artist_id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        category : str

        artist_id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Cached artist image bytes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_lidarr_artist_thumbnail(
                category="category",
                artist_id=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.api_lidarr_artist_thumbnail(
            category, artist_id, token=token, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def api_lidarr_artists(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        monitored: typing.Optional[str] = None,
        missing: typing.Optional[bool] = None,
        reason: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        monitored : typing.Optional[str]

        missing : typing.Optional[bool]
            Restrict to artists with at least one monitored album whose file is missing.

        reason : typing.Optional[str]
            Restrict to artists with at least one album whose Reason matches. Accepts Missing, Quality, CustomFormat, Upgrade, or 'Not being searched' (also matches NULL).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_lidarr_artists(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_lidarr_artists(
            category,
            q=q,
            page=page,
            page_size=page_size,
            monitored=monitored,
            missing=missing,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    async def lidarr_tracks_browse_api(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.lidarr_tracks_browse_api(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lidarr_tracks_browse_api(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def api_loglevel(
        self, *, level: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        level : typing.Optional[str]
            CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG, TRACE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_loglevel()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_loglevel(level=level, request_options=request_options)
        return _response.data

    async def api_logs_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_logs_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_logs_list(request_options=request_options)
        return _response.data

    async def api_log_content(
        self,
        name: str,
        *,
        lines: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        since_bytes: typing.Optional[int] = None,
        inode: typing.Optional[int] = None,
        around_line: typing.Optional[int] = None,
        format: typing.Optional[ApiLogContentRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogTailPayload:
        """
        Parameters
        ----------
        name : str

        lines : typing.Optional[int]

        offset : typing.Optional[int]

        since_bytes : typing.Optional[int]
            Byte cursor for incremental delta

        inode : typing.Optional[int]
            Inode from prior response to detect rotation

        around_line : typing.Optional[int]
            Return a window around this 1-based line

        format : typing.Optional[ApiLogContentRequestFormat]
            Request JSON LogTailPayload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogTailPayload
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_log_content(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_log_content(
            name,
            lines=lines,
            offset=offset,
            since_bytes=since_bytes,
            inode=inode,
            around_line=around_line,
            format=format,
            request_options=request_options,
        )
        return _response.data

    async def api_log_download(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            File download

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_log_download(
                name="name",
            )


        asyncio.run(main())
        """
        async with self._raw_client.api_log_download(name, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def api_log_search(
        self,
        name: str,
        *,
        q: str,
        case: typing.Optional[ApiLogSearchRequestCase] = None,
        regex: typing.Optional[ApiLogSearchRequestRegex] = None,
        max_matches: typing.Optional[int] = None,
        context: typing.Optional[int] = None,
        include_rotated: typing.Optional[ApiLogSearchRequestIncludeRotated] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogSearchResponse:
        """
        Parameters
        ----------
        name : str

        q : str

        case : typing.Optional[ApiLogSearchRequestCase]

        regex : typing.Optional[ApiLogSearchRequestRegex]

        max_matches : typing.Optional[int]

        context : typing.Optional[int]

        include_rotated : typing.Optional[ApiLogSearchRequestIncludeRotated]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_log_search(
                name="name",
                q="q",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_log_search(
            name,
            q=q,
            case=case,
            regex=regex,
            max_matches=max_matches,
            context=context,
            include_rotated=include_rotated,
            request_options=request_options,
        )
        return _response.data

    async def api_log_stream(
        self,
        name: str,
        *,
        since_bytes: typing.Optional[int] = None,
        inode: typing.Optional[int] = None,
        lines: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        Server-Sent Events live tail. Prefer /web/* with session cookie for EventSource (cannot set Authorization).

        Parameters
        ----------
        name : str

        since_bytes : typing.Optional[int]

        inode : typing.Optional[int]

        lines : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            SSE stream (append/rotated/ping/reconnect events)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.web_ui.api_log_stream(
                name="name",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.api_log_stream(
            name, since_bytes=since_bytes, inode=inode, lines=lines, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def api_meta(
        self, *, force: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_meta()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_meta(force=force, request_options=request_options)
        return _response.data

    async def api_processes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_processes()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_processes(request_options=request_options)
        return _response.data

    async def api_processes_restart_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_processes_restart_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_processes_restart_all(request_options=request_options)
        return _response.data

    async def api_process_restart(
        self, category: str, kind: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        kind : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_process_restart(
                category="category",
                kind="kind",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_process_restart(category, kind, request_options=request_options)
        return _response.data

    async def q_bittorrent_managed_categories_api(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.q_bittorrent_managed_categories_api()


        asyncio.run(main())
        """
        _response = await self._raw_client.q_bittorrent_managed_categories_api(request_options=request_options)
        return _response.data

    async def api_radarr_movie_thumbnail(
        self,
        category: str,
        id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        category : str

        id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Cached movie poster image bytes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_radarr_movie_thumbnail(
                category="category",
                id=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.api_radarr_movie_thumbnail(
            category, id, token=token, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def api_radarr_movies(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        year_min: typing.Optional[int] = None,
        year_max: typing.Optional[int] = None,
        monitored: typing.Optional[bool] = None,
        has_file: typing.Optional[bool] = None,
        quality_met: typing.Optional[bool] = None,
        is_request: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        year_min : typing.Optional[int]

        year_max : typing.Optional[int]

        monitored : typing.Optional[bool]

        has_file : typing.Optional[bool]

        quality_met : typing.Optional[bool]

        is_request : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_radarr_movies(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_radarr_movies(
            category,
            q=q,
            page=page,
            page_size=page_size,
            year_min=year_min,
            year_max=year_max,
            monitored=monitored,
            has_file=has_file,
            quality_met=quality_met,
            is_request=is_request,
            request_options=request_options,
        )
        return _response.data

    async def readarr_author_detail_with_books_api(
        self, category: str, author_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        author_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.readarr_author_detail_with_books_api(
                category="category",
                author_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.readarr_author_detail_with_books_api(
            category, author_id, request_options=request_options
        )
        return _response.data

    async def readarr_author_thumbnail_api(
        self, category: str, author_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        category : str

        author_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.readarr_author_thumbnail_api(
                category="category",
                author_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.readarr_author_thumbnail_api(
            category, author_id, request_options=request_options
        )
        return _response.data

    async def readarr_authors_browse_api(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.readarr_authors_browse_api(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.readarr_authors_browse_api(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def api_sonarr_series(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_sonarr_series(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_sonarr_series(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def api_sonarr_series_thumbnail(
        self,
        category: str,
        id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        category : str

        id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Cached series poster image bytes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_sonarr_series_thumbnail(
                category="category",
                id=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.api_sonarr_series_thumbnail(
            category, id, token=token, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def api_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_status(request_options=request_options)
        return _response.data

    async def api_torrents_distribution(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_torrents_distribution()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_torrents_distribution(request_options=request_options)
        return _response.data

    async def api_update(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.api_update()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_update(request_options=request_options)
        return _response.data

    async def web_arr_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_arr_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_arr_list(request_options=request_options)
        return _response.data

    async def web_arr_rebuild(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_arr_rebuild()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_arr_rebuild(request_options=request_options)
        return _response.data

    async def web_arr_test_connection(
        self,
        *,
        api_key: typing.Optional[str] = OMIT,
        arr_type: typing.Optional[str] = OMIT,
        instance_key: typing.Optional[str] = OMIT,
        uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        api_key : typing.Optional[str]

        arr_type : typing.Optional[str]

        instance_key : typing.Optional[str]

        uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_arr_test_connection()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_arr_test_connection(
            api_key=api_key, arr_type=arr_type, instance_key=instance_key, uri=uri, request_options=request_options
        )
        return _response.data

    async def redirect_to_arr_ui_for_movie_series_artist_author_web(
        self, category: str, kind: str, entry_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        category : str

        kind : str

        entry_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.redirect_to_arr_ui_for_movie_series_artist_author_web(
                category="category",
                kind="kind",
                entry_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.redirect_to_arr_ui_for_movie_series_artist_author_web(
            category, kind, entry_id, request_options=request_options
        )
        return _response.data

    async def web_arr_open_item(
        self,
        category: str,
        kind: WebArrOpenItemRequestKind,
        entry_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        category : str

        kind : WebArrOpenItemRequestKind

        entry_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.web_ui import WebArrOpenItemRequestKind

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_arr_open_item(
                category="category",
                kind=WebArrOpenItemRequestKind.MOVIE,
                entry_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_arr_open_item(category, kind, entry_id, request_options=request_options)
        return _response.data

    async def web_arr_restart(
        self, section: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        section : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_arr_restart(
                section="section",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_arr_restart(section, request_options=request_options)
        return _response.data

    async def web_config_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_config_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_config_get(request_options=request_options)
        return _response.data

    async def web_config_post(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigUpdateResponse:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigUpdateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_config_post(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_config_post(request=request, request_options=request_options)
        return _response.data

    async def web_config_schema_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Structured field registry (labels, kinds, reload hints)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_config_schema_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_config_schema_get(request_options=request_options)
        return _response.data

    async def web_download_update(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_download_update()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_download_update(request_options=request_options)
        return _response.data

    async def web_lidarr_albums(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_lidarr_albums(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_lidarr_albums(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def web_lidarr_artist_detail(
        self, category: str, artist_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        artist_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_lidarr_artist_detail(
                category="category",
                artist_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_lidarr_artist_detail(
            category, artist_id, request_options=request_options
        )
        return _response.data

    async def web_lidarr_artist_thumbnail(
        self,
        category: str,
        artist_id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        category : str

        artist_id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Cached artist image bytes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_lidarr_artist_thumbnail(
                category="category",
                artist_id=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.web_lidarr_artist_thumbnail(
            category, artist_id, token=token, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def web_lidarr_artists(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        monitored: typing.Optional[str] = None,
        missing: typing.Optional[bool] = None,
        reason: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        monitored : typing.Optional[str]

        missing : typing.Optional[bool]
            Restrict to artists with at least one monitored album whose file is missing.

        reason : typing.Optional[str]
            Restrict to artists with at least one album whose Reason matches. Accepts Missing, Quality, CustomFormat, Upgrade, or 'Not being searched' (also matches NULL).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_lidarr_artists(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_lidarr_artists(
            category,
            q=q,
            page=page,
            page_size=page_size,
            monitored=monitored,
            missing=missing,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    async def lidarr_tracks_browse_web(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.lidarr_tracks_browse_web(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lidarr_tracks_browse_web(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def web_loglevel(
        self, *, level: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        level : typing.Optional[str]
            CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG, TRACE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_loglevel()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_loglevel(level=level, request_options=request_options)
        return _response.data

    async def web_logs_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_logs_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_logs_list(request_options=request_options)
        return _response.data

    async def web_log_content(
        self,
        name: str,
        *,
        lines: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        since_bytes: typing.Optional[int] = None,
        inode: typing.Optional[int] = None,
        around_line: typing.Optional[int] = None,
        format: typing.Optional[WebLogContentRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogTailPayload:
        """
        Parameters
        ----------
        name : str

        lines : typing.Optional[int]

        offset : typing.Optional[int]

        since_bytes : typing.Optional[int]
            Byte cursor for incremental delta

        inode : typing.Optional[int]
            Inode from prior response to detect rotation

        around_line : typing.Optional[int]
            Return a window around this 1-based line

        format : typing.Optional[WebLogContentRequestFormat]
            Request JSON LogTailPayload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogTailPayload
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_log_content(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_log_content(
            name,
            lines=lines,
            offset=offset,
            since_bytes=since_bytes,
            inode=inode,
            around_line=around_line,
            format=format,
            request_options=request_options,
        )
        return _response.data

    async def web_log_download(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            File download

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_log_download(
                name="name",
            )


        asyncio.run(main())
        """
        async with self._raw_client.web_log_download(name, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def web_log_search(
        self,
        name: str,
        *,
        q: str,
        case: typing.Optional[WebLogSearchRequestCase] = None,
        regex: typing.Optional[WebLogSearchRequestRegex] = None,
        max_matches: typing.Optional[int] = None,
        context: typing.Optional[int] = None,
        include_rotated: typing.Optional[WebLogSearchRequestIncludeRotated] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogSearchResponse:
        """
        Parameters
        ----------
        name : str

        q : str

        case : typing.Optional[WebLogSearchRequestCase]

        regex : typing.Optional[WebLogSearchRequestRegex]

        max_matches : typing.Optional[int]

        context : typing.Optional[int]

        include_rotated : typing.Optional[WebLogSearchRequestIncludeRotated]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_log_search(
                name="name",
                q="q",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_log_search(
            name,
            q=q,
            case=case,
            regex=regex,
            max_matches=max_matches,
            context=context,
            include_rotated=include_rotated,
            request_options=request_options,
        )
        return _response.data

    async def web_log_stream(
        self,
        name: str,
        *,
        since_bytes: typing.Optional[int] = None,
        inode: typing.Optional[int] = None,
        lines: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        Server-Sent Events live tail. Prefer /web/* with session cookie for EventSource (cannot set Authorization).

        Parameters
        ----------
        name : str

        since_bytes : typing.Optional[int]

        inode : typing.Optional[int]

        lines : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            SSE stream (append/rotated/ping/reconnect events)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.web_ui.web_log_stream(
                name="name",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.web_log_stream(
            name, since_bytes=since_bytes, inode=inode, lines=lines, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def web_processes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_processes()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_processes(request_options=request_options)
        return _response.data

    async def web_processes_restart_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_processes_restart_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_processes_restart_all(request_options=request_options)
        return _response.data

    async def web_process_restart(
        self, category: str, kind: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        kind : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_process_restart(
                category="category",
                kind="kind",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_process_restart(category, kind, request_options=request_options)
        return _response.data

    async def web_qbit_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_qbit_categories()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_qbit_categories(request_options=request_options)
        return _response.data

    async def web_qbit_overview(
        self, *, instance: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        instance : typing.Optional[str]
            qBittorrent instance name, or omit/`all` for every instance

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_qbit_overview()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_qbit_overview(instance=instance, request_options=request_options)
        return _response.data

    async def web_radarr_movie_thumbnail(
        self,
        category: str,
        id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        category : str

        id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Cached movie poster image bytes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_radarr_movie_thumbnail(
                category="category",
                id=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.web_radarr_movie_thumbnail(
            category, id, token=token, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def web_radarr_movies(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        year_min: typing.Optional[int] = None,
        year_max: typing.Optional[int] = None,
        monitored: typing.Optional[bool] = None,
        has_file: typing.Optional[bool] = None,
        quality_met: typing.Optional[bool] = None,
        is_request: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        year_min : typing.Optional[int]

        year_max : typing.Optional[int]

        monitored : typing.Optional[bool]

        has_file : typing.Optional[bool]

        quality_met : typing.Optional[bool]

        is_request : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_radarr_movies(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_radarr_movies(
            category,
            q=q,
            page=page,
            page_size=page_size,
            year_min=year_min,
            year_max=year_max,
            monitored=monitored,
            has_file=has_file,
            quality_met=quality_met,
            is_request=is_request,
            request_options=request_options,
        )
        return _response.data

    async def readarr_author_detail_with_books_web(
        self, category: str, author_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        author_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.readarr_author_detail_with_books_web(
                category="category",
                author_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.readarr_author_detail_with_books_web(
            category, author_id, request_options=request_options
        )
        return _response.data

    async def readarr_author_thumbnail_web(
        self, category: str, author_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        category : str

        author_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.readarr_author_thumbnail_web(
                category="category",
                author_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.readarr_author_thumbnail_web(
            category, author_id, request_options=request_options
        )
        return _response.data

    async def readarr_authors_browse_web(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.readarr_authors_browse_web(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.readarr_authors_browse_web(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def web_sonarr_series(
        self,
        category: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        category : str

        q : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_sonarr_series(
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.web_sonarr_series(
            category, q=q, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def web_sonarr_series_thumbnail(
        self,
        category: str,
        id: int,
        *,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        category : str

        id : int

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Cached series poster image bytes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_sonarr_series_thumbnail(
                category="category",
                id=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.web_sonarr_series_thumbnail(
            category, id, token=token, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def web_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_status(request_options=request_options)
        return _response.data

    async def torrent_distribution_by_category_web(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.torrent_distribution_by_category_web()


        asyncio.run(main())
        """
        _response = await self._raw_client.torrent_distribution_by_category_web(request_options=request_options)
        return _response.data

    async def web_update(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_ui.web_update()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_update(request_options=request_options)
        return _response.data
