

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.data_element import DataElement
from ..types.identifier import Identifier
from .raw_client import AsyncRawFineGranularApiClient, RawFineGranularApiClient
from .types.read_data_element_request_representation import ReadDataElementRequestRepresentation
from .types.update_data_element_request_representation import UpdateDataElementRequestRepresentation


OMIT = typing.cast(typing.Any, ...)


class FineGranularApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFineGranularApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFineGranularApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFineGranularApiClient
        """
        return self._raw_client

    def read_data_element(
        self,
        dpp_id: Identifier,
        element_id_path: str,
        *,
        representation: typing.Optional[ReadDataElementRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataElement:
        """
        Returns a single data element of a DPP by its absolute path. `elementIdPath` follows RFC 9535 JSONPath and is percent-encoded. Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        element_id_path : str
            RFC 9535 JSONPath to the element (e.g. `$.netWeight.value`), percent-encoded.

        representation : typing.Optional[ReadDataElementRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataElement
            The requested data element.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )
        client.fine_granular_api.read_data_element(
            dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
            element_id_path="elementIdPath",
        )
        """
        _response = self._raw_client.read_data_element(
            dpp_id, element_id_path, representation=representation, request_options=request_options
        )
        return _response.data

    def update_data_element(
        self,
        dpp_id: Identifier,
        element_id_path: str,
        *,
        request: DataElement,
        representation: typing.Optional[UpdateDataElementRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataElement:
        """
        Updates, amends, or removes a single data element of a DPP at the given RFC 9535 JSONPath. Changes are archived per EN 18221. Conformance: should where authorized third parties hold write access.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        element_id_path : str
            RFC 9535 JSONPath to the element (e.g. `$.netWeight.value`), percent-encoded.

        request : DataElement

        representation : typing.Optional[UpdateDataElementRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataElement
            The updated data element.

        Examples
        --------
        from fern import DataElement_SingleValuedDataElement, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )
        client.fine_granular_api.update_data_element(
            dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
            element_id_path="elementIdPath",
            request=DataElement_SingleValuedDataElement(
                element_id="elementId",
            ),
        )
        """
        _response = self._raw_client.update_data_element(
            dpp_id, element_id_path, request=request, representation=representation, request_options=request_options
        )
        return _response.data


class AsyncFineGranularApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFineGranularApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFineGranularApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFineGranularApiClient
        """
        return self._raw_client

    async def read_data_element(
        self,
        dpp_id: Identifier,
        element_id_path: str,
        *,
        representation: typing.Optional[ReadDataElementRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataElement:
        """
        Returns a single data element of a DPP by its absolute path. `elementIdPath` follows RFC 9535 JSONPath and is percent-encoded. Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        element_id_path : str
            RFC 9535 JSONPath to the element (e.g. `$.netWeight.value`), percent-encoded.

        representation : typing.Optional[ReadDataElementRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataElement
            The requested data element.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fine_granular_api.read_data_element(
                dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                element_id_path="elementIdPath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_data_element(
            dpp_id, element_id_path, representation=representation, request_options=request_options
        )
        return _response.data

    async def update_data_element(
        self,
        dpp_id: Identifier,
        element_id_path: str,
        *,
        request: DataElement,
        representation: typing.Optional[UpdateDataElementRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataElement:
        """
        Updates, amends, or removes a single data element of a DPP at the given RFC 9535 JSONPath. Changes are archived per EN 18221. Conformance: should where authorized third parties hold write access.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        element_id_path : str
            RFC 9535 JSONPath to the element (e.g. `$.netWeight.value`), percent-encoded.

        request : DataElement

        representation : typing.Optional[UpdateDataElementRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataElement
            The updated data element.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DataElement_SingleValuedDataElement

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fine_granular_api.update_data_element(
                dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                element_id_path="elementIdPath",
                request=DataElement_SingleValuedDataElement(
                    element_id="elementId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_data_element(
            dpp_id, element_id_path, request=request, representation=representation, request_options=request_options
        )
        return _response.data
