

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.compare_documents_dtov2 import CompareDocumentsDtov2
from ..types.project_dto import ProjectDto
from ..types.properties_dto import PropertiesDto
from .raw_client import AsyncRawProjectsClient, RawProjectsClient


OMIT = typing.cast(typing.Any, ...)


class ProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectsClient
        """
        return self._raw_client

    def projects_api_project_search(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProjectDto]:
        """
        Search projects by filters

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProjectDto]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.projects_api_project_search(
            request="What methodology can I use for production of electricity using renewable energy technologies?",
        )
        """
        _response = self._raw_client.projects_api_project_search(request=request, request_options=request_options)
        return _response.data

    def projects_api_compare_documents_v2(
        self,
        *,
        document_id1: str,
        document_id2: str,
        document_ids: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompareDocumentsDtov2:
        """
        Compare documents.

        Parameters
        ----------
        document_id1 : str

        document_id2 : str

        document_ids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareDocumentsDtov2
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.projects_api_compare_documents_v2(
            document_id1="000000000000000000000001",
            document_id2="000000000000000000000002",
            document_ids="documentIds",
        )
        """
        _response = self._raw_client.projects_api_compare_documents_v2(
            document_id1=document_id1,
            document_id2=document_id2,
            document_ids=document_ids,
            request_options=request_options,
        )
        return _response.data

    def projects_api_get_policy_properties(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PropertiesDto]:
        """
        Get all properties

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PropertiesDto]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.projects_api_get_policy_properties()
        """
        _response = self._raw_client.projects_api_get_policy_properties(request_options=request_options)
        return _response.data


class AsyncProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectsClient
        """
        return self._raw_client

    async def projects_api_project_search(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProjectDto]:
        """
        Search projects by filters

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProjectDto]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.projects_api_project_search(
                request="What methodology can I use for production of electricity using renewable energy technologies?",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.projects_api_project_search(request=request, request_options=request_options)
        return _response.data

    async def projects_api_compare_documents_v2(
        self,
        *,
        document_id1: str,
        document_id2: str,
        document_ids: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompareDocumentsDtov2:
        """
        Compare documents.

        Parameters
        ----------
        document_id1 : str

        document_id2 : str

        document_ids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareDocumentsDtov2
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.projects_api_compare_documents_v2(
                document_id1="000000000000000000000001",
                document_id2="000000000000000000000002",
                document_ids="documentIds",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.projects_api_compare_documents_v2(
            document_id1=document_id1,
            document_id2=document_id2,
            document_ids=document_ids,
            request_options=request_options,
        )
        return _response.data

    async def projects_api_get_policy_properties(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PropertiesDto]:
        """
        Get all properties

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PropertiesDto]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.projects_api_get_policy_properties()


        asyncio.run(main())
        """
        _response = await self._raw_client.projects_api_get_policy_properties(request_options=request_options)
        return _response.data
