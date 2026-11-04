

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.destination_response import DestinationResponse
from ..types.named_ref import NamedRef
from .raw_client import AsyncRawDestinationsClient, RawDestinationsClient


OMIT = typing.cast(typing.Any, ...)


class DestinationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDestinationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDestinationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDestinationsClient
        """
        return self._raw_client

    def returns_all_available_destinations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DestinationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DestinationResponse]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destinations.returns_all_available_destinations()
        """
        _response = self._raw_client.returns_all_available_destinations(request_options=request_options)
        return _response.data

    def creates_new_destination(
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
        client.destinations.creates_new_destination(
            name="name",
            type="type",
            schema="schema",
        )
        """
        _response = self._raw_client.creates_new_destination(
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

    def returns_a_destination_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destinations.returns_a_destination_with_given_id(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_a_destination_with_given_id(id, request_options=request_options)
        return _response.data

    def updates_an_existing_destination(
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
    ) -> DestinationResponse:
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
        DestinationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destinations.updates_an_existing_destination(
            id=1000000,
            name="name",
            type="type",
            schema="schema",
        )
        """
        _response = self._raw_client.updates_an_existing_destination(
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

    def deletes_an_existing_destination(
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
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destinations.deletes_an_existing_destination(
            id=1000000,
        )
        """
        _response = self._raw_client.deletes_an_existing_destination(id, request_options=request_options)
        return _response.data


class AsyncDestinationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDestinationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDestinationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDestinationsClient
        """
        return self._raw_client

    async def returns_all_available_destinations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DestinationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DestinationResponse]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destinations.returns_all_available_destinations()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_available_destinations(request_options=request_options)
        return _response.data

    async def creates_new_destination(
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
            await client.destinations.creates_new_destination(
                name="name",
                type="type",
                schema="schema",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_new_destination(
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

    async def returns_a_destination_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destinations.returns_a_destination_with_given_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_destination_with_given_id(id, request_options=request_options)
        return _response.data

    async def updates_an_existing_destination(
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
    ) -> DestinationResponse:
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
        DestinationResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destinations.updates_an_existing_destination(
                id=1000000,
                name="name",
                type="type",
                schema="schema",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_an_existing_destination(
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

    async def deletes_an_existing_destination(
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
            await client.destinations.deletes_an_existing_destination(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_an_existing_destination(id, request_options=request_options)
        return _response.data
