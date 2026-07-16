

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.service_credential import ServiceCredential
from ..types.service_credentials_collection import ServiceCredentialsCollection
from .raw_client import AsyncRawServiceCredentialClient, RawServiceCredentialClient


class ServiceCredentialClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServiceCredentialClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServiceCredentialClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServiceCredentialClient
        """
        return self._raw_client

    def list_service_credentials(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceCredentialsCollection:
        """
        Returns an array of ServiceCredential objects

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
        ServiceCredentialsCollection
            ServiceCredentials collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_credential.list_service_credentials()
        """
        _response = self._raw_client.list_service_credentials(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def show_service_credential(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceCredential:
        """
        Returns a ServiceCredential object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceCredential
            ServiceCredential info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_credential.show_service_credential(
            id="id",
        )
        """
        _response = self._raw_client.show_service_credential(id, request_options=request_options)
        return _response.data


class AsyncServiceCredentialClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServiceCredentialClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServiceCredentialClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServiceCredentialClient
        """
        return self._raw_client

    async def list_service_credentials(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceCredentialsCollection:
        """
        Returns an array of ServiceCredential objects

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
        ServiceCredentialsCollection
            ServiceCredentials collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_credential.list_service_credentials()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_credentials(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def show_service_credential(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceCredential:
        """
        Returns a ServiceCredential object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceCredential
            ServiceCredential info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_credential.show_service_credential(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_service_credential(id, request_options=request_options)
        return _response.data
