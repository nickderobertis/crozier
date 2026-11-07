

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pool import Pool
from ..types.prebuild_environment_options import PrebuildEnvironmentOptions
from ..types.prebuild_template_info_result import PrebuildTemplateInfoResult
from ..types.secret_data_body import SecretDataBody
from ..types.storage_type import StorageType
from .raw_client import AsyncRawPrebuildsClient, RawPrebuildsClient


OMIT = typing.cast(typing.Any, ...)


class PrebuildsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPrebuildsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPrebuildsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPrebuildsClient
        """
        return self._raw_client

    def post_api_v1geneva_actions_prebuilds_pools_createorupdatesettings(
        self,
        *,
        branch_name: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        pools: typing.Optional[typing.Sequence[Pool]] = OMIT,
        repo_id: typing.Optional[str] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        subscription: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        branch_name : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        pools : typing.Optional[typing.Sequence[Pool]]

        repo_id : typing.Optional[str]

        storage_type : typing.Optional[StorageType]

        subscription : typing.Optional[str]

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
        )
        client.prebuilds.post_api_v1geneva_actions_prebuilds_pools_createorupdatesettings()
        """
        _response = self._raw_client.post_api_v1geneva_actions_prebuilds_pools_createorupdatesettings(
            branch_name=branch_name,
            dev_container_path=dev_container_path,
            pools=pools,
            repo_id=repo_id,
            storage_type=storage_type,
            subscription=subscription,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1geneva_actions_prebuilds_pools_delete(
        self,
        *,
        branch_name: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        pools: typing.Optional[typing.Sequence[Pool]] = OMIT,
        repo_id: typing.Optional[str] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        subscription: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        branch_name : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        pools : typing.Optional[typing.Sequence[Pool]]

        repo_id : typing.Optional[str]

        storage_type : typing.Optional[StorageType]

        subscription : typing.Optional[str]

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
        )
        client.prebuilds.post_api_v1geneva_actions_prebuilds_pools_delete()
        """
        _response = self._raw_client.post_api_v1geneva_actions_prebuilds_pools_delete(
            branch_name=branch_name,
            dev_container_path=dev_container_path,
            pools=pools,
            repo_id=repo_id,
            storage_type=storage_type,
            subscription=subscription,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1prebuilds_pools_pool_id_instances(
        self,
        pool_id: str,
        *,
        environment_options: typing.Optional[PrebuildEnvironmentOptions] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        pool_id : str

        environment_options : typing.Optional[PrebuildEnvironmentOptions]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

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
        )
        client.prebuilds.post_api_v1prebuilds_pools_pool_id_instances(
            pool_id="poolId",
        )
        """
        _response = self._raw_client.post_api_v1prebuilds_pools_pool_id_instances(
            pool_id, environment_options=environment_options, secrets=secrets, request_options=request_options
        )
        return _response.data

    def put_api_v1prebuilds_pools_pool_id_instances(
        self,
        pool_id: str,
        *,
        environment_options: typing.Optional[PrebuildEnvironmentOptions] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        pool_id : str

        environment_options : typing.Optional[PrebuildEnvironmentOptions]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

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
        )
        client.prebuilds.put_api_v1prebuilds_pools_pool_id_instances(
            pool_id="poolId",
        )
        """
        _response = self._raw_client.put_api_v1prebuilds_pools_pool_id_instances(
            pool_id, environment_options=environment_options, secrets=secrets, request_options=request_options
        )
        return _response.data

    def get_template_info_route(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PrebuildTemplateInfoResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrebuildTemplateInfoResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prebuilds.get_template_info_route(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.get_template_info_route(environment_id, request_options=request_options)
        return _response.data


class AsyncPrebuildsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPrebuildsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPrebuildsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPrebuildsClient
        """
        return self._raw_client

    async def post_api_v1geneva_actions_prebuilds_pools_createorupdatesettings(
        self,
        *,
        branch_name: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        pools: typing.Optional[typing.Sequence[Pool]] = OMIT,
        repo_id: typing.Optional[str] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        subscription: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        branch_name : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        pools : typing.Optional[typing.Sequence[Pool]]

        repo_id : typing.Optional[str]

        storage_type : typing.Optional[StorageType]

        subscription : typing.Optional[str]

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
        )


        async def main() -> None:
            await client.prebuilds.post_api_v1geneva_actions_prebuilds_pools_createorupdatesettings()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_prebuilds_pools_createorupdatesettings(
            branch_name=branch_name,
            dev_container_path=dev_container_path,
            pools=pools,
            repo_id=repo_id,
            storage_type=storage_type,
            subscription=subscription,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1geneva_actions_prebuilds_pools_delete(
        self,
        *,
        branch_name: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        pools: typing.Optional[typing.Sequence[Pool]] = OMIT,
        repo_id: typing.Optional[str] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        subscription: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        branch_name : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        pools : typing.Optional[typing.Sequence[Pool]]

        repo_id : typing.Optional[str]

        storage_type : typing.Optional[StorageType]

        subscription : typing.Optional[str]

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
        )


        async def main() -> None:
            await client.prebuilds.post_api_v1geneva_actions_prebuilds_pools_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_prebuilds_pools_delete(
            branch_name=branch_name,
            dev_container_path=dev_container_path,
            pools=pools,
            repo_id=repo_id,
            storage_type=storage_type,
            subscription=subscription,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1prebuilds_pools_pool_id_instances(
        self,
        pool_id: str,
        *,
        environment_options: typing.Optional[PrebuildEnvironmentOptions] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        pool_id : str

        environment_options : typing.Optional[PrebuildEnvironmentOptions]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

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
        )


        async def main() -> None:
            await client.prebuilds.post_api_v1prebuilds_pools_pool_id_instances(
                pool_id="poolId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1prebuilds_pools_pool_id_instances(
            pool_id, environment_options=environment_options, secrets=secrets, request_options=request_options
        )
        return _response.data

    async def put_api_v1prebuilds_pools_pool_id_instances(
        self,
        pool_id: str,
        *,
        environment_options: typing.Optional[PrebuildEnvironmentOptions] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        pool_id : str

        environment_options : typing.Optional[PrebuildEnvironmentOptions]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

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
        )


        async def main() -> None:
            await client.prebuilds.put_api_v1prebuilds_pools_pool_id_instances(
                pool_id="poolId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1prebuilds_pools_pool_id_instances(
            pool_id, environment_options=environment_options, secrets=secrets, request_options=request_options
        )
        return _response.data

    async def get_template_info_route(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PrebuildTemplateInfoResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrebuildTemplateInfoResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prebuilds.get_template_info_route(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_template_info_route(environment_id, request_options=request_options)
        return _response.data
