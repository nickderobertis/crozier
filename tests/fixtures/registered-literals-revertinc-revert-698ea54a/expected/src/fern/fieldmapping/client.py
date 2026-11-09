

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_account_field_mapping_response import CreateAccountFieldMappingResponse
from ..types.create_field_mapping_response import CreateFieldMappingResponse
from ..types.delete_account_field_mapping_config_response import DeleteAccountFieldMappingConfigResponse
from ..types.delete_field_mapping_response import DeleteFieldMappingResponse
from ..types.field_mapping_type import FieldMappingType
from ..types.get_field_mapping_config_response import GetFieldMappingConfigResponse
from ..types.get_field_mappings_response import GetFieldMappingsResponse
from ..types.mappable_field_type import MappableFieldType
from .raw_client import AsyncRawFieldmappingClient, RawFieldmappingClient


OMIT = typing.cast(typing.Any, ...)


class FieldmappingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFieldmappingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFieldmappingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFieldmappingClient
        """
        return self._raw_client

    def getfieldmappingconfig(
        self,
        *,
        revert_public_token: str,
        revert_t_id: str,
        revert_t_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFieldMappingConfigResponse:
        """
        Get field mappings configs for a connection

        Parameters
        ----------
        revert_public_token : str
            Your public key, to be used on the frontend usually.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        revert_t_token : str
            The temp used to identify tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFieldMappingConfigResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.fieldmapping.getfieldmappingconfig(
            revert_public_token="x-revert-public-token",
            revert_t_id="x-revert-t-id",
            revert_t_token="x-revert-t-token",
        )
        """
        _response = self._raw_client.getfieldmappingconfig(
            revert_public_token=revert_public_token,
            revert_t_id=revert_t_id,
            revert_t_token=revert_t_token,
            request_options=request_options,
        )
        return _response.data

    def createfieldmapping(
        self,
        *,
        revert_public_token: str,
        revert_t_id: str,
        revert_t_token: str,
        standard_mappings: typing.Sequence[FieldMappingType],
        custom_mappings: typing.Sequence[FieldMappingType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateFieldMappingResponse:
        """
        Create field mappings for a connection after user input

        Parameters
        ----------
        revert_public_token : str
            Your public key, to be used on the frontend usually.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        revert_t_token : str
            The temp used to identify tenant.

        standard_mappings : typing.Sequence[FieldMappingType]

        custom_mappings : typing.Sequence[FieldMappingType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateFieldMappingResponse


        Examples
        --------
        from fern import FernApi, FieldMappingType

        client = FernApi()
        client.fieldmapping.createfieldmapping(
            revert_public_token="x-revert-public-token",
            revert_t_id="x-revert-t-id",
            revert_t_token="x-revert-t-token",
            standard_mappings=[
                FieldMappingType(
                    source_field_name="sourceFieldName",
                    target_field_name="targetFieldName",
                    object="object",
                )
            ],
            custom_mappings=[
                FieldMappingType(
                    source_field_name="sourceFieldName",
                    target_field_name="targetFieldName",
                    object="object",
                )
            ],
        )
        """
        _response = self._raw_client.createfieldmapping(
            revert_public_token=revert_public_token,
            revert_t_id=revert_t_id,
            revert_t_token=revert_t_token,
            standard_mappings=standard_mappings,
            custom_mappings=custom_mappings,
            request_options=request_options,
        )
        return _response.data

    def deletefieldmapping(
        self, *, revert_api_token: str, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteFieldMappingResponse:
        """
        Delete field mappings for a connection

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteFieldMappingResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.fieldmapping.deletefieldmapping(
            revert_api_token="x-revert-api-token",
            revert_t_id="x-revert-t-id",
        )
        """
        _response = self._raw_client.deletefieldmapping(
            revert_api_token=revert_api_token, revert_t_id=revert_t_id, request_options=request_options
        )
        return _response.data

    def getfieldmappings(
        self, *, revert_api_token: str, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFieldMappingsResponse:
        """
        Get field mappings for a connection

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFieldMappingsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.fieldmapping.getfieldmappings(
            revert_api_token="x-revert-api-token",
            revert_t_id="x-revert-t-id",
        )
        """
        _response = self._raw_client.getfieldmappings(
            revert_api_token=revert_api_token, revert_t_id=revert_t_id, request_options=request_options
        )
        return _response.data

    def createaccountfieldmappingconfig(
        self,
        *,
        revert_api_token: str,
        allow_connection_override_custom_fields: bool,
        mappable_by_connection_field_list: typing.Sequence[MappableFieldType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAccountFieldMappingResponse:
        """
        Create field mappings config for an account

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        allow_connection_override_custom_fields : bool

        mappable_by_connection_field_list : typing.Sequence[MappableFieldType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAccountFieldMappingResponse


        Examples
        --------
        from fern import CommonStandardObject, FernApi, MappableFieldType

        client = FernApi()
        client.fieldmapping.createaccountfieldmappingconfig(
            revert_api_token="x-revert-api-token",
            allow_connection_override_custom_fields=True,
            mappable_by_connection_field_list=[
                MappableFieldType(
                    field_name="fieldName",
                    object_name=CommonStandardObject.COMPANY,
                )
            ],
        )
        """
        _response = self._raw_client.createaccountfieldmappingconfig(
            revert_api_token=revert_api_token,
            allow_connection_override_custom_fields=allow_connection_override_custom_fields,
            mappable_by_connection_field_list=mappable_by_connection_field_list,
            request_options=request_options,
        )
        return _response.data

    def deleteaccountfieldmappingconfig(
        self, *, revert_api_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAccountFieldMappingConfigResponse:
        """
        Delete field mappings config for an account

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAccountFieldMappingConfigResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.fieldmapping.deleteaccountfieldmappingconfig(
            revert_api_token="x-revert-api-token",
        )
        """
        _response = self._raw_client.deleteaccountfieldmappingconfig(
            revert_api_token=revert_api_token, request_options=request_options
        )
        return _response.data


class AsyncFieldmappingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFieldmappingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFieldmappingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFieldmappingClient
        """
        return self._raw_client

    async def getfieldmappingconfig(
        self,
        *,
        revert_public_token: str,
        revert_t_id: str,
        revert_t_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFieldMappingConfigResponse:
        """
        Get field mappings configs for a connection

        Parameters
        ----------
        revert_public_token : str
            Your public key, to be used on the frontend usually.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        revert_t_token : str
            The temp used to identify tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFieldMappingConfigResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.fieldmapping.getfieldmappingconfig(
                revert_public_token="x-revert-public-token",
                revert_t_id="x-revert-t-id",
                revert_t_token="x-revert-t-token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getfieldmappingconfig(
            revert_public_token=revert_public_token,
            revert_t_id=revert_t_id,
            revert_t_token=revert_t_token,
            request_options=request_options,
        )
        return _response.data

    async def createfieldmapping(
        self,
        *,
        revert_public_token: str,
        revert_t_id: str,
        revert_t_token: str,
        standard_mappings: typing.Sequence[FieldMappingType],
        custom_mappings: typing.Sequence[FieldMappingType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateFieldMappingResponse:
        """
        Create field mappings for a connection after user input

        Parameters
        ----------
        revert_public_token : str
            Your public key, to be used on the frontend usually.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        revert_t_token : str
            The temp used to identify tenant.

        standard_mappings : typing.Sequence[FieldMappingType]

        custom_mappings : typing.Sequence[FieldMappingType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateFieldMappingResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FieldMappingType

        client = AsyncFernApi()


        async def main() -> None:
            await client.fieldmapping.createfieldmapping(
                revert_public_token="x-revert-public-token",
                revert_t_id="x-revert-t-id",
                revert_t_token="x-revert-t-token",
                standard_mappings=[
                    FieldMappingType(
                        source_field_name="sourceFieldName",
                        target_field_name="targetFieldName",
                        object="object",
                    )
                ],
                custom_mappings=[
                    FieldMappingType(
                        source_field_name="sourceFieldName",
                        target_field_name="targetFieldName",
                        object="object",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createfieldmapping(
            revert_public_token=revert_public_token,
            revert_t_id=revert_t_id,
            revert_t_token=revert_t_token,
            standard_mappings=standard_mappings,
            custom_mappings=custom_mappings,
            request_options=request_options,
        )
        return _response.data

    async def deletefieldmapping(
        self, *, revert_api_token: str, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteFieldMappingResponse:
        """
        Delete field mappings for a connection

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteFieldMappingResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.fieldmapping.deletefieldmapping(
                revert_api_token="x-revert-api-token",
                revert_t_id="x-revert-t-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletefieldmapping(
            revert_api_token=revert_api_token, revert_t_id=revert_t_id, request_options=request_options
        )
        return _response.data

    async def getfieldmappings(
        self, *, revert_api_token: str, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFieldMappingsResponse:
        """
        Get field mappings for a connection

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFieldMappingsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.fieldmapping.getfieldmappings(
                revert_api_token="x-revert-api-token",
                revert_t_id="x-revert-t-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getfieldmappings(
            revert_api_token=revert_api_token, revert_t_id=revert_t_id, request_options=request_options
        )
        return _response.data

    async def createaccountfieldmappingconfig(
        self,
        *,
        revert_api_token: str,
        allow_connection_override_custom_fields: bool,
        mappable_by_connection_field_list: typing.Sequence[MappableFieldType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAccountFieldMappingResponse:
        """
        Create field mappings config for an account

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        allow_connection_override_custom_fields : bool

        mappable_by_connection_field_list : typing.Sequence[MappableFieldType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAccountFieldMappingResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CommonStandardObject, MappableFieldType

        client = AsyncFernApi()


        async def main() -> None:
            await client.fieldmapping.createaccountfieldmappingconfig(
                revert_api_token="x-revert-api-token",
                allow_connection_override_custom_fields=True,
                mappable_by_connection_field_list=[
                    MappableFieldType(
                        field_name="fieldName",
                        object_name=CommonStandardObject.COMPANY,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createaccountfieldmappingconfig(
            revert_api_token=revert_api_token,
            allow_connection_override_custom_fields=allow_connection_override_custom_fields,
            mappable_by_connection_field_list=mappable_by_connection_field_list,
            request_options=request_options,
        )
        return _response.data

    async def deleteaccountfieldmappingconfig(
        self, *, revert_api_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAccountFieldMappingConfigResponse:
        """
        Delete field mappings config for an account

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAccountFieldMappingConfigResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.fieldmapping.deleteaccountfieldmappingconfig(
                revert_api_token="x-revert-api-token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteaccountfieldmappingconfig(
            revert_api_token=revert_api_token, request_options=request_options
        )
        return _response.data
