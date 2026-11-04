

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.vsm_account_response import VsmAccountResponse
from .raw_client import AsyncRawViberServiceMessageClient, RawViberServiceMessageClient


class ViberServiceMessageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawViberServiceMessageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawViberServiceMessageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawViberServiceMessageClient
        """
        return self._raw_client

    def get_vsm_account(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VsmAccountResponse:
        """
        Parameters
        ----------
        external_id : str
            External id of the account you want to retrieve. In this case it will be your Viber Service Message ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VsmAccountResponse
            OK.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.viber_service_message.get_vsm_account(
            external_id="external_id",
        )
        """
        _response = self._raw_client.get_vsm_account(external_id, request_options=request_options)
        return _response.data


class AsyncViberServiceMessageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawViberServiceMessageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawViberServiceMessageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawViberServiceMessageClient
        """
        return self._raw_client

    async def get_vsm_account(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VsmAccountResponse:
        """
        Parameters
        ----------
        external_id : str
            External id of the account you want to retrieve. In this case it will be your Viber Service Message ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VsmAccountResponse
            OK.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.viber_service_message.get_vsm_account(
                external_id="external_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vsm_account(external_id, request_options=request_options)
        return _response.data
