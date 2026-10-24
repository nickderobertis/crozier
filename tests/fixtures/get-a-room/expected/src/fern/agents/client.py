

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAgentsClient, RawAgentsClient
from .types.use_agent_invitation_request import UseAgentInvitationRequest
from .types.use_agent_invitation_response import UseAgentInvitationResponse


OMIT = typing.cast(typing.Any, ...)


class AgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentsClient
        """
        return self._raw_client

    def use_agent_invitation(
        self, *, request: UseAgentInvitationRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> UseAgentInvitationResponse:
        """
        A zero-install facade for lead and guest agents. The complete invitation is carried only in the JSON request body; it is never echoed. join returns the task, room status, and first message page. say sends one message and check returns messages after a cursor. Lead-only finish, final, collect, and close actions complete the existing room lifecycle. Existing room limits and role permissions apply.

        Parameters
        ----------
        request : UseAgentInvitationRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UseAgentInvitationResponse
            Agent action completed; the invitation is never included in the response.

        Examples
        --------
        from fern.agents import UseAgentInvitationRequest_Join

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agents.use_agent_invitation(
            request=UseAgentInvitationRequest_Join(
                invitation="invitation",
            ),
        )
        """
        _response = self._raw_client.use_agent_invitation(request=request, request_options=request_options)
        return _response.data


class AsyncAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentsClient
        """
        return self._raw_client

    async def use_agent_invitation(
        self, *, request: UseAgentInvitationRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> UseAgentInvitationResponse:
        """
        A zero-install facade for lead and guest agents. The complete invitation is carried only in the JSON request body; it is never echoed. join returns the task, room status, and first message page. say sends one message and check returns messages after a cursor. Lead-only finish, final, collect, and close actions complete the existing room lifecycle. Existing room limits and role permissions apply.

        Parameters
        ----------
        request : UseAgentInvitationRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UseAgentInvitationResponse
            Agent action completed; the invitation is never included in the response.

        Examples
        --------
        import asyncio

        from fern.agents import UseAgentInvitationRequest_Join

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.use_agent_invitation(
                request=UseAgentInvitationRequest_Join(
                    invitation="invitation",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.use_agent_invitation(request=request, request_options=request_options)
        return _response.data
