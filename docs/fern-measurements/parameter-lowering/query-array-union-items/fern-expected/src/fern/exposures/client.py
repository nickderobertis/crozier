

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawExposuresClient, RawExposuresClient
from .types.list_exposures_request_filters_item import ListExposuresRequestFiltersItem
from .types.list_exposures_request_gains_item import ListExposuresRequestGainsItem


class ExposuresClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExposuresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExposuresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExposuresClient
        """
        return self._raw_client

    def list_exposures(
        self,
        *,
        filters: typing.Optional[
            typing.Union[ListExposuresRequestFiltersItem, typing.Sequence[ListExposuresRequestFiltersItem]]
        ] = None,
        gains: typing.Optional[
            typing.Union[ListExposuresRequestGainsItem, typing.Sequence[ListExposuresRequestGainsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        filters : typing.Optional[typing.Union[ListExposuresRequestFiltersItem, typing.Sequence[ListExposuresRequestFiltersItem]]]

        gains : typing.Optional[typing.Union[ListExposuresRequestGainsItem, typing.Sequence[ListExposuresRequestGainsItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Exposures taken with the given settings.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.exposures.list_exposures(
            gains=[1],
        )
        """
        _response = self._raw_client.list_exposures(filters=filters, gains=gains, request_options=request_options)
        return _response.data


class AsyncExposuresClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExposuresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExposuresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExposuresClient
        """
        return self._raw_client

    async def list_exposures(
        self,
        *,
        filters: typing.Optional[
            typing.Union[ListExposuresRequestFiltersItem, typing.Sequence[ListExposuresRequestFiltersItem]]
        ] = None,
        gains: typing.Optional[
            typing.Union[ListExposuresRequestGainsItem, typing.Sequence[ListExposuresRequestGainsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        filters : typing.Optional[typing.Union[ListExposuresRequestFiltersItem, typing.Sequence[ListExposuresRequestFiltersItem]]]

        gains : typing.Optional[typing.Union[ListExposuresRequestGainsItem, typing.Sequence[ListExposuresRequestGainsItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Exposures taken with the given settings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.exposures.list_exposures(
                gains=[1],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_exposures(filters=filters, gains=gains, request_options=request_options)
        return _response.data
