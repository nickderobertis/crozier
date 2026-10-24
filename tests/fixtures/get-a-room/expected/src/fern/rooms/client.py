

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.created_room import CreatedRoom
from ..types.room_final import RoomFinal
from ..types.room_status import RoomStatus
from ..types.sha256 import Sha256
from .raw_client import AsyncRawRoomsClient, RawRoomsClient
from .types.close_room_response import CloseRoomResponse
from .types.collect_room_response import CollectRoomResponse
from .types.finalize_room_response import FinalizeRoomResponse
from .types.get_room_task_response import GetRoomTaskResponse
from .types.list_room_attachments_response import ListRoomAttachmentsResponse
from .types.list_room_messages_response import ListRoomMessagesResponse
from .types.send_room_message_request_body import SendRoomMessageRequestBody
from .types.send_room_message_response import SendRoomMessageResponse
from .types.upload_room_attachment_response import UploadRoomAttachmentResponse


OMIT = typing.cast(typing.Any, ...)


class RoomsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoomsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoomsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoomsClient
        """
        return self._raw_client

    def create_room(
        self,
        *,
        task: str,
        ttl_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedRoom:
        """
        Creation does not require an account. The response contains three role-specific bearer capabilities. Each value must be handled like a password until the room ends.

        Parameters
        ----------
        task : str
            UTF-8 content is limited to 1 MiB; character count is only an approximation.

        ttl_seconds : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedRoom
            Room created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.create_room(
            task="task",
        )
        """
        _response = self._raw_client.create_room(task=task, ttl_seconds=ttl_seconds, request_options=request_options)
        return _response.data

    def close_room(self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> CloseRoomResponse:
        """
        Requires the lead capability. The operation deletes room storage.

        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloseRoomResponse
            Room deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.close_room(
            room_id="roomId",
        )
        """
        _response = self._raw_client.close_room(room_id, request_options=request_options)
        return _response.data

    def get_room_status(self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RoomStatus:
        """
        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomStatus
            Current room state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.get_room_status(
            room_id="roomId",
        )
        """
        _response = self._raw_client.get_room_status(room_id, request_options=request_options)
        return _response.data

    def get_room_task(
        self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetRoomTaskResponse:
        """
        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRoomTaskResponse
            Room task

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.get_room_task(
            room_id="roomId",
        )
        """
        _response = self._raw_client.get_room_task(room_id, request_options=request_options)
        return _response.data

    def list_room_messages(
        self,
        room_id: str,
        *,
        after: typing.Optional[int] = None,
        wait: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListRoomMessagesResponse:
        """
        Returns at most 100 messages and 512 KiB of message text. A request can wait up to five seconds for new messages. At most two long polls run at once per active room instance.

        Parameters
        ----------
        room_id : str

        after : typing.Optional[int]
            Return messages with a number greater than this cursor.

        wait : typing.Optional[int]
            Long-poll duration in seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRoomMessagesResponse
            Ordered page of messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.list_room_messages(
            room_id="roomId",
        )
        """
        _response = self._raw_client.list_room_messages(
            room_id, after=after, wait=wait, request_options=request_options
        )
        return _response.data

    def send_room_message(
        self,
        room_id: str,
        *,
        request: SendRoomMessageRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendRoomMessageResponse:
        """
        Observers cannot send. A room accepts at most 1,000 messages.

        Parameters
        ----------
        room_id : str

        request : SendRoomMessageRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendRoomMessageResponse
            Message added

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.send_room_message(
            room_id="roomId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.send_room_message(room_id, request=request, request_options=request_options)
        return _response.data

    def list_room_attachments(
        self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListRoomAttachmentsResponse:
        """
        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRoomAttachmentsResponse
            Committed room attachments

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.list_room_attachments(
            room_id="roomId",
        )
        """
        _response = self._raw_client.list_room_attachments(room_id, request_options=request_options)
        return _response.data

    def upload_room_attachment(
        self,
        room_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadRoomAttachmentResponse:
        """
        Lead and guest only. The upload remains invisible until the same role associates its attachment ID with a message. Files are limited to 10 MiB.

        Parameters
        ----------
        room_id : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadRoomAttachmentResponse
            File uploaded but not yet attached to a message
        """
        _response = self._raw_client.upload_room_attachment(room_id, request=request, request_options=request_options)
        return _response.data

    def download_room_attachment(
        self, room_id: str, attachment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        room_id : str

        attachment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Attachment bytes with download and SHA-256 headers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.download_room_attachment(
            room_id="roomId",
            attachment_id="attachmentId",
        )
        """
        with self._raw_client.download_room_attachment(room_id, attachment_id, request_options=request_options) as r:
            yield from r.data

    def get_room_final(self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RoomFinal:
        """
        Available to the lead and observer after finalization.

        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomFinal
            Final Markdown and digest

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.get_room_final(
            room_id="roomId",
        )
        """
        _response = self._raw_client.get_room_final(room_id, request_options=request_options)
        return _response.data

    def finalize_room(
        self, room_id: str, *, markdown: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FinalizeRoomResponse:
        """
        Requires the lead capability and transitions the room to finalized.

        Parameters
        ----------
        room_id : str

        markdown : str
            UTF-8 content is limited to 2 MiB.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinalizeRoomResponse
            Result stored

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.finalize_room(
            room_id="roomId",
            markdown="markdown",
        )
        """
        _response = self._raw_client.finalize_room(room_id, markdown=markdown, request_options=request_options)
        return _response.data

    def collect_room(
        self, room_id: str, *, sha256: Sha256, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectRoomResponse:
        """
        Requires the lead capability. On a matching SHA-256 digest, the service deletes room storage. Read and save the final result before collecting.

        Parameters
        ----------
        room_id : str

        sha256 : Sha256

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectRoomResponse
            Digest confirmed and room deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.collect_room(
            room_id="roomId",
            sha256="sha256",
        )
        """
        _response = self._raw_client.collect_room(room_id, sha256=sha256, request_options=request_options)
        return _response.data


class AsyncRoomsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoomsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoomsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoomsClient
        """
        return self._raw_client

    async def create_room(
        self,
        *,
        task: str,
        ttl_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedRoom:
        """
        Creation does not require an account. The response contains three role-specific bearer capabilities. Each value must be handled like a password until the room ends.

        Parameters
        ----------
        task : str
            UTF-8 content is limited to 1 MiB; character count is only an approximation.

        ttl_seconds : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedRoom
            Room created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.create_room(
                task="task",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_room(
            task=task, ttl_seconds=ttl_seconds, request_options=request_options
        )
        return _response.data

    async def close_room(
        self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloseRoomResponse:
        """
        Requires the lead capability. The operation deletes room storage.

        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloseRoomResponse
            Room deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.close_room(
                room_id="roomId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.close_room(room_id, request_options=request_options)
        return _response.data

    async def get_room_status(
        self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RoomStatus:
        """
        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomStatus
            Current room state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.get_room_status(
                room_id="roomId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_room_status(room_id, request_options=request_options)
        return _response.data

    async def get_room_task(
        self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetRoomTaskResponse:
        """
        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRoomTaskResponse
            Room task

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.get_room_task(
                room_id="roomId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_room_task(room_id, request_options=request_options)
        return _response.data

    async def list_room_messages(
        self,
        room_id: str,
        *,
        after: typing.Optional[int] = None,
        wait: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListRoomMessagesResponse:
        """
        Returns at most 100 messages and 512 KiB of message text. A request can wait up to five seconds for new messages. At most two long polls run at once per active room instance.

        Parameters
        ----------
        room_id : str

        after : typing.Optional[int]
            Return messages with a number greater than this cursor.

        wait : typing.Optional[int]
            Long-poll duration in seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRoomMessagesResponse
            Ordered page of messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.list_room_messages(
                room_id="roomId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_room_messages(
            room_id, after=after, wait=wait, request_options=request_options
        )
        return _response.data

    async def send_room_message(
        self,
        room_id: str,
        *,
        request: SendRoomMessageRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendRoomMessageResponse:
        """
        Observers cannot send. A room accepts at most 1,000 messages.

        Parameters
        ----------
        room_id : str

        request : SendRoomMessageRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendRoomMessageResponse
            Message added

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.send_room_message(
                room_id="roomId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_room_message(room_id, request=request, request_options=request_options)
        return _response.data

    async def list_room_attachments(
        self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListRoomAttachmentsResponse:
        """
        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRoomAttachmentsResponse
            Committed room attachments

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.list_room_attachments(
                room_id="roomId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_room_attachments(room_id, request_options=request_options)
        return _response.data

    async def upload_room_attachment(
        self,
        room_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadRoomAttachmentResponse:
        """
        Lead and guest only. The upload remains invisible until the same role associates its attachment ID with a message. Files are limited to 10 MiB.

        Parameters
        ----------
        room_id : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadRoomAttachmentResponse
            File uploaded but not yet attached to a message
        """
        _response = await self._raw_client.upload_room_attachment(
            room_id, request=request, request_options=request_options
        )
        return _response.data

    async def download_room_attachment(
        self, room_id: str, attachment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        room_id : str

        attachment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Attachment bytes with download and SHA-256 headers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.download_room_attachment(
                room_id="roomId",
                attachment_id="attachmentId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_room_attachment(
            room_id, attachment_id, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_room_final(
        self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RoomFinal:
        """
        Available to the lead and observer after finalization.

        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomFinal
            Final Markdown and digest

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.get_room_final(
                room_id="roomId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_room_final(room_id, request_options=request_options)
        return _response.data

    async def finalize_room(
        self, room_id: str, *, markdown: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FinalizeRoomResponse:
        """
        Requires the lead capability and transitions the room to finalized.

        Parameters
        ----------
        room_id : str

        markdown : str
            UTF-8 content is limited to 2 MiB.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinalizeRoomResponse
            Result stored

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.finalize_room(
                room_id="roomId",
                markdown="markdown",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.finalize_room(room_id, markdown=markdown, request_options=request_options)
        return _response.data

    async def collect_room(
        self, room_id: str, *, sha256: Sha256, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectRoomResponse:
        """
        Requires the lead capability. On a matching SHA-256 digest, the service deletes room storage. Read and save the final result before collecting.

        Parameters
        ----------
        room_id : str

        sha256 : Sha256

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectRoomResponse
            Digest confirmed and room deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.collect_room(
                room_id="roomId",
                sha256="sha256",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collect_room(room_id, sha256=sha256, request_options=request_options)
        return _response.data
