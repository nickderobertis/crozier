

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.property import Property
from .raw_client import AsyncRawQueryClient, RawQueryClient
from .types.post_metadata_query_response import PostMetadataQueryResponse


OMIT = typing.cast(typing.Any, ...)


class QueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueryClient
        """
        return self._raw_client

    def query_all_properties(
        self, subject: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Property:
        """
        Parameters
        ----------
        subject : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Property


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.query.query_all_properties(
            subject="subject",
        )
        """
        _response = self._raw_client.query_all_properties(subject, request_options=request_options)
        return _response.data

    def query_specific_property(
        self, subject: str, properties: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Property:
        """
        Parameters
        ----------
        subject : str

        properties : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Property


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.query.query_specific_property(
            subject="subject",
            properties="properties",
        )
        """
        _response = self._raw_client.query_specific_property(subject, properties, request_options=request_options)
        return _response.data

    def batch_metadata_query(
        self,
        *,
        subjects: typing.Sequence[str],
        properties: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostMetadataQueryResponse:
        """
        Parameters
        ----------
        subjects : typing.Sequence[str]

        properties : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostMetadataQueryResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.query.batch_metadata_query(
            subjects=["subjects"],
        )
        """
        _response = self._raw_client.batch_metadata_query(
            subjects=subjects, properties=properties, request_options=request_options
        )
        return _response.data


class AsyncQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueryClient
        """
        return self._raw_client

    async def query_all_properties(
        self, subject: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Property:
        """
        Parameters
        ----------
        subject : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Property


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.query.query_all_properties(
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query_all_properties(subject, request_options=request_options)
        return _response.data

    async def query_specific_property(
        self, subject: str, properties: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Property:
        """
        Parameters
        ----------
        subject : str

        properties : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Property


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.query.query_specific_property(
                subject="subject",
                properties="properties",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query_specific_property(subject, properties, request_options=request_options)
        return _response.data

    async def batch_metadata_query(
        self,
        *,
        subjects: typing.Sequence[str],
        properties: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostMetadataQueryResponse:
        """
        Parameters
        ----------
        subjects : typing.Sequence[str]

        properties : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostMetadataQueryResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.query.batch_metadata_query(
                subjects=["subjects"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_metadata_query(
            subjects=subjects, properties=properties, request_options=request_options
        )
        return _response.data
