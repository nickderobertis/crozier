

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.concept_id import ConceptId
from ..types.resolved_concepts_result import ResolvedConceptsResult
from .raw_client import AsyncRawConceptClient, RawConceptClient


OMIT = typing.cast(typing.Any, ...)


class ConceptClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConceptClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConceptClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConceptClient
        """
        return self._raw_client

    def resolve_concepts(
        self,
        concept: ConceptId,
        *,
        concepts: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolvedConceptsResult:
        """
        Parameters
        ----------
        concept : ConceptId

        concepts : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolvedConceptsResult
            Resolved Concepts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.concept.resolve_concepts(
            concept="concept",
        )
        """
        _response = self._raw_client.resolve_concepts(concept, concepts=concepts, request_options=request_options)
        return _response.data


class AsyncConceptClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConceptClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConceptClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConceptClient
        """
        return self._raw_client

    async def resolve_concepts(
        self,
        concept: ConceptId,
        *,
        concepts: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolvedConceptsResult:
        """
        Parameters
        ----------
        concept : ConceptId

        concepts : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolvedConceptsResult
            Resolved Concepts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.concept.resolve_concepts(
                concept="concept",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_concepts(concept, concepts=concepts, request_options=request_options)
        return _response.data
