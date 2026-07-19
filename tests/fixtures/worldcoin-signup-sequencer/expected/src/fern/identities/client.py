

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.inclusion_proof import InclusionProof
from .raw_client import AsyncRawIdentitiesClient, RawIdentitiesClient
from .types.get_v3identities_commitment_inclusion_proof_inclusion_proof_type_request_inclusion_proof_type import (
    GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType,
)


class IdentitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentitiesClient
        """
        return self._raw_client

    def add_new_identity_to_the_queue(
        self, commitment: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add a new identity commitment to the sequencer queue.
        V3 differs from V2 in that it allows re-adding deleted identities.
        If the identity was previously deleted and the leaf index contains Hash::ZERO,
        it can be re-added.

        Parameters
        ----------
        commitment : str
            Identity commitment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.identities.add_new_identity_to_the_queue(
            commitment="commitment",
        )
        """
        _response = self._raw_client.add_new_identity_to_the_queue(commitment, request_options=request_options)
        return _response.data

    def add_identity_removal_to_the_queue(
        self, commitment: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        commitment : str
            Identity commitment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.identities.add_identity_removal_to_the_queue(
            commitment="commitment",
        )
        """
        _response = self._raw_client.add_identity_removal_to_the_queue(commitment, request_options=request_options)
        return _response.data

    def get_inclusion_proof_of_identity_by_proof_type(
        self,
        commitment: str,
        inclusion_proof_type: GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InclusionProof:
        """
        Returns inclusion proof for the specified identity at different stages:
        - `processed`: Proof from the processed tree (latest committed batch)
        - `mined`: Proof from the mined tree (on-chain confirmed)
        - `bridged`: Proof from the bridged tree (cross-chain confirmed)

        Parameters
        ----------
        commitment : str
            Identity commitment

        inclusion_proof_type : GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType
            Type of inclusion proof to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InclusionProof
            OK

        Examples
        --------
        from fern.identities import (
            GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType,
        )

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.identities.get_inclusion_proof_of_identity_by_proof_type(
            commitment="commitment",
            inclusion_proof_type=GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType.PROCESSED,
        )
        """
        _response = self._raw_client.get_inclusion_proof_of_identity_by_proof_type(
            commitment, inclusion_proof_type, request_options=request_options
        )
        return _response.data


class AsyncIdentitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentitiesClient
        """
        return self._raw_client

    async def add_new_identity_to_the_queue(
        self, commitment: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add a new identity commitment to the sequencer queue.
        V3 differs from V2 in that it allows re-adding deleted identities.
        If the identity was previously deleted and the leaf index contains Hash::ZERO,
        it can be re-added.

        Parameters
        ----------
        commitment : str
            Identity commitment

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.identities.add_new_identity_to_the_queue(
                commitment="commitment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_new_identity_to_the_queue(commitment, request_options=request_options)
        return _response.data

    async def add_identity_removal_to_the_queue(
        self, commitment: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        commitment : str
            Identity commitment

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.identities.add_identity_removal_to_the_queue(
                commitment="commitment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_identity_removal_to_the_queue(
            commitment, request_options=request_options
        )
        return _response.data

    async def get_inclusion_proof_of_identity_by_proof_type(
        self,
        commitment: str,
        inclusion_proof_type: GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InclusionProof:
        """
        Returns inclusion proof for the specified identity at different stages:
        - `processed`: Proof from the processed tree (latest committed batch)
        - `mined`: Proof from the mined tree (on-chain confirmed)
        - `bridged`: Proof from the bridged tree (cross-chain confirmed)

        Parameters
        ----------
        commitment : str
            Identity commitment

        inclusion_proof_type : GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType
            Type of inclusion proof to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InclusionProof
            OK

        Examples
        --------
        import asyncio

        from fern.identities import (
            GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.identities.get_inclusion_proof_of_identity_by_proof_type(
                commitment="commitment",
                inclusion_proof_type=GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType.PROCESSED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_inclusion_proof_of_identity_by_proof_type(
            commitment, inclusion_proof_type, request_options=request_options
        )
        return _response.data
