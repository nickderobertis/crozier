

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.change_pin_response import ChangePinResponse
from ..types.get_pin_status_response import GetPinStatusResponse
from ..types.unblock_pin_response import UnblockPinResponse
from ..types.verify_pin_response import VerifyPinResponse
from .raw_client import AsyncRawCardResourceClient, RawCardResourceClient


OMIT = typing.cast(typing.Any, ...)


class CardResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCardResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCardResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCardResourceClient
        """
        return self._raw_client

    def post_card_change_pin(
        self,
        *,
        card_handle: typing.Optional[str] = OMIT,
        pin_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChangePinResponse:
        """
        Parameters
        ----------
        card_handle : typing.Optional[str]

        pin_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChangePinResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.card_resource.post_card_change_pin()
        """
        _response = self._raw_client.post_card_change_pin(
            card_handle=card_handle, pin_type=pin_type, request_options=request_options
        )
        return _response.data

    def get_card_pin_status(
        self,
        *,
        card_handle: typing.Optional[str] = None,
        pin_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPinStatusResponse:
        """
        Parameters
        ----------
        card_handle : typing.Optional[str]

        pin_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPinStatusResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.card_resource.get_card_pin_status()
        """
        _response = self._raw_client.get_card_pin_status(
            card_handle=card_handle, pin_type=pin_type, request_options=request_options
        )
        return _response.data

    def post_card_unblock_pin(self, *, request_options: typing.Optional[RequestOptions] = None) -> UnblockPinResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnblockPinResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.card_resource.post_card_unblock_pin()
        """
        _response = self._raw_client.post_card_unblock_pin(request_options=request_options)
        return _response.data

    def post_card_verify_pin(self, *, request_options: typing.Optional[RequestOptions] = None) -> VerifyPinResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyPinResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.card_resource.post_card_verify_pin()
        """
        _response = self._raw_client.post_card_verify_pin(request_options=request_options)
        return _response.data


class AsyncCardResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCardResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCardResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCardResourceClient
        """
        return self._raw_client

    async def post_card_change_pin(
        self,
        *,
        card_handle: typing.Optional[str] = OMIT,
        pin_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChangePinResponse:
        """
        Parameters
        ----------
        card_handle : typing.Optional[str]

        pin_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChangePinResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.card_resource.post_card_change_pin()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_card_change_pin(
            card_handle=card_handle, pin_type=pin_type, request_options=request_options
        )
        return _response.data

    async def get_card_pin_status(
        self,
        *,
        card_handle: typing.Optional[str] = None,
        pin_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPinStatusResponse:
        """
        Parameters
        ----------
        card_handle : typing.Optional[str]

        pin_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPinStatusResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.card_resource.get_card_pin_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_card_pin_status(
            card_handle=card_handle, pin_type=pin_type, request_options=request_options
        )
        return _response.data

    async def post_card_unblock_pin(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UnblockPinResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnblockPinResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.card_resource.post_card_unblock_pin()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_card_unblock_pin(request_options=request_options)
        return _response.data

    async def post_card_verify_pin(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyPinResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyPinResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.card_resource.post_card_verify_pin()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_card_verify_pin(request_options=request_options)
        return _response.data
