

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.complete_o_auth_response import CompleteOAuthResponse
from ..types.o_auth_consent_read import OAuthConsentRead
from ..types.o_auth_input_configuration import OAuthInputConfiguration
from ..types.source_definition_id import SourceDefinitionId
from ..types.source_id import SourceId
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawSourceOauthClient, RawSourceOauthClient


OMIT = typing.cast(typing.Any, ...)


class SourceOauthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourceOauthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourceOauthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourceOauthClient
        """
        return self._raw_client

    def complete_source_o_auth(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        query_params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompleteOAuthResponse:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        query_params : typing.Optional[typing.Dict[str, typing.Any]]
            The query parameters present in the redirect URL after a user granted consent e.g auth code

        redirect_url : typing.Optional[str]
            When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given.

        source_id : typing.Optional[SourceId]

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
        client.source_oauth.complete_source_o_auth(
            source_definition_id="sourceDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.complete_source_o_auth(
            source_definition_id=source_definition_id,
            workspace_id=workspace_id,
            o_auth_input_configuration=o_auth_input_configuration,
            query_params=query_params,
            redirect_url=redirect_url,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    def get_source_o_auth_consent(
        self,
        *,
        redirect_url: str,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OAuthConsentRead:
        """
        Parameters
        ----------
        redirect_url : str
            The url to redirect to after getting the user consent

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        source_id : typing.Optional[SourceId]

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
        client.source_oauth.get_source_o_auth_consent(
            redirect_url="redirectUrl",
            source_definition_id="sourceDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_source_o_auth_consent(
            redirect_url=redirect_url,
            source_definition_id=source_definition_id,
            workspace_id=workspace_id,
            o_auth_input_configuration=o_auth_input_configuration,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    def set_instancewide_source_oauth_params(
        self,
        *,
        params: typing.Dict[str, typing.Any],
        source_definition_id: SourceDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        params : typing.Dict[str, typing.Any]

        source_definition_id : SourceDefinitionId

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
        client.source_oauth.set_instancewide_source_oauth_params(
            params={"key": "value"},
            source_definition_id="sourceDefinitionId",
        )
        """
        _response = self._raw_client.set_instancewide_source_oauth_params(
            params=params, source_definition_id=source_definition_id, request_options=request_options
        )
        return _response.data


class AsyncSourceOauthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourceOauthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourceOauthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourceOauthClient
        """
        return self._raw_client

    async def complete_source_o_auth(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        query_params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompleteOAuthResponse:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        query_params : typing.Optional[typing.Dict[str, typing.Any]]
            The query parameters present in the redirect URL after a user granted consent e.g auth code

        redirect_url : typing.Optional[str]
            When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given.

        source_id : typing.Optional[SourceId]

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
            await client.source_oauth.complete_source_o_auth(
                source_definition_id="sourceDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_source_o_auth(
            source_definition_id=source_definition_id,
            workspace_id=workspace_id,
            o_auth_input_configuration=o_auth_input_configuration,
            query_params=query_params,
            redirect_url=redirect_url,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    async def get_source_o_auth_consent(
        self,
        *,
        redirect_url: str,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OAuthConsentRead:
        """
        Parameters
        ----------
        redirect_url : str
            The url to redirect to after getting the user consent

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        source_id : typing.Optional[SourceId]

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
            await client.source_oauth.get_source_o_auth_consent(
                redirect_url="redirectUrl",
                source_definition_id="sourceDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_source_o_auth_consent(
            redirect_url=redirect_url,
            source_definition_id=source_definition_id,
            workspace_id=workspace_id,
            o_auth_input_configuration=o_auth_input_configuration,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    async def set_instancewide_source_oauth_params(
        self,
        *,
        params: typing.Dict[str, typing.Any],
        source_definition_id: SourceDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        params : typing.Dict[str, typing.Any]

        source_definition_id : SourceDefinitionId

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
            await client.source_oauth.set_instancewide_source_oauth_params(
                params={"key": "value"},
                source_definition_id="sourceDefinitionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_instancewide_source_oauth_params(
            params=params, source_definition_id=source_definition_id, request_options=request_options
        )
        return _response.data
