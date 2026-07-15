

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.complete_o_auth_response import CompleteOAuthResponse
from ..types.destination_definition_id import DestinationDefinitionId
from ..types.destination_id import DestinationId
from ..types.o_auth_consent_read import OAuthConsentRead
from ..types.o_auth_input_configuration import OAuthInputConfiguration
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawDestinationOauthClient, RawDestinationOauthClient


OMIT = typing.cast(typing.Any, ...)


class DestinationOauthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDestinationOauthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDestinationOauthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDestinationOauthClient
        """
        return self._raw_client

    def complete_destination_o_auth(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        destination_id: typing.Optional[DestinationId] = OMIT,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        query_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompleteOAuthResponse:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        destination_id : typing.Optional[DestinationId]

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        query_params : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The query parameters present in the redirect URL after a user granted consent e.g auth code

        redirect_url : typing.Optional[str]
            When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompleteOAuthResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_oauth.complete_destination_o_auth(
            destination_definition_id="destinationDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.complete_destination_o_auth(
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            destination_id=destination_id,
            o_auth_input_configuration=o_auth_input_configuration,
            query_params=query_params,
            redirect_url=redirect_url,
            request_options=request_options,
        )
        return _response.data

    def get_destination_o_auth_consent(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        redirect_url: str,
        workspace_id: WorkspaceId,
        destination_id: typing.Optional[DestinationId] = OMIT,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OAuthConsentRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        redirect_url : str
            The url to redirect to after getting the user consent

        workspace_id : WorkspaceId

        destination_id : typing.Optional[DestinationId]

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuthConsentRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_oauth.get_destination_o_auth_consent(
            destination_definition_id="destinationDefinitionId",
            redirect_url="redirectUrl",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_destination_o_auth_consent(
            destination_definition_id=destination_definition_id,
            redirect_url=redirect_url,
            workspace_id=workspace_id,
            destination_id=destination_id,
            o_auth_input_configuration=o_auth_input_configuration,
            request_options=request_options,
        )
        return _response.data

    def set_instancewide_destination_oauth_params(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        params: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        params : typing.Dict[str, typing.Optional[typing.Any]]

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
        client.destination_oauth.set_instancewide_destination_oauth_params(
            destination_definition_id="destinationDefinitionId",
            params={"key": "value"},
        )
        """
        _response = self._raw_client.set_instancewide_destination_oauth_params(
            destination_definition_id=destination_definition_id, params=params, request_options=request_options
        )
        return _response.data


class AsyncDestinationOauthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDestinationOauthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDestinationOauthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDestinationOauthClient
        """
        return self._raw_client

    async def complete_destination_o_auth(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        destination_id: typing.Optional[DestinationId] = OMIT,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        query_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompleteOAuthResponse:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        destination_id : typing.Optional[DestinationId]

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        query_params : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The query parameters present in the redirect URL after a user granted consent e.g auth code

        redirect_url : typing.Optional[str]
            When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompleteOAuthResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_oauth.complete_destination_o_auth(
                destination_definition_id="destinationDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_destination_o_auth(
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            destination_id=destination_id,
            o_auth_input_configuration=o_auth_input_configuration,
            query_params=query_params,
            redirect_url=redirect_url,
            request_options=request_options,
        )
        return _response.data

    async def get_destination_o_auth_consent(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        redirect_url: str,
        workspace_id: WorkspaceId,
        destination_id: typing.Optional[DestinationId] = OMIT,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OAuthConsentRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        redirect_url : str
            The url to redirect to after getting the user consent

        workspace_id : WorkspaceId

        destination_id : typing.Optional[DestinationId]

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuthConsentRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_oauth.get_destination_o_auth_consent(
                destination_definition_id="destinationDefinitionId",
                redirect_url="redirectUrl",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_destination_o_auth_consent(
            destination_definition_id=destination_definition_id,
            redirect_url=redirect_url,
            workspace_id=workspace_id,
            destination_id=destination_id,
            o_auth_input_configuration=o_auth_input_configuration,
            request_options=request_options,
        )
        return _response.data

    async def set_instancewide_destination_oauth_params(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        params: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        params : typing.Dict[str, typing.Optional[typing.Any]]

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
            await client.destination_oauth.set_instancewide_destination_oauth_params(
                destination_definition_id="destinationDefinitionId",
                params={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_instancewide_destination_oauth_params(
            destination_definition_id=destination_definition_id, params=params, request_options=request_options
        )
        return _response.data
