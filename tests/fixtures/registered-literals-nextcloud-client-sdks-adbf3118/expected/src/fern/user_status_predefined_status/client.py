

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_status_predefined_status_find_all200response import UserStatusPredefinedStatusFindAll200Response
from .raw_client import AsyncRawUserStatusPredefinedStatusClient, RawUserStatusPredefinedStatusClient


class UserStatusPredefinedStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserStatusPredefinedStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserStatusPredefinedStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserStatusPredefinedStatusClient
        """
        return self._raw_client

    def find_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusPredefinedStatusFindAll200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusPredefinedStatusFindAll200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_status_predefined_status.find_all()
        """
        _response = self._raw_client.find_all(request_options=request_options)
        return _response.data


class AsyncUserStatusPredefinedStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserStatusPredefinedStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserStatusPredefinedStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserStatusPredefinedStatusClient
        """
        return self._raw_client

    async def find_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusPredefinedStatusFindAll200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusPredefinedStatusFindAll200Response


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
            await client.user_status_predefined_status.find_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all(request_options=request_options)
        return _response.data
