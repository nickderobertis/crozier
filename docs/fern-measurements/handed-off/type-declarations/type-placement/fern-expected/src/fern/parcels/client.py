

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawParcelsClient, RawParcelsClient
from .types.list_parcels_request_carrier import ListParcelsRequestCarrier
from .types.list_parcels_request_label_style import ListParcelsRequestLabelStyle
from .types.list_parcels_request_priority import ListParcelsRequestPriority


class ParcelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawParcelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawParcelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawParcelsClient
        """
        return self._raw_client

    def list_parcels(
        self,
        *,
        priority: typing.Optional[ListParcelsRequestPriority] = None,
        carrier: typing.Optional[ListParcelsRequestCarrier] = None,
        label: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        label_style: typing.Optional[ListParcelsRequestLabelStyle] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        priority : typing.Optional[ListParcelsRequestPriority]
            Sorting priority.

        carrier : typing.Optional[ListParcelsRequestCarrier]
            Carrier to filter by.

        label : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One label or several to print.

        label_style : typing.Optional[ListParcelsRequestLabelStyle]
            How the labels are printed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The parcels

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.parcels.list_parcels()
        """
        _response = self._raw_client.list_parcels(
            priority=priority, carrier=carrier, label=label, label_style=label_style, request_options=request_options
        )
        return _response.data


class AsyncParcelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawParcelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawParcelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawParcelsClient
        """
        return self._raw_client

    async def list_parcels(
        self,
        *,
        priority: typing.Optional[ListParcelsRequestPriority] = None,
        carrier: typing.Optional[ListParcelsRequestCarrier] = None,
        label: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        label_style: typing.Optional[ListParcelsRequestLabelStyle] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        priority : typing.Optional[ListParcelsRequestPriority]
            Sorting priority.

        carrier : typing.Optional[ListParcelsRequestCarrier]
            Carrier to filter by.

        label : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One label or several to print.

        label_style : typing.Optional[ListParcelsRequestLabelStyle]
            How the labels are printed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The parcels

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.parcels.list_parcels()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_parcels(
            priority=priority, carrier=carrier, label=label, label_style=label_style, request_options=request_options
        )
        return _response.data
