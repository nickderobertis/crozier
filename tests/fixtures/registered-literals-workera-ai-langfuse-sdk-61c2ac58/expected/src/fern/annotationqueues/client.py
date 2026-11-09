

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.annotation_queue import AnnotationQueue
from ..types.annotation_queue_item import AnnotationQueueItem
from ..types.annotation_queue_object_type import AnnotationQueueObjectType
from ..types.annotation_queue_status import AnnotationQueueStatus
from ..types.delete_annotation_queue_item_response import DeleteAnnotationQueueItemResponse
from ..types.paginated_annotation_queue_items import PaginatedAnnotationQueueItems
from ..types.paginated_annotation_queues import PaginatedAnnotationQueues
from .raw_client import AsyncRawAnnotationqueuesClient, RawAnnotationqueuesClient


OMIT = typing.cast(typing.Any, ...)


class AnnotationqueuesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnnotationqueuesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnnotationqueuesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnnotationqueuesClient
        """
        return self._raw_client

    def listqueues(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedAnnotationQueues:
        """
        Get all annotation queues

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedAnnotationQueues


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.annotationqueues.listqueues()
        """
        _response = self._raw_client.listqueues(page=page, limit=limit, request_options=request_options)
        return _response.data

    def getqueue(self, queue_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> AnnotationQueue:
        """
        Get an annotation queue by ID

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnnotationQueue


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.annotationqueues.getqueue(
            queue_id="queueId",
        )
        """
        _response = self._raw_client.getqueue(queue_id, request_options=request_options)
        return _response.data

    def listqueueitems(
        self,
        queue_id: str,
        *,
        status: typing.Optional[AnnotationQueueStatus] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedAnnotationQueueItems:
        """
        Get items for a specific annotation queue

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        status : typing.Optional[AnnotationQueueStatus]
            Filter by status

        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedAnnotationQueueItems


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.annotationqueues.listqueueitems(
            queue_id="queueId",
        )
        """
        _response = self._raw_client.listqueueitems(
            queue_id, status=status, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    def createqueueitem(
        self,
        queue_id: str,
        *,
        object_id: str,
        object_type: AnnotationQueueObjectType,
        status: typing.Optional[AnnotationQueueStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnnotationQueueItem:
        """
        Add an item to an annotation queue

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        object_id : str

        object_type : AnnotationQueueObjectType

        status : typing.Optional[AnnotationQueueStatus]
            Defaults to PENDING for new queue items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnnotationQueueItem


        Examples
        --------
        from fern import AnnotationQueueObjectType, FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.annotationqueues.createqueueitem(
            queue_id="queueId",
            object_id="objectId",
            object_type=AnnotationQueueObjectType.TRACE,
        )
        """
        _response = self._raw_client.createqueueitem(
            queue_id, object_id=object_id, object_type=object_type, status=status, request_options=request_options
        )
        return _response.data

    def getqueueitem(
        self, queue_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AnnotationQueueItem:
        """
        Get a specific item from an annotation queue

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        item_id : str
            The unique identifier of the annotation queue item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnnotationQueueItem


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.annotationqueues.getqueueitem(
            queue_id="queueId",
            item_id="itemId",
        )
        """
        _response = self._raw_client.getqueueitem(queue_id, item_id, request_options=request_options)
        return _response.data

    def deletequeueitem(
        self, queue_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAnnotationQueueItemResponse:
        """
        Remove an item from an annotation queue

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        item_id : str
            The unique identifier of the annotation queue item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAnnotationQueueItemResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.annotationqueues.deletequeueitem(
            queue_id="queueId",
            item_id="itemId",
        )
        """
        _response = self._raw_client.deletequeueitem(queue_id, item_id, request_options=request_options)
        return _response.data

    def updatequeueitem(
        self,
        queue_id: str,
        item_id: str,
        *,
        status: typing.Optional[AnnotationQueueStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnnotationQueueItem:
        """
        Update an annotation queue item

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        item_id : str
            The unique identifier of the annotation queue item

        status : typing.Optional[AnnotationQueueStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnnotationQueueItem


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.annotationqueues.updatequeueitem(
            queue_id="queueId",
            item_id="itemId",
        )
        """
        _response = self._raw_client.updatequeueitem(queue_id, item_id, status=status, request_options=request_options)
        return _response.data


class AsyncAnnotationqueuesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnnotationqueuesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnnotationqueuesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnnotationqueuesClient
        """
        return self._raw_client

    async def listqueues(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedAnnotationQueues:
        """
        Get all annotation queues

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedAnnotationQueues


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
            await client.annotationqueues.listqueues()


        asyncio.run(main())
        """
        _response = await self._raw_client.listqueues(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def getqueue(
        self, queue_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AnnotationQueue:
        """
        Get an annotation queue by ID

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnnotationQueue


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
            await client.annotationqueues.getqueue(
                queue_id="queueId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getqueue(queue_id, request_options=request_options)
        return _response.data

    async def listqueueitems(
        self,
        queue_id: str,
        *,
        status: typing.Optional[AnnotationQueueStatus] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedAnnotationQueueItems:
        """
        Get items for a specific annotation queue

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        status : typing.Optional[AnnotationQueueStatus]
            Filter by status

        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedAnnotationQueueItems


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
            await client.annotationqueues.listqueueitems(
                queue_id="queueId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listqueueitems(
            queue_id, status=status, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    async def createqueueitem(
        self,
        queue_id: str,
        *,
        object_id: str,
        object_type: AnnotationQueueObjectType,
        status: typing.Optional[AnnotationQueueStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnnotationQueueItem:
        """
        Add an item to an annotation queue

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        object_id : str

        object_type : AnnotationQueueObjectType

        status : typing.Optional[AnnotationQueueStatus]
            Defaults to PENDING for new queue items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnnotationQueueItem


        Examples
        --------
        import asyncio

        from fern import AnnotationQueueObjectType, AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.annotationqueues.createqueueitem(
                queue_id="queueId",
                object_id="objectId",
                object_type=AnnotationQueueObjectType.TRACE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createqueueitem(
            queue_id, object_id=object_id, object_type=object_type, status=status, request_options=request_options
        )
        return _response.data

    async def getqueueitem(
        self, queue_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AnnotationQueueItem:
        """
        Get a specific item from an annotation queue

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        item_id : str
            The unique identifier of the annotation queue item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnnotationQueueItem


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
            await client.annotationqueues.getqueueitem(
                queue_id="queueId",
                item_id="itemId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getqueueitem(queue_id, item_id, request_options=request_options)
        return _response.data

    async def deletequeueitem(
        self, queue_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAnnotationQueueItemResponse:
        """
        Remove an item from an annotation queue

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        item_id : str
            The unique identifier of the annotation queue item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAnnotationQueueItemResponse


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
            await client.annotationqueues.deletequeueitem(
                queue_id="queueId",
                item_id="itemId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletequeueitem(queue_id, item_id, request_options=request_options)
        return _response.data

    async def updatequeueitem(
        self,
        queue_id: str,
        item_id: str,
        *,
        status: typing.Optional[AnnotationQueueStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnnotationQueueItem:
        """
        Update an annotation queue item

        Parameters
        ----------
        queue_id : str
            The unique identifier of the annotation queue

        item_id : str
            The unique identifier of the annotation queue item

        status : typing.Optional[AnnotationQueueStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnnotationQueueItem


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
            await client.annotationqueues.updatequeueitem(
                queue_id="queueId",
                item_id="itemId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatequeueitem(
            queue_id, item_id, status=status, request_options=request_options
        )
        return _response.data
