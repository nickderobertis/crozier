

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.gst import Gst
from ..types.nsi import Nsi
from ..types.slice_ls import SliceLs
from ..types.time import Time
from .raw_client import AsyncRawSliceClient, RawSliceClient


OMIT = typing.cast(typing.Any, ...)


class SliceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSliceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSliceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSliceClient
        """
        return self._raw_client

    def returns_a_list_of_created_slices(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SliceLs]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SliceLs]
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.slice.returns_a_list_of_created_slices()
        """
        _response = self._raw_client.returns_a_list_of_created_slices(request_options=request_options)
        return _response.data

    def creates_a_new_slice(
        self, *, gst: typing.Optional[Gst] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        gst : typing.Optional[Gst]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.slice.creates_a_new_slice()
        """
        _response = self._raw_client.creates_a_new_slice(gst=gst, request_options=request_options)
        return _response.data

    def returns_information_about_the_given_slice(
        self, slice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Nsi:
        """
        Parameters
        ----------
        slice_id : str
            ID of slice to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Nsi
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.slice.returns_information_about_the_given_slice(
            slice_id="slice_id",
        )
        """
        _response = self._raw_client.returns_information_about_the_given_slice(
            slice_id, request_options=request_options
        )
        return _response.data

    def deletes_the_given_slice(
        self,
        slice_id: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        slice_id : str
            ID of slice to be deleted

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.slice.deletes_the_given_slice(
            slice_id="slice_id",
        )
        """
        _response = self._raw_client.deletes_the_given_slice(slice_id, force=force, request_options=request_options)
        return _response.data

    def returns_information_about_the_deployment_time_of_the_given_slice(
        self, slice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Time:
        """
        Parameters
        ----------
        slice_id : str
            ID of slice

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Time
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.slice.returns_information_about_the_deployment_time_of_the_given_slice(
            slice_id="slice_id",
        )
        """
        _response = self._raw_client.returns_information_about_the_deployment_time_of_the_given_slice(
            slice_id, request_options=request_options
        )
        return _response.data


class AsyncSliceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSliceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSliceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSliceClient
        """
        return self._raw_client

    async def returns_a_list_of_created_slices(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SliceLs]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SliceLs]
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.slice.returns_a_list_of_created_slices()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_created_slices(request_options=request_options)
        return _response.data

    async def creates_a_new_slice(
        self, *, gst: typing.Optional[Gst] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        gst : typing.Optional[Gst]

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
            await client.slice.creates_a_new_slice()


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_a_new_slice(gst=gst, request_options=request_options)
        return _response.data

    async def returns_information_about_the_given_slice(
        self, slice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Nsi:
        """
        Parameters
        ----------
        slice_id : str
            ID of slice to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Nsi
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.slice.returns_information_about_the_given_slice(
                slice_id="slice_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_information_about_the_given_slice(
            slice_id, request_options=request_options
        )
        return _response.data

    async def deletes_the_given_slice(
        self,
        slice_id: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        slice_id : str
            ID of slice to be deleted

        force : typing.Optional[bool]

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
            await client.slice.deletes_the_given_slice(
                slice_id="slice_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_given_slice(
            slice_id, force=force, request_options=request_options
        )
        return _response.data

    async def returns_information_about_the_deployment_time_of_the_given_slice(
        self, slice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Time:
        """
        Parameters
        ----------
        slice_id : str
            ID of slice

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Time
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.slice.returns_information_about_the_deployment_time_of_the_given_slice(
                slice_id="slice_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_information_about_the_deployment_time_of_the_given_slice(
            slice_id, request_options=request_options
        )
        return _response.data
