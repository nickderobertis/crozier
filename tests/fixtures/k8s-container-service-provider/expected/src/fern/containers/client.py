

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.container import Container
from ..types.container_list import ContainerList
from ..types.container_spec import ContainerSpec
from ..types.container_status import ContainerStatus
from ..types.service_info import ServiceInfo
from .raw_client import AsyncRawContainersClient, RawContainersClient


OMIT = typing.cast(typing.Any, ...)


class ContainersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContainersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContainersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContainersClient
        """
        return self._raw_client

    def list_containers(
        self,
        *,
        max_page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContainerList:
        """
        Retrieve a list of containers with pagination support

        Parameters
        ----------
        max_page_size : typing.Optional[int]
            Maximum number of resources to return in a single page

        page_token : typing.Optional[str]
            Token indicating the starting point for the page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContainerList
            Successfully retrieved containers

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.containers.list_containers()
        """
        _response = self._raw_client.list_containers(
            max_page_size=max_page_size, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_container(
        self,
        *,
        spec: ContainerSpec,
        id: typing.Optional[str] = None,
        container_id: typing.Optional[str] = OMIT,
        path: typing.Optional[str] = OMIT,
        status: typing.Optional[ContainerStatus] = OMIT,
        service: typing.Optional[ServiceInfo] = OMIT,
        create_time: typing.Optional[dt.datetime] = OMIT,
        update_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Container:
        """
        Create a new container instance

        Parameters
        ----------
        spec : ContainerSpec

        id : typing.Optional[str]
            Optional client-specified ID for the container. If not provided,
            the server will generate an ID.

            Requirements (per AEP-122):
            - 1-63 characters long
            - Start with a lowercase letter or digit
            - Contain only lowercase letters, numbers, and hyphens
            - End with letter or number

        container_id : typing.Optional[str]
            Unique identifier for the container instance

        path : typing.Optional[str]
            Resource path identifier

        status : typing.Optional[ContainerStatus]

        service : typing.Optional[ServiceInfo]

        create_time : typing.Optional[dt.datetime]
            Timestamp when the container was created

        update_time : typing.Optional[dt.datetime]
            Timestamp when the container was last updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Container
            Container created successfully

        Examples
        --------
        from fern import (
            ContainerCpu,
            ContainerImage,
            ContainerMemory,
            ContainerMetadata,
            ContainerResources,
            ContainerSpec,
            ContainerSpecServiceType,
            FernApi,
        )

        client = FernApi()
        client.containers.create_container(
            id="my-nginx-container",
            spec=ContainerSpec(
                service_type=ContainerSpecServiceType.CONTAINER,
                metadata=ContainerMetadata(
                    name="name",
                ),
                image=ContainerImage(
                    reference="quay.io/myapp:v1.2",
                ),
                resources=ContainerResources(
                    cpu=ContainerCpu(
                        min=1,
                        max=1,
                    ),
                    memory=ContainerMemory(
                        min="min",
                        max="max",
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.create_container(
            spec=spec,
            id=id,
            container_id=container_id,
            path=path,
            status=status,
            service=service,
            create_time=create_time,
            update_time=update_time,
            request_options=request_options,
        )
        return _response.data

    def get_container(self, container_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Container:
        """
        Retrieve a specific container instance by ID

        Parameters
        ----------
        container_id : str
            Unique identifier for the container

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Container
            Container retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.containers.get_container(
            container_id="my-nginx-container",
        )
        """
        _response = self._raw_client.get_container(container_id, request_options=request_options)
        return _response.data

    def delete_container(self, container_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific container instance

        Parameters
        ----------
        container_id : str
            Unique identifier for the container

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.containers.delete_container(
            container_id="my-nginx-container",
        )
        """
        _response = self._raw_client.delete_container(container_id, request_options=request_options)
        return _response.data


class AsyncContainersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContainersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContainersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContainersClient
        """
        return self._raw_client

    async def list_containers(
        self,
        *,
        max_page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContainerList:
        """
        Retrieve a list of containers with pagination support

        Parameters
        ----------
        max_page_size : typing.Optional[int]
            Maximum number of resources to return in a single page

        page_token : typing.Optional[str]
            Token indicating the starting point for the page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContainerList
            Successfully retrieved containers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.containers.list_containers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_containers(
            max_page_size=max_page_size, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_container(
        self,
        *,
        spec: ContainerSpec,
        id: typing.Optional[str] = None,
        container_id: typing.Optional[str] = OMIT,
        path: typing.Optional[str] = OMIT,
        status: typing.Optional[ContainerStatus] = OMIT,
        service: typing.Optional[ServiceInfo] = OMIT,
        create_time: typing.Optional[dt.datetime] = OMIT,
        update_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Container:
        """
        Create a new container instance

        Parameters
        ----------
        spec : ContainerSpec

        id : typing.Optional[str]
            Optional client-specified ID for the container. If not provided,
            the server will generate an ID.

            Requirements (per AEP-122):
            - 1-63 characters long
            - Start with a lowercase letter or digit
            - Contain only lowercase letters, numbers, and hyphens
            - End with letter or number

        container_id : typing.Optional[str]
            Unique identifier for the container instance

        path : typing.Optional[str]
            Resource path identifier

        status : typing.Optional[ContainerStatus]

        service : typing.Optional[ServiceInfo]

        create_time : typing.Optional[dt.datetime]
            Timestamp when the container was created

        update_time : typing.Optional[dt.datetime]
            Timestamp when the container was last updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Container
            Container created successfully

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ContainerCpu,
            ContainerImage,
            ContainerMemory,
            ContainerMetadata,
            ContainerResources,
            ContainerSpec,
            ContainerSpecServiceType,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.containers.create_container(
                id="my-nginx-container",
                spec=ContainerSpec(
                    service_type=ContainerSpecServiceType.CONTAINER,
                    metadata=ContainerMetadata(
                        name="name",
                    ),
                    image=ContainerImage(
                        reference="quay.io/myapp:v1.2",
                    ),
                    resources=ContainerResources(
                        cpu=ContainerCpu(
                            min=1,
                            max=1,
                        ),
                        memory=ContainerMemory(
                            min="min",
                            max="max",
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_container(
            spec=spec,
            id=id,
            container_id=container_id,
            path=path,
            status=status,
            service=service,
            create_time=create_time,
            update_time=update_time,
            request_options=request_options,
        )
        return _response.data

    async def get_container(
        self, container_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Container:
        """
        Retrieve a specific container instance by ID

        Parameters
        ----------
        container_id : str
            Unique identifier for the container

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Container
            Container retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.containers.get_container(
                container_id="my-nginx-container",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_container(container_id, request_options=request_options)
        return _response.data

    async def delete_container(
        self, container_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a specific container instance

        Parameters
        ----------
        container_id : str
            Unique identifier for the container

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.containers.delete_container(
                container_id="my-nginx-container",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_container(container_id, request_options=request_options)
        return _response.data
