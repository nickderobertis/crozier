

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.any import Any
from ..types.empty import Empty
from ..types.otoroshi_models_api_key import OtoroshiModelsApiKey
from ..types.otoroshi_models_service_descriptor import OtoroshiModelsServiceDescriptor
from ..types.otoroshi_models_service_group import OtoroshiModelsServiceGroup
from ..types.otoroshi_tcp_tcp_service import OtoroshiTcpTcpService
from ..types.unknown import Unknown
from .raw_client import AsyncRawTemplatesClient, RawTemplatesClient


OMIT = typing.cast(typing.Any, ...)


class TemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTemplatesClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.templates.otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_initiate_service_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.templates.otoroshi_controllers_adminapi_templates_controller_initiate_service_templates()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_service_templates(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.templates.otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.templates.otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates()
        """
        _response = (
            self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates(
                request_options=request_options
            )
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_initiate_resources(
        self, *, request: Unknown, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        request : Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.templates.otoroshi_controllers_adminapi_templates_controller_initiate_resources(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_resources(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_create_from_template_templates(
        self, entity: str, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> Any:
        """
        Parameters
        ----------
        entity : str
            the entity parameter

        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Any
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.templates.otoroshi_controllers_adminapi_templates_controller_create_from_template_templates(
            entity="entity",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_create_from_template_templates(
            entity, request=request, request_options=request_options
        )
        return _response.data


class AsyncTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTemplatesClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.templates.otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_initiate_service_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.templates.otoroshi_controllers_adminapi_templates_controller_initiate_service_templates()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_service_templates(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.templates.otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.templates.otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_initiate_resources(
        self, *, request: Unknown, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        request : Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.templates.otoroshi_controllers_adminapi_templates_controller_initiate_resources(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_resources(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_create_from_template_templates(
        self, entity: str, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> Any:
        """
        Parameters
        ----------
        entity : str
            the entity parameter

        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Any
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.templates.otoroshi_controllers_adminapi_templates_controller_create_from_template_templates(
                entity="entity",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_templates_controller_create_from_template_templates(
                entity, request=request, request_options=request_options
            )
        )
        return _response.data
