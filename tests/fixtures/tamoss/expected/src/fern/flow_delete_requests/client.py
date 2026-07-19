

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deletion_request import DeletionRequest
from .raw_client import AsyncRawFlowDeleteRequestsClient, RawFlowDeleteRequestsClient


class FlowDeleteRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFlowDeleteRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFlowDeleteRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFlowDeleteRequestsClient
        """
        return self._raw_client

    def get_flow_delete_requests(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeletionRequest]:
        """
        List ongoing flow deletion requests.

        This will not necessarily list all requests, nor return a consistent set in any particular order, and should not be relied upon by clients. However if there are any requests in the system, it will always return at least one.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeletionRequest]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flow_delete_requests.get_flow_delete_requests()
        """
        _response = self._raw_client.get_flow_delete_requests(request_options=request_options)
        return _response.data

    def head_flow_delete_requests(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return flow-delete-requests path headers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flow_delete_requests.head_flow_delete_requests()
        """
        _response = self._raw_client.head_flow_delete_requests(request_options=request_options)
        return _response.headers

    def get_flow_delete_requests_request_id(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletionRequest:
        """
        Get information about a timerange of Flow Segments that are being deleted.

        A deletion request is created when a client DELETEs a long timerange of Segments, which takes longer than a single HTTP request.
        Clients will be redirected here to monitor the request's progress.

        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletionRequest


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flow_delete_requests.get_flow_delete_requests_request_id(
            request_id="request-id",
        )
        """
        _response = self._raw_client.get_flow_delete_requests_request_id(request_id, request_options=request_options)
        return _response.data

    def head_flow_delete_requests_request_id(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow delete request path headers

        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flow_delete_requests.head_flow_delete_requests_request_id(
            request_id="request-id",
        )
        """
        _response = self._raw_client.head_flow_delete_requests_request_id(request_id, request_options=request_options)
        return _response.headers


class AsyncFlowDeleteRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFlowDeleteRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFlowDeleteRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFlowDeleteRequestsClient
        """
        return self._raw_client

    async def get_flow_delete_requests(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeletionRequest]:
        """
        List ongoing flow deletion requests.

        This will not necessarily list all requests, nor return a consistent set in any particular order, and should not be relied upon by clients. However if there are any requests in the system, it will always return at least one.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeletionRequest]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flow_delete_requests.get_flow_delete_requests()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flow_delete_requests(request_options=request_options)
        return _response.data

    async def head_flow_delete_requests(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return flow-delete-requests path headers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flow_delete_requests.head_flow_delete_requests()


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flow_delete_requests(request_options=request_options)
        return _response.headers

    async def get_flow_delete_requests_request_id(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletionRequest:
        """
        Get information about a timerange of Flow Segments that are being deleted.

        A deletion request is created when a client DELETEs a long timerange of Segments, which takes longer than a single HTTP request.
        Clients will be redirected here to monitor the request's progress.

        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletionRequest


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flow_delete_requests.get_flow_delete_requests_request_id(
                request_id="request-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flow_delete_requests_request_id(
            request_id, request_options=request_options
        )
        return _response.data

    async def head_flow_delete_requests_request_id(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow delete request path headers

        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flow_delete_requests.head_flow_delete_requests_request_id(
                request_id="request-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flow_delete_requests_request_id(
            request_id, request_options=request_options
        )
        return _response.headers
