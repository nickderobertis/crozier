

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.provider import Provider
from ..types.provider_type import ProviderType
from .raw_client import AsyncRawProvidersClient, RawProvidersClient
from .types.list_providers_request_order import ListProvidersRequestOrder
from .types.list_providers_request_order_by import ListProvidersRequestOrderBy


OMIT = typing.cast(typing.Any, ...)


class ProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProvidersClient
        """
        return self._raw_client

    def list_providers(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListProvidersRequestOrder] = None,
        order_by: typing.Optional[ListProvidersRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        provider_type: typing.Optional[ProviderType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Provider]:
        """
        Get a list of all custom providers.

        Parameters
        ----------
        before : typing.Optional[str]
            Provider ID cursor for pagination. Returns providers that come before this provider ID in the specified sort order

        after : typing.Optional[str]
            Provider ID cursor for pagination. Returns providers that come after this provider ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of providers to return

        order : typing.Optional[ListProvidersRequestOrder]
            Sort order for providers by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListProvidersRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Filter providers by name

        provider_type : typing.Optional[ProviderType]
            Filter providers by type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Provider]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.providers.list_providers()
        """
        _response = self._raw_client.list_providers(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            name=name,
            provider_type=provider_type,
            request_options=request_options,
        )
        return _response.data

    def create_provider(
        self,
        *,
        name: str,
        provider_type: ProviderType,
        api_key: str,
        access_key: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        api_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
        """
        Create a new custom provider.

        Parameters
        ----------
        name : str
            The name of the provider.

        provider_type : ProviderType
            The type of the provider.

        api_key : str
            API key or secret key used for requests to the provider.

        access_key : typing.Optional[str]
            Access key used for requests to the provider.

        region : typing.Optional[str]
            Region used for requests to the provider.

        base_url : typing.Optional[str]
            Base URL used for requests to the provider.

        api_version : typing.Optional[str]
            API version used for requests to the provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        from fern import FernApi, ProviderType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.providers.create_provider(
            name="name",
            provider_type=ProviderType.ANTHROPIC,
            api_key="api_key",
        )
        """
        _response = self._raw_client.create_provider(
            name=name,
            provider_type=provider_type,
            api_key=api_key,
            access_key=access_key,
            region=region,
            base_url=base_url,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    def retrieve_provider(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Provider:
        """
        Get a provider by ID.

        Parameters
        ----------
        provider_id : str
            The ID of the provider in the format 'provider-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.providers.retrieve_provider(
            provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_provider(provider_id, request_options=request_options)
        return _response.data

    def delete_provider(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete an existing custom provider.

        Parameters
        ----------
        provider_id : str
            The ID of the provider in the format 'provider-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.providers.delete_provider(
            provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_provider(provider_id, request_options=request_options)
        return _response.data

    def modify_provider(
        self,
        provider_id: str,
        *,
        api_key: str,
        access_key: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        api_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
        """
        Update an existing custom provider.

        Parameters
        ----------
        provider_id : str
            The ID of the provider in the format 'provider-<uuid4>'

        api_key : str
            API key or secret key used for requests to the provider.

        access_key : typing.Optional[str]
            Access key used for requests to the provider.

        region : typing.Optional[str]
            Region used for requests to the provider.

        base_url : typing.Optional[str]
            Base URL used for requests to the provider.

        api_version : typing.Optional[str]
            API version used for requests to the provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.providers.modify_provider(
            provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
            api_key="api_key",
        )
        """
        _response = self._raw_client.modify_provider(
            provider_id,
            api_key=api_key,
            access_key=access_key,
            region=region,
            base_url=base_url,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    def check_provider(
        self,
        *,
        provider_type: ProviderType,
        api_key: str,
        access_key: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        api_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Verify the API key and additional parameters for a provider.

        Parameters
        ----------
        provider_type : ProviderType
            The type of the provider.

        api_key : str
            API key or secret key used for requests to the provider.

        access_key : typing.Optional[str]
            Access key used for requests to the provider.

        region : typing.Optional[str]
            Region used for requests to the provider.

        base_url : typing.Optional[str]
            Base URL used for requests to the provider.

        api_version : typing.Optional[str]
            API version used for requests to the provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, ProviderType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.providers.check_provider(
            provider_type=ProviderType.ANTHROPIC,
            api_key="api_key",
        )
        """
        _response = self._raw_client.check_provider(
            provider_type=provider_type,
            api_key=api_key,
            access_key=access_key,
            region=region,
            base_url=base_url,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    def check_existing_provider(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Verify the API key and additional parameters for an existing provider.

        Parameters
        ----------
        provider_id : str
            The ID of the provider in the format 'provider-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.providers.check_existing_provider(
            provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.check_existing_provider(provider_id, request_options=request_options)
        return _response.data

    def refresh_provider_models(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Provider:
        """
        Refresh models for a BYOK provider by querying the provider's API.
        Adds new models and removes ones no longer available.

        Parameters
        ----------
        provider_id : str
            The ID of the provider in the format 'provider-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.providers.refresh_provider_models(
            provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.refresh_provider_models(provider_id, request_options=request_options)
        return _response.data


class AsyncProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProvidersClient
        """
        return self._raw_client

    async def list_providers(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListProvidersRequestOrder] = None,
        order_by: typing.Optional[ListProvidersRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        provider_type: typing.Optional[ProviderType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Provider]:
        """
        Get a list of all custom providers.

        Parameters
        ----------
        before : typing.Optional[str]
            Provider ID cursor for pagination. Returns providers that come before this provider ID in the specified sort order

        after : typing.Optional[str]
            Provider ID cursor for pagination. Returns providers that come after this provider ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of providers to return

        order : typing.Optional[ListProvidersRequestOrder]
            Sort order for providers by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListProvidersRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Filter providers by name

        provider_type : typing.Optional[ProviderType]
            Filter providers by type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Provider]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.list_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_providers(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            name=name,
            provider_type=provider_type,
            request_options=request_options,
        )
        return _response.data

    async def create_provider(
        self,
        *,
        name: str,
        provider_type: ProviderType,
        api_key: str,
        access_key: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        api_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
        """
        Create a new custom provider.

        Parameters
        ----------
        name : str
            The name of the provider.

        provider_type : ProviderType
            The type of the provider.

        api_key : str
            API key or secret key used for requests to the provider.

        access_key : typing.Optional[str]
            Access key used for requests to the provider.

        region : typing.Optional[str]
            Region used for requests to the provider.

        base_url : typing.Optional[str]
            Base URL used for requests to the provider.

        api_version : typing.Optional[str]
            API version used for requests to the provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProviderType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.create_provider(
                name="name",
                provider_type=ProviderType.ANTHROPIC,
                api_key="api_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_provider(
            name=name,
            provider_type=provider_type,
            api_key=api_key,
            access_key=access_key,
            region=region,
            base_url=base_url,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_provider(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Provider:
        """
        Get a provider by ID.

        Parameters
        ----------
        provider_id : str
            The ID of the provider in the format 'provider-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.retrieve_provider(
                provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_provider(provider_id, request_options=request_options)
        return _response.data

    async def delete_provider(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete an existing custom provider.

        Parameters
        ----------
        provider_id : str
            The ID of the provider in the format 'provider-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.delete_provider(
                provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_provider(provider_id, request_options=request_options)
        return _response.data

    async def modify_provider(
        self,
        provider_id: str,
        *,
        api_key: str,
        access_key: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        api_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
        """
        Update an existing custom provider.

        Parameters
        ----------
        provider_id : str
            The ID of the provider in the format 'provider-<uuid4>'

        api_key : str
            API key or secret key used for requests to the provider.

        access_key : typing.Optional[str]
            Access key used for requests to the provider.

        region : typing.Optional[str]
            Region used for requests to the provider.

        base_url : typing.Optional[str]
            Base URL used for requests to the provider.

        api_version : typing.Optional[str]
            API version used for requests to the provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.modify_provider(
                provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
                api_key="api_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_provider(
            provider_id,
            api_key=api_key,
            access_key=access_key,
            region=region,
            base_url=base_url,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    async def check_provider(
        self,
        *,
        provider_type: ProviderType,
        api_key: str,
        access_key: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        api_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Verify the API key and additional parameters for a provider.

        Parameters
        ----------
        provider_type : ProviderType
            The type of the provider.

        api_key : str
            API key or secret key used for requests to the provider.

        access_key : typing.Optional[str]
            Access key used for requests to the provider.

        region : typing.Optional[str]
            Region used for requests to the provider.

        base_url : typing.Optional[str]
            Base URL used for requests to the provider.

        api_version : typing.Optional[str]
            API version used for requests to the provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProviderType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.check_provider(
                provider_type=ProviderType.ANTHROPIC,
                api_key="api_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_provider(
            provider_type=provider_type,
            api_key=api_key,
            access_key=access_key,
            region=region,
            base_url=base_url,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    async def check_existing_provider(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Verify the API key and additional parameters for an existing provider.

        Parameters
        ----------
        provider_id : str
            The ID of the provider in the format 'provider-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.check_existing_provider(
                provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_existing_provider(provider_id, request_options=request_options)
        return _response.data

    async def refresh_provider_models(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Provider:
        """
        Refresh models for a BYOK provider by querying the provider's API.
        Adds new models and removes ones no longer available.

        Parameters
        ----------
        provider_id : str
            The ID of the provider in the format 'provider-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.refresh_provider_models(
                provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_provider_models(provider_id, request_options=request_options)
        return _response.data
