

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.service_credential_type import ServiceCredentialType
from ..types.service_credential_types_collection import ServiceCredentialTypesCollection
from .raw_client import AsyncRawServiceCredentialTypeClient, RawServiceCredentialTypeClient


class ServiceCredentialTypeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServiceCredentialTypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServiceCredentialTypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServiceCredentialTypeClient
        """
        return self._raw_client

    def list_service_credential_types(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceCredentialTypesCollection:
        """
        Returns an array of ServiceCredentialType objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceCredentialTypesCollection
            ServiceCredentialTypes collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_credential_type.list_service_credential_types()
        """
        _response = self._raw_client.list_service_credential_types(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def show_service_credential_type(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceCredentialType:
        """
        Returns a ServiceCredentialType object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceCredentialType
            ServiceCredentialType info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_credential_type.show_service_credential_type(
            id="id",
        )
        """
        _response = self._raw_client.show_service_credential_type(id, request_options=request_options)
        return _response.data


class AsyncServiceCredentialTypeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServiceCredentialTypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServiceCredentialTypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServiceCredentialTypeClient
        """
        return self._raw_client

    async def list_service_credential_types(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceCredentialTypesCollection:
        """
        Returns an array of ServiceCredentialType objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceCredentialTypesCollection
            ServiceCredentialTypes collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_credential_type.list_service_credential_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_credential_types(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def show_service_credential_type(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceCredentialType:
        """
        Returns a ServiceCredentialType object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceCredentialType
            ServiceCredentialType info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_credential_type.show_service_credential_type(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_service_credential_type(id, request_options=request_options)
        return _response.data
