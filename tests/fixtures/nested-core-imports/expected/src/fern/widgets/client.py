

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWidgetsClient, RawWidgetsClient
from .types.update_widget_request_details import UpdateWidgetRequestDetails


OMIT = typing.cast(typing.Any, ...)


class WidgetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWidgetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWidgetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWidgetsClient
        """
        return self._raw_client

    def update_widget(
        self,
        widget_id: str,
        *,
        details: typing.Optional[UpdateWidgetRequestDetails] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        widget_id : str

        details : typing.Optional[UpdateWidgetRequestDetails]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.widgets.update_widget(
            widget_id="widget_id",
        )
        """
        _response = self._raw_client.update_widget(widget_id, details=details, request_options=request_options)
        return _response.data


class AsyncWidgetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWidgetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWidgetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWidgetsClient
        """
        return self._raw_client

    async def update_widget(
        self,
        widget_id: str,
        *,
        details: typing.Optional[UpdateWidgetRequestDetails] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        widget_id : str

        details : typing.Optional[UpdateWidgetRequestDetails]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.widgets.update_widget(
                widget_id="widget_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_widget(widget_id, details=details, request_options=request_options)
        return _response.data
