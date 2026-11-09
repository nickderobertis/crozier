

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEmergencyClient, RawEmergencyClient
from .types.emergency_revoke_response import EmergencyRevokeResponse


OMIT = typing.cast(typing.Any, ...)


class EmergencyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmergencyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmergencyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmergencyClient
        """
        return self._raw_client

    def revoke(
        self,
        *,
        agent_id: str,
        revocation_secret: str,
        human_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmergencyRevokeResponse:
        """
        Revokes all keys for an agent using a pre-registered emergency revocation
        secret. Rate-limited to 5 requests per minute per IP.

        Parameters
        ----------
        agent_id : str

        revocation_secret : str

        human_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmergencyRevokeResponse
            Agent revoked

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.emergency.revoke(
            agent_id="agent-001",
            revocation_secret="a1b2c3d4e5f6...",
        )
        """
        _response = self._raw_client.revoke(
            agent_id=agent_id, revocation_secret=revocation_secret, human_id=human_id, request_options=request_options
        )
        return _response.data


class AsyncEmergencyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmergencyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmergencyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmergencyClient
        """
        return self._raw_client

    async def revoke(
        self,
        *,
        agent_id: str,
        revocation_secret: str,
        human_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmergencyRevokeResponse:
        """
        Revokes all keys for an agent using a pre-registered emergency revocation
        secret. Rate-limited to 5 requests per minute per IP.

        Parameters
        ----------
        agent_id : str

        revocation_secret : str

        human_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmergencyRevokeResponse
            Agent revoked

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.emergency.revoke(
                agent_id="agent-001",
                revocation_secret="a1b2c3d4e5f6...",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke(
            agent_id=agent_id, revocation_secret=revocation_secret, human_id=human_id, request_options=request_options
        )
        return _response.data
