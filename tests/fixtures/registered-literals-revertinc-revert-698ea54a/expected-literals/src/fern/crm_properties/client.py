

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_standard_object import CommonStandardObject
from ..types.crm_get_object_properties_response import CrmGetObjectPropertiesResponse
from ..types.crm_set_object_properties_response import CrmSetObjectPropertiesResponse
from .raw_client import AsyncRawCrmPropertiesClient, RawCrmPropertiesClient


OMIT = typing.cast(typing.Any, ...)


class CrmPropertiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmPropertiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmPropertiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmPropertiesClient
        """
        return self._raw_client

    def crm_properties_get_object_properties(
        self, object_name: CommonStandardObject, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CrmGetObjectPropertiesResponse:
        """
        Get object properties for connection

        Parameters
        ----------
        object_name : CommonStandardObject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetObjectPropertiesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_properties.crm_properties_get_object_properties(
            object_name="company",
        )
        """
        _response = self._raw_client.crm_properties_get_object_properties(object_name, request_options=request_options)
        return _response.data

    def crm_properties_set_custom_properties(
        self,
        object_name: CommonStandardObject,
        *,
        additional: typing.Any,
        name: str,
        type: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSetObjectPropertiesResponse:
        """
        Set custom properties on an object for a given connection

        Parameters
        ----------
        object_name : CommonStandardObject

        additional : typing.Any

        name : str

        type : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSetObjectPropertiesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_properties.crm_properties_set_custom_properties(
            object_name="company",
            additional={"key": "value"},
            name="name",
            type="type",
            description="description",
        )
        """
        _response = self._raw_client.crm_properties_set_custom_properties(
            object_name,
            additional=additional,
            name=name,
            type=type,
            description=description,
            request_options=request_options,
        )
        return _response.data


class AsyncCrmPropertiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmPropertiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmPropertiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmPropertiesClient
        """
        return self._raw_client

    async def crm_properties_get_object_properties(
        self, object_name: CommonStandardObject, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CrmGetObjectPropertiesResponse:
        """
        Get object properties for connection

        Parameters
        ----------
        object_name : CommonStandardObject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetObjectPropertiesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_properties.crm_properties_get_object_properties(
                object_name="company",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_properties_get_object_properties(
            object_name, request_options=request_options
        )
        return _response.data

    async def crm_properties_set_custom_properties(
        self,
        object_name: CommonStandardObject,
        *,
        additional: typing.Any,
        name: str,
        type: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSetObjectPropertiesResponse:
        """
        Set custom properties on an object for a given connection

        Parameters
        ----------
        object_name : CommonStandardObject

        additional : typing.Any

        name : str

        type : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSetObjectPropertiesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_properties.crm_properties_set_custom_properties(
                object_name="company",
                additional={"key": "value"},
                name="name",
                type="type",
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_properties_set_custom_properties(
            object_name,
            additional=additional,
            name=name,
            type=type,
            description=description,
            request_options=request_options,
        )
        return _response.data
