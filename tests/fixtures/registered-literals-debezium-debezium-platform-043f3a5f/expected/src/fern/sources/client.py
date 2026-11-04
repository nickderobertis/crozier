

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.named_ref import NamedRef
from ..types.source_response import SourceResponse
from .raw_client import AsyncRawSourcesClient, RawSourcesClient
from .types.post_api_sources_signals_verify_response import PostApiSourcesSignalsVerifyResponse


OMIT = typing.cast(typing.Any, ...)


class SourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourcesClient
        """
        return self._raw_client

    def returns_all_available_sources(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SourceResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SourceResponse]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sources.returns_all_available_sources()
        """
        _response = self._raw_client.returns_all_available_sources(request_options=request_options)
        return _response.data

    def creates_new_source(
        self,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        connection: typing.Optional[NamedRef] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        connection : typing.Optional[NamedRef]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sources.creates_new_source(
            name="name",
            type="type",
            schema="schema",
        )
        """
        _response = self._raw_client.creates_new_source(
            name=name,
            type=type,
            schema=schema,
            description=description,
            connection=connection,
            vaults=vaults,
            config=config,
            request_options=request_options,
        )
        return _response.data

    def verify_that_signal_data_collection_is_configured_correctly(
        self,
        *,
        connection_id: int,
        fully_qualified_table_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiSourcesSignalsVerifyResponse:
        """
        Parameters
        ----------
        connection_id : int

        fully_qualified_table_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiSourcesSignalsVerifyResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sources.verify_that_signal_data_collection_is_configured_correctly(
            connection_id=1000000,
            fully_qualified_table_name="fullyQualifiedTableName",
        )
        """
        _response = self._raw_client.verify_that_signal_data_collection_is_configured_correctly(
            connection_id=connection_id,
            fully_qualified_table_name=fully_qualified_table_name,
            request_options=request_options,
        )
        return _response.data

    def returns_a_source_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sources.returns_a_source_with_given_id(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_a_source_with_given_id(id, request_options=request_options)
        return _response.data

    def updates_an_existing_source(
        self,
        id: int,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        connection: typing.Optional[NamedRef] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        connection : typing.Optional[NamedRef]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sources.updates_an_existing_source(
            id=1000000,
            name="name",
            type="type",
            schema="schema",
        )
        """
        _response = self._raw_client.updates_an_existing_source(
            id,
            name=name,
            type=type,
            schema=schema,
            description=description,
            connection=connection,
            vaults=vaults,
            config=config,
            request_options=request_options,
        )
        return _response.data

    def deletes_an_existing_source(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

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
        client.sources.deletes_an_existing_source(
            id=1000000,
        )
        """
        _response = self._raw_client.deletes_an_existing_source(id, request_options=request_options)
        return _response.data


class AsyncSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourcesClient
        """
        return self._raw_client

    async def returns_all_available_sources(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SourceResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SourceResponse]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.returns_all_available_sources()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_available_sources(request_options=request_options)
        return _response.data

    async def creates_new_source(
        self,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        connection: typing.Optional[NamedRef] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        connection : typing.Optional[NamedRef]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.creates_new_source(
                name="name",
                type="type",
                schema="schema",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_new_source(
            name=name,
            type=type,
            schema=schema,
            description=description,
            connection=connection,
            vaults=vaults,
            config=config,
            request_options=request_options,
        )
        return _response.data

    async def verify_that_signal_data_collection_is_configured_correctly(
        self,
        *,
        connection_id: int,
        fully_qualified_table_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiSourcesSignalsVerifyResponse:
        """
        Parameters
        ----------
        connection_id : int

        fully_qualified_table_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiSourcesSignalsVerifyResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.verify_that_signal_data_collection_is_configured_correctly(
                connection_id=1000000,
                fully_qualified_table_name="fullyQualifiedTableName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_that_signal_data_collection_is_configured_correctly(
            connection_id=connection_id,
            fully_qualified_table_name=fully_qualified_table_name,
            request_options=request_options,
        )
        return _response.data

    async def returns_a_source_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.returns_a_source_with_given_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_source_with_given_id(id, request_options=request_options)
        return _response.data

    async def updates_an_existing_source(
        self,
        id: int,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        connection: typing.Optional[NamedRef] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        connection : typing.Optional[NamedRef]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.updates_an_existing_source(
                id=1000000,
                name="name",
                type="type",
                schema="schema",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_an_existing_source(
            id,
            name=name,
            type=type,
            schema=schema,
            description=description,
            connection=connection,
            vaults=vaults,
            config=config,
            request_options=request_options,
        )
        return _response.data

    async def deletes_an_existing_source(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

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
            await client.sources.deletes_an_existing_source(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_an_existing_source(id, request_options=request_options)
        return _response.data
