

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.wa_account_response import WaAccountResponse
from .raw_client import AsyncRawWhatsAppClient, RawWhatsAppClient


class WhatsAppClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWhatsAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWhatsAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWhatsAppClient
        """
        return self._raw_client

    def get_wa_account(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WaAccountResponse:
        """
        Parameters
        ----------
        external_id : str
            External id of the account you want to retrieve. In this case it will be the WhatsApp number.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WaAccountResponse
            OK.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.whats_app.get_wa_account(
            external_id="external_id",
        )
        """
        _response = self._raw_client.get_wa_account(external_id, request_options=request_options)
        return _response.data


class AsyncWhatsAppClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWhatsAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWhatsAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWhatsAppClient
        """
        return self._raw_client

    async def get_wa_account(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WaAccountResponse:
        """
        Parameters
        ----------
        external_id : str
            External id of the account you want to retrieve. In this case it will be the WhatsApp number.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WaAccountResponse
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
            await client.whats_app.get_wa_account(
                external_id="external_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wa_account(external_id, request_options=request_options)
        return _response.data
