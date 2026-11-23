

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pet import Pet
from .raw_client import AsyncRawKennelClient, RawKennelClient
from .types.list_tasks_response_item import ListTasksResponseItem


OMIT = typing.cast(typing.Any, ...)


class KennelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKennelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKennelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKennelClient
        """
        return self._raw_client

    def add_pet(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        age: typing.Optional[int] = OMIT,
        species: typing.Optional[str] = OMIT,
        breed: typing.Optional[str] = OMIT,
        size: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pet:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        age : typing.Optional[int]

        species : typing.Optional[str]

        breed : typing.Optional[str]

        size : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pet
            Added.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.kennel.add_pet()
        """
        _response = self._raw_client.add_pet(
            name=name, age=age, species=species, breed=breed, size=size, request_options=request_options
        )
        return _response.data

    def list_tasks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListTasksResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListTasksResponseItem]
            The tasks.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.kennel.list_tasks()
        """
        _response = self._raw_client.list_tasks(request_options=request_options)
        return _response.data


class AsyncKennelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKennelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKennelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKennelClient
        """
        return self._raw_client

    async def add_pet(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        age: typing.Optional[int] = OMIT,
        species: typing.Optional[str] = OMIT,
        breed: typing.Optional[str] = OMIT,
        size: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pet:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        age : typing.Optional[int]

        species : typing.Optional[str]

        breed : typing.Optional[str]

        size : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pet
            Added.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.kennel.add_pet()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_pet(
            name=name, age=age, species=species, breed=breed, size=size, request_options=request_options
        )
        return _response.data

    async def list_tasks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListTasksResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListTasksResponseItem]
            The tasks.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.kennel.list_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tasks(request_options=request_options)
        return _response.data
