

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1alpha1config_resource_create_response import V1Alpha1ConfigResourceCreateResponse
from ..types.v1alpha1config_resource_read_response import V1Alpha1ConfigResourceReadResponse
from ..types.v1alpha1config_resource_spec import V1Alpha1ConfigResourceSpec
from ..types.v1alpha1config_resource_update_response import V1Alpha1ConfigResourceUpdateResponse
from ..types.v1alpha1resource_metadata import V1Alpha1ResourceMetadata
from .raw_client import AsyncRawConfigsClient, RawConfigsClient
from .types.create_config_request_body import CreateConfigRequestBody


OMIT = typing.cast(typing.Any, ...)


class ConfigsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConfigsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConfigsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConfigsClient
        """
        return self._raw_client

    def list_configs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Alpha1ConfigResourceReadResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Alpha1ConfigResourceReadResponse]
            List of Configs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.configs.list_configs()
        """
        _response = self._raw_client.list_configs(request_options=request_options)
        return _response.data

    def create_config(
        self, *, request: CreateConfigRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1ConfigResourceCreateResponse:
        """
        Parameters
        ----------
        request : CreateConfigRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1ConfigResourceCreateResponse
            Created Config

        Examples
        --------
        from fern import (
            FernApi,
            V1Alpha1ConfigResourceCreateRequest,
            V1Alpha1ConfigResourceSpec,
            V1Alpha1ResourceMetadata,
        )

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.configs.create_config(
            request=V1Alpha1ConfigResourceCreateRequest(
                metadata=V1Alpha1ResourceMetadata(
                    name="name",
                ),
                spec=V1Alpha1ConfigResourceSpec(
                    data={"key": "value"},
                ),
            ),
        )
        """
        _response = self._raw_client.create_config(request=request, request_options=request_options)
        return _response.data

    def get_config(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1ConfigResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1ConfigResourceReadResponse
            Config

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.configs.get_config(
            identifier="identifier",
        )
        """
        _response = self._raw_client.get_config(identifier, request_options=request_options)
        return _response.data

    def update_config(
        self,
        identifier: str,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1ConfigResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1ConfigResourceUpdateResponse:
        """
        Parameters
        ----------
        identifier : str

        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1ConfigResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1ConfigResourceUpdateResponse
            Updated Config

        Examples
        --------
        from fern import FernApi, V1Alpha1ConfigResourceSpec, V1Alpha1ResourceMetadata

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.configs.update_config(
            identifier="identifier",
            metadata=V1Alpha1ResourceMetadata(
                name="name",
            ),
            spec=V1Alpha1ConfigResourceSpec(
                data={"key": "value"},
            ),
        )
        """
        _response = self._raw_client.update_config(
            identifier, metadata=metadata, spec=spec, kind=kind, request_options=request_options
        )
        return _response.data

    def delete_config(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1ConfigResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1ConfigResourceReadResponse
            Deleted Config

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.configs.delete_config(
            identifier="identifier",
        )
        """
        _response = self._raw_client.delete_config(identifier, request_options=request_options)
        return _response.data


class AsyncConfigsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConfigsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConfigsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConfigsClient
        """
        return self._raw_client

    async def list_configs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Alpha1ConfigResourceReadResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Alpha1ConfigResourceReadResponse]
            List of Configs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.configs.list_configs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_configs(request_options=request_options)
        return _response.data

    async def create_config(
        self, *, request: CreateConfigRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1ConfigResourceCreateResponse:
        """
        Parameters
        ----------
        request : CreateConfigRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1ConfigResourceCreateResponse
            Created Config

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            V1Alpha1ConfigResourceCreateRequest,
            V1Alpha1ConfigResourceSpec,
            V1Alpha1ResourceMetadata,
        )

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.configs.create_config(
                request=V1Alpha1ConfigResourceCreateRequest(
                    metadata=V1Alpha1ResourceMetadata(
                        name="name",
                    ),
                    spec=V1Alpha1ConfigResourceSpec(
                        data={"key": "value"},
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_config(request=request, request_options=request_options)
        return _response.data

    async def get_config(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1ConfigResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1ConfigResourceReadResponse
            Config

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.configs.get_config(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_config(identifier, request_options=request_options)
        return _response.data

    async def update_config(
        self,
        identifier: str,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1ConfigResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1ConfigResourceUpdateResponse:
        """
        Parameters
        ----------
        identifier : str

        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1ConfigResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1ConfigResourceUpdateResponse
            Updated Config

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            V1Alpha1ConfigResourceSpec,
            V1Alpha1ResourceMetadata,
        )

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.configs.update_config(
                identifier="identifier",
                metadata=V1Alpha1ResourceMetadata(
                    name="name",
                ),
                spec=V1Alpha1ConfigResourceSpec(
                    data={"key": "value"},
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_config(
            identifier, metadata=metadata, spec=spec, kind=kind, request_options=request_options
        )
        return _response.data

    async def delete_config(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1ConfigResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1ConfigResourceReadResponse
            Deleted Config

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.configs.delete_config(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_config(identifier, request_options=request_options)
        return _response.data
