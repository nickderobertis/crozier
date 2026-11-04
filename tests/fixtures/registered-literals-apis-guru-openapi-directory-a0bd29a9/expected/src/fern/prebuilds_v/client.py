

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_template_result import CreateTemplateResult
from ..types.experimental_features_body import ExperimentalFeaturesBody
from ..types.prebuild_readiness_result import PrebuildReadinessResult
from ..types.prebuild_template_info import PrebuildTemplateInfo
from ..types.seed_info_body import SeedInfoBody
from ..types.storage_type import StorageType
from .raw_client import AsyncRawPrebuildsVClient, RawPrebuildsVClient


OMIT = typing.cast(typing.Any, ...)


class PrebuildsVClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPrebuildsVClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPrebuildsVClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPrebuildsVClient
        """
        return self._raw_client

    def post_api_v2prebuilds_delete(
        self,
        *,
        branch_name: str,
        repo_id: int,
        dev_container_path: typing.Optional[str] = OMIT,
        prebuild_configuration_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        branch_name : str

        repo_id : int

        dev_container_path : typing.Optional[str]

        prebuild_configuration_id : typing.Optional[int]

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
        client.prebuilds_v.post_api_v2prebuilds_delete(
            branch_name="branchName",
            repo_id=1000000,
        )
        """
        _response = self._raw_client.post_api_v2prebuilds_delete(
            branch_name=branch_name,
            repo_id=repo_id,
            dev_container_path=dev_container_path,
            prebuild_configuration_id=prebuild_configuration_id,
            request_options=request_options,
        )
        return _response.data

    def delete_api_v2prebuilds_repository_repo_id_branch_branch_name(
        self, repo_id: int, branch_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        repo_id : int

        branch_name : str

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
        client.prebuilds_v.delete_api_v2prebuilds_repository_repo_id_branch_branch_name(
            repo_id=1000000,
            branch_name="branchName",
        )
        """
        _response = self._raw_client.delete_api_v2prebuilds_repository_repo_id_branch_branch_name(
            repo_id, branch_name, request_options=request_options
        )
        return _response.data

    def post_api_v2prebuilds_templates(
        self,
        *,
        friendly_name: str,
        dev_container_path: typing.Optional[str] = OMIT,
        experimental_features: typing.Optional[ExperimentalFeaturesBody] = OMIT,
        features: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        git_hub_prebuild_instance_endpoint: typing.Optional[str] = OMIT,
        git_hub_prebuild_template_endpoint: typing.Optional[str] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        seed: typing.Optional[SeedInfoBody] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        template_info: typing.Optional[PrebuildTemplateInfo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTemplateResult:
        """
        Parameters
        ----------
        friendly_name : str

        dev_container_path : typing.Optional[str]

        experimental_features : typing.Optional[ExperimentalFeaturesBody]

        features : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        git_hub_prebuild_instance_endpoint : typing.Optional[str]

        git_hub_prebuild_template_endpoint : typing.Optional[str]

        plan_id : typing.Optional[str]

        seed : typing.Optional[SeedInfoBody]

        storage_type : typing.Optional[StorageType]

        template_info : typing.Optional[PrebuildTemplateInfo]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTemplateResult
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prebuilds_v.post_api_v2prebuilds_templates(
            friendly_name="friendlyName",
        )
        """
        _response = self._raw_client.post_api_v2prebuilds_templates(
            friendly_name=friendly_name,
            dev_container_path=dev_container_path,
            experimental_features=experimental_features,
            features=features,
            git_hub_prebuild_instance_endpoint=git_hub_prebuild_instance_endpoint,
            git_hub_prebuild_template_endpoint=git_hub_prebuild_template_endpoint,
            plan_id=plan_id,
            seed=seed,
            storage_type=storage_type,
            template_info=template_info,
            request_options=request_options,
        )
        return _response.data

    def get_prebuild_readiness_skus_route(
        self,
        repo_id: str,
        branch_name: str,
        prebuild_hash: str,
        location: str,
        dev_container_path: str,
        *,
        storage_type: typing.Optional[StorageType] = None,
        fast_path_enabled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrebuildReadinessResult:
        """
        Parameters
        ----------
        repo_id : str

        branch_name : str

        prebuild_hash : str

        location : str

        dev_container_path : str

        storage_type : typing.Optional[StorageType]

        fast_path_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrebuildReadinessResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prebuilds_v.get_prebuild_readiness_skus_route(
            repo_id="repoId",
            branch_name="branchName",
            prebuild_hash="prebuildHash",
            location="location",
            dev_container_path="devContainerPath",
        )
        """
        _response = self._raw_client.get_prebuild_readiness_skus_route(
            repo_id,
            branch_name,
            prebuild_hash,
            location,
            dev_container_path,
            storage_type=storage_type,
            fast_path_enabled=fast_path_enabled,
            request_options=request_options,
        )
        return _response.data

    def post_api_v2prebuilds_templates_updatemaxversions(
        self,
        *,
        branch_name: str,
        max_prebuild_template_versions: int,
        repo_id: int,
        dev_container_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        branch_name : str

        max_prebuild_template_versions : int

        repo_id : int

        dev_container_path : typing.Optional[str]

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
        client.prebuilds_v.post_api_v2prebuilds_templates_updatemaxversions(
            branch_name="branchName",
            max_prebuild_template_versions=1,
            repo_id=1000000,
        )
        """
        _response = self._raw_client.post_api_v2prebuilds_templates_updatemaxversions(
            branch_name=branch_name,
            max_prebuild_template_versions=max_prebuild_template_versions,
            repo_id=repo_id,
            dev_container_path=dev_container_path,
            request_options=request_options,
        )
        return _response.data

    def post_api_v2prebuilds_templates_template_id_updatestatus(
        self, template_id: str, *, is_success: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        template_id : str

        is_success : bool

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
        client.prebuilds_v.post_api_v2prebuilds_templates_template_id_updatestatus(
            template_id="templateId",
            is_success=True,
        )
        """
        _response = self._raw_client.post_api_v2prebuilds_templates_template_id_updatestatus(
            template_id, is_success=is_success, request_options=request_options
        )
        return _response.data


class AsyncPrebuildsVClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPrebuildsVClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPrebuildsVClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPrebuildsVClient
        """
        return self._raw_client

    async def post_api_v2prebuilds_delete(
        self,
        *,
        branch_name: str,
        repo_id: int,
        dev_container_path: typing.Optional[str] = OMIT,
        prebuild_configuration_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        branch_name : str

        repo_id : int

        dev_container_path : typing.Optional[str]

        prebuild_configuration_id : typing.Optional[int]

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
            await client.prebuilds_v.post_api_v2prebuilds_delete(
                branch_name="branchName",
                repo_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v2prebuilds_delete(
            branch_name=branch_name,
            repo_id=repo_id,
            dev_container_path=dev_container_path,
            prebuild_configuration_id=prebuild_configuration_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_v2prebuilds_repository_repo_id_branch_branch_name(
        self, repo_id: int, branch_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        repo_id : int

        branch_name : str

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
            await client.prebuilds_v.delete_api_v2prebuilds_repository_repo_id_branch_branch_name(
                repo_id=1000000,
                branch_name="branchName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v2prebuilds_repository_repo_id_branch_branch_name(
            repo_id, branch_name, request_options=request_options
        )
        return _response.data

    async def post_api_v2prebuilds_templates(
        self,
        *,
        friendly_name: str,
        dev_container_path: typing.Optional[str] = OMIT,
        experimental_features: typing.Optional[ExperimentalFeaturesBody] = OMIT,
        features: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        git_hub_prebuild_instance_endpoint: typing.Optional[str] = OMIT,
        git_hub_prebuild_template_endpoint: typing.Optional[str] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        seed: typing.Optional[SeedInfoBody] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        template_info: typing.Optional[PrebuildTemplateInfo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTemplateResult:
        """
        Parameters
        ----------
        friendly_name : str

        dev_container_path : typing.Optional[str]

        experimental_features : typing.Optional[ExperimentalFeaturesBody]

        features : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        git_hub_prebuild_instance_endpoint : typing.Optional[str]

        git_hub_prebuild_template_endpoint : typing.Optional[str]

        plan_id : typing.Optional[str]

        seed : typing.Optional[SeedInfoBody]

        storage_type : typing.Optional[StorageType]

        template_info : typing.Optional[PrebuildTemplateInfo]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTemplateResult
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prebuilds_v.post_api_v2prebuilds_templates(
                friendly_name="friendlyName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v2prebuilds_templates(
            friendly_name=friendly_name,
            dev_container_path=dev_container_path,
            experimental_features=experimental_features,
            features=features,
            git_hub_prebuild_instance_endpoint=git_hub_prebuild_instance_endpoint,
            git_hub_prebuild_template_endpoint=git_hub_prebuild_template_endpoint,
            plan_id=plan_id,
            seed=seed,
            storage_type=storage_type,
            template_info=template_info,
            request_options=request_options,
        )
        return _response.data

    async def get_prebuild_readiness_skus_route(
        self,
        repo_id: str,
        branch_name: str,
        prebuild_hash: str,
        location: str,
        dev_container_path: str,
        *,
        storage_type: typing.Optional[StorageType] = None,
        fast_path_enabled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrebuildReadinessResult:
        """
        Parameters
        ----------
        repo_id : str

        branch_name : str

        prebuild_hash : str

        location : str

        dev_container_path : str

        storage_type : typing.Optional[StorageType]

        fast_path_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrebuildReadinessResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prebuilds_v.get_prebuild_readiness_skus_route(
                repo_id="repoId",
                branch_name="branchName",
                prebuild_hash="prebuildHash",
                location="location",
                dev_container_path="devContainerPath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prebuild_readiness_skus_route(
            repo_id,
            branch_name,
            prebuild_hash,
            location,
            dev_container_path,
            storage_type=storage_type,
            fast_path_enabled=fast_path_enabled,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v2prebuilds_templates_updatemaxversions(
        self,
        *,
        branch_name: str,
        max_prebuild_template_versions: int,
        repo_id: int,
        dev_container_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        branch_name : str

        max_prebuild_template_versions : int

        repo_id : int

        dev_container_path : typing.Optional[str]

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
            await client.prebuilds_v.post_api_v2prebuilds_templates_updatemaxversions(
                branch_name="branchName",
                max_prebuild_template_versions=1,
                repo_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v2prebuilds_templates_updatemaxversions(
            branch_name=branch_name,
            max_prebuild_template_versions=max_prebuild_template_versions,
            repo_id=repo_id,
            dev_container_path=dev_container_path,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v2prebuilds_templates_template_id_updatestatus(
        self, template_id: str, *, is_success: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        template_id : str

        is_success : bool

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
            await client.prebuilds_v.post_api_v2prebuilds_templates_template_id_updatestatus(
                template_id="templateId",
                is_success=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v2prebuilds_templates_template_id_updatestatus(
            template_id, is_success=is_success, request_options=request_options
        )
        return _response.data
