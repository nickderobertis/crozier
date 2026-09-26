

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_server_fastapi_server_public_models_data_indices_upload_models_identifier import (
    ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier,
)
from ..types.document_description import DocumentDescription
from ..types.document_statistics import DocumentStatistics
from ..types.project_agents import ProjectAgents
from ..types.project_document import ProjectDocument
from ..types.project_document_url import ProjectDocumentUrl
from ..types.project_documents import ProjectDocuments
from ..types.response_document_artifacts import ResponseDocumentArtifacts
from ..types.response_grouped_documents import ResponseGroupedDocuments
from ..types.response_upload_jobs import ResponseUploadJobs
from ..types.status_filter import StatusFilter
from .raw_client import AsyncRawContentManagerClient, RawContentManagerClient


OMIT = typing.cast(typing.Any, ...)


class ContentManagerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContentManagerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContentManagerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContentManagerClient
        """
        return self._raw_client

    def get_project_agents(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectAgents:
        """
        Get project agents.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAgents
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_agents(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.get_project_agents(proj_key, request_options=request_options)
        return _response.data

    def get_project_documents_by_transaction(
        self,
        proj_key: str,
        index_key: str,
        transaction_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocuments:
        """
        Get project documents by transaction ID.

        Parameters
        ----------
        proj_key : str

        index_key : str

        transaction_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocuments
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_documents_by_transaction(
            proj_key="proj_key",
            index_key="index_key",
            transaction_id="transaction_id",
        )
        """
        _response = self._raw_client.get_project_documents_by_transaction(
            proj_key, index_key, transaction_id, request_options=request_options
        )
        return _response.data

    def get_all_project_data_index_documents(
        self,
        proj_key: str,
        index_key: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocuments:
        """
        Get all project documents

        Parameters
        ----------
        proj_key : str

        index_key : str

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocuments
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_all_project_data_index_documents(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.get_all_project_data_index_documents(
            proj_key, index_key, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def get_project_conversion_statistics(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentStatistics:
        """
        Get project conversion statistics.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentStatistics
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_conversion_statistics(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.get_project_conversion_statistics(
            proj_key, index_key, request_options=request_options
        )
        return _response.data

    def get_project_data_index_documents(
        self,
        proj_key: str,
        index_key: str,
        agent_name: str,
        *,
        status: typing.Optional[StatusFilter] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocuments:
        """
        Get project documents, can be filter by status.

        Parameters
        ----------
        proj_key : str

        index_key : str

        agent_name : str

        status : typing.Optional[StatusFilter]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocuments
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_data_index_documents(
            proj_key="proj_key",
            index_key="index_key",
            agent_name="agent_name",
        )
        """
        _response = self._raw_client.get_project_data_index_documents(
            proj_key,
            index_key,
            agent_name,
            status=status,
            page=page,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def get_project_data_index_grouped_documents(
        self,
        proj_key: str,
        index_key: str,
        agent_name: str,
        *,
        status: typing.Optional[StatusFilter] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseGroupedDocuments:
        """
        Get project documents grouped by upload.

        Parameters
        ----------
        proj_key : str

        index_key : str

        agent_name : str

        status : typing.Optional[StatusFilter]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseGroupedDocuments
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_data_index_grouped_documents(
            proj_key="proj_key",
            index_key="index_key",
            agent_name="agent_name",
        )
        """
        _response = self._raw_client.get_project_data_index_grouped_documents(
            proj_key,
            index_key,
            agent_name,
            status=status,
            page=page,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def get_project_index_upload_jobs(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseUploadJobs:
        """
        Get project upload jobs.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseUploadJobs
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_index_upload_jobs(
            proj_key="proj_key",
            index_key="index_key",
        )
        """
        _response = self._raw_client.get_project_index_upload_jobs(proj_key, index_key, request_options=request_options)
        return _response.data

    def get_project_data_index_document_markdown(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocumentUrl:
        """
        Get project document Markdown.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocumentUrl
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_data_index_document_markdown(
            proj_key="proj_key",
            index_key="index_key",
            document_hash="document_hash",
        )
        """
        _response = self._raw_client.get_project_data_index_document_markdown(
            proj_key, index_key, document_hash, request_options=request_options
        )
        return _response.data

    def get_project_data_index_pdf_document(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocumentUrl:
        """
        Get project PDF document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocumentUrl
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_data_index_pdf_document(
            proj_key="proj_key",
            index_key="index_key",
            document_hash="document_hash",
        )
        """
        _response = self._raw_client.get_project_data_index_pdf_document(
            proj_key, index_key, document_hash, request_options=request_options
        )
        return _response.data

    def get_project_data_index_json_document(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get project JSON document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_data_index_json_document(
            proj_key="proj_key",
            index_key="index_key",
            document_hash="document_hash",
        )
        """
        _response = self._raw_client.get_project_data_index_json_document(
            proj_key, index_key, document_hash, request_options=request_options
        )
        return _response.data

    def get_project_data_index_document_artifacts(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseDocumentArtifacts:
        """
        Get project document artifacts.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseDocumentArtifacts
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_data_index_document_artifacts(
            proj_key="proj_key",
            index_key="index_key",
            document_hash="document_hash",
        )
        """
        _response = self._raw_client.get_project_data_index_document_artifacts(
            proj_key, index_key, document_hash, request_options=request_options
        )
        return _response.data

    def get_project_data_index_document_metadata(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocument:
        """
        Get project document metadata.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocument
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_data_index_document_metadata(
            proj_key="proj_key",
            index_key="index_key",
            document_hash="document_hash",
        )
        """
        _response = self._raw_client.get_project_data_index_document_metadata(
            proj_key, index_key, document_hash, request_options=request_options
        )
        return _response.data

    def add_project_data_index_document_metadata(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        filename: typing.Optional[str] = OMIT,
        description: typing.Optional[DocumentDescription] = OMIT,
        identifiers: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Insert project document metadata.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        filename : typing.Optional[str]

        description : typing.Optional[DocumentDescription]

        identifiers : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]]

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
        client.content_manager.add_project_data_index_document_metadata(
            proj_key="proj_key",
            index_key="index_key",
            document_hash="document_hash",
        )
        """
        _response = self._raw_client.add_project_data_index_document_metadata(
            proj_key,
            index_key,
            document_hash,
            filename=filename,
            description=description,
            identifiers=identifiers,
            request_options=request_options,
        )
        return _response.data

    def get_project_data_index_document_events(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        agent_name: typing.Optional[str] = None,
        status: typing.Optional[StatusFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get events of a project document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        agent_name : typing.Optional[str]

        status : typing.Optional[StatusFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content_manager.get_project_data_index_document_events(
            proj_key="proj_key",
            index_key="index_key",
            document_hash="document_hash",
        )
        """
        _response = self._raw_client.get_project_data_index_document_events(
            proj_key, index_key, document_hash, agent_name=agent_name, status=status, request_options=request_options
        )
        return _response.data


class AsyncContentManagerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContentManagerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContentManagerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContentManagerClient
        """
        return self._raw_client

    async def get_project_agents(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectAgents:
        """
        Get project agents.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectAgents
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_agents(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_agents(proj_key, request_options=request_options)
        return _response.data

    async def get_project_documents_by_transaction(
        self,
        proj_key: str,
        index_key: str,
        transaction_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocuments:
        """
        Get project documents by transaction ID.

        Parameters
        ----------
        proj_key : str

        index_key : str

        transaction_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocuments
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_documents_by_transaction(
                proj_key="proj_key",
                index_key="index_key",
                transaction_id="transaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_documents_by_transaction(
            proj_key, index_key, transaction_id, request_options=request_options
        )
        return _response.data

    async def get_all_project_data_index_documents(
        self,
        proj_key: str,
        index_key: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocuments:
        """
        Get all project documents

        Parameters
        ----------
        proj_key : str

        index_key : str

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocuments
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_all_project_data_index_documents(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_project_data_index_documents(
            proj_key, index_key, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def get_project_conversion_statistics(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentStatistics:
        """
        Get project conversion statistics.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentStatistics
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_conversion_statistics(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_conversion_statistics(
            proj_key, index_key, request_options=request_options
        )
        return _response.data

    async def get_project_data_index_documents(
        self,
        proj_key: str,
        index_key: str,
        agent_name: str,
        *,
        status: typing.Optional[StatusFilter] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocuments:
        """
        Get project documents, can be filter by status.

        Parameters
        ----------
        proj_key : str

        index_key : str

        agent_name : str

        status : typing.Optional[StatusFilter]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocuments
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_data_index_documents(
                proj_key="proj_key",
                index_key="index_key",
                agent_name="agent_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_index_documents(
            proj_key,
            index_key,
            agent_name,
            status=status,
            page=page,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def get_project_data_index_grouped_documents(
        self,
        proj_key: str,
        index_key: str,
        agent_name: str,
        *,
        status: typing.Optional[StatusFilter] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseGroupedDocuments:
        """
        Get project documents grouped by upload.

        Parameters
        ----------
        proj_key : str

        index_key : str

        agent_name : str

        status : typing.Optional[StatusFilter]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseGroupedDocuments
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_data_index_grouped_documents(
                proj_key="proj_key",
                index_key="index_key",
                agent_name="agent_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_index_grouped_documents(
            proj_key,
            index_key,
            agent_name,
            status=status,
            page=page,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def get_project_index_upload_jobs(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseUploadJobs:
        """
        Get project upload jobs.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseUploadJobs
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_index_upload_jobs(
                proj_key="proj_key",
                index_key="index_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_index_upload_jobs(
            proj_key, index_key, request_options=request_options
        )
        return _response.data

    async def get_project_data_index_document_markdown(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocumentUrl:
        """
        Get project document Markdown.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocumentUrl
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_data_index_document_markdown(
                proj_key="proj_key",
                index_key="index_key",
                document_hash="document_hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_index_document_markdown(
            proj_key, index_key, document_hash, request_options=request_options
        )
        return _response.data

    async def get_project_data_index_pdf_document(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocumentUrl:
        """
        Get project PDF document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocumentUrl
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_data_index_pdf_document(
                proj_key="proj_key",
                index_key="index_key",
                document_hash="document_hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_index_pdf_document(
            proj_key, index_key, document_hash, request_options=request_options
        )
        return _response.data

    async def get_project_data_index_json_document(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get project JSON document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_data_index_json_document(
                proj_key="proj_key",
                index_key="index_key",
                document_hash="document_hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_index_json_document(
            proj_key, index_key, document_hash, request_options=request_options
        )
        return _response.data

    async def get_project_data_index_document_artifacts(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseDocumentArtifacts:
        """
        Get project document artifacts.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseDocumentArtifacts
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_data_index_document_artifacts(
                proj_key="proj_key",
                index_key="index_key",
                document_hash="document_hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_index_document_artifacts(
            proj_key, index_key, document_hash, request_options=request_options
        )
        return _response.data

    async def get_project_data_index_document_metadata(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectDocument:
        """
        Get project document metadata.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDocument
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_data_index_document_metadata(
                proj_key="proj_key",
                index_key="index_key",
                document_hash="document_hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_index_document_metadata(
            proj_key, index_key, document_hash, request_options=request_options
        )
        return _response.data

    async def add_project_data_index_document_metadata(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        filename: typing.Optional[str] = OMIT,
        description: typing.Optional[DocumentDescription] = OMIT,
        identifiers: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Insert project document metadata.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        filename : typing.Optional[str]

        description : typing.Optional[DocumentDescription]

        identifiers : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]]

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
            await client.content_manager.add_project_data_index_document_metadata(
                proj_key="proj_key",
                index_key="index_key",
                document_hash="document_hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_project_data_index_document_metadata(
            proj_key,
            index_key,
            document_hash,
            filename=filename,
            description=description,
            identifiers=identifiers,
            request_options=request_options,
        )
        return _response.data

    async def get_project_data_index_document_events(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        agent_name: typing.Optional[str] = None,
        status: typing.Optional[StatusFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get events of a project document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        agent_name : typing.Optional[str]

        status : typing.Optional[StatusFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content_manager.get_project_data_index_document_events(
                proj_key="proj_key",
                index_key="index_key",
                document_hash="document_hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_data_index_document_events(
            proj_key, index_key, document_hash, agent_name=agent_name, status=status, request_options=request_options
        )
        return _response.data
