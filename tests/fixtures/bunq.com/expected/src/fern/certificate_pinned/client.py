

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.certificate import Certificate
from ..types.certificate_pinned_create import CertificatePinnedCreate
from ..types.certificate_pinned_delete import CertificatePinnedDelete
from ..types.certificate_pinned_listing import CertificatePinnedListing
from ..types.certificate_pinned_read import CertificatePinnedRead
from .raw_client import AsyncRawCertificatePinnedClient, RawCertificatePinnedClient


OMIT = typing.cast(typing.Any, ...)


class CertificatePinnedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCertificatePinnedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCertificatePinnedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCertificatePinnedClient
        """
        return self._raw_client

    def list_all_certificate_pinned_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CertificatePinnedListing]:
        """
        List all the pinned certificate chain for the given user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CertificatePinnedListing]
            This endpoint allow you to pin the certificate chains to your account. These certificate chains are used for SSL validation whenever a callback is initiated to one of your https callback urls.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.certificate_pinned.list_all_certificate_pinned_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_certificate_pinned_for_user(user_id, request_options=request_options)
        return _response.data

    def create_certificate_pinned_for_user(
        self,
        user_id: int,
        *,
        certificate_chain: typing.Sequence[Certificate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertificatePinnedCreate:
        """
        Pin the certificate chain.

        Parameters
        ----------
        user_id : int


        certificate_chain : typing.Sequence[Certificate]
            The certificate chain in .PEM format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertificatePinnedCreate
            This endpoint allow you to pin the certificate chains to your account. These certificate chains are used for SSL validation whenever a callback is initiated to one of your https callback urls.

        Examples
        --------
        from fern import Certificate, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.certificate_pinned.create_certificate_pinned_for_user(
            user_id=1,
            certificate_chain=[Certificate()],
        )
        """
        _response = self._raw_client.create_certificate_pinned_for_user(
            user_id, certificate_chain=certificate_chain, request_options=request_options
        )
        return _response.data

    def read_certificate_pinned_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CertificatePinnedRead:
        """
        Get the pinned certificate chain with the specified ID.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertificatePinnedRead
            This endpoint allow you to pin the certificate chains to your account. These certificate chains are used for SSL validation whenever a callback is initiated to one of your https callback urls.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.certificate_pinned.read_certificate_pinned_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_certificate_pinned_for_user(user_id, item_id, request_options=request_options)
        return _response.data

    def delete_certificate_pinned_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CertificatePinnedDelete:
        """
        Remove the pinned certificate chain with the specific ID.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertificatePinnedDelete
            This endpoint allow you to pin the certificate chains to your account. These certificate chains are used for SSL validation whenever a callback is initiated to one of your https callback urls.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.certificate_pinned.delete_certificate_pinned_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_certificate_pinned_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncCertificatePinnedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCertificatePinnedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCertificatePinnedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCertificatePinnedClient
        """
        return self._raw_client

    async def list_all_certificate_pinned_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CertificatePinnedListing]:
        """
        List all the pinned certificate chain for the given user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CertificatePinnedListing]
            This endpoint allow you to pin the certificate chains to your account. These certificate chains are used for SSL validation whenever a callback is initiated to one of your https callback urls.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.certificate_pinned.list_all_certificate_pinned_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_certificate_pinned_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_certificate_pinned_for_user(
        self,
        user_id: int,
        *,
        certificate_chain: typing.Sequence[Certificate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertificatePinnedCreate:
        """
        Pin the certificate chain.

        Parameters
        ----------
        user_id : int


        certificate_chain : typing.Sequence[Certificate]
            The certificate chain in .PEM format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertificatePinnedCreate
            This endpoint allow you to pin the certificate chains to your account. These certificate chains are used for SSL validation whenever a callback is initiated to one of your https callback urls.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Certificate

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.certificate_pinned.create_certificate_pinned_for_user(
                user_id=1,
                certificate_chain=[Certificate()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_certificate_pinned_for_user(
            user_id, certificate_chain=certificate_chain, request_options=request_options
        )
        return _response.data

    async def read_certificate_pinned_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CertificatePinnedRead:
        """
        Get the pinned certificate chain with the specified ID.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertificatePinnedRead
            This endpoint allow you to pin the certificate chains to your account. These certificate chains are used for SSL validation whenever a callback is initiated to one of your https callback urls.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.certificate_pinned.read_certificate_pinned_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_certificate_pinned_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    async def delete_certificate_pinned_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CertificatePinnedDelete:
        """
        Remove the pinned certificate chain with the specific ID.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertificatePinnedDelete
            This endpoint allow you to pin the certificate chains to your account. These certificate chains are used for SSL validation whenever a callback is initiated to one of your https callback urls.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.certificate_pinned.delete_certificate_pinned_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_certificate_pinned_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
