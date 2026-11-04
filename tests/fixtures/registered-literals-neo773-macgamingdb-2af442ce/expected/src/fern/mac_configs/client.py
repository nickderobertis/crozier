

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMacConfigsClient, RawMacConfigsClient
from .types.review_get_mac_config_by_id_response import ReviewGetMacConfigByIdResponse
from .types.review_get_mac_configs_response_item import ReviewGetMacConfigsResponseItem


class MacConfigsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMacConfigsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMacConfigsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMacConfigsClient
        """
        return self._raw_client

    def review_get_mac_configs(
        self,
        *,
        search: typing.Optional[str] = None,
        selected_config_identifier: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ReviewGetMacConfigsResponseItem]:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        selected_config_identifier : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReviewGetMacConfigsResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mac_configs.review_get_mac_configs()
        """
        _response = self._raw_client.review_get_mac_configs(
            search=search, selected_config_identifier=selected_config_identifier, request_options=request_options
        )
        return _response.data

    def review_get_mac_config_by_id(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ReviewGetMacConfigByIdResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ReviewGetMacConfigByIdResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mac_configs.review_get_mac_config_by_id(
            identifier="identifier",
        )
        """
        _response = self._raw_client.review_get_mac_config_by_id(identifier, request_options=request_options)
        return _response.data


class AsyncMacConfigsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMacConfigsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMacConfigsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMacConfigsClient
        """
        return self._raw_client

    async def review_get_mac_configs(
        self,
        *,
        search: typing.Optional[str] = None,
        selected_config_identifier: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ReviewGetMacConfigsResponseItem]:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        selected_config_identifier : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReviewGetMacConfigsResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mac_configs.review_get_mac_configs()


        asyncio.run(main())
        """
        _response = await self._raw_client.review_get_mac_configs(
            search=search, selected_config_identifier=selected_config_identifier, request_options=request_options
        )
        return _response.data

    async def review_get_mac_config_by_id(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ReviewGetMacConfigByIdResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ReviewGetMacConfigByIdResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mac_configs.review_get_mac_config_by_id(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.review_get_mac_config_by_id(identifier, request_options=request_options)
        return _response.data
