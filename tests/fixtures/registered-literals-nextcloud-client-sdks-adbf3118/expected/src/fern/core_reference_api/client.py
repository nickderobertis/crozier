

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_reference_api_get_providers_info200response import CoreReferenceApiGetProvidersInfo200Response
from ..types.core_reference_api_resolve_one200response import CoreReferenceApiResolveOne200Response
from ..types.core_reference_api_touch_provider200response import CoreReferenceApiTouchProvider200Response
from .raw_client import AsyncRawCoreReferenceApiClient, RawCoreReferenceApiClient


class CoreReferenceApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreReferenceApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreReferenceApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreReferenceApiClient
        """
        return self._raw_client

    def resolve_one(
        self, *, reference: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreReferenceApiResolveOne200Response:
        """
        Parameters
        ----------
        reference : str
            Reference to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiResolveOne200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_reference_api.resolve_one(
            reference="reference",
        )
        """
        _response = self._raw_client.resolve_one(reference=reference, request_options=request_options)
        return _response.data

    def resolve(
        self,
        *,
        references: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreReferenceApiResolveOne200Response:
        """
        Parameters
        ----------
        references : str
            References to resolve

        limit : typing.Optional[int]
            Maximum amount of references to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiResolveOne200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_reference_api.resolve(
            references="references",
        )
        """
        _response = self._raw_client.resolve(references=references, limit=limit, request_options=request_options)
        return _response.data

    def extract(
        self,
        *,
        text: str,
        resolve: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreReferenceApiResolveOne200Response:
        """
        Parameters
        ----------
        text : str
            Text to extract from

        resolve : typing.Optional[int]
            Resolve the references

        limit : typing.Optional[int]
            Maximum amount of references to extract

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiResolveOne200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_reference_api.extract(
            text="text",
        )
        """
        _response = self._raw_client.extract(text=text, resolve=resolve, limit=limit, request_options=request_options)
        return _response.data

    def get_providers_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreReferenceApiGetProvidersInfo200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiGetProvidersInfo200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_reference_api.get_providers_info()
        """
        _response = self._raw_client.get_providers_info(request_options=request_options)
        return _response.data

    def touch_provider(
        self,
        provider_id: str,
        *,
        timestamp: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreReferenceApiTouchProvider200Response:
        """
        Parameters
        ----------
        provider_id : str
            ID of the provider

        timestamp : typing.Optional[int]
            Timestamp of the last usage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiTouchProvider200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_reference_api.touch_provider(
            provider_id="providerId",
        )
        """
        _response = self._raw_client.touch_provider(provider_id, timestamp=timestamp, request_options=request_options)
        return _response.data


class AsyncCoreReferenceApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreReferenceApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreReferenceApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreReferenceApiClient
        """
        return self._raw_client

    async def resolve_one(
        self, *, reference: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreReferenceApiResolveOne200Response:
        """
        Parameters
        ----------
        reference : str
            Reference to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiResolveOne200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_reference_api.resolve_one(
                reference="reference",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_one(reference=reference, request_options=request_options)
        return _response.data

    async def resolve(
        self,
        *,
        references: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreReferenceApiResolveOne200Response:
        """
        Parameters
        ----------
        references : str
            References to resolve

        limit : typing.Optional[int]
            Maximum amount of references to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiResolveOne200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_reference_api.resolve(
                references="references",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve(references=references, limit=limit, request_options=request_options)
        return _response.data

    async def extract(
        self,
        *,
        text: str,
        resolve: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreReferenceApiResolveOne200Response:
        """
        Parameters
        ----------
        text : str
            Text to extract from

        resolve : typing.Optional[int]
            Resolve the references

        limit : typing.Optional[int]
            Maximum amount of references to extract

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiResolveOne200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_reference_api.extract(
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.extract(
            text=text, resolve=resolve, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_providers_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreReferenceApiGetProvidersInfo200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiGetProvidersInfo200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_reference_api.get_providers_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_providers_info(request_options=request_options)
        return _response.data

    async def touch_provider(
        self,
        provider_id: str,
        *,
        timestamp: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreReferenceApiTouchProvider200Response:
        """
        Parameters
        ----------
        provider_id : str
            ID of the provider

        timestamp : typing.Optional[int]
            Timestamp of the last usage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiTouchProvider200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_reference_api.touch_provider(
                provider_id="providerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.touch_provider(
            provider_id, timestamp=timestamp, request_options=request_options
        )
        return _response.data
