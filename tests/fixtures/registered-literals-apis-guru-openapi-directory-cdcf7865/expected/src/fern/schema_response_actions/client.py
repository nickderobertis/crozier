

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSchemaResponseActionsClient, RawSchemaResponseActionsClient
from .types.get_schema_responses_schema_response_id_actions_schema_response_action_id_response import (
    GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse,
)
from .types.schema_response_action_read_response import SchemaResponseActionReadResponse


class SchemaResponseActionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSchemaResponseActionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSchemaResponseActionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSchemaResponseActionsClient
        """
        return self._raw_client

    def schema_response_action_read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaResponseActionReadResponse:
        """
        This retrieves a paginated list of all Schema Response Actions created for a Schema Response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
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
        SchemaResponseActionReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.schema_response_actions.schema_response_action_read(
            schema_response_id="schema_response_id",
        )
        """
        _response = self._raw_client.schema_response_action_read(schema_response_id, request_options=request_options)
        return _response.data

    def create_a_new_schema_response_action(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        This creates a new Schema Response Action in order to trigger a state transition for a Schema Response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.schema_response_actions.create_a_new_schema_response_action(
            schema_response_id="schema_response_id",
        )
        """
        _response = self._raw_client.create_a_new_schema_response_action(
            schema_response_id, request_options=request_options
        )
        return _response.data

    def a_schema_response_action_from_a_schema_response(
        self,
        schema_response_id: str,
        schema_response_action_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse:
        """
        Retrieves a Schema Response Action by it's ID.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Schema Response example `61b9cd62eb66180215222669`.

        schema_response_action_id : str
            The unique identifier of the Schema Response Action example `61b9eae1a7d8ac025c4c46d3`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.schema_response_actions.a_schema_response_action_from_a_schema_response(
            schema_response_id="schema_response_id",
            schema_response_action_id="schema_response_action_id",
        )
        """
        _response = self._raw_client.a_schema_response_action_from_a_schema_response(
            schema_response_id, schema_response_action_id, request_options=request_options
        )
        return _response.data


class AsyncSchemaResponseActionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSchemaResponseActionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSchemaResponseActionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSchemaResponseActionsClient
        """
        return self._raw_client

    async def schema_response_action_read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaResponseActionReadResponse:
        """
        This retrieves a paginated list of all Schema Response Actions created for a Schema Response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
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
        SchemaResponseActionReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.schema_response_actions.schema_response_action_read(
                schema_response_id="schema_response_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_response_action_read(
            schema_response_id, request_options=request_options
        )
        return _response.data

    async def create_a_new_schema_response_action(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        This creates a new Schema Response Action in order to trigger a state transition for a Schema Response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.schema_response_actions.create_a_new_schema_response_action(
                schema_response_id="schema_response_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_schema_response_action(
            schema_response_id, request_options=request_options
        )
        return _response.data

    async def a_schema_response_action_from_a_schema_response(
        self,
        schema_response_id: str,
        schema_response_action_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse:
        """
        Retrieves a Schema Response Action by it's ID.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Schema Response example `61b9cd62eb66180215222669`.

        schema_response_action_id : str
            The unique identifier of the Schema Response Action example `61b9eae1a7d8ac025c4c46d3`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.schema_response_actions.a_schema_response_action_from_a_schema_response(
                schema_response_id="schema_response_id",
                schema_response_action_id="schema_response_action_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.a_schema_response_action_from_a_schema_response(
            schema_response_id, schema_response_action_id, request_options=request_options
        )
        return _response.data
