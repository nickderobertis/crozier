

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.component_list_element import ComponentListElement
from ..types.component_usages_in_scenario import ComponentUsagesInScenario
from .raw_client import AsyncRawComponentsClient, RawComponentsClient


class ComponentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawComponentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawComponentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawComponentsClient
        """
        return self._raw_client

    def get_api_components_id_usages(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ComponentUsagesInScenario]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ComponentUsagesInScenario]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.components.get_api_components_id_usages(
            id="id",
        )
        """
        _response = self._raw_client.get_api_components_id_usages(id, request_options=request_options)
        return _response.data

    def get_api_components(
        self,
        *,
        skip_usages: typing.Optional[bool] = None,
        skip_fragments: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ComponentListElement]:
        """
        Parameters
        ----------
        skip_usages : typing.Optional[bool]

        skip_fragments : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ComponentListElement]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.components.get_api_components()
        """
        _response = self._raw_client.get_api_components(
            skip_usages=skip_usages, skip_fragments=skip_fragments, request_options=request_options
        )
        return _response.data


class AsyncComponentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawComponentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawComponentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawComponentsClient
        """
        return self._raw_client

    async def get_api_components_id_usages(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ComponentUsagesInScenario]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ComponentUsagesInScenario]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.components.get_api_components_id_usages(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_components_id_usages(id, request_options=request_options)
        return _response.data

    async def get_api_components(
        self,
        *,
        skip_usages: typing.Optional[bool] = None,
        skip_fragments: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ComponentListElement]:
        """
        Parameters
        ----------
        skip_usages : typing.Optional[bool]

        skip_fragments : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ComponentListElement]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.components.get_api_components()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_components(
            skip_usages=skip_usages, skip_fragments=skip_fragments, request_options=request_options
        )
        return _response.data
