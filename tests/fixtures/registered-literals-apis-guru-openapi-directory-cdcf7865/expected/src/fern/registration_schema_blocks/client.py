

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRegistrationSchemaBlocksClient, RawRegistrationSchemaBlocksClient
from .types.get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response import (
    GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse,
)
from .types.schema_response_blocks_read_response import SchemaResponseBlocksReadResponse


class RegistrationSchemaBlocksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRegistrationSchemaBlocksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRegistrationSchemaBlocksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRegistrationSchemaBlocksClient
        """
        return self._raw_client

    def schema_response_blocks_read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaResponseBlocksReadResponse:
        """
        This returns a list of all the Registration Schema Blocks are contained in Registration Schema.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaResponseBlocksReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.registration_schema_blocks.schema_response_blocks_read(
            schema_response_id="schema_response_id",
        )
        """
        _response = self._raw_client.schema_response_blocks_read(schema_response_id, request_options=request_options)
        return _response.data

    def retrieve_a_registration_schema_block(
        self,
        schema_response_id: str,
        schema_response_block_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse:
        """
        This returns a Registration Schema Block by it's ID.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        schema_response_block_id : str
            The unique identifier of the Schema Response Block example `61b79f9eadbb5701424a2d5e`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.registration_schema_blocks.retrieve_a_registration_schema_block(
            schema_response_id="schema_response_id",
            schema_response_block_id="schema_response_block_id",
        )
        """
        _response = self._raw_client.retrieve_a_registration_schema_block(
            schema_response_id, schema_response_block_id, request_options=request_options
        )
        return _response.data


class AsyncRegistrationSchemaBlocksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRegistrationSchemaBlocksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRegistrationSchemaBlocksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRegistrationSchemaBlocksClient
        """
        return self._raw_client

    async def schema_response_blocks_read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaResponseBlocksReadResponse:
        """
        This returns a list of all the Registration Schema Blocks are contained in Registration Schema.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaResponseBlocksReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.registration_schema_blocks.schema_response_blocks_read(
                schema_response_id="schema_response_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_response_blocks_read(
            schema_response_id, request_options=request_options
        )
        return _response.data

    async def retrieve_a_registration_schema_block(
        self,
        schema_response_id: str,
        schema_response_block_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse:
        """
        This returns a Registration Schema Block by it's ID.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        schema_response_block_id : str
            The unique identifier of the Schema Response Block example `61b79f9eadbb5701424a2d5e`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.registration_schema_blocks.retrieve_a_registration_schema_block(
                schema_response_id="schema_response_id",
                schema_response_block_id="schema_response_block_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_registration_schema_block(
            schema_response_id, schema_response_block_id, request_options=request_options
        )
        return _response.data
