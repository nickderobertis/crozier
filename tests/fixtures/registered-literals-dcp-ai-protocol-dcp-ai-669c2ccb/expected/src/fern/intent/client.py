

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.signed_payload import SignedPayload
from .raw_client import AsyncRawIntentClient, RawIntentClient
from .types.declare_intent_response import DeclareIntentResponse


OMIT = typing.cast(typing.Any, ...)


class IntentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIntentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIntentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIntentClient
        """
        return self._raw_client

    def declare_intent(
        self, *, signed_intent: SignedPayload, request_options: typing.Optional[RequestOptions] = None
    ) -> DeclareIntentResponse:
        """
        Submits a signed intent declaration. The server computes a risk score,
        security tier, and policy decision (approve/escalate/block).

        Parameters
        ----------
        signed_intent : SignedPayload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeclareIntentResponse
            Policy decision

        Examples
        --------
        from fern import (
            CompositeSignature,
            CompositeSignatureBinding,
            CompositeSignatureClassical,
            FernApi,
            SignedPayload,
        )

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.intent.declare_intent(
            signed_intent=SignedPayload(
                payload={
                    "dcp_version": "2.0",
                    "intent_id": "intent-001",
                    "agent_id": "agent-001",
                    "session_nonce": "a1b2c3d4...",
                    "action_type": "api_call",
                    "estimated_impact": "low",
                },
                composite_sig=CompositeSignature(
                    classical=CompositeSignatureClassical(
                        alg="ed25519",
                        kid="abc123",
                        sig_b64="...",
                    ),
                    binding=CompositeSignatureBinding.CLASSICAL_ONLY,
                ),
            ),
        )
        """
        _response = self._raw_client.declare_intent(signed_intent=signed_intent, request_options=request_options)
        return _response.data


class AsyncIntentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIntentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIntentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIntentClient
        """
        return self._raw_client

    async def declare_intent(
        self, *, signed_intent: SignedPayload, request_options: typing.Optional[RequestOptions] = None
    ) -> DeclareIntentResponse:
        """
        Submits a signed intent declaration. The server computes a risk score,
        security tier, and policy decision (approve/escalate/block).

        Parameters
        ----------
        signed_intent : SignedPayload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeclareIntentResponse
            Policy decision

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            CompositeSignature,
            CompositeSignatureBinding,
            CompositeSignatureClassical,
            SignedPayload,
        )

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.intent.declare_intent(
                signed_intent=SignedPayload(
                    payload={
                        "dcp_version": "2.0",
                        "intent_id": "intent-001",
                        "agent_id": "agent-001",
                        "session_nonce": "a1b2c3d4...",
                        "action_type": "api_call",
                        "estimated_impact": "low",
                    },
                    composite_sig=CompositeSignature(
                        classical=CompositeSignatureClassical(
                            alg="ed25519",
                            kid="abc123",
                            sig_b64="...",
                        ),
                        binding=CompositeSignatureBinding.CLASSICAL_ONLY,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.declare_intent(signed_intent=signed_intent, request_options=request_options)
        return _response.data
