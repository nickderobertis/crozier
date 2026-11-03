

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.span import Span
from .raw_client import AsyncRawRecordsClient, RawRecordsClient
from .types.search_records_request_filters_value import SearchRecordsRequestFiltersValue
from .types.search_records_response_item import SearchRecordsResponseItem


OMIT = typing.cast(typing.Any, ...)


class RecordsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRecordsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRecordsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRecordsClient
        """
        return self._raw_client

    def search_records(
        self,
        *,
        query: str,
        filters: typing.Optional[typing.Dict[str, SearchRecordsRequestFiltersValue]] = OMIT,
        bounds: typing.Optional[typing.Dict[str, Span]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SearchRecordsResponseItem]:
        """
        Parameters
        ----------
        query : str

        filters : typing.Optional[typing.Dict[str, SearchRecordsRequestFiltersValue]]

        bounds : typing.Optional[typing.Dict[str, Span]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SearchRecordsResponseItem]
            The matching records.

        Examples
        --------
        from fern import FernApi, Span

        client = FernApi()
        client.records.search_records(
            query="harbour charters",
            filters={
                "language": ["Welsh"],
                "accessioned": Span(
                    from_="1901-01-01",
                    to="1910-12-31",
                ),
                "sealed": [
                    Span(
                        from_="1921-01-01",
                        to="1921-12-31",
                    ),
                    Span(
                        from_="1938-01-01",
                        to="1938-12-31",
                    ),
                ],
            },
            bounds={
                "shelf": Span(
                    from_="A",
                    to="F",
                )
            },
        )
        """
        _response = self._raw_client.search_records(
            query=query, filters=filters, bounds=bounds, request_options=request_options
        )
        return _response.data


class AsyncRecordsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRecordsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRecordsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRecordsClient
        """
        return self._raw_client

    async def search_records(
        self,
        *,
        query: str,
        filters: typing.Optional[typing.Dict[str, SearchRecordsRequestFiltersValue]] = OMIT,
        bounds: typing.Optional[typing.Dict[str, Span]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SearchRecordsResponseItem]:
        """
        Parameters
        ----------
        query : str

        filters : typing.Optional[typing.Dict[str, SearchRecordsRequestFiltersValue]]

        bounds : typing.Optional[typing.Dict[str, Span]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SearchRecordsResponseItem]
            The matching records.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Span

        client = AsyncFernApi()


        async def main() -> None:
            await client.records.search_records(
                query="harbour charters",
                filters={
                    "language": ["Welsh"],
                    "accessioned": Span(
                        from_="1901-01-01",
                        to="1910-12-31",
                    ),
                    "sealed": [
                        Span(
                            from_="1921-01-01",
                            to="1921-12-31",
                        ),
                        Span(
                            from_="1938-01-01",
                            to="1938-12-31",
                        ),
                    ],
                },
                bounds={
                    "shelf": Span(
                        from_="A",
                        to="F",
                    )
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_records(
            query=query, filters=filters, bounds=bounds, request_options=request_options
        )
        return _response.data
