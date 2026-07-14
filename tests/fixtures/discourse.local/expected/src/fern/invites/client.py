

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawInvitesClient, RawInvitesClient
from .types.create_invite_response import CreateInviteResponse


OMIT = typing.cast(typing.Any, ...)


class InvitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInvitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInvitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInvitesClient
        """
        return self._raw_client

    def create_invite(
        self,
        *,
        api_key: str,
        api_username: str,
        custom_message: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[str] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        group_names: typing.Optional[str] = OMIT,
        max_redemptions_allowed: typing.Optional[int] = OMIT,
        skip_email: typing.Optional[bool] = OMIT,
        topic_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateInviteResponse:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        custom_message : typing.Optional[str]
            optional, for email invites

        email : typing.Optional[str]
            required for email invites only

        expires_at : typing.Optional[str]
            optional, if not supplied, the invite_expiry_days site
            setting is used

        group_id : typing.Optional[int]
            optional, either this or `group_names`

        group_names : typing.Optional[str]
            optional, either this or `group_id`

        max_redemptions_allowed : typing.Optional[int]
            optional, for link invites

        skip_email : typing.Optional[bool]

        topic_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateInviteResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.invites.create_invite(
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.create_invite(
            api_key=api_key,
            api_username=api_username,
            custom_message=custom_message,
            email=email,
            expires_at=expires_at,
            group_id=group_id,
            group_names=group_names,
            max_redemptions_allowed=max_redemptions_allowed,
            skip_email=skip_email,
            topic_id=topic_id,
            request_options=request_options,
        )
        return _response.data


class AsyncInvitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInvitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInvitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInvitesClient
        """
        return self._raw_client

    async def create_invite(
        self,
        *,
        api_key: str,
        api_username: str,
        custom_message: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[str] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        group_names: typing.Optional[str] = OMIT,
        max_redemptions_allowed: typing.Optional[int] = OMIT,
        skip_email: typing.Optional[bool] = OMIT,
        topic_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateInviteResponse:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        custom_message : typing.Optional[str]
            optional, for email invites

        email : typing.Optional[str]
            required for email invites only

        expires_at : typing.Optional[str]
            optional, if not supplied, the invite_expiry_days site
            setting is used

        group_id : typing.Optional[int]
            optional, either this or `group_names`

        group_names : typing.Optional[str]
            optional, either this or `group_id`

        max_redemptions_allowed : typing.Optional[int]
            optional, for link invites

        skip_email : typing.Optional[bool]

        topic_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateInviteResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.invites.create_invite(
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_invite(
            api_key=api_key,
            api_username=api_username,
            custom_message=custom_message,
            email=email,
            expires_at=expires_at,
            group_id=group_id,
            group_names=group_names,
            max_redemptions_allowed=max_redemptions_allowed,
            skip_email=skip_email,
            topic_id=topic_id,
            request_options=request_options,
        )
        return _response.data
