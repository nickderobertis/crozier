

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.types_animal import TypesAnimal
from .raw_client import AsyncRawEndpointsUnionClient, RawEndpointsUnionClient


OMIT = typing.cast(typing.Any, ...)


class EndpointsUnionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEndpointsUnionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEndpointsUnionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEndpointsUnionClient
        """
        return self._raw_client

    def endpoints_union_get_and_return_union(
        self, *, request: TypesAnimal, request_options: typing.Optional[RequestOptions] = None
    ) -> TypesAnimal:
        """
        Parameters
        ----------
        request : TypesAnimal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TypesAnimal


        Examples
        --------
        from fern import FernApi, TypesAnimalZero, TypesAnimalZeroAnimal

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints_union.endpoints_union_get_and_return_union(
            request=TypesAnimalZero(
                name="name",
                likes_to_woof=True,
                animal=TypesAnimalZeroAnimal.DOG,
            ),
        )
        """
        _response = self._raw_client.endpoints_union_get_and_return_union(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncEndpointsUnionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEndpointsUnionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEndpointsUnionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEndpointsUnionClient
        """
        return self._raw_client

    async def endpoints_union_get_and_return_union(
        self, *, request: TypesAnimal, request_options: typing.Optional[RequestOptions] = None
    ) -> TypesAnimal:
        """
        Parameters
        ----------
        request : TypesAnimal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TypesAnimal


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TypesAnimalZero, TypesAnimalZeroAnimal

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints_union.endpoints_union_get_and_return_union(
                request=TypesAnimalZero(
                    name="name",
                    likes_to_woof=True,
                    animal=TypesAnimalZeroAnimal.DOG,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.endpoints_union_get_and_return_union(
            request=request, request_options=request_options
        )
        return _response.data
