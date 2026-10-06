

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawXmlPrescriptionResourceClient, RawXmlPrescriptionResourceClient


class XmlPrescriptionResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawXmlPrescriptionResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawXmlPrescriptionResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawXmlPrescriptionResourceClient
        """
        return self._raw_client

    def post_xml_prescription(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.xml_prescription_resource.post_xml_prescription()
        """
        _response = self._raw_client.post_xml_prescription(request_options=request_options)
        return _response.data


class AsyncXmlPrescriptionResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawXmlPrescriptionResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawXmlPrescriptionResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawXmlPrescriptionResourceClient
        """
        return self._raw_client

    async def post_xml_prescription(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.xml_prescription_resource.post_xml_prescription()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_xml_prescription(request_options=request_options)
        return _response.data
