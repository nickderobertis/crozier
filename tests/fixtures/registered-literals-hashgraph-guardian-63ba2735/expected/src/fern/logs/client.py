

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLogsClient, RawLogsClient
from .types.log_filters_sort_direction import LogFiltersSortDirection
from .types.post_logs_response import PostLogsResponse


OMIT = typing.cast(typing.Any, ...)


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

    def returns_logs(
        self,
        *,
        type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        attributes: typing.Optional[typing.Sequence[str]] = OMIT,
        message: typing.Optional[str] = OMIT,
        page_size: typing.Optional[float] = OMIT,
        page_index: typing.Optional[float] = OMIT,
        sort_direction: typing.Optional[LogFiltersSortDirection] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLogsResponse:
        """
        Returns logs. For users with the Standard Registry role only.

        Parameters
        ----------
        type : typing.Optional[str]

        start_date : typing.Optional[str]

        end_date : typing.Optional[str]

        attributes : typing.Optional[typing.Sequence[str]]

        message : typing.Optional[str]

        page_size : typing.Optional[float]

        page_index : typing.Optional[float]

        sort_direction : typing.Optional[LogFiltersSortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLogsResponse
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.logs.returns_logs()
        """
        _response = self._raw_client.returns_logs(
            type=type,
            start_date=start_date,
            end_date=end_date,
            attributes=attributes,
            message=message,
            page_size=page_size,
            page_index=page_index,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def returns_logs_attributes(
        self,
        *,
        name: typing.Optional[str] = None,
        existing_attributes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Returns logs attributes. For users with the Standard Registry role only.

        Parameters
        ----------
        name : typing.Optional[str]
            Part of name.

        existing_attributes : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Attributes to exclude.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.logs.returns_logs_attributes()
        """
        _response = self._raw_client.returns_logs_attributes(
            name=name, existing_attributes=existing_attributes, request_options=request_options
        )
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

    async def returns_logs(
        self,
        *,
        type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        attributes: typing.Optional[typing.Sequence[str]] = OMIT,
        message: typing.Optional[str] = OMIT,
        page_size: typing.Optional[float] = OMIT,
        page_index: typing.Optional[float] = OMIT,
        sort_direction: typing.Optional[LogFiltersSortDirection] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLogsResponse:
        """
        Returns logs. For users with the Standard Registry role only.

        Parameters
        ----------
        type : typing.Optional[str]

        start_date : typing.Optional[str]

        end_date : typing.Optional[str]

        attributes : typing.Optional[typing.Sequence[str]]

        message : typing.Optional[str]

        page_size : typing.Optional[float]

        page_index : typing.Optional[float]

        sort_direction : typing.Optional[LogFiltersSortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLogsResponse
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.logs.returns_logs()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_logs(
            type=type,
            start_date=start_date,
            end_date=end_date,
            attributes=attributes,
            message=message,
            page_size=page_size,
            page_index=page_index,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def returns_logs_attributes(
        self,
        *,
        name: typing.Optional[str] = None,
        existing_attributes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Returns logs attributes. For users with the Standard Registry role only.

        Parameters
        ----------
        name : typing.Optional[str]
            Part of name.

        existing_attributes : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Attributes to exclude.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.logs.returns_logs_attributes()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_logs_attributes(
            name=name, existing_attributes=existing_attributes, request_options=request_options
        )
        return _response.data
