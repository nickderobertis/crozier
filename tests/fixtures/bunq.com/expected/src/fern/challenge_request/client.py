

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.master_card_identity_check_challenge_request_user_read import (
    MasterCardIdentityCheckChallengeRequestUserRead,
)
from ..types.master_card_identity_check_challenge_request_user_update import (
    MasterCardIdentityCheckChallengeRequestUserUpdate,
)
from .raw_client import AsyncRawChallengeRequestClient, RawChallengeRequestClient


OMIT = typing.cast(typing.Any, ...)


class ChallengeRequestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChallengeRequestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChallengeRequestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChallengeRequestClient
        """
        return self._raw_client

    def read_challenge_request_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MasterCardIdentityCheckChallengeRequestUserRead:
        """
        Endpoint for apps to fetch a challenge request.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MasterCardIdentityCheckChallengeRequestUserRead
            Endpoint for apps to fetch a challenge request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.challenge_request.read_challenge_request_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_challenge_request_for_user(user_id, item_id, request_options=request_options)
        return _response.data

    def update_challenge_request_for_user(
        self, user_id: int, item_id: int, *, status: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MasterCardIdentityCheckChallengeRequestUserUpdate:
        """
        Endpoint for apps to fetch a challenge request.

        Parameters
        ----------
        user_id : int


        item_id : int


        status : str
            The status of the identity check. Can be ACCEPTED_PENDING_RESPONSE or REJECTED_PENDING_RESPONSE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MasterCardIdentityCheckChallengeRequestUserUpdate
            Endpoint for apps to fetch a challenge request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.challenge_request.update_challenge_request_for_user(
            user_id=1,
            item_id=1,
            status="status",
        )
        """
        _response = self._raw_client.update_challenge_request_for_user(
            user_id, item_id, status=status, request_options=request_options
        )
        return _response.data


class AsyncChallengeRequestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChallengeRequestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChallengeRequestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChallengeRequestClient
        """
        return self._raw_client

    async def read_challenge_request_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MasterCardIdentityCheckChallengeRequestUserRead:
        """
        Endpoint for apps to fetch a challenge request.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MasterCardIdentityCheckChallengeRequestUserRead
            Endpoint for apps to fetch a challenge request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.challenge_request.read_challenge_request_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_challenge_request_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_challenge_request_for_user(
        self, user_id: int, item_id: int, *, status: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MasterCardIdentityCheckChallengeRequestUserUpdate:
        """
        Endpoint for apps to fetch a challenge request.

        Parameters
        ----------
        user_id : int


        item_id : int


        status : str
            The status of the identity check. Can be ACCEPTED_PENDING_RESPONSE or REJECTED_PENDING_RESPONSE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MasterCardIdentityCheckChallengeRequestUserUpdate
            Endpoint for apps to fetch a challenge request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.challenge_request.update_challenge_request_for_user(
                user_id=1,
                item_id=1,
                status="status",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_challenge_request_for_user(
            user_id, item_id, status=status, request_options=request_options
        )
        return _response.data
