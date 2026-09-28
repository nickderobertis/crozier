

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEntitiesClient, RawEntitiesClient


class EntitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntitiesClient
        """
        return self._raw_client

    def otoroshi_next_controllers_adminapi_entities_controller_get_entity_graph(
        self, entity: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        entity : str
            the entity parameter

        id : str
            the id parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.entities.otoroshi_next_controllers_adminapi_entities_controller_get_entity_graph(
            entity="entity",
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_entities_controller_get_entity_graph(
            entity, id, request_options=request_options
        )
        return _response.data


class AsyncEntitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntitiesClient
        """
        return self._raw_client

    async def otoroshi_next_controllers_adminapi_entities_controller_get_entity_graph(
        self, entity: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        entity : str
            the entity parameter

        id : str
            the id parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.entities.otoroshi_next_controllers_adminapi_entities_controller_get_entity_graph(
                entity="entity",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_entities_controller_get_entity_graph(
            entity, id, request_options=request_options
        )
        return _response.data
