

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.field_element import FieldElement
from ..types.semaphore_proof import SemaphoreProof
from ..types.semaphore_proof_verification_result import SemaphoreProofVerificationResult
from .raw_client import AsyncRawSemaphoreProofClient, RawSemaphoreProofClient


OMIT = typing.cast(typing.Any, ...)


class SemaphoreProofClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSemaphoreProofClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSemaphoreProofClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSemaphoreProofClient
        """
        return self._raw_client

    def verify_semaphore_proof(
        self,
        *,
        root: FieldElement,
        signal_hash: FieldElement,
        nullifier_hash: FieldElement,
        external_nullifier_hash: FieldElement,
        proof: SemaphoreProof,
        max_root_age_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SemaphoreProofVerificationResult:
        """
        Parameters
        ----------
        root : FieldElement

        signal_hash : FieldElement

        nullifier_hash : FieldElement

        external_nullifier_hash : FieldElement

        proof : SemaphoreProof

        max_root_age_seconds : typing.Optional[int]
            Maximum age of the root in seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SemaphoreProofVerificationResult
            Verification processed, check response for result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.semaphore_proof.verify_semaphore_proof(
            root="0x00000abbda2bb9080713c20975bd1b711ebcd413e52a2a5d4c1d6114cb179b0f",
            signal_hash="0x000041b9e22987d04f56445733b5b351693afd82f0584e3442de71adfcd408ca",
            nullifier_hash="0x000012e8498adcc7a2e04ac3c4ef82ee13db7a710a7174b9623fdb8c8ccd38fd",
            external_nullifier_hash="0x000003282d8e4502363cf69bf7d236bd777b8aab7a232bb96b1a17ec2bbb029a",
            proof=[
                [
                    "0x000012bab4c2b8ee80203b053f7edd25408ce4898f9ee48cd1cf5fa05b382258",
                    "0x0000ffed4784db6fd39228c98015be3332bf594460340301dd02e05ccad3a7e5",
                ],
                [
                    [
                        "0x0000ba984420b405e2102ec8a3f991d207ae29b65804d4b9ab41f752fcd6f9b0",
                        "0x000072d536482dd3f680a869050426cb0230b0aaf999b89206848406c6b070ac",
                    ],
                    [
                        "0x000059f64d1f40212a4be836ec09c1bc675b3315e2f0a6343f7c3c96dac99941",
                        "0x0000ea95958f6182420c86be4e1507f640d77ba9f377bbf3025ff196067411a3",
                    ],
                ],
                [
                    "0x00007c66ab60056f9e021d55f98ea3e6e9ce8db0ef5ca3af6b2c8db1b3018425",
                    "0x0000c0eb8ef9f315815947adce6ed324f49b58a544a37a77185eab9a7202ca1b",
                ],
            ],
            max_root_age_seconds=3600,
        )
        """
        _response = self._raw_client.verify_semaphore_proof(
            root=root,
            signal_hash=signal_hash,
            nullifier_hash=nullifier_hash,
            external_nullifier_hash=external_nullifier_hash,
            proof=proof,
            max_root_age_seconds=max_root_age_seconds,
            request_options=request_options,
        )
        return _response.data


class AsyncSemaphoreProofClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSemaphoreProofClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSemaphoreProofClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSemaphoreProofClient
        """
        return self._raw_client

    async def verify_semaphore_proof(
        self,
        *,
        root: FieldElement,
        signal_hash: FieldElement,
        nullifier_hash: FieldElement,
        external_nullifier_hash: FieldElement,
        proof: SemaphoreProof,
        max_root_age_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SemaphoreProofVerificationResult:
        """
        Parameters
        ----------
        root : FieldElement

        signal_hash : FieldElement

        nullifier_hash : FieldElement

        external_nullifier_hash : FieldElement

        proof : SemaphoreProof

        max_root_age_seconds : typing.Optional[int]
            Maximum age of the root in seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SemaphoreProofVerificationResult
            Verification processed, check response for result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.semaphore_proof.verify_semaphore_proof(
                root="0x00000abbda2bb9080713c20975bd1b711ebcd413e52a2a5d4c1d6114cb179b0f",
                signal_hash="0x000041b9e22987d04f56445733b5b351693afd82f0584e3442de71adfcd408ca",
                nullifier_hash="0x000012e8498adcc7a2e04ac3c4ef82ee13db7a710a7174b9623fdb8c8ccd38fd",
                external_nullifier_hash="0x000003282d8e4502363cf69bf7d236bd777b8aab7a232bb96b1a17ec2bbb029a",
                proof=[
                    [
                        "0x000012bab4c2b8ee80203b053f7edd25408ce4898f9ee48cd1cf5fa05b382258",
                        "0x0000ffed4784db6fd39228c98015be3332bf594460340301dd02e05ccad3a7e5",
                    ],
                    [
                        [
                            "0x0000ba984420b405e2102ec8a3f991d207ae29b65804d4b9ab41f752fcd6f9b0",
                            "0x000072d536482dd3f680a869050426cb0230b0aaf999b89206848406c6b070ac",
                        ],
                        [
                            "0x000059f64d1f40212a4be836ec09c1bc675b3315e2f0a6343f7c3c96dac99941",
                            "0x0000ea95958f6182420c86be4e1507f640d77ba9f377bbf3025ff196067411a3",
                        ],
                    ],
                    [
                        "0x00007c66ab60056f9e021d55f98ea3e6e9ce8db0ef5ca3af6b2c8db1b3018425",
                        "0x0000c0eb8ef9f315815947adce6ed324f49b58a544a37a77185eab9a7202ca1b",
                    ],
                ],
                max_root_age_seconds=3600,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_semaphore_proof(
            root=root,
            signal_hash=signal_hash,
            nullifier_hash=nullifier_hash,
            external_nullifier_hash=external_nullifier_hash,
            proof=proof,
            max_root_age_seconds=max_root_age_seconds,
            request_options=request_options,
        )
        return _response.data
