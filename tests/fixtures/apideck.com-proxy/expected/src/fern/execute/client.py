

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawExecuteClient, RawExecuteClient
from .types.patch_proxy_request_body import PatchProxyRequestBody
from .types.post_proxy_request_body import PostProxyRequestBody
from .types.put_proxy_request_body import PutProxyRequestBody


OMIT = typing.cast(typing.Any, ...)


class ExecuteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExecuteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExecuteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExecuteClient
        """
        return self._raw_client

    def get_proxy(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
            apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.execute.get_proxy()
        """
        _response = self._raw_client.get_proxy(request_options=request_options)
        return _response.data

    def post_proxy(
        self, *, request: PostProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PostProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Ok

        Examples
        --------
        from fern.execute import PostProxyRequestBodyZero

        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
            apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.execute.post_proxy(
            request=PostProxyRequestBodyZero(),
        )
        """
        _response = self._raw_client.post_proxy(request=request, request_options=request_options)
        return _response.data

    def put_proxy(
        self, *, request: PutProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PutProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Ok

        Examples
        --------
        from fern.execute import PutProxyRequestBodyZero

        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
            apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.execute.put_proxy(
            request=PutProxyRequestBodyZero(),
        )
        """
        _response = self._raw_client.put_proxy(request=request, request_options=request_options)
        return _response.data

    def delete_proxy(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
            apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.execute.delete_proxy()
        """
        _response = self._raw_client.delete_proxy(request_options=request_options)
        return _response.data

    def patch_proxy(
        self, *, request: PatchProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PatchProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Ok

        Examples
        --------
        from fern.execute import PatchProxyRequestBodyZero

        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
            apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.execute.patch_proxy(
            request=PatchProxyRequestBodyZero(),
        )
        """
        _response = self._raw_client.patch_proxy(request=request, request_options=request_options)
        return _response.data


class AsyncExecuteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExecuteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExecuteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExecuteClient
        """
        return self._raw_client

    async def get_proxy(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
            apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.execute.get_proxy()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy(request_options=request_options)
        return _response.data

    async def post_proxy(
        self, *, request: PostProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PostProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Ok

        Examples
        --------
        import asyncio

        from fern.execute import PostProxyRequestBodyZero

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
            apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.execute.post_proxy(
                request=PostProxyRequestBodyZero(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy(request=request, request_options=request_options)
        return _response.data

    async def put_proxy(
        self, *, request: PutProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PutProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Ok

        Examples
        --------
        import asyncio

        from fern.execute import PutProxyRequestBodyZero

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
            apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.execute.put_proxy(
                request=PutProxyRequestBodyZero(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_proxy(request=request, request_options=request_options)
        return _response.data

    async def delete_proxy(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
            apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.execute.delete_proxy()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_proxy(request_options=request_options)
        return _response.data

    async def patch_proxy(
        self, *, request: PatchProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PatchProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Ok

        Examples
        --------
        import asyncio

        from fern.execute import PatchProxyRequestBodyZero

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
            apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.execute.patch_proxy(
                request=PatchProxyRequestBodyZero(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_proxy(request=request, request_options=request_options)
        return _response.data
