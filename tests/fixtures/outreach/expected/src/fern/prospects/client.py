

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.prospect_list_response import ProspectListResponse
from ..types.prospect_response import ProspectResponse
from .raw_client import AsyncRawProspectsClient, RawProspectsClient
from .types.prospect_create_request_data import ProspectCreateRequestData
from .types.prospect_update_request_data import ProspectUpdateRequestData


OMIT = typing.cast(typing.Any, ...)


class ProspectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProspectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProspectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProspectsClient
        """
        return self._raw_client

    def list_prospects(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProspectListResponse:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

        sort : typing.Optional[str]
            Sort field (prefix with - for descending)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProspectListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prospects.list_prospects()
        """
        _response = self._raw_client.list_prospects(
            page_offset=page_offset, page_limit=page_limit, sort=sort, request_options=request_options
        )
        return _response.data

    def create_prospect(
        self,
        *,
        data: typing.Optional[ProspectCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProspectResponse:
        """
        Parameters
        ----------
        data : typing.Optional[ProspectCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProspectResponse
            Prospect created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prospects.create_prospect()
        """
        _response = self._raw_client.create_prospect(data=data, request_options=request_options)
        return _response.data

    def get_prospect(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ProspectResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProspectResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prospects.get_prospect(
            id=1,
        )
        """
        _response = self._raw_client.get_prospect(id, request_options=request_options)
        return _response.data

    def delete_prospect(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

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
        client.prospects.delete_prospect(
            id=1,
        )
        """
        _response = self._raw_client.delete_prospect(id, request_options=request_options)
        return _response.data

    def update_prospect(
        self,
        id: int,
        *,
        data: typing.Optional[ProspectUpdateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProspectResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        data : typing.Optional[ProspectUpdateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProspectResponse
            Prospect updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prospects.update_prospect(
            id=1,
        )
        """
        _response = self._raw_client.update_prospect(id, data=data, request_options=request_options)
        return _response.data


class AsyncProspectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProspectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProspectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProspectsClient
        """
        return self._raw_client

    async def list_prospects(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProspectListResponse:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

        sort : typing.Optional[str]
            Sort field (prefix with - for descending)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProspectListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prospects.list_prospects()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_prospects(
            page_offset=page_offset, page_limit=page_limit, sort=sort, request_options=request_options
        )
        return _response.data

    async def create_prospect(
        self,
        *,
        data: typing.Optional[ProspectCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProspectResponse:
        """
        Parameters
        ----------
        data : typing.Optional[ProspectCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProspectResponse
            Prospect created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prospects.create_prospect()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_prospect(data=data, request_options=request_options)
        return _response.data

    async def get_prospect(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProspectResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProspectResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prospects.get_prospect(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prospect(id, request_options=request_options)
        return _response.data

    async def delete_prospect(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

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
            await client.prospects.delete_prospect(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_prospect(id, request_options=request_options)
        return _response.data

    async def update_prospect(
        self,
        id: int,
        *,
        data: typing.Optional[ProspectUpdateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProspectResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        data : typing.Optional[ProspectUpdateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProspectResponse
            Prospect updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prospects.update_prospect(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_prospect(id, data=data, request_options=request_options)
        return _response.data
