

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.scheduler_data import SchedulerData
from .raw_client import AsyncRawDynamicSchedulerClient, RawDynamicSchedulerClient


OMIT = typing.cast(typing.Any, ...)


class DynamicSchedulerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDynamicSchedulerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDynamicSchedulerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDynamicSchedulerClient
        """
        return self._raw_client

    def update_service_observation(
        self, node_uuid: str, *, is_disabled: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        node_uuid : str

        is_disabled : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_scheduler.update_service_observation(
            node_uuid="node_uuid",
            is_disabled=True,
        )
        """
        _response = self._raw_client.update_service_observation(
            node_uuid, is_disabled=is_disabled, request_options=request_options
        )
        return _response.data

    def delete_service_containers(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_scheduler.delete_service_containers(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.delete_service_containers(node_uuid, request_options=request_options)
        return _response.data

    def get_service_state(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchedulerData:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulerData
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_scheduler.get_service_state(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.get_service_state(node_uuid, request_options=request_options)
        return _response.data

    def save_service_state(self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_scheduler.save_service_state(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.save_service_state(node_uuid, request_options=request_options)
        return _response.data

    def push_service_outputs(self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_scheduler.push_service_outputs(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.push_service_outputs(node_uuid, request_options=request_options)
        return _response.data

    def delete_service_docker_resources(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_scheduler.delete_service_docker_resources(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.delete_service_docker_resources(node_uuid, request_options=request_options)
        return _response.data

    def free_reserved_disk_space(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_scheduler.free_reserved_disk_space(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.free_reserved_disk_space(node_uuid, request_options=request_options)
        return _response.data


class AsyncDynamicSchedulerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDynamicSchedulerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDynamicSchedulerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDynamicSchedulerClient
        """
        return self._raw_client

    async def update_service_observation(
        self, node_uuid: str, *, is_disabled: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        node_uuid : str

        is_disabled : bool

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
            await client.dynamic_scheduler.update_service_observation(
                node_uuid="node_uuid",
                is_disabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_service_observation(
            node_uuid, is_disabled=is_disabled, request_options=request_options
        )
        return _response.data

    async def delete_service_containers(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_scheduler.delete_service_containers(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_service_containers(node_uuid, request_options=request_options)
        return _response.data

    async def get_service_state(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchedulerData:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulerData
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_scheduler.get_service_state(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_state(node_uuid, request_options=request_options)
        return _response.data

    async def save_service_state(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_scheduler.save_service_state(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_service_state(node_uuid, request_options=request_options)
        return _response.data

    async def push_service_outputs(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_scheduler.push_service_outputs(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.push_service_outputs(node_uuid, request_options=request_options)
        return _response.data

    async def delete_service_docker_resources(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_scheduler.delete_service_docker_resources(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_service_docker_resources(node_uuid, request_options=request_options)
        return _response.data

    async def free_reserved_disk_space(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        node_uuid : str

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
            await client.dynamic_scheduler.free_reserved_disk_space(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.free_reserved_disk_space(node_uuid, request_options=request_options)
        return _response.data
