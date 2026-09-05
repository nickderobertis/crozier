

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.content import Content
from ..types.delete_address import DeleteAddress
from ..types.export_address import ExportAddress
from ..types.import_address import ImportAddress
from ..types.list_addresses import ListAddresses
from ..types.new_address import NewAddress
from .raw_client import AsyncRawAddressRequestsClient, RawAddressRequestsClient


OMIT = typing.cast(typing.Any, ...)


class AddressRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAddressRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAddressRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAddressRequestsClient
        """
        return self._raw_client

    def delete_address(
        self,
        *,
        authorization: str,
        ethereumaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteAddress:
        """
        Deletes an existing ethereum address. Be careful when using this function.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.address_requests.delete_address(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            ethereumaddress="0x71892689ed0d79d88ab6ea3783b571b8ece9bee3",
            password="padN39QkRA2hJ",
        )
        """
        _response = self._raw_client.delete_address(
            authorization=authorization,
            ethereumaddress=ethereumaddress,
            password=password,
            request_options=request_options,
        )
        return _response.data

    def export_address(
        self,
        *,
        authorization: str,
        ethaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportAddress:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        ethaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.address_requests.export_address(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            ethaddress="0x71892889ed4d79d88ab6ea3783b571b8ece9bef4",
            password="padN39QkRA2hJ",
        )
        """
        _response = self._raw_client.export_address(
            authorization=authorization, ethaddress=ethaddress, password=password, request_options=request_options
        )
        return _response.data

    def import_address(
        self,
        *,
        authorization: str,
        content: Content,
        filename: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportAddress:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        content : Content

        filename : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportAddress


        Examples
        --------
        from fern import Cipherparams, Content, Crypto, FernApi, Kdfparams

        client = FernApi()
        client.address_requests.import_address(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            content=Content(
                address="71892889ed4d79d88ab6ea3783b571b8ece9bef4",
                crypto=Crypto(
                    cipher="aes-128-ctr",
                    cipherparams=Cipherparams(
                        iv="76e6f2497b9f2a8e024fc752a5418a6d",
                    ),
                    ciphertext="9d74262517b984f9b0560b8f23b5e3340f7be0f56b70cd91ff445dcaf5b1968f",
                    kdf="scrypt",
                    kdfparams=Kdfparams(
                        dklen=32,
                        n=131072,
                        p=1,
                        r=8,
                        salt="d11d996a7cc4bfad730d4c9b9057eff2c0fb3940b5bfc59db62ae218c14a54f4",
                    ),
                    mac="dcc342bbbbb8eea97c89b47bafc23de568fc1a48e0bd21ae8d776a95c4704ac9",
                ),
                id="85b790ff-408e-42b8-b123-bec9523964dc",
                version=3,
            ),
            filename="UTC--2020-09-19T10-42-26.196Z--71892889ed4d79d88ab6ea3783b571b8ece9bef4",
            password="padN39QkRA2hJ",
        )
        """
        _response = self._raw_client.import_address(
            authorization=authorization,
            content=content,
            filename=filename,
            password=password,
            request_options=request_options,
        )
        return _response.data

    def list_addresses(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAddresses:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAddresses


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.address_requests.list_addresses(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
        )
        """
        _response = self._raw_client.list_addresses(authorization=authorization, request_options=request_options)
        return _response.data

    def new_address(
        self, *, authorization: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> NewAddress:
        """
        Generates a new ethereum addresses you can use to send or receive funds. Do not lose the password! We can't restore access to an address if you lose it.

        Parameters
        ----------
        authorization : str
            API Key

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.address_requests.new_address(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            password="padN39QkRA2hJ",
        )
        """
        _response = self._raw_client.new_address(
            authorization=authorization, password=password, request_options=request_options
        )
        return _response.data


class AsyncAddressRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAddressRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAddressRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAddressRequestsClient
        """
        return self._raw_client

    async def delete_address(
        self,
        *,
        authorization: str,
        ethereumaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteAddress:
        """
        Deletes an existing ethereum address. Be careful when using this function.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.address_requests.delete_address(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                ethereumaddress="0x71892689ed0d79d88ab6ea3783b571b8ece9bee3",
                password="padN39QkRA2hJ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_address(
            authorization=authorization,
            ethereumaddress=ethereumaddress,
            password=password,
            request_options=request_options,
        )
        return _response.data

    async def export_address(
        self,
        *,
        authorization: str,
        ethaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportAddress:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        ethaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.address_requests.export_address(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                ethaddress="0x71892889ed4d79d88ab6ea3783b571b8ece9bef4",
                password="padN39QkRA2hJ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_address(
            authorization=authorization, ethaddress=ethaddress, password=password, request_options=request_options
        )
        return _response.data

    async def import_address(
        self,
        *,
        authorization: str,
        content: Content,
        filename: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportAddress:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        content : Content

        filename : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Cipherparams, Content, Crypto, Kdfparams

        client = AsyncFernApi()


        async def main() -> None:
            await client.address_requests.import_address(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                content=Content(
                    address="71892889ed4d79d88ab6ea3783b571b8ece9bef4",
                    crypto=Crypto(
                        cipher="aes-128-ctr",
                        cipherparams=Cipherparams(
                            iv="76e6f2497b9f2a8e024fc752a5418a6d",
                        ),
                        ciphertext="9d74262517b984f9b0560b8f23b5e3340f7be0f56b70cd91ff445dcaf5b1968f",
                        kdf="scrypt",
                        kdfparams=Kdfparams(
                            dklen=32,
                            n=131072,
                            p=1,
                            r=8,
                            salt="d11d996a7cc4bfad730d4c9b9057eff2c0fb3940b5bfc59db62ae218c14a54f4",
                        ),
                        mac="dcc342bbbbb8eea97c89b47bafc23de568fc1a48e0bd21ae8d776a95c4704ac9",
                    ),
                    id="85b790ff-408e-42b8-b123-bec9523964dc",
                    version=3,
                ),
                filename="UTC--2020-09-19T10-42-26.196Z--71892889ed4d79d88ab6ea3783b571b8ece9bef4",
                password="padN39QkRA2hJ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_address(
            authorization=authorization,
            content=content,
            filename=filename,
            password=password,
            request_options=request_options,
        )
        return _response.data

    async def list_addresses(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAddresses:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAddresses


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.address_requests.list_addresses(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_addresses(authorization=authorization, request_options=request_options)
        return _response.data

    async def new_address(
        self, *, authorization: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> NewAddress:
        """
        Generates a new ethereum addresses you can use to send or receive funds. Do not lose the password! We can't restore access to an address if you lose it.

        Parameters
        ----------
        authorization : str
            API Key

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.address_requests.new_address(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                password="padN39QkRA2hJ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.new_address(
            authorization=authorization, password=password, request_options=request_options
        )
        return _response.data
