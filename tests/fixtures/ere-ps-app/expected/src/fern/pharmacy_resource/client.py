

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bundle import Bundle
from .raw_client import AsyncRawPharmacyResourceClient, RawPharmacyResourceClient


class PharmacyResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPharmacyResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPharmacyResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPharmacyResourceClient
        """
        return self._raw_client

    def get_pharmacy_accept(
        self, *, token: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Bundle:
        """
        Parameters
        ----------
        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bundle
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pharmacy_resource.get_pharmacy_accept()
        """
        _response = self._raw_client.get_pharmacy_accept(token=token, request_options=request_options)
        return _response.data

    def get_pharmacy_task(
        self,
        *,
        egk_handle: typing.Optional[str] = None,
        smcb_handle: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Bundle:
        """
        Parameters
        ----------
        egk_handle : typing.Optional[str]

        smcb_handle : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bundle
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pharmacy_resource.get_pharmacy_task()
        """
        _response = self._raw_client.get_pharmacy_task(
            egk_handle=egk_handle, smcb_handle=smcb_handle, request_options=request_options
        )
        return _response.data


class AsyncPharmacyResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPharmacyResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPharmacyResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPharmacyResourceClient
        """
        return self._raw_client

    async def get_pharmacy_accept(
        self, *, token: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Bundle:
        """
        Parameters
        ----------
        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bundle
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pharmacy_resource.get_pharmacy_accept()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pharmacy_accept(token=token, request_options=request_options)
        return _response.data

    async def get_pharmacy_task(
        self,
        *,
        egk_handle: typing.Optional[str] = None,
        smcb_handle: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Bundle:
        """
        Parameters
        ----------
        egk_handle : typing.Optional[str]

        smcb_handle : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bundle
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pharmacy_resource.get_pharmacy_task()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pharmacy_task(
            egk_handle=egk_handle, smcb_handle=smcb_handle, request_options=request_options
        )
        return _response.data
