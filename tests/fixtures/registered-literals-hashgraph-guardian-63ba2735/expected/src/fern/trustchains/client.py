

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.trust_chains import TrustChains
from ..types.verifiable_presentation import VerifiablePresentation
from .raw_client import AsyncRawTrustchainsClient, RawTrustchainsClient


class TrustchainsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrustchainsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrustchainsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrustchainsClient
        """
        return self._raw_client

    def returns_a_list_of_all_vp_documents(
        self,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        policy_id: typing.Optional[str] = None,
        policy_owner: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[VerifiablePresentation]:
        """
        Requests all VP documents. Only users with the Auditor role are allowed to make the request.

        Parameters
        ----------
        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        policy_id : typing.Optional[str]
            Selected policy ID.

        policy_owner : typing.Optional[str]
            Selected Standard Registry (DID).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[VerifiablePresentation]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.trustchains.returns_a_list_of_all_vp_documents()
        """
        _response = self._raw_client.returns_a_list_of_all_vp_documents(
            page_index=page_index,
            page_size=page_size,
            policy_id=policy_id,
            policy_owner=policy_owner,
            request_options=request_options,
        )
        return _response.data

    def returns_a_trustchain_for_a_vp_document(
        self, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrustChains:
        """
        Builds and returns a trustchain, from the VP to the root VC document. Only users with the Auditor role are allowed to make the request.

        Parameters
        ----------
        hash : str
            Hash or ID of a VP document.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustChains
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.trustchains.returns_a_trustchain_for_a_vp_document(
            hash="hash",
        )
        """
        _response = self._raw_client.returns_a_trustchain_for_a_vp_document(hash, request_options=request_options)
        return _response.data


class AsyncTrustchainsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrustchainsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrustchainsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrustchainsClient
        """
        return self._raw_client

    async def returns_a_list_of_all_vp_documents(
        self,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        policy_id: typing.Optional[str] = None,
        policy_owner: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[VerifiablePresentation]:
        """
        Requests all VP documents. Only users with the Auditor role are allowed to make the request.

        Parameters
        ----------
        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        policy_id : typing.Optional[str]
            Selected policy ID.

        policy_owner : typing.Optional[str]
            Selected Standard Registry (DID).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[VerifiablePresentation]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.trustchains.returns_a_list_of_all_vp_documents()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_all_vp_documents(
            page_index=page_index,
            page_size=page_size,
            policy_id=policy_id,
            policy_owner=policy_owner,
            request_options=request_options,
        )
        return _response.data

    async def returns_a_trustchain_for_a_vp_document(
        self, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrustChains:
        """
        Builds and returns a trustchain, from the VP to the root VC document. Only users with the Auditor role are allowed to make the request.

        Parameters
        ----------
        hash : str
            Hash or ID of a VP document.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustChains
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.trustchains.returns_a_trustchain_for_a_vp_document(
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_trustchain_for_a_vp_document(hash, request_options=request_options)
        return _response.data
