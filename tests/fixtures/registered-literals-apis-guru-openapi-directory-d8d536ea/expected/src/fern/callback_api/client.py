

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.callback_list_response import CallbackListResponse
from .raw_client import AsyncRawCallbackApiClient, RawCallbackApiClient
from .types.get_callbacks_request_status import GetCallbacksRequestStatus


class CallbackApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCallbackApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCallbackApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCallbackApiClient
        """
        return self._raw_client

    def get_callbacks(
        self,
        *,
        date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCallbacksRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CallbackListResponse:
        """
        Get list of callback types with count for a requested Date.

        Parameters
        ----------
        date : typing.Optional[dt.datetime]
            Date for which fetch the callback type list. By default, the date will be set to current date.

        status : typing.Optional[GetCallbacksRequestStatus]
            Status of the callbacks. Default status will fetch all callbacks.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CallbackListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.callback_api.get_callbacks()
        """
        _response = self._raw_client.get_callbacks(date=date, status=status, request_options=request_options)
        return _response.data


class AsyncCallbackApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCallbackApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCallbackApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCallbackApiClient
        """
        return self._raw_client

    async def get_callbacks(
        self,
        *,
        date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCallbacksRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CallbackListResponse:
        """
        Get list of callback types with count for a requested Date.

        Parameters
        ----------
        date : typing.Optional[dt.datetime]
            Date for which fetch the callback type list. By default, the date will be set to current date.

        status : typing.Optional[GetCallbacksRequestStatus]
            Status of the callbacks. Default status will fetch all callbacks.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CallbackListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.callback_api.get_callbacks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_callbacks(date=date, status=status, request_options=request_options)
        return _response.data
