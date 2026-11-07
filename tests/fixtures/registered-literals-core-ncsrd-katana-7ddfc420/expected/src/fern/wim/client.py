

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sbi_ls import SbiLs
from ..types.wim import Wim
from .raw_client import AsyncRawWimClient, RawWimClient


OMIT = typing.cast(typing.Any, ...)


class WimClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWimClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWimClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWimClient
        """
        return self._raw_client

    def returns_a_list_of_registered_wi_ms(
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
        client.wim.returns_a_list_of_registered_wi_ms()
        """
        _response = self._raw_client.returns_a_list_of_registered_wi_ms(request_options=request_options)
        return _response.data

    def adds_a_new_wim(
        self,
        *,
        id: str,
        url: str,
        type: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique id

        url : str
            WIM's authentication URL - example: http://10.200.64.2:5000/

        type : str
            WIM's type

        name : typing.Optional[str]
            The name for the new WIM

        description : typing.Optional[str]
            A description for the WIM

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wim.adds_a_new_wim(
            id="id",
            url="url",
            type="type",
        )
        """
        _response = self._raw_client.adds_a_new_wim(
            id=id, url=url, type=type, name=name, description=description, request_options=request_options
        )
        return _response.data

    def returns_information_about_the_given_wim(
        self, wim_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Wim:
        """
        Parameters
        ----------
        wim_id : str
            ID of WIM to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Wim
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wim.returns_information_about_the_given_wim(
            wim_id="wim_id",
        )
        """
        _response = self._raw_client.returns_information_about_the_given_wim(wim_id, request_options=request_options)
        return _response.data

    def updates_the_given_wim(self, wim_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        wim_id : str
            ID of WIM to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wim.updates_the_given_wim(
            wim_id="wim_id",
        )
        """
        _response = self._raw_client.updates_the_given_wim(wim_id, request_options=request_options)
        return _response.data

    def deletes_the_given_wim(self, wim_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        wim_id : str
            ID of WIM to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wim.deletes_the_given_wim(
            wim_id="wim_id",
        )
        """
        _response = self._raw_client.deletes_the_given_wim(wim_id, request_options=request_options)
        return _response.data


class AsyncWimClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWimClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWimClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWimClient
        """
        return self._raw_client

    async def returns_a_list_of_registered_wi_ms(
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
            await client.wim.returns_a_list_of_registered_wi_ms()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_registered_wi_ms(request_options=request_options)
        return _response.data

    async def adds_a_new_wim(
        self,
        *,
        id: str,
        url: str,
        type: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique id

        url : str
            WIM's authentication URL - example: http://10.200.64.2:5000/

        type : str
            WIM's type

        name : typing.Optional[str]
            The name for the new WIM

        description : typing.Optional[str]
            A description for the WIM

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
            await client.wim.adds_a_new_wim(
                id="id",
                url="url",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.adds_a_new_wim(
            id=id, url=url, type=type, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def returns_information_about_the_given_wim(
        self, wim_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Wim:
        """
        Parameters
        ----------
        wim_id : str
            ID of WIM to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Wim
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wim.returns_information_about_the_given_wim(
                wim_id="wim_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_information_about_the_given_wim(
            wim_id, request_options=request_options
        )
        return _response.data

    async def updates_the_given_wim(
        self, wim_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wim_id : str
            ID of WIM to be updated

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
            await client.wim.updates_the_given_wim(
                wim_id="wim_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_the_given_wim(wim_id, request_options=request_options)
        return _response.data

    async def deletes_the_given_wim(
        self, wim_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wim_id : str
            ID of WIM to be deleted

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
            await client.wim.deletes_the_given_wim(
                wim_id="wim_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_given_wim(wim_id, request_options=request_options)
        return _response.data
