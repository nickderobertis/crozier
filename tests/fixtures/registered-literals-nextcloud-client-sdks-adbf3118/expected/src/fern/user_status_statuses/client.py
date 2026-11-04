

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_status_statuses_find200response import UserStatusStatusesFind200Response
from ..types.user_status_statuses_find_all200response import UserStatusStatusesFindAll200Response
from .raw_client import AsyncRawUserStatusStatusesClient, RawUserStatusStatusesClient


class UserStatusStatusesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserStatusStatusesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserStatusStatusesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserStatusStatusesClient
        """
        return self._raw_client

    def find_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserStatusStatusesFindAll200Response:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of statuses to find

        offset : typing.Optional[int]
            Offset for finding statuses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusStatusesFindAll200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_status_statuses.find_all()
        """
        _response = self._raw_client.find_all(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def find(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusStatusesFind200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusStatusesFind200Response
            The status was found successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_status_statuses.find(
            user_id="userId",
        )
        """
        _response = self._raw_client.find(user_id, request_options=request_options)
        return _response.data


class AsyncUserStatusStatusesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserStatusStatusesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserStatusStatusesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserStatusStatusesClient
        """
        return self._raw_client

    async def find_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserStatusStatusesFindAll200Response:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of statuses to find

        offset : typing.Optional[int]
            Offset for finding statuses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusStatusesFindAll200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_status_statuses.find_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    async def find(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusStatusesFind200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusStatusesFind200Response
            The status was found successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_status_statuses.find(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find(user_id, request_options=request_options)
        return _response.data
