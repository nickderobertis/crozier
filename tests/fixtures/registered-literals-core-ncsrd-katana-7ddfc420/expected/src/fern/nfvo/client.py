

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.nfvo import Nfvo
from ..types.nfvo_config import NfvoConfig
from ..types.sbi_ls import SbiLs
from .raw_client import AsyncRawNfvoClient, RawNfvoClient


OMIT = typing.cast(typing.Any, ...)


class NfvoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNfvoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNfvoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNfvoClient
        """
        return self._raw_client

    def returns_a_list_of_registered_nfv_os(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SbiLs]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SbiLs]
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nfvo.returns_a_list_of_registered_nfv_os()
        """
        _response = self._raw_client.returns_a_list_of_registered_nfv_os(request_options=request_options)
        return _response.data

    def adds_a_new_nfvo(
        self,
        *,
        id: str,
        nfvoip: str,
        nfvousername: str,
        nfvopassword: str,
        name: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[NfvoConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique id

        nfvoip : str
            NFVO's authentication URL - example: http://10.200.64.2:5000/v3/

        nfvousername : str
            The admin username

        nfvopassword : str
            The admin password

        name : typing.Optional[str]
            The name for the new NFVO

        type : typing.Optional[str]
            NFVO's type

        version : typing.Optional[str]
            The version of the NFVO's OS

        description : typing.Optional[str]
            A description for the NFVO

        config : typing.Optional[NfvoConfig]
            Optional parameters regarding the NFVO operation - example: network: flat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nfvo.adds_a_new_nfvo(
            id="id",
            nfvoip="nfvoip",
            nfvousername="nfvousername",
            nfvopassword="nfvopassword",
        )
        """
        _response = self._raw_client.adds_a_new_nfvo(
            id=id,
            nfvoip=nfvoip,
            nfvousername=nfvousername,
            nfvopassword=nfvopassword,
            name=name,
            type=type,
            version=version,
            description=description,
            config=config,
            request_options=request_options,
        )
        return _response.data

    def returns_information_about_the_given_nfvo_id(
        self, nfvo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Nfvo:
        """
        Parameters
        ----------
        nfvo_id : str
            ID of NFVO to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Nfvo
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nfvo.returns_information_about_the_given_nfvo_id(
            nfvo_id="nfvo_id",
        )
        """
        _response = self._raw_client.returns_information_about_the_given_nfvo_id(
            nfvo_id, request_options=request_options
        )
        return _response.data

    def updates_the_given_nfvo(self, nfvo_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        nfvo_id : str
            ID of NFVO to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nfvo.updates_the_given_nfvo(
            nfvo_id="nfvo_id",
        )
        """
        _response = self._raw_client.updates_the_given_nfvo(nfvo_id, request_options=request_options)
        return _response.data

    def deletes_the_given_nfvo(self, nfvo_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        nfvo_id : str
            ID of NFVO to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nfvo.deletes_the_given_nfvo(
            nfvo_id="nfvo_id",
        )
        """
        _response = self._raw_client.deletes_the_given_nfvo(nfvo_id, request_options=request_options)
        return _response.data


class AsyncNfvoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNfvoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNfvoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNfvoClient
        """
        return self._raw_client

    async def returns_a_list_of_registered_nfv_os(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SbiLs]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SbiLs]
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nfvo.returns_a_list_of_registered_nfv_os()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_registered_nfv_os(request_options=request_options)
        return _response.data

    async def adds_a_new_nfvo(
        self,
        *,
        id: str,
        nfvoip: str,
        nfvousername: str,
        nfvopassword: str,
        name: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[NfvoConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique id

        nfvoip : str
            NFVO's authentication URL - example: http://10.200.64.2:5000/v3/

        nfvousername : str
            The admin username

        nfvopassword : str
            The admin password

        name : typing.Optional[str]
            The name for the new NFVO

        type : typing.Optional[str]
            NFVO's type

        version : typing.Optional[str]
            The version of the NFVO's OS

        description : typing.Optional[str]
            A description for the NFVO

        config : typing.Optional[NfvoConfig]
            Optional parameters regarding the NFVO operation - example: network: flat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nfvo.adds_a_new_nfvo(
                id="id",
                nfvoip="nfvoip",
                nfvousername="nfvousername",
                nfvopassword="nfvopassword",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.adds_a_new_nfvo(
            id=id,
            nfvoip=nfvoip,
            nfvousername=nfvousername,
            nfvopassword=nfvopassword,
            name=name,
            type=type,
            version=version,
            description=description,
            config=config,
            request_options=request_options,
        )
        return _response.data

    async def returns_information_about_the_given_nfvo_id(
        self, nfvo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Nfvo:
        """
        Parameters
        ----------
        nfvo_id : str
            ID of NFVO to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Nfvo
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nfvo.returns_information_about_the_given_nfvo_id(
                nfvo_id="nfvo_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_information_about_the_given_nfvo_id(
            nfvo_id, request_options=request_options
        )
        return _response.data

    async def updates_the_given_nfvo(
        self, nfvo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        nfvo_id : str
            ID of NFVO to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nfvo.updates_the_given_nfvo(
                nfvo_id="nfvo_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_the_given_nfvo(nfvo_id, request_options=request_options)
        return _response.data

    async def deletes_the_given_nfvo(
        self, nfvo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        nfvo_id : str
            ID of NFVO to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nfvo.deletes_the_given_nfvo(
                nfvo_id="nfvo_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_given_nfvo(nfvo_id, request_options=request_options)
        return _response.data
