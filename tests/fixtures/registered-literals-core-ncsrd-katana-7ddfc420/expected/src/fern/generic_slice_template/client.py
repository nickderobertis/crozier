

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.gst import Gst
from .raw_client import AsyncRawGenericSliceTemplateClient, RawGenericSliceTemplateClient


class GenericSliceTemplateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGenericSliceTemplateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGenericSliceTemplateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGenericSliceTemplateClient
        """
        return self._raw_client

    def returns_a_list_of_the_received_gs_ts_for_slice_instantiation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.generic_slice_template.returns_a_list_of_the_received_gs_ts_for_slice_instantiation()
        """
        _response = self._raw_client.returns_a_list_of_the_received_gs_ts_for_slice_instantiation(
            request_options=request_options
        )
        return _response.data

    def return_info_about_a_specific_gst(
        self, gst_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Gst:
        """
        Parameters
        ----------
        gst_id : str
            ID of GST

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Gst
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.generic_slice_template.return_info_about_a_specific_gst(
            gst_id="gst_id",
        )
        """
        _response = self._raw_client.return_info_about_a_specific_gst(gst_id, request_options=request_options)
        return _response.data


class AsyncGenericSliceTemplateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGenericSliceTemplateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGenericSliceTemplateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGenericSliceTemplateClient
        """
        return self._raw_client

    async def returns_a_list_of_the_received_gs_ts_for_slice_instantiation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.generic_slice_template.returns_a_list_of_the_received_gs_ts_for_slice_instantiation()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_the_received_gs_ts_for_slice_instantiation(
            request_options=request_options
        )
        return _response.data

    async def return_info_about_a_specific_gst(
        self, gst_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Gst:
        """
        Parameters
        ----------
        gst_id : str
            ID of GST

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Gst
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.generic_slice_template.return_info_about_a_specific_gst(
                gst_id="gst_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_info_about_a_specific_gst(gst_id, request_options=request_options)
        return _response.data
