

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cursor import Cursor
from ..types.e_tag import ETag
from ..types.file_entry import FileEntry
from ..types.file_hash import FileHash
from ..types.name_conflict_policy import NameConflictPolicy
from ..types.playback_session import PlaybackSession
from ..types.public_share import PublicShare
from ..types.upload_part import UploadPart
from ..types.upload_session import UploadSession
from ..types.uuid_ import Uuid
from .raw_client import AsyncRawPublicSharesClient, RawPublicSharesClient
from .types.download_public_share_file_legacy_request_download import DownloadPublicShareFileLegacyRequestDownload
from .types.download_public_share_file_request_download import DownloadPublicShareFileRequestDownload
from .types.download_public_share_legacy_request_download import DownloadPublicShareLegacyRequestDownload
from .types.download_public_share_request_download import DownloadPublicShareRequestDownload
from .types.list_public_share_files_response import ListPublicShareFilesResponse


OMIT = typing.cast(typing.Any, ...)


class PublicSharesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPublicSharesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPublicSharesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPublicSharesClient
        """
        return self._raw_client

    def create_public_playback(
        self,
        token: str,
        file_id: Uuid,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlaybackSession:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        share_password : typing.Optional[str]

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
        client.public_shares.create_public_playback(
            token="token",
            file_id="fileId",
        )
        """
        _response = self._raw_client.create_public_playback(
            token, file_id, share_password=share_password, request_options=request_options
        )
        return _response.data

    def get_public_share(
        self,
        token: str,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublicShare:
        """
        Parameters
        ----------
        token : str

        share_password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicShare
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.public_shares.get_public_share(
            token="token",
        )
        """
        _response = self._raw_client.get_public_share(
            token, share_password=share_password, request_options=request_options
        )
        return _response.data

    def list_public_share_files(
        self,
        token: str,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        path: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPublicShareFilesResponse:
        """
        List children within a publicly shared folder.

        Parameters
        ----------
        token : str

        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        path : typing.Optional[str]
            Folder path relative to the shared folder root.

        search : typing.Optional[str]

        share_password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPublicShareFilesResponse
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.public_shares.list_public_share_files(
            token="token",
        )
        """
        _response = self._raw_client.list_public_share_files(
            token,
            cursor=cursor,
            limit=limit,
            path=path,
            search=search,
            share_password=share_password,
            request_options=request_options,
        )
        return _response.data

    def download_public_share_file(
        self,
        token: str,
        file_id: Uuid,
        file_name: str,
        *,
        download: typing.Optional[DownloadPublicShareFileRequestDownload] = None,
        share_password: typing.Optional[str] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        file_name : str

        download : typing.Optional[DownloadPublicShareFileRequestDownload]
            Force a browser download instead of inline display.

        share_password : typing.Optional[str]

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
        client.public_shares.download_public_share_file(
            token="token",
            file_id="fileId",
            file_name="fileName",
        )
        """
        with self._raw_client.download_public_share_file(
            token,
            file_id,
            file_name,
            download=download,
            share_password=share_password,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            yield from r.data

    def head_public_share_file(
        self,
        token: str,
        file_id: Uuid,
        file_name: str,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        file_name : str

        share_password : typing.Optional[str]

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
        client.public_shares.head_public_share_file(
            token="token",
            file_id="fileId",
            file_name="fileName",
        )
        """
        _response = self._raw_client.head_public_share_file(
            token, file_id, file_name, share_password=share_password, request_options=request_options
        )
        return _response.headers

    def download_public_share(
        self,
        token: str,
        file_name: str,
        *,
        download: typing.Optional[DownloadPublicShareRequestDownload] = None,
        share_password: typing.Optional[str] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        token : str

        file_name : str

        download : typing.Optional[DownloadPublicShareRequestDownload]
            Force a browser download instead of inline display.

        share_password : typing.Optional[str]

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
        client.public_shares.download_public_share(
            token="token",
            file_name="fileName",
        )
        """
        with self._raw_client.download_public_share(
            token,
            file_name,
            download=download,
            share_password=share_password,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            yield from r.data

    def head_public_share(
        self,
        token: str,
        file_name: str,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        token : str

        file_name : str

        share_password : typing.Optional[str]

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
        client.public_shares.head_public_share(
            token="token",
            file_name="fileName",
        )
        """
        _response = self._raw_client.head_public_share(
            token, file_name, share_password=share_password, request_options=request_options
        )
        return _response.headers

    def download_public_share_file_legacy(
        self,
        token: str,
        file_id: Uuid,
        *,
        download: typing.Optional[DownloadPublicShareFileLegacyRequestDownload] = None,
        share_password: typing.Optional[str] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        download : typing.Optional[DownloadPublicShareFileLegacyRequestDownload]
            Force a browser download instead of inline display.

        share_password : typing.Optional[str]

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
        client.public_shares.download_public_share_file_legacy(
            token="token",
            file_id="fileId",
        )
        """
        with self._raw_client.download_public_share_file_legacy(
            token,
            file_id,
            download=download,
            share_password=share_password,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            yield from r.data

    def head_public_share_file_legacy(
        self,
        token: str,
        file_id: Uuid,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        share_password : typing.Optional[str]

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
        client.public_shares.head_public_share_file_legacy(
            token="token",
            file_id="fileId",
        )
        """
        _response = self._raw_client.head_public_share_file_legacy(
            token, file_id, share_password=share_password, request_options=request_options
        )
        return _response.headers

    def download_public_share_legacy(
        self,
        token: str,
        *,
        download: typing.Optional[DownloadPublicShareLegacyRequestDownload] = None,
        share_password: typing.Optional[str] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        token : str

        download : typing.Optional[DownloadPublicShareLegacyRequestDownload]
            Force a browser download instead of inline display.

        share_password : typing.Optional[str]

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
        client.public_shares.download_public_share_legacy(
            token="token",
        )
        """
        with self._raw_client.download_public_share_legacy(
            token,
            download=download,
            share_password=share_password,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            yield from r.data

    def head_public_share_legacy(
        self,
        token: str,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        token : str

        share_password : typing.Optional[str]

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
        client.public_shares.head_public_share_legacy(
            token="token",
        )
        """
        _response = self._raw_client.head_public_share_legacy(
            token, share_password=share_password, request_options=request_options
        )
        return _response.headers

    def create_public_share_folder(
        self,
        token: str,
        *,
        name: str,
        share_password: typing.Optional[str] = None,
        parent_id: typing.Optional[Uuid] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        mod_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Parameters
        ----------
        token : str

        name : str

        share_password : typing.Optional[str]

        parent_id : typing.Optional[Uuid]

        conflict_policy : typing.Optional[NameConflictPolicy]

        mod_time : typing.Optional[dt.datetime]

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
        client.public_shares.create_public_share_folder(
            token="token",
            name="name",
        )
        """
        _response = self._raw_client.create_public_share_folder(
            token,
            name=name,
            share_password=share_password,
            parent_id=parent_id,
            conflict_policy=conflict_policy,
            mod_time=mod_time,
            request_options=request_options,
        )
        return _response.data

    def trash_public_share_file(
        self,
        token: str,
        file_id: Uuid,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        share_password : typing.Optional[str]

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
        client.public_shares.trash_public_share_file(
            token="token",
            file_id="fileId",
        )
        """
        _response = self._raw_client.trash_public_share_file(
            token, file_id, share_password=share_password, request_options=request_options
        )
        return _response.data

    def update_public_share_file(
        self,
        token: str,
        file_id: Uuid,
        *,
        if_match: ETag,
        share_password: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        mod_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        if_match : ETag

        share_password : typing.Optional[str]

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
        client.public_shares.update_public_share_file(
            token="token",
            file_id="fileId",
            if_match="If-Match",
        )
        """
        _response = self._raw_client.update_public_share_file(
            token,
            file_id,
            if_match=if_match,
            share_password=share_password,
            name=name,
            mod_time=mod_time,
            request_options=request_options,
        )
        return _response.data

    def create_public_share_upload(
        self,
        token: str,
        *,
        idempotency_key: Uuid,
        name: str,
        size: int,
        mod_time: dt.datetime,
        share_password: typing.Optional[str] = None,
        parent_id: typing.Optional[Uuid] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        hash: typing.Optional[FileHash] = OMIT,
        encryption: typing.Optional[bool] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        preferred_part_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadSession:
        """
        Parameters
        ----------
        token : str

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        name : str

        size : int
            Expected size in bytes, or -1 when the size is unknown until completion.

        mod_time : dt.datetime

        share_password : typing.Optional[str]

        parent_id : typing.Optional[Uuid]

        mime_type : typing.Optional[str]

        hash : typing.Optional[FileHash]

        encryption : typing.Optional[bool]

        conflict_policy : typing.Optional[NameConflictPolicy]

        preferred_part_size : typing.Optional[int]
            Optional preferred part size. The server may choose a different value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.public_shares.create_public_share_upload(
            token="token",
            idempotency_key="Idempotency-Key",
            name="name",
            size=1000000,
            mod_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.create_public_share_upload(
            token,
            idempotency_key=idempotency_key,
            name=name,
            size=size,
            mod_time=mod_time,
            share_password=share_password,
            parent_id=parent_id,
            mime_type=mime_type,
            hash=hash,
            encryption=encryption,
            conflict_policy=conflict_policy,
            preferred_part_size=preferred_part_size,
            request_options=request_options,
        )
        return _response.data

    def put_public_share_upload_part(
        self,
        token: str,
        upload_id: Uuid,
        part_no: int,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadPart:
        """
        Parameters
        ----------
        token : str

        upload_id : Uuid

        part_no : int

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadPart
            The request has succeeded.
        """
        _response = self._raw_client.put_public_share_upload_part(
            token, upload_id, part_no, request=request, request_options=request_options
        )
        return _response.data

    def complete_public_share_upload(
        self,
        token: str,
        upload_id: Uuid,
        *,
        idempotency_key: Uuid,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Parameters
        ----------
        token : str

        upload_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        share_password : typing.Optional[str]

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
        client.public_shares.complete_public_share_upload(
            token="token",
            upload_id="uploadId",
            idempotency_key="Idempotency-Key",
        )
        """
        _response = self._raw_client.complete_public_share_upload(
            token,
            upload_id,
            idempotency_key=idempotency_key,
            share_password=share_password,
            request_options=request_options,
        )
        return _response.data

    def abort_public_share_upload(
        self,
        token: str,
        upload_id: Uuid,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        token : str

        upload_id : Uuid

        share_password : typing.Optional[str]

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
        client.public_shares.abort_public_share_upload(
            token="token",
            upload_id="uploadId",
        )
        """
        _response = self._raw_client.abort_public_share_upload(
            token, upload_id, share_password=share_password, request_options=request_options
        )
        return _response.data


class AsyncPublicSharesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPublicSharesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPublicSharesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPublicSharesClient
        """
        return self._raw_client

    async def create_public_playback(
        self,
        token: str,
        file_id: Uuid,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlaybackSession:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        share_password : typing.Optional[str]

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
            await client.public_shares.create_public_playback(
                token="token",
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_public_playback(
            token, file_id, share_password=share_password, request_options=request_options
        )
        return _response.data

    async def get_public_share(
        self,
        token: str,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublicShare:
        """
        Parameters
        ----------
        token : str

        share_password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicShare
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
            await client.public_shares.get_public_share(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_public_share(
            token, share_password=share_password, request_options=request_options
        )
        return _response.data

    async def list_public_share_files(
        self,
        token: str,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        path: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPublicShareFilesResponse:
        """
        List children within a publicly shared folder.

        Parameters
        ----------
        token : str

        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        path : typing.Optional[str]
            Folder path relative to the shared folder root.

        search : typing.Optional[str]

        share_password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPublicShareFilesResponse
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
            await client.public_shares.list_public_share_files(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_public_share_files(
            token,
            cursor=cursor,
            limit=limit,
            path=path,
            search=search,
            share_password=share_password,
            request_options=request_options,
        )
        return _response.data

    async def download_public_share_file(
        self,
        token: str,
        file_id: Uuid,
        file_name: str,
        *,
        download: typing.Optional[DownloadPublicShareFileRequestDownload] = None,
        share_password: typing.Optional[str] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        file_name : str

        download : typing.Optional[DownloadPublicShareFileRequestDownload]
            Force a browser download instead of inline display.

        share_password : typing.Optional[str]

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
            await client.public_shares.download_public_share_file(
                token="token",
                file_id="fileId",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_public_share_file(
            token,
            file_id,
            file_name,
            download=download,
            share_password=share_password,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def head_public_share_file(
        self,
        token: str,
        file_id: Uuid,
        file_name: str,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        file_name : str

        share_password : typing.Optional[str]

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
            await client.public_shares.head_public_share_file(
                token="token",
                file_id="fileId",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_public_share_file(
            token, file_id, file_name, share_password=share_password, request_options=request_options
        )
        return _response.headers

    async def download_public_share(
        self,
        token: str,
        file_name: str,
        *,
        download: typing.Optional[DownloadPublicShareRequestDownload] = None,
        share_password: typing.Optional[str] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        token : str

        file_name : str

        download : typing.Optional[DownloadPublicShareRequestDownload]
            Force a browser download instead of inline display.

        share_password : typing.Optional[str]

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
            await client.public_shares.download_public_share(
                token="token",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_public_share(
            token,
            file_name,
            download=download,
            share_password=share_password,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def head_public_share(
        self,
        token: str,
        file_name: str,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        token : str

        file_name : str

        share_password : typing.Optional[str]

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
            await client.public_shares.head_public_share(
                token="token",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_public_share(
            token, file_name, share_password=share_password, request_options=request_options
        )
        return _response.headers

    async def download_public_share_file_legacy(
        self,
        token: str,
        file_id: Uuid,
        *,
        download: typing.Optional[DownloadPublicShareFileLegacyRequestDownload] = None,
        share_password: typing.Optional[str] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        download : typing.Optional[DownloadPublicShareFileLegacyRequestDownload]
            Force a browser download instead of inline display.

        share_password : typing.Optional[str]

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
            await client.public_shares.download_public_share_file_legacy(
                token="token",
                file_id="fileId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_public_share_file_legacy(
            token,
            file_id,
            download=download,
            share_password=share_password,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def head_public_share_file_legacy(
        self,
        token: str,
        file_id: Uuid,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        share_password : typing.Optional[str]

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
            await client.public_shares.head_public_share_file_legacy(
                token="token",
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_public_share_file_legacy(
            token, file_id, share_password=share_password, request_options=request_options
        )
        return _response.headers

    async def download_public_share_legacy(
        self,
        token: str,
        *,
        download: typing.Optional[DownloadPublicShareLegacyRequestDownload] = None,
        share_password: typing.Optional[str] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        token : str

        download : typing.Optional[DownloadPublicShareLegacyRequestDownload]
            Force a browser download instead of inline display.

        share_password : typing.Optional[str]

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
            await client.public_shares.download_public_share_legacy(
                token="token",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_public_share_legacy(
            token,
            download=download,
            share_password=share_password,
            range=range,
            if_none_match=if_none_match,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def head_public_share_legacy(
        self,
        token: str,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        token : str

        share_password : typing.Optional[str]

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
            await client.public_shares.head_public_share_legacy(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_public_share_legacy(
            token, share_password=share_password, request_options=request_options
        )
        return _response.headers

    async def create_public_share_folder(
        self,
        token: str,
        *,
        name: str,
        share_password: typing.Optional[str] = None,
        parent_id: typing.Optional[Uuid] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        mod_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Parameters
        ----------
        token : str

        name : str

        share_password : typing.Optional[str]

        parent_id : typing.Optional[Uuid]

        conflict_policy : typing.Optional[NameConflictPolicy]

        mod_time : typing.Optional[dt.datetime]

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
            await client.public_shares.create_public_share_folder(
                token="token",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_public_share_folder(
            token,
            name=name,
            share_password=share_password,
            parent_id=parent_id,
            conflict_policy=conflict_policy,
            mod_time=mod_time,
            request_options=request_options,
        )
        return _response.data

    async def trash_public_share_file(
        self,
        token: str,
        file_id: Uuid,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        share_password : typing.Optional[str]

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
            await client.public_shares.trash_public_share_file(
                token="token",
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trash_public_share_file(
            token, file_id, share_password=share_password, request_options=request_options
        )
        return _response.data

    async def update_public_share_file(
        self,
        token: str,
        file_id: Uuid,
        *,
        if_match: ETag,
        share_password: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        mod_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Parameters
        ----------
        token : str

        file_id : Uuid

        if_match : ETag

        share_password : typing.Optional[str]

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
            await client.public_shares.update_public_share_file(
                token="token",
                file_id="fileId",
                if_match="If-Match",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_public_share_file(
            token,
            file_id,
            if_match=if_match,
            share_password=share_password,
            name=name,
            mod_time=mod_time,
            request_options=request_options,
        )
        return _response.data

    async def create_public_share_upload(
        self,
        token: str,
        *,
        idempotency_key: Uuid,
        name: str,
        size: int,
        mod_time: dt.datetime,
        share_password: typing.Optional[str] = None,
        parent_id: typing.Optional[Uuid] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        hash: typing.Optional[FileHash] = OMIT,
        encryption: typing.Optional[bool] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        preferred_part_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadSession:
        """
        Parameters
        ----------
        token : str

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        name : str

        size : int
            Expected size in bytes, or -1 when the size is unknown until completion.

        mod_time : dt.datetime

        share_password : typing.Optional[str]

        parent_id : typing.Optional[Uuid]

        mime_type : typing.Optional[str]

        hash : typing.Optional[FileHash]

        encryption : typing.Optional[bool]

        conflict_policy : typing.Optional[NameConflictPolicy]

        preferred_part_size : typing.Optional[int]
            Optional preferred part size. The server may choose a different value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.public_shares.create_public_share_upload(
                token="token",
                idempotency_key="Idempotency-Key",
                name="name",
                size=1000000,
                mod_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_public_share_upload(
            token,
            idempotency_key=idempotency_key,
            name=name,
            size=size,
            mod_time=mod_time,
            share_password=share_password,
            parent_id=parent_id,
            mime_type=mime_type,
            hash=hash,
            encryption=encryption,
            conflict_policy=conflict_policy,
            preferred_part_size=preferred_part_size,
            request_options=request_options,
        )
        return _response.data

    async def put_public_share_upload_part(
        self,
        token: str,
        upload_id: Uuid,
        part_no: int,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadPart:
        """
        Parameters
        ----------
        token : str

        upload_id : Uuid

        part_no : int

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadPart
            The request has succeeded.
        """
        _response = await self._raw_client.put_public_share_upload_part(
            token, upload_id, part_no, request=request, request_options=request_options
        )
        return _response.data

    async def complete_public_share_upload(
        self,
        token: str,
        upload_id: Uuid,
        *,
        idempotency_key: Uuid,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileEntry:
        """
        Parameters
        ----------
        token : str

        upload_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        share_password : typing.Optional[str]

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
            await client.public_shares.complete_public_share_upload(
                token="token",
                upload_id="uploadId",
                idempotency_key="Idempotency-Key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_public_share_upload(
            token,
            upload_id,
            idempotency_key=idempotency_key,
            share_password=share_password,
            request_options=request_options,
        )
        return _response.data

    async def abort_public_share_upload(
        self,
        token: str,
        upload_id: Uuid,
        *,
        share_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        token : str

        upload_id : Uuid

        share_password : typing.Optional[str]

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
            await client.public_shares.abort_public_share_upload(
                token="token",
                upload_id="uploadId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.abort_public_share_upload(
            token, upload_id, share_password=share_password, request_options=request_options
        )
        return _response.data
