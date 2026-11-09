

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ats_create_or_update_candidate_request import AtsCreateOrUpdateCandidateRequest
from ..types.ats_create_or_update_candidate_response import AtsCreateOrUpdateCandidateResponse
from ..types.ats_delete_candidate_response import AtsDeleteCandidateResponse
from ..types.ats_get_candidate_response import AtsGetCandidateResponse
from ..types.ats_get_candidates_response import AtsGetCandidatesResponse
from .raw_client import AsyncRawAtsCandidateClient, RawAtsCandidateClient


OMIT = typing.cast(typing.Any, ...)


class AtsCandidateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAtsCandidateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAtsCandidateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAtsCandidateClient
        """
        return self._raw_client

    def ats_candidate_get_candidate(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsGetCandidateResponse:
        """
        Get details of a candidate.

        Parameters
        ----------
        id : str
            The unique `id` of the candidate.

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetCandidateResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_candidate.ats_candidate_get_candidate(
            id="id",
        )
        """
        _response = self._raw_client.ats_candidate_get_candidate(id, fields=fields, request_options=request_options)
        return _response.data

    def ats_candidate_delete_candidate(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsDeleteCandidateResponse:
        """
        Delete details of an Candidate

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsDeleteCandidateResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_candidate.ats_candidate_delete_candidate(
            id="id",
        )
        """
        _response = self._raw_client.ats_candidate_delete_candidate(id, fields=fields, request_options=request_options)
        return _response.data

    def ats_candidate_update_candidate(
        self,
        id: str,
        *,
        request: AtsCreateOrUpdateCandidateRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateCandidateResponse:
        """
        Update a Candidate

        Parameters
        ----------
        id : str

        request : AtsCreateOrUpdateCandidateRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateCandidateResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_candidate.ats_candidate_update_candidate(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.ats_candidate_update_candidate(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    def ats_candidate_get_candidates(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsGetCandidatesResponse:
        """
        Get all the Candidates.

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetCandidatesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_candidate.ats_candidate_get_candidates()
        """
        _response = self._raw_client.ats_candidate_get_candidates(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    def ats_candidate_create_candidate(
        self,
        *,
        request: AtsCreateOrUpdateCandidateRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateCandidateResponse:
        """
        Create a new Candidate

        Parameters
        ----------
        request : AtsCreateOrUpdateCandidateRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateCandidateResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_candidate.ats_candidate_create_candidate(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.ats_candidate_create_candidate(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data


class AsyncAtsCandidateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAtsCandidateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAtsCandidateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAtsCandidateClient
        """
        return self._raw_client

    async def ats_candidate_get_candidate(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsGetCandidateResponse:
        """
        Get details of a candidate.

        Parameters
        ----------
        id : str
            The unique `id` of the candidate.

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetCandidateResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_candidate.ats_candidate_get_candidate(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_candidate_get_candidate(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    async def ats_candidate_delete_candidate(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsDeleteCandidateResponse:
        """
        Delete details of an Candidate

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsDeleteCandidateResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_candidate.ats_candidate_delete_candidate(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_candidate_delete_candidate(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    async def ats_candidate_update_candidate(
        self,
        id: str,
        *,
        request: AtsCreateOrUpdateCandidateRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateCandidateResponse:
        """
        Update a Candidate

        Parameters
        ----------
        id : str

        request : AtsCreateOrUpdateCandidateRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateCandidateResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_candidate.ats_candidate_update_candidate(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_candidate_update_candidate(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    async def ats_candidate_get_candidates(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsGetCandidatesResponse:
        """
        Get all the Candidates.

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetCandidatesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_candidate.ats_candidate_get_candidates()


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_candidate_get_candidates(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def ats_candidate_create_candidate(
        self,
        *,
        request: AtsCreateOrUpdateCandidateRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateCandidateResponse:
        """
        Create a new Candidate

        Parameters
        ----------
        request : AtsCreateOrUpdateCandidateRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateCandidateResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_candidate.ats_candidate_create_candidate(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_candidate_create_candidate(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data
