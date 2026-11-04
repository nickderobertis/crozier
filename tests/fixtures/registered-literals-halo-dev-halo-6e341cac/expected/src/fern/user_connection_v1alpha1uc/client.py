

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_connection import UserConnection
from .raw_client import AsyncRawUserConnectionV1Alpha1UcClient, RawUserConnectionV1Alpha1UcClient


class UserConnectionV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserConnectionV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserConnectionV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserConnectionV1Alpha1UcClient
        """
        return self._raw_client

    def disconnect_my_connection(
        self, register_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserConnection]:
        """
        Disconnect my connection from a third-party platform.

        Parameters
        ----------
        register_id : str
            The registration ID of the third-party platform.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserConnection]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_connection_v1alpha1uc.disconnect_my_connection(
            register_id="registerId",
        )
        """
        _response = self._raw_client.disconnect_my_connection(register_id, request_options=request_options)
        return _response.data


class AsyncUserConnectionV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserConnectionV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserConnectionV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserConnectionV1Alpha1UcClient
        """
        return self._raw_client

    async def disconnect_my_connection(
        self, register_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserConnection]:
        """
        Disconnect my connection from a third-party platform.

        Parameters
        ----------
        register_id : str
            The registration ID of the third-party platform.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserConnection]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_connection_v1alpha1uc.disconnect_my_connection(
                register_id="registerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disconnect_my_connection(register_id, request_options=request_options)
        return _response.data
