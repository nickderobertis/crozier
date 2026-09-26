

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cps_task import CpsTask
from ..types.semantic_ingest_req_params import SemanticIngestReqParams
from .raw_client import AsyncRawSemanticClient, RawSemanticClient
from .types.semantic_ingest_request_source import SemanticIngestRequestSource


OMIT = typing.cast(typing.Any, ...)


class SemanticClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSemanticClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSemanticClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSemanticClient
        """
        return self._raw_client

    def ingest(
        self,
        proj_key: str,
        *,
        source: SemanticIngestRequestSource,
        parameters: SemanticIngestReqParams,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Ingest documents and collections for RAG

        Parameters
        ----------
        proj_key : str

        source : SemanticIngestRequestSource

        parameters : SemanticIngestReqParams

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CpsTask
            Successful Response

        Examples
        --------
        from fern.semantic import SemanticIngestRequestSource_Url

        from fern import FernApi, SemanticIngestReqParams

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.semantic.ingest(
            proj_key="proj_key",
            source=SemanticIngestRequestSource_Url(
                url="url",
            ),
            parameters=SemanticIngestReqParams(
                skip_ingested_docs=True,
            ),
        )
        """
        _response = self._raw_client.ingest(
            proj_key, source=source, parameters=parameters, request_options=request_options
        )
        return _response.data


class AsyncSemanticClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSemanticClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSemanticClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSemanticClient
        """
        return self._raw_client

    async def ingest(
        self,
        proj_key: str,
        *,
        source: SemanticIngestRequestSource,
        parameters: SemanticIngestReqParams,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CpsTask:
        """
        Ingest documents and collections for RAG

        Parameters
        ----------
        proj_key : str

        source : SemanticIngestRequestSource

        parameters : SemanticIngestReqParams

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CpsTask
            Successful Response

        Examples
        --------
        import asyncio

        from fern.semantic import SemanticIngestRequestSource_Url

        from fern import AsyncFernApi, SemanticIngestReqParams

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.semantic.ingest(
                proj_key="proj_key",
                source=SemanticIngestRequestSource_Url(
                    url="url",
                ),
                parameters=SemanticIngestReqParams(
                    skip_ingested_docs=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ingest(
            proj_key, source=source, parameters=parameters, request_options=request_options
        )
        return _response.data
