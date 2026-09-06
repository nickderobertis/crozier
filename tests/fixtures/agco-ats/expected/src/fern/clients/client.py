

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_available_update_group_subscription import (
    ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription,
)
from ..types.api_paged_response_update_system_models_update_group_subscription import (
    ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
)
from ..types.update_system_models_client import UpdateSystemModelsClient
from .raw_client import AsyncRawClientsClient, RawClientsClient


OMIT = typing.cast(typing.Any, ...)


class ClientsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientsClient
        """
        return self._raw_client

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> UpdateSystemModelsClient:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsClient
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.clients.get(
            id="ID",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def put(
        self,
        id: str,
        *,
        client_id: typing.Optional[str] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        client_id : typing.Optional[str]
            Read Only. The id of the client

        last_checkin : typing.Optional[dt.datetime]
            Read Only. The time of the client's last checkin with the server.

        tag : typing.Optional[str]
            A description of the client that can be used for easy reference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.clients.put(
            id="ID",
        )
        """
        _response = self._raw_client.put(
            id, client_id=client_id, last_checkin=last_checkin, tag=tag, request_options=request_options
        )
        return _response.data

    def getavailablesubscriptions(
        self,
        id: str,
        *,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.clients.getavailablesubscriptions(
            id="ID",
        )
        """
        _response = self._raw_client.getavailablesubscriptions(
            id, update_group_id=update_group_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def getsubscriptions(
        self,
        id: str,
        *,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.clients.getsubscriptions(
            id="ID",
        )
        """
        _response = self._raw_client.getsubscriptions(
            id, update_group_id=update_group_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data


class AsyncClientsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientsClient
        """
        return self._raw_client

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsClient:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsClient
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.clients.get(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def put(
        self,
        id: str,
        *,
        client_id: typing.Optional[str] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        client_id : typing.Optional[str]
            Read Only. The id of the client

        last_checkin : typing.Optional[dt.datetime]
            Read Only. The time of the client's last checkin with the server.

        tag : typing.Optional[str]
            A description of the client that can be used for easy reference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.clients.put(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(
            id, client_id=client_id, last_checkin=last_checkin, tag=tag, request_options=request_options
        )
        return _response.data

    async def getavailablesubscriptions(
        self,
        id: str,
        *,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.clients.getavailablesubscriptions(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getavailablesubscriptions(
            id, update_group_id=update_group_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def getsubscriptions(
        self,
        id: str,
        *,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.clients.getsubscriptions(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getsubscriptions(
            id, update_group_id=update_group_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data
