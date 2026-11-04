

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.contact import Contact
from ..types.create_customer_resp_body import CreateCustomerRespBody
from ..types.delete_customer_resp_body import DeleteCustomerRespBody
from ..types.email import Email
from ..types.get_customer_resp_body import GetCustomerRespBody
from ..types.list_customers_resp_body import ListCustomersRespBody
from ..types.upload_avatar_resp_body import UploadAvatarRespBody
from .raw_client import AsyncRawCustomersClient, RawCustomersClient


OMIT = typing.cast(typing.Any, ...)


class CustomersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomersClient
        """
        return self._raw_client

    def list_customers(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomersRespBody:
        """
        List customers.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomersRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.list_customers(
            limit=1,
        )
        """
        _response = self._raw_client.list_customers(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    def create_customer(
        self,
        *,
        contact: Contact,
        email: Email,
        name: str,
        primary_address: Address,
        bio: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomerRespBody:
        """
        Create a customer.

        Parameters
        ----------
        contact : Contact

        email : Email

        name : str

        primary_address : Address

        bio : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomerRespBody
            Created

        Examples
        --------
        from fern import Address, Contact, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.create_customer(
            contact=Contact(),
            email="email",
            name="name",
            primary_address=Address(
                city="city",
                country="country",
                postal_code="postalCode",
                street="street",
            ),
        )
        """
        _response = self._raw_client.create_customer(
            contact=contact,
            email=email,
            name=name,
            primary_address=primary_address,
            bio=bio,
            request_options=request_options,
        )
        return _response.data

    def get_customer(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetCustomerRespBody:
        """
        Fetch one customer.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.get_customer(
            id="id",
        )
        """
        _response = self._raw_client.get_customer(id, request_options=request_options)
        return _response.data

    def delete_customer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCustomerRespBody:
        """
        Delete a customer. Idempotent.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCustomerRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.delete_customer(
            id="id",
        )
        """
        _response = self._raw_client.delete_customer(id, request_options=request_options)
        return _response.data

    def upload_avatar(
        self, id: str, *, image: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadAvatarRespBody:
        """
        Upload customer avatar (multipart, ≤5MB).

        Parameters
        ----------
        id : str

        image : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadAvatarRespBody
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.upload_avatar(
            id="id",
        )
        """
        _response = self._raw_client.upload_avatar(id, image=image, request_options=request_options)
        return _response.data


class AsyncCustomersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomersClient
        """
        return self._raw_client

    async def list_customers(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomersRespBody:
        """
        List customers.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomersRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.list_customers(
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_customers(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    async def create_customer(
        self,
        *,
        contact: Contact,
        email: Email,
        name: str,
        primary_address: Address,
        bio: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomerRespBody:
        """
        Create a customer.

        Parameters
        ----------
        contact : Contact

        email : Email

        name : str

        primary_address : Address

        bio : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomerRespBody
            Created

        Examples
        --------
        import asyncio

        from fern import Address, AsyncFernApi, Contact

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.create_customer(
                contact=Contact(),
                email="email",
                name="name",
                primary_address=Address(
                    city="city",
                    country="country",
                    postal_code="postalCode",
                    street="street",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_customer(
            contact=contact,
            email=email,
            name=name,
            primary_address=primary_address,
            bio=bio,
            request_options=request_options,
        )
        return _response.data

    async def get_customer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerRespBody:
        """
        Fetch one customer.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.get_customer(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customer(id, request_options=request_options)
        return _response.data

    async def delete_customer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCustomerRespBody:
        """
        Delete a customer. Idempotent.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCustomerRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.delete_customer(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_customer(id, request_options=request_options)
        return _response.data

    async def upload_avatar(
        self, id: str, *, image: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadAvatarRespBody:
        """
        Upload customer avatar (multipart, ≤5MB).

        Parameters
        ----------
        id : str

        image : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadAvatarRespBody
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.upload_avatar(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_avatar(id, image=image, request_options=request_options)
        return _response.data
