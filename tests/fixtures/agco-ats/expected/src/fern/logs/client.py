

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_models_log import ApiModelsLog
from ..types.api_paged_response_api_models_log import ApiPagedResponseApiModelsLog
from .raw_client import AsyncRawLogsClient, RawLogsClient


class LogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLogsClient
        """
        return self._raw_client

    def getlogs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsLog:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsLog
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.logs.getlogs()
        """
        _response = self._raw_client.getlogs(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def postlog(self, *, message: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        message : str
            Message to enter into the log

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.logs.postlog(
            message="Message",
        )
        """
        _response = self._raw_client.postlog(message=message, request_options=request_options)
        return _response.data

    def getlog(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiModelsLog:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Log ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsLog
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.logs.getlog(
            id="ID",
        )
        """
        _response = self._raw_client.getlog(id, request_options=request_options)
        return _response.data


class AsyncLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLogsClient
        """
        return self._raw_client

    async def getlogs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsLog:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsLog
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.logs.getlogs()


        asyncio.run(main())
        """
        _response = await self._raw_client.getlogs(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    async def postlog(self, *, message: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        message : str
            Message to enter into the log

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.logs.postlog(
                message="Message",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postlog(message=message, request_options=request_options)
        return _response.data

    async def getlog(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiModelsLog:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Log ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsLog
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.logs.getlog(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getlog(id, request_options=request_options)
        return _response.data
