

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ipsec_crypto_profiles_ah import IpsecCryptoProfilesAh
from ..types.ipsec_crypto_profiles_dh_group import IpsecCryptoProfilesDhGroup
from ..types.ipsec_crypto_profiles_esp import IpsecCryptoProfilesEsp
from ..types.ipsec_crypto_profiles_response import IpsecCryptoProfilesResponse
from ..types.lifesize import Lifesize
from ..types.lifetime import Lifetime
from ..types.uuid_response import UuidResponse
from .raw_client import AsyncRawIpSecCryptoProfilesClient, RawIpSecCryptoProfilesClient
from .types.get_v1ipsec_crypto_profiles_read_response import GetV1IpsecCryptoProfilesReadResponse


OMIT = typing.cast(typing.Any, ...)


class IpSecCryptoProfilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIpSecCryptoProfilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIpSecCryptoProfilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIpSecCryptoProfilesClient
        """
        return self._raw_client

    def get_v1ipsec_crypto_profiles(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> IpsecCryptoProfilesResponse:
        """
        Lists the status of IPSec Crypto Profiles. Shows results of create, modify, and delete actions with their associated UUIDs.
        Users can perform these actions and then use this GET request to verify the status by referencing the UUID received during the initial action.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpsecCryptoProfilesResponse
            Status of the created IPSEC Crypto Profiles.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ip_sec_crypto_profiles.get_v1ipsec_crypto_profiles(
            id="id",
        )
        """
        _response = self._raw_client.get_v1ipsec_crypto_profiles(id=id, request_options=request_options)
        return _response.data

    def post_v1ipsec_crypto_profiles(
        self,
        *,
        lifetime: Lifetime,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        ah: typing.Optional[IpsecCryptoProfilesAh] = OMIT,
        dh_group: typing.Optional[IpsecCryptoProfilesDhGroup] = OMIT,
        esp: typing.Optional[IpsecCryptoProfilesEsp] = OMIT,
        lifesize: typing.Optional[Lifesize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create an IPSec crypto profile.

        Parameters
        ----------
        lifetime : Lifetime

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ah : typing.Optional[IpsecCryptoProfilesAh]

        dh_group : typing.Optional[IpsecCryptoProfilesDhGroup]
            phase-2 DH group (PFS DH group)

        esp : typing.Optional[IpsecCryptoProfilesEsp]

        lifesize : typing.Optional[Lifesize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        from fern import FernApi, LifetimeSeconds

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ip_sec_crypto_profiles.post_v1ipsec_crypto_profiles(
            lifetime=LifetimeSeconds(),
            name="name",
        )
        """
        _response = self._raw_client.post_v1ipsec_crypto_profiles(
            lifetime=lifetime,
            name=name,
            sub_tenant_name=sub_tenant_name,
            ah=ah,
            dh_group=dh_group,
            esp=esp,
            lifesize=lifesize,
            request_options=request_options,
        )
        return _response.data

    def put_v1ipsec_crypto_profiles(
        self,
        *,
        lifetime: Lifetime,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        ah: typing.Optional[IpsecCryptoProfilesAh] = OMIT,
        dh_group: typing.Optional[IpsecCryptoProfilesDhGroup] = OMIT,
        esp: typing.Optional[IpsecCryptoProfilesEsp] = OMIT,
        lifesize: typing.Optional[Lifesize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Edit an IPSec crypto profile.

        Parameters
        ----------
        lifetime : Lifetime

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ah : typing.Optional[IpsecCryptoProfilesAh]

        dh_group : typing.Optional[IpsecCryptoProfilesDhGroup]
            phase-2 DH group (PFS DH group)

        esp : typing.Optional[IpsecCryptoProfilesEsp]

        lifesize : typing.Optional[Lifesize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        from fern import FernApi, LifetimeSeconds

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ip_sec_crypto_profiles.put_v1ipsec_crypto_profiles(
            lifetime=LifetimeSeconds(),
            name="name",
        )
        """
        _response = self._raw_client.put_v1ipsec_crypto_profiles(
            lifetime=lifetime,
            name=name,
            sub_tenant_name=sub_tenant_name,
            ah=ah,
            dh_group=dh_group,
            esp=esp,
            lifesize=lifesize,
            request_options=request_options,
        )
        return _response.data

    def delete_v1ipsec_crypto_profiles(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Delete an IPSec crypto profile.

        Parameters
        ----------
        name : str
            IPSEC Crypto Profile name.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ip_sec_crypto_profiles.delete_v1ipsec_crypto_profiles(
            name="name",
        )
        """
        _response = self._raw_client.delete_v1ipsec_crypto_profiles(
            name=name, sub_tenant_name=sub_tenant_name, request_options=request_options
        )
        return _response.data

    def get_v1ipsec_crypto_profiles_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1IpsecCryptoProfilesReadResponse:
        """
        You can read a list of Internet Protocol Security (IPSec) crypto profiles configurations that are created.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1IpsecCryptoProfilesReadResponse
            List of IPSEC Crypto Profiles configurations.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ip_sec_crypto_profiles.get_v1ipsec_crypto_profiles_read(
            id="id",
        )
        """
        _response = self._raw_client.get_v1ipsec_crypto_profiles_read(id=id, request_options=request_options)
        return _response.data

    def post_v1ipsec_crypto_profiles_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        ipsec_crypto_profiles_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create a request to read a list IPSec Crypto Profile.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ipsec_crypto_profiles_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ip_sec_crypto_profiles.post_v1ipsec_crypto_profiles_read()
        """
        _response = self._raw_client.post_v1ipsec_crypto_profiles_read(
            sub_tenant_name=sub_tenant_name,
            ipsec_crypto_profiles_names=ipsec_crypto_profiles_names,
            request_options=request_options,
        )
        return _response.data


class AsyncIpSecCryptoProfilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIpSecCryptoProfilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIpSecCryptoProfilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIpSecCryptoProfilesClient
        """
        return self._raw_client

    async def get_v1ipsec_crypto_profiles(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> IpsecCryptoProfilesResponse:
        """
        Lists the status of IPSec Crypto Profiles. Shows results of create, modify, and delete actions with their associated UUIDs.
        Users can perform these actions and then use this GET request to verify the status by referencing the UUID received during the initial action.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpsecCryptoProfilesResponse
            Status of the created IPSEC Crypto Profiles.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ip_sec_crypto_profiles.get_v1ipsec_crypto_profiles(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1ipsec_crypto_profiles(id=id, request_options=request_options)
        return _response.data

    async def post_v1ipsec_crypto_profiles(
        self,
        *,
        lifetime: Lifetime,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        ah: typing.Optional[IpsecCryptoProfilesAh] = OMIT,
        dh_group: typing.Optional[IpsecCryptoProfilesDhGroup] = OMIT,
        esp: typing.Optional[IpsecCryptoProfilesEsp] = OMIT,
        lifesize: typing.Optional[Lifesize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create an IPSec crypto profile.

        Parameters
        ----------
        lifetime : Lifetime

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ah : typing.Optional[IpsecCryptoProfilesAh]

        dh_group : typing.Optional[IpsecCryptoProfilesDhGroup]
            phase-2 DH group (PFS DH group)

        esp : typing.Optional[IpsecCryptoProfilesEsp]

        lifesize : typing.Optional[Lifesize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LifetimeSeconds

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ip_sec_crypto_profiles.post_v1ipsec_crypto_profiles(
                lifetime=LifetimeSeconds(),
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1ipsec_crypto_profiles(
            lifetime=lifetime,
            name=name,
            sub_tenant_name=sub_tenant_name,
            ah=ah,
            dh_group=dh_group,
            esp=esp,
            lifesize=lifesize,
            request_options=request_options,
        )
        return _response.data

    async def put_v1ipsec_crypto_profiles(
        self,
        *,
        lifetime: Lifetime,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        ah: typing.Optional[IpsecCryptoProfilesAh] = OMIT,
        dh_group: typing.Optional[IpsecCryptoProfilesDhGroup] = OMIT,
        esp: typing.Optional[IpsecCryptoProfilesEsp] = OMIT,
        lifesize: typing.Optional[Lifesize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Edit an IPSec crypto profile.

        Parameters
        ----------
        lifetime : Lifetime

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ah : typing.Optional[IpsecCryptoProfilesAh]

        dh_group : typing.Optional[IpsecCryptoProfilesDhGroup]
            phase-2 DH group (PFS DH group)

        esp : typing.Optional[IpsecCryptoProfilesEsp]

        lifesize : typing.Optional[Lifesize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LifetimeSeconds

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ip_sec_crypto_profiles.put_v1ipsec_crypto_profiles(
                lifetime=LifetimeSeconds(),
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_v1ipsec_crypto_profiles(
            lifetime=lifetime,
            name=name,
            sub_tenant_name=sub_tenant_name,
            ah=ah,
            dh_group=dh_group,
            esp=esp,
            lifesize=lifesize,
            request_options=request_options,
        )
        return _response.data

    async def delete_v1ipsec_crypto_profiles(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Delete an IPSec crypto profile.

        Parameters
        ----------
        name : str
            IPSEC Crypto Profile name.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ip_sec_crypto_profiles.delete_v1ipsec_crypto_profiles(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_v1ipsec_crypto_profiles(
            name=name, sub_tenant_name=sub_tenant_name, request_options=request_options
        )
        return _response.data

    async def get_v1ipsec_crypto_profiles_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1IpsecCryptoProfilesReadResponse:
        """
        You can read a list of Internet Protocol Security (IPSec) crypto profiles configurations that are created.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1IpsecCryptoProfilesReadResponse
            List of IPSEC Crypto Profiles configurations.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ip_sec_crypto_profiles.get_v1ipsec_crypto_profiles_read(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1ipsec_crypto_profiles_read(id=id, request_options=request_options)
        return _response.data

    async def post_v1ipsec_crypto_profiles_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        ipsec_crypto_profiles_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create a request to read a list IPSec Crypto Profile.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ipsec_crypto_profiles_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ip_sec_crypto_profiles.post_v1ipsec_crypto_profiles_read()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1ipsec_crypto_profiles_read(
            sub_tenant_name=sub_tenant_name,
            ipsec_crypto_profiles_names=ipsec_crypto_profiles_names,
            request_options=request_options,
        )
        return _response.data
