

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.signed_bundle_v2 import SignedBundleV2
from ..types.verification_result import VerificationResult
from .raw_client import AsyncRawVerificationClient, RawVerificationClient
from .types.verify_bundle_request_signed_bundle import VerifyBundleRequestSignedBundle
from .types.verify_bundle_v2response import VerifyBundleV2Response


OMIT = typing.cast(typing.Any, ...)


class VerificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVerificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVerificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVerificationClient
        """
        return self._raw_client

    def verify_bundle(
        self,
        *,
        signed_bundle: VerifyBundleRequestSignedBundle,
        public_key_b64: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VerificationResult:
        """
        Performs full DCP verification with automatic version detection:

        V1: Schema validation, Ed25519 signature, bundle hash integrity,
        Merkle root, intent hash chain, and previous hash chain verification.

        V2: Composite signature structure, session nonce consistency,
        manifest integrity, tier-aware policy enforcement.

        Parameters
        ----------
        signed_bundle : VerifyBundleRequestSignedBundle

        public_key_b64 : typing.Optional[str]
            Optional Ed25519 public key (base64) for V1. Falls back to signer.public_key_b64.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerificationResult
            Verification result

        Examples
        --------
        from fern import (
            BundleManifest,
            CitizenshipBundleV2,
            CompositeSignature,
            CompositeSignatureClassical,
            CompositeSignaturePq,
            FernApi,
            SignedBundleV2,
            SignedBundleV2Signature,
            SignedPayload,
        )

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.verification.verify_bundle(
            signed_bundle=SignedBundleV2(
                bundle=CitizenshipBundleV2(
                    dcp_bundle_version="2.0",
                    manifest=BundleManifest(
                        session_nonce="a1b2c3...",
                        rpr_hash="sha256:...",
                        passport_hash="sha256:...",
                        intent_hash="sha256:...",
                        policy_hash="sha256:...",
                        audit_merkle_root="sha256:...",
                        audit_count=1,
                    ),
                    responsible_principal_record=SignedPayload(
                        payload={"key": "value"},
                        composite_sig=CompositeSignature(),
                    ),
                    agent_passport=SignedPayload(
                        payload={"key": "value"},
                        composite_sig=CompositeSignature(),
                    ),
                    intent=SignedPayload(
                        payload={"key": "value"},
                        composite_sig=CompositeSignature(),
                    ),
                    policy_decision=SignedPayload(
                        payload={"key": "value"},
                        composite_sig=CompositeSignature(),
                    ),
                    audit_entries=[{"key": "value"}],
                ),
                signature=SignedBundleV2Signature(
                    composite_sig=CompositeSignature(
                        classical=CompositeSignatureClassical(
                            alg="ed25519",
                            kid="abc123",
                            sig_b64="...",
                        ),
                        pq=CompositeSignaturePq(
                            alg="ml-dsa-65",
                            kid="def456",
                            sig_b64="...",
                        ),
                        binding="pq_over_classical",
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.verify_bundle(
            signed_bundle=signed_bundle, public_key_b64=public_key_b64, request_options=request_options
        )
        return _response.data

    def verify_bundle_v2(
        self,
        *,
        signed_bundle: typing.Optional[SignedBundleV2] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VerifyBundleV2Response:
        """
        Performs tier-aware V2 bundle verification including composite signature
        validation, session binding, manifest integrity, and security tier enforcement.

        Parameters
        ----------
        signed_bundle : typing.Optional[SignedBundleV2]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyBundleV2Response
            V2 verification result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.verification.verify_bundle_v2()
        """
        _response = self._raw_client.verify_bundle_v2(signed_bundle=signed_bundle, request_options=request_options)
        return _response.data


class AsyncVerificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVerificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVerificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVerificationClient
        """
        return self._raw_client

    async def verify_bundle(
        self,
        *,
        signed_bundle: VerifyBundleRequestSignedBundle,
        public_key_b64: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VerificationResult:
        """
        Performs full DCP verification with automatic version detection:

        V1: Schema validation, Ed25519 signature, bundle hash integrity,
        Merkle root, intent hash chain, and previous hash chain verification.

        V2: Composite signature structure, session nonce consistency,
        manifest integrity, tier-aware policy enforcement.

        Parameters
        ----------
        signed_bundle : VerifyBundleRequestSignedBundle

        public_key_b64 : typing.Optional[str]
            Optional Ed25519 public key (base64) for V1. Falls back to signer.public_key_b64.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerificationResult
            Verification result

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            BundleManifest,
            CitizenshipBundleV2,
            CompositeSignature,
            CompositeSignatureClassical,
            CompositeSignaturePq,
            SignedBundleV2,
            SignedBundleV2Signature,
            SignedPayload,
        )

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.verification.verify_bundle(
                signed_bundle=SignedBundleV2(
                    bundle=CitizenshipBundleV2(
                        dcp_bundle_version="2.0",
                        manifest=BundleManifest(
                            session_nonce="a1b2c3...",
                            rpr_hash="sha256:...",
                            passport_hash="sha256:...",
                            intent_hash="sha256:...",
                            policy_hash="sha256:...",
                            audit_merkle_root="sha256:...",
                            audit_count=1,
                        ),
                        responsible_principal_record=SignedPayload(
                            payload={"key": "value"},
                            composite_sig=CompositeSignature(),
                        ),
                        agent_passport=SignedPayload(
                            payload={"key": "value"},
                            composite_sig=CompositeSignature(),
                        ),
                        intent=SignedPayload(
                            payload={"key": "value"},
                            composite_sig=CompositeSignature(),
                        ),
                        policy_decision=SignedPayload(
                            payload={"key": "value"},
                            composite_sig=CompositeSignature(),
                        ),
                        audit_entries=[{"key": "value"}],
                    ),
                    signature=SignedBundleV2Signature(
                        composite_sig=CompositeSignature(
                            classical=CompositeSignatureClassical(
                                alg="ed25519",
                                kid="abc123",
                                sig_b64="...",
                            ),
                            pq=CompositeSignaturePq(
                                alg="ml-dsa-65",
                                kid="def456",
                                sig_b64="...",
                            ),
                            binding="pq_over_classical",
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_bundle(
            signed_bundle=signed_bundle, public_key_b64=public_key_b64, request_options=request_options
        )
        return _response.data

    async def verify_bundle_v2(
        self,
        *,
        signed_bundle: typing.Optional[SignedBundleV2] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VerifyBundleV2Response:
        """
        Performs tier-aware V2 bundle verification including composite signature
        validation, session binding, manifest integrity, and security tier enforcement.

        Parameters
        ----------
        signed_bundle : typing.Optional[SignedBundleV2]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyBundleV2Response
            V2 verification result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.verification.verify_bundle_v2()


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_bundle_v2(
            signed_bundle=signed_bundle, request_options=request_options
        )
        return _response.data
