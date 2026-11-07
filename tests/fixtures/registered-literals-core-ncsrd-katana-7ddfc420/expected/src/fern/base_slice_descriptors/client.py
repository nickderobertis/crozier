

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.base_slice_des import BaseSliceDes
from .raw_client import AsyncRawBaseSliceDescriptorsClient, RawBaseSliceDescriptorsClient
from .types.get_base_slice_des_response_item import GetBaseSliceDesResponseItem


class BaseSliceDescriptorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBaseSliceDescriptorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBaseSliceDescriptorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBaseSliceDescriptorsClient
        """
        return self._raw_client

    def returns_a_list_of_the_base_slice_descriptors_that_are_part_of_the_gst(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetBaseSliceDesResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetBaseSliceDesResponseItem]
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.base_slice_descriptors.returns_a_list_of_the_base_slice_descriptors_that_are_part_of_the_gst()
        """
        _response = self._raw_client.returns_a_list_of_the_base_slice_descriptors_that_are_part_of_the_gst(
            request_options=request_options
        )
        return _response.data

    def defines_a_new_base_slice_descriptor_for_the_platform(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.base_slice_descriptors.defines_a_new_base_slice_descriptor_for_the_platform()
        """
        _response = self._raw_client.defines_a_new_base_slice_descriptor_for_the_platform(
            request_options=request_options
        )
        return _response.data

    def return_info_about_a_specific_base_slice_descriptor(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BaseSliceDes:
        """
        Parameters
        ----------
        id : str
            ID of base_slice_des

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseSliceDes
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.base_slice_descriptors.return_info_about_a_specific_base_slice_descriptor(
            id="id",
        )
        """
        _response = self._raw_client.return_info_about_a_specific_base_slice_descriptor(
            id, request_options=request_options
        )
        return _response.data

    def add_or_update_a_base_slice_descriptor(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            ID of base_slice_des

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.base_slice_descriptors.add_or_update_a_base_slice_descriptor(
            id="id",
        )
        """
        _response = self._raw_client.add_or_update_a_base_slice_descriptor(id, request_options=request_options)
        return _response.data

    def delete_a_base_slice_descriptor(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            ID of base_slice_des

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.base_slice_descriptors.delete_a_base_slice_descriptor(
            id="id",
        )
        """
        _response = self._raw_client.delete_a_base_slice_descriptor(id, request_options=request_options)
        return _response.data


class AsyncBaseSliceDescriptorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBaseSliceDescriptorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBaseSliceDescriptorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBaseSliceDescriptorsClient
        """
        return self._raw_client

    async def returns_a_list_of_the_base_slice_descriptors_that_are_part_of_the_gst(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetBaseSliceDesResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetBaseSliceDesResponseItem]
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.base_slice_descriptors.returns_a_list_of_the_base_slice_descriptors_that_are_part_of_the_gst()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_the_base_slice_descriptors_that_are_part_of_the_gst(
            request_options=request_options
        )
        return _response.data

    async def defines_a_new_base_slice_descriptor_for_the_platform(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            await client.base_slice_descriptors.defines_a_new_base_slice_descriptor_for_the_platform()


        asyncio.run(main())
        """
        _response = await self._raw_client.defines_a_new_base_slice_descriptor_for_the_platform(
            request_options=request_options
        )
        return _response.data

    async def return_info_about_a_specific_base_slice_descriptor(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BaseSliceDes:
        """
        Parameters
        ----------
        id : str
            ID of base_slice_des

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseSliceDes
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.base_slice_descriptors.return_info_about_a_specific_base_slice_descriptor(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_info_about_a_specific_base_slice_descriptor(
            id, request_options=request_options
        )
        return _response.data

    async def add_or_update_a_base_slice_descriptor(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            ID of base_slice_des

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
            await client.base_slice_descriptors.add_or_update_a_base_slice_descriptor(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_or_update_a_base_slice_descriptor(id, request_options=request_options)
        return _response.data

    async def delete_a_base_slice_descriptor(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            ID of base_slice_des

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
            await client.base_slice_descriptors.delete_a_base_slice_descriptor(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_base_slice_descriptor(id, request_options=request_options)
        return _response.data
