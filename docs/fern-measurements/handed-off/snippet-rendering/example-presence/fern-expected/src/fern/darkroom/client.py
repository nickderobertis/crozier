

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.print import Print
from .raw_client import AsyncRawDarkroomClient, RawDarkroomClient


OMIT = typing.cast(typing.Any, ...)


class DarkroomClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDarkroomClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDarkroomClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDarkroomClient
        """
        return self._raw_client

    def get_contact_sheet(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The contact sheet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.darkroom.get_contact_sheet()
        """
        with self._raw_client.get_contact_sheet(request_options=request_options) as r:
            yield from r.data

    def get_archive(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The archive.
        """
        with self._raw_client.get_archive(request_options=request_options) as r:
            yield from r.data

    def replace_scan(
        self,
        print_id: str,
        *,
        scan: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Print:
        """
        Parameters
        ----------
        print_id : str

        scan : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Print
            The print.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.darkroom.replace_scan(
            print_id="printId",
        )
        """
        _response = self._raw_client.replace_scan(print_id, scan=scan, request_options=request_options)
        return _response.data

    def upload_negative(self, *, negative: core.File, request_options: typing.Optional[RequestOptions] = None) -> Print:
        """
        Parameters
        ----------
        negative : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Print
            The print made from it.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.darkroom.upload_negative()
        """
        _response = self._raw_client.upload_negative(negative=negative, request_options=request_options)
        return _response.data

    def add_proof(
        self, print_id: str, *, proof: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Print:
        """
        Parameters
        ----------
        print_id : str

        proof : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Print
            The print.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.darkroom.add_proof(
            print_id="printId",
        )
        """
        _response = self._raw_client.add_proof(print_id, proof=proof, request_options=request_options)
        return _response.data

    def flash_enlarger(self, *, image: core.File, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The enlarger restarts after flashing.
        """
        _response = self._raw_client.flash_enlarger(image=image, request_options=request_options)
        return _response.data


class AsyncDarkroomClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDarkroomClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDarkroomClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDarkroomClient
        """
        return self._raw_client

    async def get_contact_sheet(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The contact sheet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.darkroom.get_contact_sheet()


        asyncio.run(main())
        """
        async with self._raw_client.get_contact_sheet(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_archive(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The archive.
        """
        async with self._raw_client.get_archive(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def replace_scan(
        self,
        print_id: str,
        *,
        scan: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Print:
        """
        Parameters
        ----------
        print_id : str

        scan : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Print
            The print.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.darkroom.replace_scan(
                print_id="printId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_scan(print_id, scan=scan, request_options=request_options)
        return _response.data

    async def upload_negative(
        self, *, negative: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Print:
        """
        Parameters
        ----------
        negative : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Print
            The print made from it.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.darkroom.upload_negative()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_negative(negative=negative, request_options=request_options)
        return _response.data

    async def add_proof(
        self, print_id: str, *, proof: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Print:
        """
        Parameters
        ----------
        print_id : str

        proof : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Print
            The print.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.darkroom.add_proof(
                print_id="printId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_proof(print_id, proof=proof, request_options=request_options)
        return _response.data

    async def flash_enlarger(self, *, image: core.File, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The enlarger restarts after flashing.
        """
        _response = await self._raw_client.flash_enlarger(image=image, request_options=request_options)
        return _response.data
