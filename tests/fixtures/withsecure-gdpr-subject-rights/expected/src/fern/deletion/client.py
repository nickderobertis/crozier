

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.context_uuid import ContextUuid
from ..types.deletion_ready_response import DeletionReadyResponse
from ..types.deletion_request_grounds import DeletionRequestGrounds
from ..types.deletion_request_response import DeletionRequestResponse
from ..types.deletion_request_uuid import DeletionRequestUuid
from ..types.supplied_auth import SuppliedAuth
from .raw_client import AsyncRawDeletionClient, RawDeletionClient


OMIT = typing.cast(typing.Any, ...)


class DeletionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeletionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeletionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeletionClient
        """
        return self._raw_client

    def delete_personal_data(
        self,
        context_uuid: ContextUuid,
        *,
        request_grounds: typing.Optional[DeletionRequestGrounds] = OMIT,
        authenticated_identifiers: typing.Optional[SuppliedAuth] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeletionRequestResponse:
        """
        Create a deletion request to delete all personal data stored within a particular personal data context. This will only schedule a deletion. The status and result must be polled for separately.

        Parameters
        ----------
        context_uuid : ContextUuid
            The personal data context (data category) to delete.

        request_grounds : typing.Optional[DeletionRequestGrounds]

        authenticated_identifiers : typing.Optional[SuppliedAuth]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletionRequestResponse
            Deletion request queued

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.deletion.delete_personal_data(
            context_uuid="1234",
        )
        """
        _response = self._raw_client.delete_personal_data(
            context_uuid,
            request_grounds=request_grounds,
            authenticated_identifiers=authenticated_identifiers,
            request_options=request_options,
        )
        return _response.data

    def query_the_status_of_a_deletion_request(
        self,
        *,
        accept_language: typing.Optional[str] = None,
        deletion_request_id: typing.Optional[DeletionRequestUuid] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeletionReadyResponse:
        """
        Query the status of a deletion request. The status should be polled for until completed.

        Parameters
        ----------
        accept_language : typing.Optional[str]
            A list of accepted languages

        deletion_request_id : typing.Optional[DeletionRequestUuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletionReadyResponse
            Deletion request processed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.deletion.query_the_status_of_a_deletion_request(
            accept_language="fi_FI",
        )
        """
        _response = self._raw_client.query_the_status_of_a_deletion_request(
            accept_language=accept_language, deletion_request_id=deletion_request_id, request_options=request_options
        )
        return _response.data


class AsyncDeletionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeletionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeletionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeletionClient
        """
        return self._raw_client

    async def delete_personal_data(
        self,
        context_uuid: ContextUuid,
        *,
        request_grounds: typing.Optional[DeletionRequestGrounds] = OMIT,
        authenticated_identifiers: typing.Optional[SuppliedAuth] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeletionRequestResponse:
        """
        Create a deletion request to delete all personal data stored within a particular personal data context. This will only schedule a deletion. The status and result must be polled for separately.

        Parameters
        ----------
        context_uuid : ContextUuid
            The personal data context (data category) to delete.

        request_grounds : typing.Optional[DeletionRequestGrounds]

        authenticated_identifiers : typing.Optional[SuppliedAuth]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletionRequestResponse
            Deletion request queued

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.deletion.delete_personal_data(
                context_uuid="1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_personal_data(
            context_uuid,
            request_grounds=request_grounds,
            authenticated_identifiers=authenticated_identifiers,
            request_options=request_options,
        )
        return _response.data

    async def query_the_status_of_a_deletion_request(
        self,
        *,
        accept_language: typing.Optional[str] = None,
        deletion_request_id: typing.Optional[DeletionRequestUuid] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeletionReadyResponse:
        """
        Query the status of a deletion request. The status should be polled for until completed.

        Parameters
        ----------
        accept_language : typing.Optional[str]
            A list of accepted languages

        deletion_request_id : typing.Optional[DeletionRequestUuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletionReadyResponse
            Deletion request processed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.deletion.query_the_status_of_a_deletion_request(
                accept_language="fi_FI",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query_the_status_of_a_deletion_request(
            accept_language=accept_language, deletion_request_id=deletion_request_id, request_options=request_options
        )
        return _response.data
