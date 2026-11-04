

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.instance_out import InstanceOut
from .raw_client import AsyncRawInstancesClient, RawInstancesClient
from .types.deploy_request_engine import DeployRequestEngine
from .types.deploy_request_gpu_selection import DeployRequestGpuSelection
from .types.deploy_request_profile import DeployRequestProfile


OMIT = typing.cast(typing.Any, ...)


class InstancesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInstancesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInstancesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInstancesClient
        """
        return self._raw_client

    def list_instances(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[InstanceOut]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstanceOut]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.instances.list_instances()
        """
        _response = self._raw_client.list_instances(request_options=request_options)
        return _response.data

    def deploy(
        self,
        *,
        model_id: str,
        cluster_id: str,
        engine: DeployRequestEngine,
        profile: DeployRequestProfile,
        replicas: typing.Optional[int] = OMIT,
        gpu_selection: typing.Optional[DeployRequestGpuSelection] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[InstanceOut]:
        """
        Parameters
        ----------
        model_id : str

        cluster_id : str

        engine : DeployRequestEngine

        profile : DeployRequestProfile

        replicas : typing.Optional[int]

        gpu_selection : typing.Optional[DeployRequestGpuSelection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstanceOut]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.instances.deploy(
            model_id="model_id",
            cluster_id="cluster_id",
            engine="vllm",
            profile="latency",
        )
        """
        _response = self._raw_client.deploy(
            model_id=model_id,
            cluster_id=cluster_id,
            engine=engine,
            profile=profile,
            replicas=replicas,
            gpu_selection=gpu_selection,
            request_options=request_options,
        )
        return _response.data

    def stop_instance(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InstanceOut:
        """
        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstanceOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.instances.stop_instance(
            instance_id="instance_id",
        )
        """
        _response = self._raw_client.stop_instance(instance_id, request_options=request_options)
        return _response.data

    def restart_instance(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InstanceOut:
        """
        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstanceOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.instances.restart_instance(
            instance_id="instance_id",
        )
        """
        _response = self._raw_client.restart_instance(instance_id, request_options=request_options)
        return _response.data

    def delete_instance(self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.instances.delete_instance(
            instance_id="instance_id",
        )
        """
        _response = self._raw_client.delete_instance(instance_id, request_options=request_options)
        return _response.data


class AsyncInstancesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInstancesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInstancesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInstancesClient
        """
        return self._raw_client

    async def list_instances(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstanceOut]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstanceOut]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.instances.list_instances()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_instances(request_options=request_options)
        return _response.data

    async def deploy(
        self,
        *,
        model_id: str,
        cluster_id: str,
        engine: DeployRequestEngine,
        profile: DeployRequestProfile,
        replicas: typing.Optional[int] = OMIT,
        gpu_selection: typing.Optional[DeployRequestGpuSelection] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[InstanceOut]:
        """
        Parameters
        ----------
        model_id : str

        cluster_id : str

        engine : DeployRequestEngine

        profile : DeployRequestProfile

        replicas : typing.Optional[int]

        gpu_selection : typing.Optional[DeployRequestGpuSelection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstanceOut]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.instances.deploy(
                model_id="model_id",
                cluster_id="cluster_id",
                engine="vllm",
                profile="latency",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deploy(
            model_id=model_id,
            cluster_id=cluster_id,
            engine=engine,
            profile=profile,
            replicas=replicas,
            gpu_selection=gpu_selection,
            request_options=request_options,
        )
        return _response.data

    async def stop_instance(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InstanceOut:
        """
        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstanceOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.instances.stop_instance(
                instance_id="instance_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_instance(instance_id, request_options=request_options)
        return _response.data

    async def restart_instance(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InstanceOut:
        """
        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstanceOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.instances.restart_instance(
                instance_id="instance_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restart_instance(instance_id, request_options=request_options)
        return _response.data

    async def delete_instance(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.instances.delete_instance(
                instance_id="instance_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_instance(instance_id, request_options=request_options)
        return _response.data
