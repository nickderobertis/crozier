

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ocr_options import OcrOptions
from ..types.project_data_index_conversion_settings_output import ProjectDataIndexConversionSettingsOutput
from ..types.project_data_index_with_status import ProjectDataIndexWithStatus
from ..types.table_structure_options import TableStructureOptions
from ..types.token_response import TokenResponse
from .raw_client import AsyncRawDataIndicesClient, RawDataIndicesClient
from .types.create_project_data_index_request_body import CreateProjectDataIndexRequestBody
from .types.update_project_data_index_request_body import UpdateProjectDataIndexRequestBody


OMIT = typing.cast(typing.Any, ...)


class DataIndicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataIndicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataIndicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataIndicesClient
        """
        return self._raw_client

    def get_project_data_indices(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProjectDataIndexWithStatus]:
        """
        Get project data indices.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProjectDataIndexWithStatus]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_indices.get_project_data_indices(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.get_project_data_indices(proj_key, request_options=request_options)
        return _response.data

    def create_project_data_index(
        self,
        proj_key: str,
        *,
        request: CreateProjectDataIndexRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDataIndexWithStatus:
        """
        Create a project data index.

        Parameters
        ----------
        proj_key : str

        request : CreateProjectDataIndexRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDataIndexWithStatus
            Successful Response

        Examples
        --------
        from fern import (
            ElasticIndexSearchQueryOptions,
            FernApi,
            ProjectDataIndexView,
            ProjectSourceDataIndex,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_indices.create_project_data_index(
            proj_key="proj_key",
            request=ProjectDataIndexView(
                name="name",
                view_of=ProjectSourceDataIndex(
                    index_key="index_key",
                    query_options=ElasticIndexSearchQueryOptions(),
                    proj_key="proj_key",
                ),
            ),
        )
        """
        _response = self._raw_client.create_project_data_index(
            proj_key, request=request, request_options=request_options
        )
        return _response.data

    def get_project_data_index(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectDataIndexWithStatus:
        """
        Get project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDataIndexWithStatus
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_indices.get_project_data_index(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.get_project_data_index(proj_key, index_key, request_options=request_options)
        return _response.data

    def delete_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        confirmation_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Delete a project index data.

        Parameters
        ----------
        proj_key : str

        index_key : str

        confirmation_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_indices.delete_project_data_index(
            proj_key="proj_key",
            index_key="index_key",
            confirmation_token="confirmation_token",
        )
        """
        _response = self._raw_client.delete_project_data_index(
            proj_key, index_key, confirmation_token=confirmation_token, request_options=request_options
        )
        return _response.data

    def update_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        request: UpdateProjectDataIndexRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDataIndexWithStatus:
        """
        Update a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request : UpdateProjectDataIndexRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDataIndexWithStatus
            Successful Response

        Examples
        --------
        from fern import (
            ElasticIndexSearchQueryOptions,
            FernApi,
            ProjectDataIndexView,
            ProjectSourceDataIndex,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_indices.update_project_data_index(
            proj_key="proj_key",
            index_key="index_key",
            request=ProjectDataIndexView(
                name="name",
                view_of=ProjectSourceDataIndex(
                    index_key="index_key",
                    query_options=ElasticIndexSearchQueryOptions(),
                    proj_key="proj_key",
                ),
            ),
        )
        """
        _response = self._raw_client.update_project_data_index(
            proj_key, index_key, request=request, request_options=request_options
        )
        return _response.data

    def create_project_data_index_delete_token(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Get a token used to confirm the deletion of a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_indices.create_project_data_index_delete_token(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.create_project_data_index_delete_token(
            proj_key, index_key, request_options=request_options
        )
        return _response.data

    def get_project_data_index_conversion_settings(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ProjectDataIndexConversionSettingsOutput]:
        """
        Get project data index conversion settings.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProjectDataIndexConversionSettingsOutput]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_indices.get_project_data_index_conversion_settings(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.get_project_data_index_conversion_settings(
            proj_key, index_key, request_options=request_options
        )
        return _response.data

    def update_project_data_index_conversion_settings(
        self,
        proj_key: str,
        index_key: str,
        *,
        ocr: typing.Optional[OcrOptions] = OMIT,
        table_structure: typing.Optional[TableStructureOptions] = OMIT,
        generate_page_images: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[ProjectDataIndexConversionSettingsOutput]:
        """
        Update a project data index conversion settings.

        Parameters
        ----------
        proj_key : str

        index_key : str

        ocr : typing.Optional[OcrOptions]

        table_structure : typing.Optional[TableStructureOptions]

        generate_page_images : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProjectDataIndexConversionSettingsOutput]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_indices.update_project_data_index_conversion_settings(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.update_project_data_index_conversion_settings(
            proj_key,
            index_key,
            ocr=ocr,
            table_structure=table_structure,
            generate_page_images=generate_page_images,
            request_options=request_options,
        )
        return _response.data


class AsyncDataIndicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataIndicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataIndicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataIndicesClient
        """
        return self._raw_client

    async def get_project_data_indices(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProjectDataIndexWithStatus]:
        """
        Get project data indices.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProjectDataIndexWithStatus]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_indices.get_project_data_indices(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_indices(proj_key, request_options=request_options)
        return _response.data

    async def create_project_data_index(
        self,
        proj_key: str,
        *,
        request: CreateProjectDataIndexRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDataIndexWithStatus:
        """
        Create a project data index.

        Parameters
        ----------
        proj_key : str

        request : CreateProjectDataIndexRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDataIndexWithStatus
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ElasticIndexSearchQueryOptions,
            ProjectDataIndexView,
            ProjectSourceDataIndex,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_indices.create_project_data_index(
                proj_key="proj_key",
                request=ProjectDataIndexView(
                    name="name",
                    view_of=ProjectSourceDataIndex(
                        index_key="index_key",
                        query_options=ElasticIndexSearchQueryOptions(),
                        proj_key="proj_key",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project_data_index(
            proj_key, request=request, request_options=request_options
        )
        return _response.data

    async def get_project_data_index(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectDataIndexWithStatus:
        """
        Get project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDataIndexWithStatus
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_indices.get_project_data_index(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_index(proj_key, index_key, request_options=request_options)
        return _response.data

    async def delete_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        confirmation_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Delete a project index data.

        Parameters
        ----------
        proj_key : str

        index_key : str

        confirmation_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_indices.delete_project_data_index(
                proj_key="proj_key",
                index_key="index_key",
                confirmation_token="confirmation_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_data_index(
            proj_key, index_key, confirmation_token=confirmation_token, request_options=request_options
        )
        return _response.data

    async def update_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        request: UpdateProjectDataIndexRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDataIndexWithStatus:
        """
        Update a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request : UpdateProjectDataIndexRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDataIndexWithStatus
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ElasticIndexSearchQueryOptions,
            ProjectDataIndexView,
            ProjectSourceDataIndex,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_indices.update_project_data_index(
                proj_key="proj_key",
                index_key="index_key",
                request=ProjectDataIndexView(
                    name="name",
                    view_of=ProjectSourceDataIndex(
                        index_key="index_key",
                        query_options=ElasticIndexSearchQueryOptions(),
                        proj_key="proj_key",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project_data_index(
            proj_key, index_key, request=request, request_options=request_options
        )
        return _response.data

    async def create_project_data_index_delete_token(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Get a token used to confirm the deletion of a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_indices.create_project_data_index_delete_token(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project_data_index_delete_token(
            proj_key, index_key, request_options=request_options
        )
        return _response.data

    async def get_project_data_index_conversion_settings(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ProjectDataIndexConversionSettingsOutput]:
        """
        Get project data index conversion settings.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProjectDataIndexConversionSettingsOutput]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_indices.get_project_data_index_conversion_settings(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_index_conversion_settings(
            proj_key, index_key, request_options=request_options
        )
        return _response.data

    async def update_project_data_index_conversion_settings(
        self,
        proj_key: str,
        index_key: str,
        *,
        ocr: typing.Optional[OcrOptions] = OMIT,
        table_structure: typing.Optional[TableStructureOptions] = OMIT,
        generate_page_images: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[ProjectDataIndexConversionSettingsOutput]:
        """
        Update a project data index conversion settings.

        Parameters
        ----------
        proj_key : str

        index_key : str

        ocr : typing.Optional[OcrOptions]

        table_structure : typing.Optional[TableStructureOptions]

        generate_page_images : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProjectDataIndexConversionSettingsOutput]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_indices.update_project_data_index_conversion_settings(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project_data_index_conversion_settings(
            proj_key,
            index_key,
            ocr=ocr,
            table_structure=table_structure,
            generate_page_images=generate_page_images,
            request_options=request_options,
        )
        return _response.data
