

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ike_crypto_profiles_dh_group_item import IkeCryptoProfilesDhGroupItem
from ..types.ike_crypto_profiles_encryption_item import IkeCryptoProfilesEncryptionItem
from ..types.ike_crypto_profiles_hash_item import IkeCryptoProfilesHashItem
from ..types.ike_crypto_profiles_lifetime import IkeCryptoProfilesLifetime
from ..types.ike_crypto_profiles_response import IkeCryptoProfilesResponse
from ..types.uuid_response import UuidResponse
from .raw_client import AsyncRawIkeCryptoProfilesClient, RawIkeCryptoProfilesClient
from .types.get_v1ike_crypto_profiles_read_response import GetV1IkeCryptoProfilesReadResponse


OMIT = typing.cast(typing.Any, ...)


class IkeCryptoProfilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIkeCryptoProfilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIkeCryptoProfilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIkeCryptoProfilesClient
        """
        return self._raw_client

    def get_v1ike_crypto_profiles(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> IkeCryptoProfilesResponse:
        """
        Provides a status of Internet Key Exchange(IKE) Crypto Profiles created along with the UUID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IkeCryptoProfilesResponse
            Status of the created IKE Crypto Profiles.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ike_crypto_profiles.get_v1ike_crypto_profiles(
            id="id",
        )
        """
        _response = self._raw_client.get_v1ike_crypto_profiles(id=id, request_options=request_options)
        return _response.data

    def post_v1ike_crypto_profiles(
        self,
        *,
        dh_group: typing.Sequence[IkeCryptoProfilesDhGroupItem],
        encryption: typing.Sequence[IkeCryptoProfilesEncryptionItem],
        hash: typing.Sequence[IkeCryptoProfilesHashItem],
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        authentication_multiple: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        lifetime: typing.Optional[IkeCryptoProfilesLifetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create an IKE Crypto Profiles.

        Parameters
        ----------
        dh_group : typing.Sequence[IkeCryptoProfilesDhGroupItem]

        encryption : typing.Sequence[IkeCryptoProfilesEncryptionItem]
            Encryption algorithm

        hash : typing.Sequence[IkeCryptoProfilesHashItem]

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        authentication_multiple : typing.Optional[int]
            IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication disabled

        id : typing.Optional[str]
            uuid of the resource

        lifetime : typing.Optional[IkeCryptoProfilesLifetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        from fern import (
            FernApi,
            IkeCryptoProfilesDhGroupItem,
            IkeCryptoProfilesEncryptionItem,
            IkeCryptoProfilesHashItem,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ike_crypto_profiles.post_v1ike_crypto_profiles(
            dh_group=[IkeCryptoProfilesDhGroupItem.GROUP1],
            encryption=[IkeCryptoProfilesEncryptionItem.DES],
            hash=[IkeCryptoProfilesHashItem.MD5],
            name="name",
        )
        """
        _response = self._raw_client.post_v1ike_crypto_profiles(
            dh_group=dh_group,
            encryption=encryption,
            hash=hash,
            name=name,
            sub_tenant_name=sub_tenant_name,
            authentication_multiple=authentication_multiple,
            id=id,
            lifetime=lifetime,
            request_options=request_options,
        )
        return _response.data

    def put_v1ike_crypto_profiles(
        self,
        *,
        dh_group: typing.Sequence[IkeCryptoProfilesDhGroupItem],
        encryption: typing.Sequence[IkeCryptoProfilesEncryptionItem],
        hash: typing.Sequence[IkeCryptoProfilesHashItem],
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        authentication_multiple: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        lifetime: typing.Optional[IkeCryptoProfilesLifetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Edit an IKE Crypto Profiles.

        Parameters
        ----------
        dh_group : typing.Sequence[IkeCryptoProfilesDhGroupItem]

        encryption : typing.Sequence[IkeCryptoProfilesEncryptionItem]
            Encryption algorithm

        hash : typing.Sequence[IkeCryptoProfilesHashItem]

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        authentication_multiple : typing.Optional[int]
            IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication disabled

        id : typing.Optional[str]
            uuid of the resource

        lifetime : typing.Optional[IkeCryptoProfilesLifetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        from fern import (
            FernApi,
            IkeCryptoProfilesDhGroupItem,
            IkeCryptoProfilesEncryptionItem,
            IkeCryptoProfilesHashItem,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ike_crypto_profiles.put_v1ike_crypto_profiles(
            dh_group=[IkeCryptoProfilesDhGroupItem.GROUP1],
            encryption=[IkeCryptoProfilesEncryptionItem.DES],
            hash=[IkeCryptoProfilesHashItem.MD5],
            name="name",
        )
        """
        _response = self._raw_client.put_v1ike_crypto_profiles(
            dh_group=dh_group,
            encryption=encryption,
            hash=hash,
            name=name,
            sub_tenant_name=sub_tenant_name,
            authentication_multiple=authentication_multiple,
            id=id,
            lifetime=lifetime,
            request_options=request_options,
        )
        return _response.data

    def delete_v1ike_crypto_profiles(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Delete an IKE Crypto Profiles.

        Parameters
        ----------
        name : str
            IKE Crypto Profile name.

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
        client.ike_crypto_profiles.delete_v1ike_crypto_profiles(
            name="name",
        )
        """
        _response = self._raw_client.delete_v1ike_crypto_profiles(
            name=name, sub_tenant_name=sub_tenant_name, request_options=request_options
        )
        return _response.data

    def get_v1ike_crypto_profiles_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1IkeCryptoProfilesReadResponse:
        """
        Read the list of IKE Crypto Profiles.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1IkeCryptoProfilesReadResponse
            List of IKE Crypto Profiles configurations.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ike_crypto_profiles.get_v1ike_crypto_profiles_read(
            id="id",
        )
        """
        _response = self._raw_client.get_v1ike_crypto_profiles_read(id=id, request_options=request_options)
        return _response.data

    def post_v1ike_crypto_profiles_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        ike_crypto_profiles_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create a request to read the list of IKE Crypto Profiles.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ike_crypto_profiles_names : typing.Optional[typing.Sequence[str]]

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
        client.ike_crypto_profiles.post_v1ike_crypto_profiles_read()
        """
        _response = self._raw_client.post_v1ike_crypto_profiles_read(
            sub_tenant_name=sub_tenant_name,
            ike_crypto_profiles_names=ike_crypto_profiles_names,
            request_options=request_options,
        )
        return _response.data


class AsyncIkeCryptoProfilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIkeCryptoProfilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIkeCryptoProfilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIkeCryptoProfilesClient
        """
        return self._raw_client

    async def get_v1ike_crypto_profiles(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> IkeCryptoProfilesResponse:
        """
        Provides a status of Internet Key Exchange(IKE) Crypto Profiles created along with the UUID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IkeCryptoProfilesResponse
            Status of the created IKE Crypto Profiles.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ike_crypto_profiles.get_v1ike_crypto_profiles(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1ike_crypto_profiles(id=id, request_options=request_options)
        return _response.data

    async def post_v1ike_crypto_profiles(
        self,
        *,
        dh_group: typing.Sequence[IkeCryptoProfilesDhGroupItem],
        encryption: typing.Sequence[IkeCryptoProfilesEncryptionItem],
        hash: typing.Sequence[IkeCryptoProfilesHashItem],
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        authentication_multiple: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        lifetime: typing.Optional[IkeCryptoProfilesLifetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create an IKE Crypto Profiles.

        Parameters
        ----------
        dh_group : typing.Sequence[IkeCryptoProfilesDhGroupItem]

        encryption : typing.Sequence[IkeCryptoProfilesEncryptionItem]
            Encryption algorithm

        hash : typing.Sequence[IkeCryptoProfilesHashItem]

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        authentication_multiple : typing.Optional[int]
            IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication disabled

        id : typing.Optional[str]
            uuid of the resource

        lifetime : typing.Optional[IkeCryptoProfilesLifetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            IkeCryptoProfilesDhGroupItem,
            IkeCryptoProfilesEncryptionItem,
            IkeCryptoProfilesHashItem,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ike_crypto_profiles.post_v1ike_crypto_profiles(
                dh_group=[IkeCryptoProfilesDhGroupItem.GROUP1],
                encryption=[IkeCryptoProfilesEncryptionItem.DES],
                hash=[IkeCryptoProfilesHashItem.MD5],
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1ike_crypto_profiles(
            dh_group=dh_group,
            encryption=encryption,
            hash=hash,
            name=name,
            sub_tenant_name=sub_tenant_name,
            authentication_multiple=authentication_multiple,
            id=id,
            lifetime=lifetime,
            request_options=request_options,
        )
        return _response.data

    async def put_v1ike_crypto_profiles(
        self,
        *,
        dh_group: typing.Sequence[IkeCryptoProfilesDhGroupItem],
        encryption: typing.Sequence[IkeCryptoProfilesEncryptionItem],
        hash: typing.Sequence[IkeCryptoProfilesHashItem],
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        authentication_multiple: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        lifetime: typing.Optional[IkeCryptoProfilesLifetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Edit an IKE Crypto Profiles.

        Parameters
        ----------
        dh_group : typing.Sequence[IkeCryptoProfilesDhGroupItem]

        encryption : typing.Sequence[IkeCryptoProfilesEncryptionItem]
            Encryption algorithm

        hash : typing.Sequence[IkeCryptoProfilesHashItem]

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        authentication_multiple : typing.Optional[int]
            IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication disabled

        id : typing.Optional[str]
            uuid of the resource

        lifetime : typing.Optional[IkeCryptoProfilesLifetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            IkeCryptoProfilesDhGroupItem,
            IkeCryptoProfilesEncryptionItem,
            IkeCryptoProfilesHashItem,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ike_crypto_profiles.put_v1ike_crypto_profiles(
                dh_group=[IkeCryptoProfilesDhGroupItem.GROUP1],
                encryption=[IkeCryptoProfilesEncryptionItem.DES],
                hash=[IkeCryptoProfilesHashItem.MD5],
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_v1ike_crypto_profiles(
            dh_group=dh_group,
            encryption=encryption,
            hash=hash,
            name=name,
            sub_tenant_name=sub_tenant_name,
            authentication_multiple=authentication_multiple,
            id=id,
            lifetime=lifetime,
            request_options=request_options,
        )
        return _response.data

    async def delete_v1ike_crypto_profiles(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Delete an IKE Crypto Profiles.

        Parameters
        ----------
        name : str
            IKE Crypto Profile name.

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
            await client.ike_crypto_profiles.delete_v1ike_crypto_profiles(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_v1ike_crypto_profiles(
            name=name, sub_tenant_name=sub_tenant_name, request_options=request_options
        )
        return _response.data

    async def get_v1ike_crypto_profiles_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1IkeCryptoProfilesReadResponse:
        """
        Read the list of IKE Crypto Profiles.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1IkeCryptoProfilesReadResponse
            List of IKE Crypto Profiles configurations.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ike_crypto_profiles.get_v1ike_crypto_profiles_read(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1ike_crypto_profiles_read(id=id, request_options=request_options)
        return _response.data

    async def post_v1ike_crypto_profiles_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        ike_crypto_profiles_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create a request to read the list of IKE Crypto Profiles.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ike_crypto_profiles_names : typing.Optional[typing.Sequence[str]]

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
            await client.ike_crypto_profiles.post_v1ike_crypto_profiles_read()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1ike_crypto_profiles_read(
            sub_tenant_name=sub_tenant_name,
            ike_crypto_profiles_names=ike_crypto_profiles_names,
            request_options=request_options,
        )
        return _response.data
