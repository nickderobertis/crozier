

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.casting_devices import CastingDevices
from ..types.casting_relay import CastingRelay
from ..types.cursor import Cursor
from ..types.drive_statistics import DriveStatistics
from ..types.e_tag import ETag
from ..types.file_bulk_result import FileBulkResult
from ..types.file_category import FileCategory
from ..types.file_category_statistics import FileCategoryStatistics
from ..types.file_entry import FileEntry
from ..types.file_kind import FileKind
from ..types.file_list_scope import FileListScope
from ..types.file_search_type import FileSearchType
from ..types.file_sort import FileSort
from ..types.file_status import FileStatus
from ..types.file_view_state import FileViewState
from ..types.media_tracks import MediaTracks
from ..types.name_conflict_policy import NameConflictPolicy
from ..types.playback_diagnostics import PlaybackDiagnostics
from ..types.playback_session import PlaybackSession
from ..types.sort_order import SortOrder
from ..types.uuid_ import Uuid
from ..types.viewer_kind import ViewerKind
from .raw_client import AsyncRawFilesClient, RawFilesClient
from .types.casting_start_mode import CastingStartMode
from .types.control_casting_device_request_command import ControlCastingDeviceRequestCommand
from .types.download_file_legacy_request_download import DownloadFileLegacyRequestDownload
from .types.download_file_request_download import DownloadFileRequestDownload
from .types.list_files_response import ListFilesResponse
from .types.stream_playback_request_download import StreamPlaybackRequestDownload
from .types.stream_playback_request_mode import StreamPlaybackRequestMode


OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesClient
        """
        return self._raw_client

    def create_playback(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaybackSession:
        """
        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaybackSession
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.create_playback(
            file_id="fileId",
        )
        """
        _response = self._raw_client.create_playback(file_id, request_options=request_options)
        return _response.data

    def stream_playback(
        self,
        *,
        ticket: str,
        mode: typing.Optional[StreamPlaybackRequestMode] = None,
        start: typing.Optional[float] = None,
        audio: typing.Optional[int] = None,
        video: typing.Optional[int] = None,
        subtitle: typing.Optional[int] = None,
        download: typing.Optional[StreamPlaybackRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        ticket : str

        mode : typing.Optional[StreamPlaybackRequestMode]

        start : typing.Optional[float]

        audio : typing.Optional[int]

        video : typing.Optional[int]

        subtitle : typing.Optional[int]

        download : typing.Optional[StreamPlaybackRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.stream_playback(
            ticket="blackcurrant....................",
        )
        """
        with self._raw_client.stream_playback(
            ticket=ticket,
            mode=mode,
            start=start,
            audio=audio,
            video=video,
            subtitle=subtitle,
            download=download,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            yield from r.data

    def get_playback_diagnostics(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaybackDiagnostics:
        """
        Owner-session-only, bounded in-memory statistics for one playback ticket. No Telegram credentials, internal addresses or ticket values are included. The edge merges authorized primary and secondary snapshots.

        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaybackDiagnostics
            Current server counters, recent streams and bot identities.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.get_playback_diagnostics(
            ticket="ticket",
        )
        """
        _response = self._raw_client.get_playback_diagnostics(ticket=ticket, request_options=request_options)
        return _response.data

    def get_playback_tracks(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MediaTracks:
        """
        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MediaTracks
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.get_playback_tracks(
            ticket="ticket",
        )
        """
        _response = self._raw_client.get_playback_tracks(ticket=ticket, request_options=request_options)
        return _response.data

    def get_playback_subtitles(
        self,
        *,
        ticket: str,
        track: int,
        start: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        ticket : str

        track : int

        start : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.get_playback_subtitles(
            ticket="blackcurrant....................",
            track=1024,
        )
        """
        with self._raw_client.get_playback_subtitles(
            ticket=ticket, track=track, start=start, request_options=request_options
        ) as r:
            yield from r.data

    def create_casting_relay(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CastingRelay:
        """
        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CastingRelay
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.create_casting_relay(
            ticket="ticket",
        )
        """
        _response = self._raw_client.create_casting_relay(ticket=ticket, request_options=request_options)
        return _response.data

    def list_casting_devices(self, *, request_options: typing.Optional[RequestOptions] = None) -> CastingDevices:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CastingDevices
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.list_casting_devices()
        """
        _response = self._raw_client.list_casting_devices(request_options=request_options)
        return _response.data

    def play_on_casting_device(
        self,
        device_id: str,
        *,
        ticket: str,
        server_url: str,
        mode: CastingStartMode,
        start: typing.Optional[float] = OMIT,
        audio: typing.Optional[int] = OMIT,
        subtitle: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        device_id : str

        ticket : str

        server_url : str

        mode : CastingStartMode

        start : typing.Optional[float]

        audio : typing.Optional[int]

        subtitle : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.files import CastingStartMode

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.play_on_casting_device(
            device_id="deviceId",
            ticket="ticket",
            server_url="serverUrl",
            mode=CastingStartMode.ORIGINAL,
        )
        """
        _response = self._raw_client.play_on_casting_device(
            device_id,
            ticket=ticket,
            server_url=server_url,
            mode=mode,
            start=start,
            audio=audio,
            subtitle=subtitle,
            request_options=request_options,
        )
        return _response.data

    def control_casting_device(
        self,
        device_id: str,
        *,
        command: ControlCastingDeviceRequestCommand,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        device_id : str

        command : ControlCastingDeviceRequestCommand

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.files import ControlCastingDeviceRequestCommand

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.control_casting_device(
            device_id="deviceId",
            command=ControlCastingDeviceRequestCommand.PLAY,
        )
        """
        _response = self._raw_client.control_casting_device(device_id, command=command, request_options=request_options)
        return _response.data

    def list_files(
        self,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        scope: typing.Optional[FileListScope] = None,
        parent_id: typing.Optional[Uuid] = None,
        path: typing.Optional[str] = None,
        kind: typing.Optional[FileKind] = None,
        status: typing.Optional[FileStatus] = None,
        search: typing.Optional[str] = None,
        search_type: typing.Optional[FileSearchType] = None,
        category: typing.Optional[typing.Union[FileCategory, typing.Sequence[FileCategory]]] = None,
        updated_after: typing.Optional[dt.datetime] = None,
        updated_before: typing.Optional[dt.datetime] = None,
        sort: typing.Optional[FileSort] = None,
        order: typing.Optional[SortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFilesResponse:
        """
        List one folder or search within the authenticated user's drive.

        Parameters
        ----------
        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        scope : typing.Optional[FileListScope]

        parent_id : typing.Optional[Uuid]

        path : typing.Optional[str]
            Resolve the listing root relative to the user's drive root.

        kind : typing.Optional[FileKind]

        status : typing.Optional[FileStatus]

        search : typing.Optional[str]
            File-name search. Text search is case-insensitive; regex uses PostgreSQL-compatible regular expressions.

        search_type : typing.Optional[FileSearchType]

        category : typing.Optional[typing.Union[FileCategory, typing.Sequence[FileCategory]]]

        updated_after : typing.Optional[dt.datetime]

        updated_before : typing.Optional[dt.datetime]

        sort : typing.Optional[FileSort]

        order : typing.Optional[SortOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFilesResponse
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.list_files()
        """
        _response = self._raw_client.list_files(
            cursor=cursor,
            limit=limit,
            scope=scope,
            parent_id=parent_id,
            path=path,
            kind=kind,
            status=status,
            search=search,
            search_type=search_type,
            category=category,
            updated_after=updated_after,
            updated_before=updated_before,
            sort=sort,
            order=order,
            request_options=request_options,
        )
        return _response.data

    def get_file(self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> FileEntry:
        """
        Return file or folder metadata.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileEntry
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.get_file(
            file_id="fileId",
        )
        """
        _response = self._raw_client.get_file(file_id, request_options=request_options)
        return _response.data

    def trash_file(self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Move a file or folder to trash.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.trash_file(
            file_id="fileId",
        )
        """
        _response = self._raw_client.trash_file(file_id, request_options=request_options)
        return _response.data

    def update_file(
        self,
        file_id: Uuid,
        *,
        if_match: typing.Optional[ETag] = None,
        name: typing.Optional[str] = OMIT,
        mod_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Rename a file/folder or update its modification time.

        Parameters
        ----------
        file_id : Uuid

        if_match : typing.Optional[ETag]

        name : typing.Optional[str]

        mod_time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileEntry
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.update_file(
            file_id="fileId",
        )
        """
        _response = self._raw_client.update_file(
            file_id, if_match=if_match, name=name, mod_time=mod_time, request_options=request_options
        )
        return _response.data

    def move_file(
        self,
        file_id: Uuid,
        *,
        idempotency_key: Uuid,
        if_match: typing.Optional[ETag] = None,
        parent_id: typing.Optional[Uuid] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Move a file or folder using metadata only.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        if_match : typing.Optional[ETag]

        parent_id : typing.Optional[Uuid]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileEntry
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.move_file(
            file_id="fileId",
            idempotency_key="Idempotency-Key",
        )
        """
        _response = self._raw_client.move_file(
            file_id,
            idempotency_key=idempotency_key,
            if_match=if_match,
            parent_id=parent_id,
            conflict_policy=conflict_policy,
            request_options=request_options,
        )
        return _response.data

    def copy_file(
        self,
        file_id: Uuid,
        *,
        idempotency_key: Uuid,
        parent_id: typing.Optional[Uuid] = OMIT,
        name: typing.Optional[str] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Copy a file or folder to another destination.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        parent_id : typing.Optional[Uuid]

        name : typing.Optional[str]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileEntry
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.copy_file(
            file_id="fileId",
            idempotency_key="Idempotency-Key",
        )
        """
        _response = self._raw_client.copy_file(
            file_id,
            idempotency_key=idempotency_key,
            parent_id=parent_id,
            name=name,
            conflict_policy=conflict_policy,
            request_options=request_options,
        )
        return _response.data

    def restore_file(
        self, file_id: Uuid, *, idempotency_key: Uuid, request_options: typing.Optional[RequestOptions] = None
    ) -> FileEntry:
        """
        Restore a trashed file or folder.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileEntry
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.restore_file(
            file_id="fileId",
            idempotency_key="Idempotency-Key",
        )
        """
        _response = self._raw_client.restore_file(
            file_id, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def purge_file(self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently delete a trashed file or folder from the catalog.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.purge_file(
            file_id="fileId",
        )
        """
        _response = self._raw_client.purge_file(file_id, request_options=request_options)
        return _response.data

    def clean_trash(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Move every trashed file and folder owned by the authenticated user to deletion pending.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.clean_trash()
        """
        _response = self._raw_client.clean_trash(request_options=request_options)
        return _response.data

    def download_file(
        self,
        file_id: Uuid,
        file_name: str,
        *,
        download: typing.Optional[DownloadFileRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Stream complete or partial file content. The filename path segment gives command-line clients a useful output name.

        Parameters
        ----------
        file_id : Uuid

        file_name : str

        download : typing.Optional[DownloadFileRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.download_file(
            file_id="fileId",
            file_name="fileName",
        )
        """
        with self._raw_client.download_file(
            file_id,
            file_name,
            download=download,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            yield from r.data

    def head_file(
        self, file_id: Uuid, file_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return content metadata without streaming the file.

        Parameters
        ----------
        file_id : Uuid

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.head_file(
            file_id="fileId",
            file_name="fileName",
        )
        """
        _response = self._raw_client.head_file(file_id, file_name, request_options=request_options)
        return _response.headers

    def download_file_legacy(
        self,
        file_id: Uuid,
        *,
        download: typing.Optional[DownloadFileLegacyRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Stream file content using the legacy URL without a filename segment.

        Parameters
        ----------
        file_id : Uuid

        download : typing.Optional[DownloadFileLegacyRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.download_file_legacy(
            file_id="fileId",
        )
        """
        with self._raw_client.download_file_legacy(
            file_id, download=download, range=range, if_none_match=if_none_match, request_options=request_options
        ) as r:
            yield from r.data

    def head_file_legacy(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return file metadata using the legacy URL without a filename segment.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.head_file_legacy(
            file_id="fileId",
        )
        """
        _response = self._raw_client.head_file_legacy(file_id, request_options=request_options)
        return _response.headers

    def get_file_view_state(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[FileViewState]:
        """
        Return the authenticated user's synchronized viewer state for a file.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FileViewState]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.get_file_view_state(
            file_id="fileId",
        )
        """
        _response = self._raw_client.get_file_view_state(file_id, request_options=request_options)
        return _response.data

    def put_file_view_state(
        self,
        file_id: Uuid,
        *,
        kind: ViewerKind,
        position: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        preferences: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        bookmarks: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileViewState:
        """
        Create or replace the authenticated user's synchronized viewer state.

        Parameters
        ----------
        file_id : Uuid

        kind : ViewerKind

        position : typing.Optional[typing.Dict[str, typing.Any]]

        preferences : typing.Optional[typing.Dict[str, typing.Any]]

        bookmarks : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileViewState
            The request has succeeded.

        Examples
        --------
        from fern import FernApi, ViewerKind

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.put_file_view_state(
            file_id="fileId",
            kind=ViewerKind.IMAGE,
        )
        """
        _response = self._raw_client.put_file_view_state(
            file_id,
            kind=kind,
            position=position,
            preferences=preferences,
            bookmarks=bookmarks,
            request_options=request_options,
        )
        return _response.data

    def delete_file_view_state(self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Clear the authenticated user's synchronized viewer state.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.delete_file_view_state(
            file_id="fileId",
        )
        """
        _response = self._raw_client.delete_file_view_state(file_id, request_options=request_options)
        return _response.data

    def bulk_move_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        parent_id: typing.Optional[Uuid] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileBulkResult:
        """
        Transactionally move multiple files or folders.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        parent_id : typing.Optional[Uuid]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileBulkResult
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.bulk_move_files(
            idempotency_key="Idempotency-Key",
            file_ids=["fileIds"],
        )
        """
        _response = self._raw_client.bulk_move_files(
            idempotency_key=idempotency_key,
            file_ids=file_ids,
            parent_id=parent_id,
            conflict_policy=conflict_policy,
            request_options=request_options,
        )
        return _response.data

    def bulk_spam_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileBulkResult:
        """
        Quarantine owned files and folders and revoke their sharing.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileBulkResult
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.bulk_spam_files(
            idempotency_key="Idempotency-Key",
            file_ids=["fileIds"],
        )
        """
        _response = self._raw_client.bulk_spam_files(
            idempotency_key=idempotency_key, file_ids=file_ids, request_options=request_options
        )
        return _response.data

    def bulk_trash_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileBulkResult:
        """
        Transactionally move multiple files or folders to trash.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileBulkResult
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.bulk_trash_files(
            idempotency_key="Idempotency-Key",
            file_ids=["fileIds"],
        )
        """
        _response = self._raw_client.bulk_trash_files(
            idempotency_key=idempotency_key, file_ids=file_ids, request_options=request_options
        )
        return _response.data

    def get_file_category_statistics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FileCategoryStatistics]:
        """
        Aggregate active file counts and bytes by category.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileCategoryStatistics]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.get_file_category_statistics()
        """
        _response = self._raw_client.get_file_category_statistics(request_options=request_options)
        return _response.data

    def get_drive_statistics(self, *, request_options: typing.Optional[RequestOptions] = None) -> DriveStatistics:
        """
        Aggregate drive-level counters for the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DriveStatistics
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.files.get_drive_statistics()
        """
        _response = self._raw_client.get_drive_statistics(request_options=request_options)
        return _response.data


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesClient
        """
        return self._raw_client

    async def create_playback(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaybackSession:
        """
        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaybackSession
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.create_playback(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_playback(file_id, request_options=request_options)
        return _response.data

    async def stream_playback(
        self,
        *,
        ticket: str,
        mode: typing.Optional[StreamPlaybackRequestMode] = None,
        start: typing.Optional[float] = None,
        audio: typing.Optional[int] = None,
        video: typing.Optional[int] = None,
        subtitle: typing.Optional[int] = None,
        download: typing.Optional[StreamPlaybackRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        ticket : str

        mode : typing.Optional[StreamPlaybackRequestMode]

        start : typing.Optional[float]

        audio : typing.Optional[int]

        video : typing.Optional[int]

        subtitle : typing.Optional[int]

        download : typing.Optional[StreamPlaybackRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.stream_playback(
                ticket="blackcurrant....................",
            )


        asyncio.run(main())
        """
        async with self._raw_client.stream_playback(
            ticket=ticket,
            mode=mode,
            start=start,
            audio=audio,
            video=video,
            subtitle=subtitle,
            download=download,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_playback_diagnostics(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaybackDiagnostics:
        """
        Owner-session-only, bounded in-memory statistics for one playback ticket. No Telegram credentials, internal addresses or ticket values are included. The edge merges authorized primary and secondary snapshots.

        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaybackDiagnostics
            Current server counters, recent streams and bot identities.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.get_playback_diagnostics(
                ticket="ticket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_playback_diagnostics(ticket=ticket, request_options=request_options)
        return _response.data

    async def get_playback_tracks(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MediaTracks:
        """
        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MediaTracks
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.get_playback_tracks(
                ticket="ticket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_playback_tracks(ticket=ticket, request_options=request_options)
        return _response.data

    async def get_playback_subtitles(
        self,
        *,
        ticket: str,
        track: int,
        start: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        ticket : str

        track : int

        start : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.get_playback_subtitles(
                ticket="blackcurrant....................",
                track=1024,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_playback_subtitles(
            ticket=ticket, track=track, start=start, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def create_casting_relay(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CastingRelay:
        """
        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CastingRelay
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.create_casting_relay(
                ticket="ticket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_casting_relay(ticket=ticket, request_options=request_options)
        return _response.data

    async def list_casting_devices(self, *, request_options: typing.Optional[RequestOptions] = None) -> CastingDevices:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CastingDevices
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.list_casting_devices()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_casting_devices(request_options=request_options)
        return _response.data

    async def play_on_casting_device(
        self,
        device_id: str,
        *,
        ticket: str,
        server_url: str,
        mode: CastingStartMode,
        start: typing.Optional[float] = OMIT,
        audio: typing.Optional[int] = OMIT,
        subtitle: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        device_id : str

        ticket : str

        server_url : str

        mode : CastingStartMode

        start : typing.Optional[float]

        audio : typing.Optional[int]

        subtitle : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.files import CastingStartMode

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.play_on_casting_device(
                device_id="deviceId",
                ticket="ticket",
                server_url="serverUrl",
                mode=CastingStartMode.ORIGINAL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.play_on_casting_device(
            device_id,
            ticket=ticket,
            server_url=server_url,
            mode=mode,
            start=start,
            audio=audio,
            subtitle=subtitle,
            request_options=request_options,
        )
        return _response.data

    async def control_casting_device(
        self,
        device_id: str,
        *,
        command: ControlCastingDeviceRequestCommand,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        device_id : str

        command : ControlCastingDeviceRequestCommand

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.files import ControlCastingDeviceRequestCommand

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.control_casting_device(
                device_id="deviceId",
                command=ControlCastingDeviceRequestCommand.PLAY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.control_casting_device(
            device_id, command=command, request_options=request_options
        )
        return _response.data

    async def list_files(
        self,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        scope: typing.Optional[FileListScope] = None,
        parent_id: typing.Optional[Uuid] = None,
        path: typing.Optional[str] = None,
        kind: typing.Optional[FileKind] = None,
        status: typing.Optional[FileStatus] = None,
        search: typing.Optional[str] = None,
        search_type: typing.Optional[FileSearchType] = None,
        category: typing.Optional[typing.Union[FileCategory, typing.Sequence[FileCategory]]] = None,
        updated_after: typing.Optional[dt.datetime] = None,
        updated_before: typing.Optional[dt.datetime] = None,
        sort: typing.Optional[FileSort] = None,
        order: typing.Optional[SortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFilesResponse:
        """
        List one folder or search within the authenticated user's drive.

        Parameters
        ----------
        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        scope : typing.Optional[FileListScope]

        parent_id : typing.Optional[Uuid]

        path : typing.Optional[str]
            Resolve the listing root relative to the user's drive root.

        kind : typing.Optional[FileKind]

        status : typing.Optional[FileStatus]

        search : typing.Optional[str]
            File-name search. Text search is case-insensitive; regex uses PostgreSQL-compatible regular expressions.

        search_type : typing.Optional[FileSearchType]

        category : typing.Optional[typing.Union[FileCategory, typing.Sequence[FileCategory]]]

        updated_after : typing.Optional[dt.datetime]

        updated_before : typing.Optional[dt.datetime]

        sort : typing.Optional[FileSort]

        order : typing.Optional[SortOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFilesResponse
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.list_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_files(
            cursor=cursor,
            limit=limit,
            scope=scope,
            parent_id=parent_id,
            path=path,
            kind=kind,
            status=status,
            search=search,
            search_type=search_type,
            category=category,
            updated_after=updated_after,
            updated_before=updated_before,
            sort=sort,
            order=order,
            request_options=request_options,
        )
        return _response.data

    async def get_file(self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> FileEntry:
        """
        Return file or folder metadata.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileEntry
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.get_file(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file(file_id, request_options=request_options)
        return _response.data

    async def trash_file(self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Move a file or folder to trash.

        Parameters
        ----------
        file_id : Uuid

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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.trash_file(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trash_file(file_id, request_options=request_options)
        return _response.data

    async def update_file(
        self,
        file_id: Uuid,
        *,
        if_match: typing.Optional[ETag] = None,
        name: typing.Optional[str] = OMIT,
        mod_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Rename a file/folder or update its modification time.

        Parameters
        ----------
        file_id : Uuid

        if_match : typing.Optional[ETag]

        name : typing.Optional[str]

        mod_time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileEntry
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.update_file(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file(
            file_id, if_match=if_match, name=name, mod_time=mod_time, request_options=request_options
        )
        return _response.data

    async def move_file(
        self,
        file_id: Uuid,
        *,
        idempotency_key: Uuid,
        if_match: typing.Optional[ETag] = None,
        parent_id: typing.Optional[Uuid] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Move a file or folder using metadata only.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        if_match : typing.Optional[ETag]

        parent_id : typing.Optional[Uuid]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileEntry
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.move_file(
                file_id="fileId",
                idempotency_key="Idempotency-Key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.move_file(
            file_id,
            idempotency_key=idempotency_key,
            if_match=if_match,
            parent_id=parent_id,
            conflict_policy=conflict_policy,
            request_options=request_options,
        )
        return _response.data

    async def copy_file(
        self,
        file_id: Uuid,
        *,
        idempotency_key: Uuid,
        parent_id: typing.Optional[Uuid] = OMIT,
        name: typing.Optional[str] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Copy a file or folder to another destination.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        parent_id : typing.Optional[Uuid]

        name : typing.Optional[str]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileEntry
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.copy_file(
                file_id="fileId",
                idempotency_key="Idempotency-Key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.copy_file(
            file_id,
            idempotency_key=idempotency_key,
            parent_id=parent_id,
            name=name,
            conflict_policy=conflict_policy,
            request_options=request_options,
        )
        return _response.data

    async def restore_file(
        self, file_id: Uuid, *, idempotency_key: Uuid, request_options: typing.Optional[RequestOptions] = None
    ) -> FileEntry:
        """
        Restore a trashed file or folder.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileEntry
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.restore_file(
                file_id="fileId",
                idempotency_key="Idempotency-Key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file(
            file_id, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def purge_file(self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently delete a trashed file or folder from the catalog.

        Parameters
        ----------
        file_id : Uuid

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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.purge_file(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.purge_file(file_id, request_options=request_options)
        return _response.data

    async def clean_trash(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Move every trashed file and folder owned by the authenticated user to deletion pending.

        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.clean_trash()


        asyncio.run(main())
        """
        _response = await self._raw_client.clean_trash(request_options=request_options)
        return _response.data

    async def download_file(
        self,
        file_id: Uuid,
        file_name: str,
        *,
        download: typing.Optional[DownloadFileRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Stream complete or partial file content. The filename path segment gives command-line clients a useful output name.

        Parameters
        ----------
        file_id : Uuid

        file_name : str

        download : typing.Optional[DownloadFileRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.download_file(
                file_id="fileId",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_file(
            file_id,
            file_name,
            download=download,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def head_file(
        self, file_id: Uuid, file_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return content metadata without streaming the file.

        Parameters
        ----------
        file_id : Uuid

        file_name : str

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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.head_file(
                file_id="fileId",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_file(file_id, file_name, request_options=request_options)
        return _response.headers

    async def download_file_legacy(
        self,
        file_id: Uuid,
        *,
        download: typing.Optional[DownloadFileLegacyRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Stream file content using the legacy URL without a filename segment.

        Parameters
        ----------
        file_id : Uuid

        download : typing.Optional[DownloadFileLegacyRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.download_file_legacy(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_file_legacy(
            file_id, download=download, range=range, if_none_match=if_none_match, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def head_file_legacy(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return file metadata using the legacy URL without a filename segment.

        Parameters
        ----------
        file_id : Uuid

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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.head_file_legacy(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_file_legacy(file_id, request_options=request_options)
        return _response.headers

    async def get_file_view_state(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[FileViewState]:
        """
        Return the authenticated user's synchronized viewer state for a file.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FileViewState]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.get_file_view_state(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_view_state(file_id, request_options=request_options)
        return _response.data

    async def put_file_view_state(
        self,
        file_id: Uuid,
        *,
        kind: ViewerKind,
        position: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        preferences: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        bookmarks: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileViewState:
        """
        Create or replace the authenticated user's synchronized viewer state.

        Parameters
        ----------
        file_id : Uuid

        kind : ViewerKind

        position : typing.Optional[typing.Dict[str, typing.Any]]

        preferences : typing.Optional[typing.Dict[str, typing.Any]]

        bookmarks : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileViewState
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ViewerKind

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.put_file_view_state(
                file_id="fileId",
                kind=ViewerKind.IMAGE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_file_view_state(
            file_id,
            kind=kind,
            position=position,
            preferences=preferences,
            bookmarks=bookmarks,
            request_options=request_options,
        )
        return _response.data

    async def delete_file_view_state(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Clear the authenticated user's synchronized viewer state.

        Parameters
        ----------
        file_id : Uuid

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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.delete_file_view_state(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_view_state(file_id, request_options=request_options)
        return _response.data

    async def bulk_move_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        parent_id: typing.Optional[Uuid] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileBulkResult:
        """
        Transactionally move multiple files or folders.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        parent_id : typing.Optional[Uuid]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileBulkResult
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.bulk_move_files(
                idempotency_key="Idempotency-Key",
                file_ids=["fileIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_move_files(
            idempotency_key=idempotency_key,
            file_ids=file_ids,
            parent_id=parent_id,
            conflict_policy=conflict_policy,
            request_options=request_options,
        )
        return _response.data

    async def bulk_spam_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileBulkResult:
        """
        Quarantine owned files and folders and revoke their sharing.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileBulkResult
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.bulk_spam_files(
                idempotency_key="Idempotency-Key",
                file_ids=["fileIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_spam_files(
            idempotency_key=idempotency_key, file_ids=file_ids, request_options=request_options
        )
        return _response.data

    async def bulk_trash_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileBulkResult:
        """
        Transactionally move multiple files or folders to trash.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileBulkResult
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.bulk_trash_files(
                idempotency_key="Idempotency-Key",
                file_ids=["fileIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_trash_files(
            idempotency_key=idempotency_key, file_ids=file_ids, request_options=request_options
        )
        return _response.data

    async def get_file_category_statistics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FileCategoryStatistics]:
        """
        Aggregate active file counts and bytes by category.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileCategoryStatistics]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.get_file_category_statistics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_category_statistics(request_options=request_options)
        return _response.data

    async def get_drive_statistics(self, *, request_options: typing.Optional[RequestOptions] = None) -> DriveStatistics:
        """
        Aggregate drive-level counters for the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DriveStatistics
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.get_drive_statistics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_drive_statistics(request_options=request_options)
        return _response.data
