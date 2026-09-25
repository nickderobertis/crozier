

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_server_fastapi_server_public_models_data_indices_upload_models_http_source import (
    ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource,
)
from ..types.attachment_upload_data import AttachmentUploadData
from ..types.cps_task import CpsTask
from ..types.document_meta import DocumentMeta
from ..types.s3document_source import S3DocumentSource
from ..types.target_conversion_parameters import TargetConversionParameters
from .raw_client import AsyncRawDataIndicesUploadClient, RawDataIndicesUploadClient
from .types.convert_documents_request_body_conversion_settings import ConvertDocumentsRequestBodyConversionSettings
from .types.convert_documents_request_body_without_operations_item import (
    ConvertDocumentsRequestBodyWithoutOperationsItem,
)
from .types.convert_upload_documents_request_body_conversion_settings import (
    ConvertUploadDocumentsRequestBodyConversionSettings,
)
from .types.data_index_upload_file_source_conversion_settings import DataIndexUploadFileSourceConversionSettings
from .types.data_index_upload_file_source_urls import DataIndexUploadFileSourceUrls
from .types.upload_elastic_request_body_with_operations_item import UploadElasticRequestBodyWithOperationsItem


OMIT = typing.cast(typing.Any, ...)


class DataIndicesUploadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataIndicesUploadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataIndicesUploadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataIndicesUploadClient
        """
        return self._raw_client

    def upload_project_data_index_file(
        self, proj_key: str, index_key: str, *, file_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CpsTask:
        """
        Upload a file to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : str

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
        client.data_indices_upload.upload_project_data_index_file(
            proj_key="proj_key",
            index_key="index_key",
            file_url="file_url",
        )
        """
        _response = self._raw_client.upload_project_data_index_file(
            proj_key, index_key, file_url=file_url, request_options=request_options
        )
        return _response.data

    def upload_register_project_documents(
        self,
        proj_key: str,
        index_key: str,
        *,
        file_url: typing.Optional[typing.Sequence[str]] = OMIT,
        http_source: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
        ] = OMIT,
        s3source: typing.Optional[S3DocumentSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Upload and register documents to be converted later.

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : typing.Optional[typing.Sequence[str]]
            List of File's URL to be converted and uploaded to the data index.

        http_source : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]]
            List of Internal File's URLs to be converted and uploaded to the data index.

        s3source : typing.Optional[S3DocumentSource]
            Coordinates to object store to get files to convert. Can specify which files with object keys.

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
        client.data_indices_upload.upload_register_project_documents(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.upload_register_project_documents(
            proj_key,
            index_key,
            file_url=file_url,
            http_source=http_source,
            s3source=s3source,
            request_options=request_options,
        )
        return _response.data

    def load_project_data_index_files_elastic(
        self,
        proj_key: str,
        index_key: str,
        *,
        document_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        with_operations: typing.Optional[typing.Sequence[UploadElasticRequestBodyWithOperationsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Load file(s) in a project data index to elastic.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hashes : typing.Optional[typing.Sequence[str]]
            List of document hashes to be used as filter.

        with_operations : typing.Optional[typing.Sequence[UploadElasticRequestBodyWithOperationsItem]]
            List of Operation Status documents don't have to be used as filter.

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
        client.data_indices_upload.load_project_data_index_files_elastic(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.load_project_data_index_files_elastic(
            proj_key,
            index_key,
            document_hashes=document_hashes,
            with_operations=with_operations,
            request_options=request_options,
        )
        return _response.data

    def ccs_convert_file_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        conversion_settings: typing.Optional[ConvertDocumentsRequestBodyConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        document_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        without_operations: typing.Optional[typing.Sequence[ConvertDocumentsRequestBodyWithoutOperationsItem]] = OMIT,
        upload_to_elastic: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Convert files via CCS previously registered and in a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        conversion_settings : typing.Optional[ConvertDocumentsRequestBodyConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

        document_hashes : typing.Optional[typing.Sequence[str]]
            List of document hashes to be used as filter.

        without_operations : typing.Optional[typing.Sequence[ConvertDocumentsRequestBodyWithoutOperationsItem]]
            List of Operation Status documents don't have to be used as filter.

        upload_to_elastic : typing.Optional[bool]

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
        client.data_indices_upload.ccs_convert_file_project_data_index(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.ccs_convert_file_project_data_index(
            proj_key,
            index_key,
            conversion_settings=conversion_settings,
            target_settings=target_settings,
            document_hashes=document_hashes,
            without_operations=without_operations,
            upload_to_elastic=upload_to_elastic,
            request_options=request_options,
        )
        return _response.data

    def ccs_convert_upload_file_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        file_url: typing.Optional[typing.Sequence[str]] = OMIT,
        http_source: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
        ] = OMIT,
        s3source: typing.Optional[S3DocumentSource] = OMIT,
        upload_to_elastic: typing.Optional[bool] = OMIT,
        meta: typing.Optional[DocumentMeta] = OMIT,
        conversion_settings: typing.Optional[ConvertUploadDocumentsRequestBodyConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Convert files via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema).

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : typing.Optional[typing.Sequence[str]]
            List of File's URL to be converted and uploaded to the data index.

        http_source : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]]
            List of Internal File's URLs to be converted and uploaded to the data index.

        s3source : typing.Optional[S3DocumentSource]
            Coordinates to object store to get files to convert. Can specify which files with object keys.

        upload_to_elastic : typing.Optional[bool]

        meta : typing.Optional[DocumentMeta]

        conversion_settings : typing.Optional[ConvertUploadDocumentsRequestBodyConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

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
        client.data_indices_upload.ccs_convert_upload_file_project_data_index(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.ccs_convert_upload_file_project_data_index(
            proj_key,
            index_key,
            file_url=file_url,
            http_source=http_source,
            s3source=s3source,
            upload_to_elastic=upload_to_elastic,
            meta=meta,
            conversion_settings=conversion_settings,
            target_settings=target_settings,
            request_options=request_options,
        )
        return _response.data

    def html_print_convert_upload(
        self,
        proj_key: str,
        index_key: str,
        *,
        urls: DataIndexUploadFileSourceUrls,
        conversion_settings: typing.Optional[DataIndexUploadFileSourceConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Convert a list of HTML pages to PDF, convert them via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema).

        Parameters
        ----------
        proj_key : str

        index_key : str

        urls : DataIndexUploadFileSourceUrls
            List of URLs to be printed to PDF, converted and uploaded to the data index.

        conversion_settings : typing.Optional[DataIndexUploadFileSourceConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

        headers : typing.Optional[typing.Dict[str, typing.Any]]

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
        client.data_indices_upload.html_print_convert_upload(
            proj_key="proj_key",
            index_key="index_key",
            urls="urls",
        )
        """
        _response = self._raw_client.html_print_convert_upload(
            proj_key,
            index_key,
            urls=urls,
            conversion_settings=conversion_settings,
            target_settings=target_settings,
            headers=headers,
            request_options=request_options,
        )
        return _response.data

    def get_attachment_upload_data(
        self,
        proj_key: str,
        index_key: str,
        index_item_id: str,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AttachmentUploadData:
        """
        Get url and path to upload an attachment to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        index_item_id : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentUploadData
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_indices_upload.get_attachment_upload_data(
            proj_key="proj_key",
            index_key="index_key",
            index_item_id="index_item_id",
            filename="filename",
        )
        """
        _response = self._raw_client.get_attachment_upload_data(
            proj_key, index_key, index_item_id, filename, request_options=request_options
        )
        return _response.data

    def register_attachment(
        self,
        proj_key: str,
        index_key: str,
        index_item_id: str,
        *,
        attachment_path: str,
        attachment_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Notify upload completion of an attachment to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        index_item_id : str

        attachment_path : str

        attachment_key : typing.Optional[str]

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
        client.data_indices_upload.register_attachment(
            proj_key="proj_key",
            index_key="index_key",
            index_item_id="index_item_id",
            attachment_path="attachment_path",
        )
        """
        _response = self._raw_client.register_attachment(
            proj_key,
            index_key,
            index_item_id,
            attachment_path=attachment_path,
            attachment_key=attachment_key,
            request_options=request_options,
        )
        return _response.data


class AsyncDataIndicesUploadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataIndicesUploadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataIndicesUploadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataIndicesUploadClient
        """
        return self._raw_client

    async def upload_project_data_index_file(
        self, proj_key: str, index_key: str, *, file_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CpsTask:
        """
        Upload a file to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : str

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
            await client.data_indices_upload.upload_project_data_index_file(
                proj_key="proj_key",
                index_key="index_key",
                file_url="file_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_project_data_index_file(
            proj_key, index_key, file_url=file_url, request_options=request_options
        )
        return _response.data

    async def upload_register_project_documents(
        self,
        proj_key: str,
        index_key: str,
        *,
        file_url: typing.Optional[typing.Sequence[str]] = OMIT,
        http_source: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
        ] = OMIT,
        s3source: typing.Optional[S3DocumentSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Upload and register documents to be converted later.

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : typing.Optional[typing.Sequence[str]]
            List of File's URL to be converted and uploaded to the data index.

        http_source : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]]
            List of Internal File's URLs to be converted and uploaded to the data index.

        s3source : typing.Optional[S3DocumentSource]
            Coordinates to object store to get files to convert. Can specify which files with object keys.

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
            await client.data_indices_upload.upload_register_project_documents(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_register_project_documents(
            proj_key,
            index_key,
            file_url=file_url,
            http_source=http_source,
            s3source=s3source,
            request_options=request_options,
        )
        return _response.data

    async def load_project_data_index_files_elastic(
        self,
        proj_key: str,
        index_key: str,
        *,
        document_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        with_operations: typing.Optional[typing.Sequence[UploadElasticRequestBodyWithOperationsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Load file(s) in a project data index to elastic.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hashes : typing.Optional[typing.Sequence[str]]
            List of document hashes to be used as filter.

        with_operations : typing.Optional[typing.Sequence[UploadElasticRequestBodyWithOperationsItem]]
            List of Operation Status documents don't have to be used as filter.

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
            await client.data_indices_upload.load_project_data_index_files_elastic(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.load_project_data_index_files_elastic(
            proj_key,
            index_key,
            document_hashes=document_hashes,
            with_operations=with_operations,
            request_options=request_options,
        )
        return _response.data

    async def ccs_convert_file_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        conversion_settings: typing.Optional[ConvertDocumentsRequestBodyConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        document_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        without_operations: typing.Optional[typing.Sequence[ConvertDocumentsRequestBodyWithoutOperationsItem]] = OMIT,
        upload_to_elastic: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Convert files via CCS previously registered and in a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        conversion_settings : typing.Optional[ConvertDocumentsRequestBodyConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

        document_hashes : typing.Optional[typing.Sequence[str]]
            List of document hashes to be used as filter.

        without_operations : typing.Optional[typing.Sequence[ConvertDocumentsRequestBodyWithoutOperationsItem]]
            List of Operation Status documents don't have to be used as filter.

        upload_to_elastic : typing.Optional[bool]

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
            await client.data_indices_upload.ccs_convert_file_project_data_index(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ccs_convert_file_project_data_index(
            proj_key,
            index_key,
            conversion_settings=conversion_settings,
            target_settings=target_settings,
            document_hashes=document_hashes,
            without_operations=without_operations,
            upload_to_elastic=upload_to_elastic,
            request_options=request_options,
        )
        return _response.data

    async def ccs_convert_upload_file_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        file_url: typing.Optional[typing.Sequence[str]] = OMIT,
        http_source: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
        ] = OMIT,
        s3source: typing.Optional[S3DocumentSource] = OMIT,
        upload_to_elastic: typing.Optional[bool] = OMIT,
        meta: typing.Optional[DocumentMeta] = OMIT,
        conversion_settings: typing.Optional[ConvertUploadDocumentsRequestBodyConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Convert files via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema).

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : typing.Optional[typing.Sequence[str]]
            List of File's URL to be converted and uploaded to the data index.

        http_source : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]]
            List of Internal File's URLs to be converted and uploaded to the data index.

        s3source : typing.Optional[S3DocumentSource]
            Coordinates to object store to get files to convert. Can specify which files with object keys.

        upload_to_elastic : typing.Optional[bool]

        meta : typing.Optional[DocumentMeta]

        conversion_settings : typing.Optional[ConvertUploadDocumentsRequestBodyConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

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
            await client.data_indices_upload.ccs_convert_upload_file_project_data_index(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ccs_convert_upload_file_project_data_index(
            proj_key,
            index_key,
            file_url=file_url,
            http_source=http_source,
            s3source=s3source,
            upload_to_elastic=upload_to_elastic,
            meta=meta,
            conversion_settings=conversion_settings,
            target_settings=target_settings,
            request_options=request_options,
        )
        return _response.data

    async def html_print_convert_upload(
        self,
        proj_key: str,
        index_key: str,
        *,
        urls: DataIndexUploadFileSourceUrls,
        conversion_settings: typing.Optional[DataIndexUploadFileSourceConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Convert a list of HTML pages to PDF, convert them via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema).

        Parameters
        ----------
        proj_key : str

        index_key : str

        urls : DataIndexUploadFileSourceUrls
            List of URLs to be printed to PDF, converted and uploaded to the data index.

        conversion_settings : typing.Optional[DataIndexUploadFileSourceConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

        headers : typing.Optional[typing.Dict[str, typing.Any]]

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
            await client.data_indices_upload.html_print_convert_upload(
                proj_key="proj_key",
                index_key="index_key",
                urls="urls",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.html_print_convert_upload(
            proj_key,
            index_key,
            urls=urls,
            conversion_settings=conversion_settings,
            target_settings=target_settings,
            headers=headers,
            request_options=request_options,
        )
        return _response.data

    async def get_attachment_upload_data(
        self,
        proj_key: str,
        index_key: str,
        index_item_id: str,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AttachmentUploadData:
        """
        Get url and path to upload an attachment to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        index_item_id : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentUploadData
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_indices_upload.get_attachment_upload_data(
                proj_key="proj_key",
                index_key="index_key",
                index_item_id="index_item_id",
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_attachment_upload_data(
            proj_key, index_key, index_item_id, filename, request_options=request_options
        )
        return _response.data

    async def register_attachment(
        self,
        proj_key: str,
        index_key: str,
        index_item_id: str,
        *,
        attachment_path: str,
        attachment_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Notify upload completion of an attachment to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        index_item_id : str

        attachment_path : str

        attachment_key : typing.Optional[str]

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
            await client.data_indices_upload.register_attachment(
                proj_key="proj_key",
                index_key="index_key",
                index_item_id="index_item_id",
                attachment_path="attachment_path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_attachment(
            proj_key,
            index_key,
            index_item_id,
            attachment_path=attachment_path,
            attachment_key=attachment_key,
            request_options=request_options,
        )
        return _response.data
