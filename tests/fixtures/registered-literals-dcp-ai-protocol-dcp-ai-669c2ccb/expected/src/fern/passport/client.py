

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.signed_payload import SignedPayload
from .raw_client import AsyncRawPassportClient, RawPassportClient
from .types.register_passport_response import RegisterPassportResponse


OMIT = typing.cast(typing.Any, ...)


class PassportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPassportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPassportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPassportClient
        """
        return self._raw_client

    def register_passport(
        self, *, signed_passport: SignedPayload, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterPassportResponse:
        """
        Registers a V2 agent passport with composite-signed keys.
        Verifies deterministic kid derivation and stores keys in the registry.
        Optionally registers an emergency revocation token.

        Parameters
        ----------
        signed_passport : SignedPayload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterPassportResponse
            Passport registered

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
        client.passport.register_passport(
            signed_passport=SignedPayload(
                payload={
                    "dcp_version": "2.0",
                    "agent_id": "agent-001",
                    "session_nonce": "a1b2c3d4...",
                    "keys": [
                        {
                            "kid": "abc123...",
                            "alg": "ed25519",
                            "public_key_b64": "...",
                            "created_at": "2026-03-01T00:00:00Z",
                            "status": "active",
                        }
                    ],
                    "emergency_revocation_token": "sha256:...",
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
        _response = self._raw_client.register_passport(signed_passport=signed_passport, request_options=request_options)
        return _response.data


class AsyncPassportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPassportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPassportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPassportClient
        """
        return self._raw_client

    async def register_passport(
        self, *, signed_passport: SignedPayload, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterPassportResponse:
        """
        Registers a V2 agent passport with composite-signed keys.
        Verifies deterministic kid derivation and stores keys in the registry.
        Optionally registers an emergency revocation token.

        Parameters
        ----------
        signed_passport : SignedPayload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterPassportResponse
            Passport registered

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
            await client.passport.register_passport(
                signed_passport=SignedPayload(
                    payload={
                        "dcp_version": "2.0",
                        "agent_id": "agent-001",
                        "session_nonce": "a1b2c3d4...",
                        "keys": [
                            {
                                "kid": "abc123...",
                                "alg": "ed25519",
                                "public_key_b64": "...",
                                "created_at": "2026-03-01T00:00:00Z",
                                "status": "active",
                            }
                        ],
                        "emergency_revocation_token": "sha256:...",
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
        _response = await self._raw_client.register_passport(
            signed_passport=signed_passport, request_options=request_options
        )
        return _response.data
