

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSchemaResponsesClient, RawSchemaResponsesClient
from .types.schema_response_patch_request_attributes import SchemaResponsePatchRequestAttributes
from .types.schema_response_patch_request_links import SchemaResponsePatchRequestLinks
from .types.schema_response_patch_request_relationships import SchemaResponsePatchRequestRelationships
from .types.schema_response_patch_response import SchemaResponsePatchResponse
from .types.schema_response_ppost_request_attributes import SchemaResponsePpostRequestAttributes
from .types.schema_response_ppost_request_links import SchemaResponsePpostRequestLinks
from .types.schema_response_ppost_request_relationships import SchemaResponsePpostRequestRelationships
from .types.schema_response_ppost_response import SchemaResponsePpostResponse
from .types.schema_responses_list_response import SchemaResponsesListResponse
from .types.schema_responses_read_response import SchemaResponsesReadResponse


OMIT = typing.cast(typing.Any, ...)


class SchemaResponsesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSchemaResponsesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSchemaResponsesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSchemaResponsesClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> SchemaResponsesListResponse:
        """
        This retrieves a paginated list of all active Schema Responses that are public.
        #### Returns
        Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of 10 Schema Responses. Each resource in the array is a separate Registration Schemas object. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaResponsesListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.schema_responses.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def schema_response_ppost(
        self,
        *,
        attributes: SchemaResponsePpostRequestAttributes,
        type: str,
        links: typing.Optional[SchemaResponsePpostRequestLinks] = OMIT,
        relationships: typing.Optional[SchemaResponsePpostRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchemaResponsePpostResponse:
        """
        This endpoint creates a new Schema Response with an `in_progress` state. A new response can only be created if the current schema response is in an `approved` state.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        attributes : SchemaResponsePpostRequestAttributes
            The properties of the Schema Response.

        type : str
            The type identifier of the Schema Response (`schema-response`).

        links : typing.Optional[SchemaResponsePpostRequestLinks]
            URLs to alternative representations of the Schema Response entity.

        relationships : typing.Optional[SchemaResponsePpostRequestRelationships]
            Links to other entities or entity collections that have a relationship to the file entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaResponsePpostResponse
            OK

        Examples
        --------
        from fern.schema_responses import SchemaResponsePpostRequestAttributes

        from fern import FernApi

        client = FernApi()
        client.schema_responses.schema_response_ppost(
            attributes=SchemaResponsePpostRequestAttributes(),
            type="type",
        )
        """
        _response = self._raw_client.schema_response_ppost(
            attributes=attributes, type=type, links=links, relationships=relationships, request_options=request_options
        )
        return _response.data

    def read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaResponsesReadResponse:
        """
        This retrieves a single Schema response using it's id.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response, if the request is successful.
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
        SchemaResponsesReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.schema_responses.read(
            schema_response_id="schema_response_id",
        )
        """
        _response = self._raw_client.read(schema_response_id, request_options=request_options)
        return _response.data

    def schema_response_delete(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        This endpoint deletes a new Schema Response. Schema Responses can only be deleted in the `in_progress` state. Once a Schema Response is transitioned to an `approved` it is immutable and another Schema Response must be created to update the Schema Response for that registration.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
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
        client.schema_responses.schema_response_delete(
            schema_response_id="schema_response_id",
        )
        """
        _response = self._raw_client.schema_response_delete(schema_response_id, request_options=request_options)
        return _response.data

    def schema_response_patch(
        self,
        schema_response_id: str,
        *,
        attributes: SchemaResponsePatchRequestAttributes,
        type: str,
        links: typing.Optional[SchemaResponsePatchRequestLinks] = OMIT,
        relationships: typing.Optional[SchemaResponsePatchRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchemaResponsePatchResponse:
        """
        Patching to this endpoint allows one to directly edit the revision responses on the Schema Response of a Registration if that Schema Response is in an `in_progress` state.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        attributes : SchemaResponsePatchRequestAttributes
            The properties of the Schema Response.

        type : str
            The type identifier of the Schema Response (`schema-response`).

        links : typing.Optional[SchemaResponsePatchRequestLinks]
            URLs to alternative representations of the Schema Response entity.

        relationships : typing.Optional[SchemaResponsePatchRequestRelationships]
            Links to other entities or entity collections that have a relationship to the file entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaResponsePatchResponse
            OK

        Examples
        --------
        from fern.schema_responses import SchemaResponsePatchRequestAttributes

        from fern import FernApi

        client = FernApi()
        client.schema_responses.schema_response_patch(
            schema_response_id="schema_response_id",
            attributes=SchemaResponsePatchRequestAttributes(),
            type="type",
        )
        """
        _response = self._raw_client.schema_response_patch(
            schema_response_id,
            attributes=attributes,
            type=type,
            links=links,
            relationships=relationships,
            request_options=request_options,
        )
        return _response.data


class AsyncSchemaResponsesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSchemaResponsesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSchemaResponsesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSchemaResponsesClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> SchemaResponsesListResponse:
        """
        This retrieves a paginated list of all active Schema Responses that are public.
        #### Returns
        Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of 10 Schema Responses. Each resource in the array is a separate Registration Schemas object. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaResponsesListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.schema_responses.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def schema_response_ppost(
        self,
        *,
        attributes: SchemaResponsePpostRequestAttributes,
        type: str,
        links: typing.Optional[SchemaResponsePpostRequestLinks] = OMIT,
        relationships: typing.Optional[SchemaResponsePpostRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchemaResponsePpostResponse:
        """
        This endpoint creates a new Schema Response with an `in_progress` state. A new response can only be created if the current schema response is in an `approved` state.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        attributes : SchemaResponsePpostRequestAttributes
            The properties of the Schema Response.

        type : str
            The type identifier of the Schema Response (`schema-response`).

        links : typing.Optional[SchemaResponsePpostRequestLinks]
            URLs to alternative representations of the Schema Response entity.

        relationships : typing.Optional[SchemaResponsePpostRequestRelationships]
            Links to other entities or entity collections that have a relationship to the file entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaResponsePpostResponse
            OK

        Examples
        --------
        import asyncio

        from fern.schema_responses import SchemaResponsePpostRequestAttributes

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.schema_responses.schema_response_ppost(
                attributes=SchemaResponsePpostRequestAttributes(),
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_response_ppost(
            attributes=attributes, type=type, links=links, relationships=relationships, request_options=request_options
        )
        return _response.data

    async def read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaResponsesReadResponse:
        """
        This retrieves a single Schema response using it's id.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response, if the request is successful.
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
        SchemaResponsesReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.schema_responses.read(
                schema_response_id="schema_response_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read(schema_response_id, request_options=request_options)
        return _response.data

    async def schema_response_delete(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        This endpoint deletes a new Schema Response. Schema Responses can only be deleted in the `in_progress` state. Once a Schema Response is transitioned to an `approved` it is immutable and another Schema Response must be created to update the Schema Response for that registration.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
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
            await client.schema_responses.schema_response_delete(
                schema_response_id="schema_response_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_response_delete(schema_response_id, request_options=request_options)
        return _response.data

    async def schema_response_patch(
        self,
        schema_response_id: str,
        *,
        attributes: SchemaResponsePatchRequestAttributes,
        type: str,
        links: typing.Optional[SchemaResponsePatchRequestLinks] = OMIT,
        relationships: typing.Optional[SchemaResponsePatchRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchemaResponsePatchResponse:
        """
        Patching to this endpoint allows one to directly edit the revision responses on the Schema Response of a Registration if that Schema Response is in an `in_progress` state.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        attributes : SchemaResponsePatchRequestAttributes
            The properties of the Schema Response.

        type : str
            The type identifier of the Schema Response (`schema-response`).

        links : typing.Optional[SchemaResponsePatchRequestLinks]
            URLs to alternative representations of the Schema Response entity.

        relationships : typing.Optional[SchemaResponsePatchRequestRelationships]
            Links to other entities or entity collections that have a relationship to the file entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaResponsePatchResponse
            OK

        Examples
        --------
        import asyncio

        from fern.schema_responses import SchemaResponsePatchRequestAttributes

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.schema_responses.schema_response_patch(
                schema_response_id="schema_response_id",
                attributes=SchemaResponsePatchRequestAttributes(),
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_response_patch(
            schema_response_id,
            attributes=attributes,
            type=type,
            links=links,
            relationships=relationships,
            request_options=request_options,
        )
        return _response.data
