

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.endpoint_get_audiences import EndpointGetAudiences
from ..types.endpoint_get_audiences_id import EndpointGetAudiencesId
from ..types.endpoint_post_audiences_id_memberships import EndpointPostAudiencesIdMemberships
from .raw_client import AsyncRawAudiencesClient, RawAudiencesClient


class AudiencesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAudiencesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAudiencesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAudiencesClient
        """
        return self._raw_client

    def get_audiences(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetAudiences:
        """
        Fetch all Daniapp audience segments that comprise the current access token's bubble.

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetAudiences
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audiences.get_audiences()
        """
        _response = self._raw_client.get_audiences(offset=offset, limit=limit, request_options=request_options)
        return _response.data

    def get_audiences_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetAudiencesId:
        """
        Fetch an array of Daniapp audience segments that comprise the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetAudiencesId
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audiences.get_audiences_id(
            id="ID",
        )
        """
        _response = self._raw_client.get_audiences_id(id, request_options=request_options)
        return _response.data

    def post_audiences_id_memberships(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointPostAudiencesIdMemberships:
        """
        Create a membership record for the OAuth'ed end-user based on the current audience segment/bubble combination.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostAudiencesIdMemberships
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audiences.post_audiences_id_memberships(
            id=1,
        )
        """
        _response = self._raw_client.post_audiences_id_memberships(id, request_options=request_options)
        return _response.data


class AsyncAudiencesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAudiencesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAudiencesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAudiencesClient
        """
        return self._raw_client

    async def get_audiences(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetAudiences:
        """
        Fetch all Daniapp audience segments that comprise the current access token's bubble.

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetAudiences
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audiences.get_audiences()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audiences(offset=offset, limit=limit, request_options=request_options)
        return _response.data

    async def get_audiences_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetAudiencesId:
        """
        Fetch an array of Daniapp audience segments that comprise the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetAudiencesId
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audiences.get_audiences_id(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audiences_id(id, request_options=request_options)
        return _response.data

    async def post_audiences_id_memberships(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointPostAudiencesIdMemberships:
        """
        Create a membership record for the OAuth'ed end-user based on the current audience segment/bubble combination.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostAudiencesIdMemberships
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audiences.post_audiences_id_memberships(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_audiences_id_memberships(id, request_options=request_options)
        return _response.data
