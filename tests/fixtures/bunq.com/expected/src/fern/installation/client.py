

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.installation_create import InstallationCreate
from ..types.installation_listing import InstallationListing
from ..types.installation_read import InstallationRead
from .raw_client import AsyncRawInstallationClient, RawInstallationClient


OMIT = typing.cast(typing.Any, ...)


class InstallationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInstallationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInstallationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInstallationClient
        """
        return self._raw_client

    def list_all_installation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstallationListing]:
        """
        You must have an active session to make this call. This call returns the Id of the the Installation you are using in your session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstallationListing]
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.

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
        client.installation.list_all_installation()
        """
        _response = self._raw_client.list_all_installation(request_options=request_options)
        return _response.data

    def create_installation(
        self, *, client_public_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InstallationCreate:
        """
        This is the only API call that does not require you to use the "X-Bunq-Client-Authentication" and "X-Bunq-Client-Signature" headers.
         You provide the server with the public part of the key pair that you are going to use to create the value of the signature header for all future API calls. The server creates an installation for you. Store the Installation Token and ServerPublicKey from the response. This token is used in the "X-Bunq-Client-Authentication" header for the creation of a DeviceServer and SessionServer.

        Parameters
        ----------
        client_public_key : str
            Your public key. This is the public part of the key pair that you are going to use to create value of the "X-Bunq-Client-Signature" header for all future API calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstallationCreate
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.

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
        client.installation.create_installation(
            client_public_key="client_public_key",
        )
        """
        _response = self._raw_client.create_installation(
            client_public_key=client_public_key, request_options=request_options
        )
        return _response.data

    def read_installation(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InstallationRead:
        """
        You must have an active session to make this call. This call is used to check whether the Id you provide is the Id of your current installation or not.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstallationRead
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.

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
        client.installation.read_installation(
            item_id=1,
        )
        """
        _response = self._raw_client.read_installation(item_id, request_options=request_options)
        return _response.data


class AsyncInstallationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInstallationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInstallationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInstallationClient
        """
        return self._raw_client

    async def list_all_installation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstallationListing]:
        """
        You must have an active session to make this call. This call returns the Id of the the Installation you are using in your session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstallationListing]
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.

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
            await client.installation.list_all_installation()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_installation(request_options=request_options)
        return _response.data

    async def create_installation(
        self, *, client_public_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InstallationCreate:
        """
        This is the only API call that does not require you to use the "X-Bunq-Client-Authentication" and "X-Bunq-Client-Signature" headers.
         You provide the server with the public part of the key pair that you are going to use to create the value of the signature header for all future API calls. The server creates an installation for you. Store the Installation Token and ServerPublicKey from the response. This token is used in the "X-Bunq-Client-Authentication" header for the creation of a DeviceServer and SessionServer.

        Parameters
        ----------
        client_public_key : str
            Your public key. This is the public part of the key pair that you are going to use to create value of the "X-Bunq-Client-Signature" header for all future API calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstallationCreate
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.

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
            await client.installation.create_installation(
                client_public_key="client_public_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_installation(
            client_public_key=client_public_key, request_options=request_options
        )
        return _response.data

    async def read_installation(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InstallationRead:
        """
        You must have an active session to make this call. This call is used to check whether the Id you provide is the Id of your current installation or not.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstallationRead
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.

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
            await client.installation.read_installation(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_installation(item_id, request_options=request_options)
        return _response.data
