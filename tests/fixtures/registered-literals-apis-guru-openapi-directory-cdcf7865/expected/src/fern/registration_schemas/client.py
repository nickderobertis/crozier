

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRegistrationSchemasClient, RawRegistrationSchemasClient
from .types.registration_schema_read_response import RegistrationSchemaReadResponse
from .types.registration_schemas_list_response import RegistrationSchemasListResponse


class RegistrationSchemasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRegistrationSchemasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRegistrationSchemasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRegistrationSchemasClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> RegistrationSchemasListResponse:
        """
        Retrieve a paginated list of all active Registration Schemas. Registration Schemas describe the supplemental questions that accompany a registration. Registration Schemas are read-only for API users.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.
        The `data` key contains an array of 10 Registration Schemas. Each resource in the array is a separate Registration Schemas object.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistrationSchemasListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.registration_schemas.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def registration_schema_read(
        self, registration_schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegistrationSchemaReadResponse:
        """
        Retrieves the details of a given Registration Schema. Registration Schemas defines the desired supplemental information that should accompany be included in a Registration. Registration Schemas are Read-only to API users.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_schema_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistrationSchemaReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.registration_schemas.registration_schema_read(
            registration_schema_id="registration_schema_id",
        )
        """
        _response = self._raw_client.registration_schema_read(registration_schema_id, request_options=request_options)
        return _response.data


class AsyncRegistrationSchemasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRegistrationSchemasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRegistrationSchemasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRegistrationSchemasClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> RegistrationSchemasListResponse:
        """
        Retrieve a paginated list of all active Registration Schemas. Registration Schemas describe the supplemental questions that accompany a registration. Registration Schemas are read-only for API users.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.
        The `data` key contains an array of 10 Registration Schemas. Each resource in the array is a separate Registration Schemas object.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistrationSchemasListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.registration_schemas.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def registration_schema_read(
        self, registration_schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegistrationSchemaReadResponse:
        """
        Retrieves the details of a given Registration Schema. Registration Schemas defines the desired supplemental information that should accompany be included in a Registration. Registration Schemas are Read-only to API users.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_schema_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistrationSchemaReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.registration_schemas.registration_schema_read(
                registration_schema_id="registration_schema_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.registration_schema_read(
            registration_schema_id, request_options=request_options
        )
        return _response.data
