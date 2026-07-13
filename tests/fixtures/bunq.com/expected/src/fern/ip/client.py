

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.permitted_ip_create import PermittedIpCreate
from ..types.permitted_ip_listing import PermittedIpListing
from ..types.permitted_ip_read import PermittedIpRead
from ..types.permitted_ip_update import PermittedIpUpdate
from .raw_client import AsyncRawIpClient, RawIpClient


OMIT = typing.cast(typing.Any, ...)


class IpClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIpClient
        """
        return self._raw_client

    def list_all_ip_for_user_credential_password_ip(
        self, user_id: int, credential_password_ip_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PermittedIpListing]:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PermittedIpListing]
            Manage the IPs which may be used for a credential of a user for server authentication.

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
        client.ip.list_all_ip_for_user_credential_password_ip(
            user_id=1,
            credential_password_ip_id=1,
        )
        """
        _response = self._raw_client.list_all_ip_for_user_credential_password_ip(
            user_id, credential_password_ip_id, request_options=request_options
        )
        return _response.data

    def create_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        *,
        ip: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PermittedIpCreate:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        ip : str
            The IP address.

        status : typing.Optional[str]
            The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PermittedIpCreate
            Manage the IPs which may be used for a credential of a user for server authentication.

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
        client.ip.create_ip_for_user_credential_password_ip(
            user_id=1,
            credential_password_ip_id=1,
            ip="ip",
        )
        """
        _response = self._raw_client.create_ip_for_user_credential_password_ip(
            user_id, credential_password_ip_id, ip=ip, status=status, request_options=request_options
        )
        return _response.data

    def read_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PermittedIpRead:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PermittedIpRead
            Manage the IPs which may be used for a credential of a user for server authentication.

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
        client.ip.read_ip_for_user_credential_password_ip(
            user_id=1,
            credential_password_ip_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_ip_for_user_credential_password_ip(
            user_id, credential_password_ip_id, item_id, request_options=request_options
        )
        return _response.data

    def update_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        item_id: int,
        *,
        ip: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PermittedIpUpdate:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        item_id : int


        ip : str
            The IP address.

        status : typing.Optional[str]
            The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PermittedIpUpdate
            Manage the IPs which may be used for a credential of a user for server authentication.

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
        client.ip.update_ip_for_user_credential_password_ip(
            user_id=1,
            credential_password_ip_id=1,
            item_id=1,
            ip="ip",
        )
        """
        _response = self._raw_client.update_ip_for_user_credential_password_ip(
            user_id, credential_password_ip_id, item_id, ip=ip, status=status, request_options=request_options
        )
        return _response.data


class AsyncIpClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIpClient
        """
        return self._raw_client

    async def list_all_ip_for_user_credential_password_ip(
        self, user_id: int, credential_password_ip_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PermittedIpListing]:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PermittedIpListing]
            Manage the IPs which may be used for a credential of a user for server authentication.

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
            await client.ip.list_all_ip_for_user_credential_password_ip(
                user_id=1,
                credential_password_ip_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_ip_for_user_credential_password_ip(
            user_id, credential_password_ip_id, request_options=request_options
        )
        return _response.data

    async def create_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        *,
        ip: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PermittedIpCreate:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        ip : str
            The IP address.

        status : typing.Optional[str]
            The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PermittedIpCreate
            Manage the IPs which may be used for a credential of a user for server authentication.

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
            await client.ip.create_ip_for_user_credential_password_ip(
                user_id=1,
                credential_password_ip_id=1,
                ip="ip",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_ip_for_user_credential_password_ip(
            user_id, credential_password_ip_id, ip=ip, status=status, request_options=request_options
        )
        return _response.data

    async def read_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PermittedIpRead:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PermittedIpRead
            Manage the IPs which may be used for a credential of a user for server authentication.

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
            await client.ip.read_ip_for_user_credential_password_ip(
                user_id=1,
                credential_password_ip_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_ip_for_user_credential_password_ip(
            user_id, credential_password_ip_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_ip_for_user_credential_password_ip(
        self,
        user_id: int,
        credential_password_ip_id: int,
        item_id: int,
        *,
        ip: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PermittedIpUpdate:
        """
        Manage the IPs which may be used for a credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        credential_password_ip_id : int


        item_id : int


        ip : str
            The IP address.

        status : typing.Optional[str]
            The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PermittedIpUpdate
            Manage the IPs which may be used for a credential of a user for server authentication.

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
            await client.ip.update_ip_for_user_credential_password_ip(
                user_id=1,
                credential_password_ip_id=1,
                item_id=1,
                ip="ip",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_ip_for_user_credential_password_ip(
            user_id, credential_password_ip_id, item_id, ip=ip, status=status, request_options=request_options
        )
        return _response.data
