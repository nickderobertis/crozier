

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_info_presentation import AppInfoPresentation
from .raw_client import AsyncRawMetaInformationClient, RawMetaInformationClient


class MetaInformationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetaInformationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetaInformationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetaInformationClient
        """
        return self._raw_client

    def application_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> AppInfoPresentation:
        """
        Retrieving version information about ID4i.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppInfoPresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.meta_information.application_info()
        """
        _response = self._raw_client.application_info(request_options=request_options)
        return _response.data


class AsyncMetaInformationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetaInformationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetaInformationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetaInformationClient
        """
        return self._raw_client

    async def application_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> AppInfoPresentation:
        """
        Retrieving version information about ID4i.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppInfoPresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.meta_information.application_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.application_info(request_options=request_options)
        return _response.data
