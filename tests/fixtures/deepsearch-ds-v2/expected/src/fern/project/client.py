

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_server_fastapi_server_public_models_project_models_http_source import (
    ApiServerFastapiServerPublicModelsProjectModelsHttpSource,
)
from ..types.ccs_project import CcsProject
from ..types.cps_task import CpsTask
from ..types.data_flow import DataFlow
from ..types.default_values import DefaultValues
from ..types.file_source import FileSource
from ..types.image_urls_info import ImageUrlsInfo
from ..types.package import Package
from ..types.project_data_index_conversion_settings_input import ProjectDataIndexConversionSettingsInput
from ..types.task_context import TaskContext
from ..types.task_result import TaskResult
from .raw_client import AsyncRawProjectClient, RawProjectClient
from .types.get_project_integration_config_genai_response import GetProjectIntegrationConfigGenaiResponse
from .types.update_project_integration_config_genai_request_body import UpdateProjectIntegrationConfigGenaiRequestBody


OMIT = typing.cast(typing.Any, ...)


class ProjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectClient
        """
        return self._raw_client

    def get_project_default_values(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DefaultValues:
        """
        List project's default values.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DefaultValues
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.get_project_default_values(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.get_project_default_values(proj_key, request_options=request_options)
        return _response.data

    def update_project_default_values(
        self,
        proj_key: str,
        *,
        ccs_project: CcsProject,
        dataflow: typing.Optional[DataFlow] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Update project's default values.

        Parameters
        ----------
        proj_key : str

        ccs_project : CcsProject

        dataflow : typing.Optional[DataFlow]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import CcsProject, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.update_project_default_values(
            proj_key="proj_key",
            ccs_project=CcsProject(
                name="name",
                proj_key="proj_key",
                collection_name="collection_name",
            ),
        )
        """
        _response = self._raw_client.update_project_default_values(
            proj_key, ccs_project=ccs_project, dataflow=dataflow, request_options=request_options
        )
        return _response.data

    def get_project_integration_config_genai(
        self,
        proj_key: str,
        *,
        decode_secrets: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectIntegrationConfigGenaiResponse:
        """
        Get the GenAI config for a given project.

        Parameters
        ----------
        proj_key : str

        decode_secrets : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectIntegrationConfigGenaiResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.get_project_integration_config_genai(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.get_project_integration_config_genai(
            proj_key, decode_secrets=decode_secrets, request_options=request_options
        )
        return _response.data

    def update_project_integration_config_genai(
        self,
        proj_key: str,
        *,
        request: UpdateProjectIntegrationConfigGenaiRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the GenAI config for a given project.

        Parameters
        ----------
        proj_key : str

        request : UpdateProjectIntegrationConfigGenaiRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.project import UpdateProjectIntegrationConfigGenaiRequestBody_Bam

        from fern import FernApi, GenAibamConfig

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.update_project_integration_config_genai(
            proj_key="proj_key",
            request=UpdateProjectIntegrationConfigGenaiRequestBody_Bam(
                config=GenAibamConfig(
                    genai_api="GENAI_API",
                    genai_key="GENAI_KEY",
                ),
            ),
        )
        """
        _response = self._raw_client.update_project_integration_config_genai(
            proj_key, request=request, request_options=request_options
        )
        return _response.data

    def delete_project_integration_config_genai(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the GenAI config for a given project integration.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.delete_project_integration_config_genai(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.delete_project_integration_config_genai(proj_key, request_options=request_options)
        return _response.data

    def provision_project_packages(
        self,
        proj_key: str,
        *,
        packages: typing.Sequence[Package],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskContext:
        """
        Install packages on a project.

        Parameters
        ----------
        proj_key : str

        packages : typing.Sequence[Package]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskContext
            Successful Response

        Examples
        --------
        from fern import FernApi, Package

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.provision_project_packages(
            proj_key="proj_key",
            packages=[
                Package(
                    overrides={"key": "value"},
                    package_id="package_id",
                )
            ],
        )
        """
        _response = self._raw_client.provision_project_packages(
            proj_key, packages=packages, request_options=request_options
        )
        return _response.data

    def convert_document(
        self,
        proj_key: str,
        *,
        http_source: typing.Optional[ApiServerFastapiServerPublicModelsProjectModelsHttpSource] = OMIT,
        file_source: typing.Optional[FileSource] = OMIT,
        settings: typing.Optional[ProjectDataIndexConversionSettingsInput] = OMIT,
        image_urls: typing.Optional[ImageUrlsInfo] = OMIT,
        truncate_pages: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Convert a document directly with Docling.

        Parameters
        ----------
        proj_key : str

        http_source : typing.Optional[ApiServerFastapiServerPublicModelsProjectModelsHttpSource]

        file_source : typing.Optional[FileSource]

        settings : typing.Optional[ProjectDataIndexConversionSettingsInput]

        image_urls : typing.Optional[ImageUrlsInfo]

        truncate_pages : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CpsTask
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.convert_document(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.convert_document(
            proj_key,
            http_source=http_source,
            file_source=file_source,
            settings=settings,
            image_urls=image_urls,
            truncate_pages=truncate_pages,
            request_options=request_options,
        )
        return _response.data

    def get_convert_task(
        self,
        proj_key: str,
        task_id: str,
        *,
        wait: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskResult:
        """
        Check status of a Docling conversion task; return presign urls for MD and JSON file if finished conversion successfully.

        Parameters
        ----------
        proj_key : str

        task_id : str

        wait : typing.Optional[int]
            Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.get_convert_task(
            proj_key="proj_key",
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_convert_task(proj_key, task_id, wait=wait, request_options=request_options)
        return _response.data


class AsyncProjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectClient
        """
        return self._raw_client

    async def get_project_default_values(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DefaultValues:
        """
        List project's default values.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DefaultValues
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.get_project_default_values(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_default_values(proj_key, request_options=request_options)
        return _response.data

    async def update_project_default_values(
        self,
        proj_key: str,
        *,
        ccs_project: CcsProject,
        dataflow: typing.Optional[DataFlow] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Update project's default values.

        Parameters
        ----------
        proj_key : str

        ccs_project : CcsProject

        dataflow : typing.Optional[DataFlow]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CcsProject

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.update_project_default_values(
                proj_key="proj_key",
                ccs_project=CcsProject(
                    name="name",
                    proj_key="proj_key",
                    collection_name="collection_name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project_default_values(
            proj_key, ccs_project=ccs_project, dataflow=dataflow, request_options=request_options
        )
        return _response.data

    async def get_project_integration_config_genai(
        self,
        proj_key: str,
        *,
        decode_secrets: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectIntegrationConfigGenaiResponse:
        """
        Get the GenAI config for a given project.

        Parameters
        ----------
        proj_key : str

        decode_secrets : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectIntegrationConfigGenaiResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.get_project_integration_config_genai(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_integration_config_genai(
            proj_key, decode_secrets=decode_secrets, request_options=request_options
        )
        return _response.data

    async def update_project_integration_config_genai(
        self,
        proj_key: str,
        *,
        request: UpdateProjectIntegrationConfigGenaiRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the GenAI config for a given project.

        Parameters
        ----------
        proj_key : str

        request : UpdateProjectIntegrationConfigGenaiRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.project import UpdateProjectIntegrationConfigGenaiRequestBody_Bam

        from fern import AsyncFernApi, GenAibamConfig

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.update_project_integration_config_genai(
                proj_key="proj_key",
                request=UpdateProjectIntegrationConfigGenaiRequestBody_Bam(
                    config=GenAibamConfig(
                        genai_api="GENAI_API",
                        genai_key="GENAI_KEY",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project_integration_config_genai(
            proj_key, request=request, request_options=request_options
        )
        return _response.data

    async def delete_project_integration_config_genai(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the GenAI config for a given project integration.

        Parameters
        ----------
        proj_key : str

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.delete_project_integration_config_genai(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_integration_config_genai(
            proj_key, request_options=request_options
        )
        return _response.data

    async def provision_project_packages(
        self,
        proj_key: str,
        *,
        packages: typing.Sequence[Package],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskContext:
        """
        Install packages on a project.

        Parameters
        ----------
        proj_key : str

        packages : typing.Sequence[Package]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskContext
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Package

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.provision_project_packages(
                proj_key="proj_key",
                packages=[
                    Package(
                        overrides={"key": "value"},
                        package_id="package_id",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provision_project_packages(
            proj_key, packages=packages, request_options=request_options
        )
        return _response.data

    async def convert_document(
        self,
        proj_key: str,
        *,
        http_source: typing.Optional[ApiServerFastapiServerPublicModelsProjectModelsHttpSource] = OMIT,
        file_source: typing.Optional[FileSource] = OMIT,
        settings: typing.Optional[ProjectDataIndexConversionSettingsInput] = OMIT,
        image_urls: typing.Optional[ImageUrlsInfo] = OMIT,
        truncate_pages: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Convert a document directly with Docling.

        Parameters
        ----------
        proj_key : str

        http_source : typing.Optional[ApiServerFastapiServerPublicModelsProjectModelsHttpSource]

        file_source : typing.Optional[FileSource]

        settings : typing.Optional[ProjectDataIndexConversionSettingsInput]

        image_urls : typing.Optional[ImageUrlsInfo]

        truncate_pages : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CpsTask
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.convert_document(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.convert_document(
            proj_key,
            http_source=http_source,
            file_source=file_source,
            settings=settings,
            image_urls=image_urls,
            truncate_pages=truncate_pages,
            request_options=request_options,
        )
        return _response.data

    async def get_convert_task(
        self,
        proj_key: str,
        task_id: str,
        *,
        wait: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskResult:
        """
        Check status of a Docling conversion task; return presign urls for MD and JSON file if finished conversion successfully.

        Parameters
        ----------
        proj_key : str

        task_id : str

        wait : typing.Optional[int]
            Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.get_convert_task(
                proj_key="proj_key",
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_convert_task(
            proj_key, task_id, wait=wait, request_options=request_options
        )
        return _response.data
