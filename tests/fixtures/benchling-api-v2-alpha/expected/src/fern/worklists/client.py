

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collaborations_paginated_list import CollaborationsPaginatedList
from .raw_client import AsyncRawWorklistsClient, RawWorklistsClient


class WorklistsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorklistsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorklistsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorklistsClient
        """
        return self._raw_client

    def list_worklist_collaborations(
        self,
        worklist_id: str,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollaborationsPaginatedList:
        """
        Returns information about collaborations on the specified Worklists.

        Parameters
        ----------
        worklist_id : str
            ID of worklist for which to retrieve collaborations.

        page_size : typing.Optional[int]

        next_token : typing.Optional[str]
            Token for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollaborationsPaginatedList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.worklists.list_worklist_collaborations(
            worklist_id="worklist_id",
        )
        """
        _response = self._raw_client.list_worklist_collaborations(
            worklist_id, page_size=page_size, next_token=next_token, request_options=request_options
        )
        return _response.data


class AsyncWorklistsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorklistsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorklistsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorklistsClient
        """
        return self._raw_client

    async def list_worklist_collaborations(
        self,
        worklist_id: str,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollaborationsPaginatedList:
        """
        Returns information about collaborations on the specified Worklists.

        Parameters
        ----------
        worklist_id : str
            ID of worklist for which to retrieve collaborations.

        page_size : typing.Optional[int]

        next_token : typing.Optional[str]
            Token for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollaborationsPaginatedList
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.worklists.list_worklist_collaborations(
                worklist_id="worklist_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_worklist_collaborations(
            worklist_id, page_size=page_size, next_token=next_token, request_options=request_options
        )
        return _response.data
