

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAddressesClient, RawAddressesClient
from .types.create_address_request_data import CreateAddressRequestData
from .types.update_address_request_data import UpdateAddressRequestData


OMIT = typing.cast(typing.Any, ...)


class AddressesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAddressesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAddressesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAddressesClient
        """
        return self._raw_client

    def get_address(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get address

        Parameters
        ----------
        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.addresses.get_address(
            include="customer,country",
        )
        """
        _response = self._raw_client.get_address(include=include, request_options=request_options)
        return _response.data

    def delete_address(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete address

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.addresses.delete_address()
        """
        _response = self._raw_client.delete_address(request_options=request_options)
        return _response.data

    def update_address(
        self,
        *,
        data: typing.Optional[UpdateAddressRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update address

        Parameters
        ----------
        data : typing.Optional[UpdateAddressRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.addresses import (
            UpdateAddressRequestData,
            UpdateAddressRequestDataAttributes,
            UpdateAddressRequestDataRelationships,
            UpdateAddressRequestDataRelationshipsCountry,
            UpdateAddressRequestDataRelationshipsCountryData,
            UpdateAddressRequestDataRelationshipsCustomer,
            UpdateAddressRequestDataRelationshipsCustomerData,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.addresses.update_address(
            data=UpdateAddressRequestData(
                attributes=UpdateAddressRequestDataAttributes(
                    city="New York",
                    company_in="12345678",
                    company_name="ABC Company",
                    company_tin="CZ12345678",
                    contact_phone="789456789",
                    first_name="Jane",
                    last_name="Doe",
                    line_one="123 Main Street",
                    postcode="10001",
                ),
                id="1",
                relationships=UpdateAddressRequestDataRelationships(
                    country=UpdateAddressRequestDataRelationshipsCountry(
                        data=UpdateAddressRequestDataRelationshipsCountryData(
                            id="1",
                            type="countries",
                        ),
                    ),
                    customer=UpdateAddressRequestDataRelationshipsCustomer(
                        data=UpdateAddressRequestDataRelationshipsCustomerData(
                            id="1",
                            type="customers",
                        ),
                    ),
                ),
                type="addresses",
            ),
        )
        """
        _response = self._raw_client.update_address(data=data, request_options=request_options)
        return _response.data

    def create_address(
        self,
        *,
        data: typing.Optional[CreateAddressRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create address

        Parameters
        ----------
        data : typing.Optional[CreateAddressRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.addresses import (
            CreateAddressRequestData,
            CreateAddressRequestDataAttributes,
            CreateAddressRequestDataRelationships,
            CreateAddressRequestDataRelationshipsCountry,
            CreateAddressRequestDataRelationshipsCountryData,
            CreateAddressRequestDataRelationshipsCustomer,
            CreateAddressRequestDataRelationshipsCustomerData,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.addresses.create_address(
            data=CreateAddressRequestData(
                attributes=CreateAddressRequestDataAttributes(
                    city="New York",
                    company_name="ABC Company",
                    first_name="John",
                    last_name="Doe",
                    line_one="123 Main Street",
                    postcode="10001",
                ),
                relationships=CreateAddressRequestDataRelationships(
                    country=CreateAddressRequestDataRelationshipsCountry(
                        data=CreateAddressRequestDataRelationshipsCountryData(
                            id="1",
                            type="countries",
                        ),
                    ),
                    customer=CreateAddressRequestDataRelationshipsCustomer(
                        data=CreateAddressRequestDataRelationshipsCustomerData(
                            id="1",
                            type="customers",
                        ),
                    ),
                ),
                type="addresses",
            ),
        )
        """
        _response = self._raw_client.create_address(data=data, request_options=request_options)
        return _response.data

    def get_address_country(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get address country

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.addresses.get_address_country()
        """
        _response = self._raw_client.get_address_country(request_options=request_options)
        return _response.data

    def get_address_country_relationship(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get address country relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.addresses.get_address_country_relationship()
        """
        _response = self._raw_client.get_address_country_relationship(request_options=request_options)
        return _response.data

    def get_address_customer(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get address customer

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.addresses.get_address_customer()
        """
        _response = self._raw_client.get_address_customer(request_options=request_options)
        return _response.data

    def get_address_customer_relationship(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get address customer relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.addresses.get_address_customer_relationship()
        """
        _response = self._raw_client.get_address_customer_relationship(request_options=request_options)
        return _response.data


class AsyncAddressesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAddressesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAddressesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAddressesClient
        """
        return self._raw_client

    async def get_address(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get address

        Parameters
        ----------
        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.addresses.get_address(
                include="customer,country",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_address(include=include, request_options=request_options)
        return _response.data

    async def delete_address(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete address

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.addresses.delete_address()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_address(request_options=request_options)
        return _response.data

    async def update_address(
        self,
        *,
        data: typing.Optional[UpdateAddressRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update address

        Parameters
        ----------
        data : typing.Optional[UpdateAddressRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.addresses import (
            UpdateAddressRequestData,
            UpdateAddressRequestDataAttributes,
            UpdateAddressRequestDataRelationships,
            UpdateAddressRequestDataRelationshipsCountry,
            UpdateAddressRequestDataRelationshipsCountryData,
            UpdateAddressRequestDataRelationshipsCustomer,
            UpdateAddressRequestDataRelationshipsCustomerData,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.addresses.update_address(
                data=UpdateAddressRequestData(
                    attributes=UpdateAddressRequestDataAttributes(
                        city="New York",
                        company_in="12345678",
                        company_name="ABC Company",
                        company_tin="CZ12345678",
                        contact_phone="789456789",
                        first_name="Jane",
                        last_name="Doe",
                        line_one="123 Main Street",
                        postcode="10001",
                    ),
                    id="1",
                    relationships=UpdateAddressRequestDataRelationships(
                        country=UpdateAddressRequestDataRelationshipsCountry(
                            data=UpdateAddressRequestDataRelationshipsCountryData(
                                id="1",
                                type="countries",
                            ),
                        ),
                        customer=UpdateAddressRequestDataRelationshipsCustomer(
                            data=UpdateAddressRequestDataRelationshipsCustomerData(
                                id="1",
                                type="customers",
                            ),
                        ),
                    ),
                    type="addresses",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_address(data=data, request_options=request_options)
        return _response.data

    async def create_address(
        self,
        *,
        data: typing.Optional[CreateAddressRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create address

        Parameters
        ----------
        data : typing.Optional[CreateAddressRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.addresses import (
            CreateAddressRequestData,
            CreateAddressRequestDataAttributes,
            CreateAddressRequestDataRelationships,
            CreateAddressRequestDataRelationshipsCountry,
            CreateAddressRequestDataRelationshipsCountryData,
            CreateAddressRequestDataRelationshipsCustomer,
            CreateAddressRequestDataRelationshipsCustomerData,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.addresses.create_address(
                data=CreateAddressRequestData(
                    attributes=CreateAddressRequestDataAttributes(
                        city="New York",
                        company_name="ABC Company",
                        first_name="John",
                        last_name="Doe",
                        line_one="123 Main Street",
                        postcode="10001",
                    ),
                    relationships=CreateAddressRequestDataRelationships(
                        country=CreateAddressRequestDataRelationshipsCountry(
                            data=CreateAddressRequestDataRelationshipsCountryData(
                                id="1",
                                type="countries",
                            ),
                        ),
                        customer=CreateAddressRequestDataRelationshipsCustomer(
                            data=CreateAddressRequestDataRelationshipsCustomerData(
                                id="1",
                                type="customers",
                            ),
                        ),
                    ),
                    type="addresses",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_address(data=data, request_options=request_options)
        return _response.data

    async def get_address_country(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get address country

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.addresses.get_address_country()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_address_country(request_options=request_options)
        return _response.data

    async def get_address_country_relationship(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get address country relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.addresses.get_address_country_relationship()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_address_country_relationship(request_options=request_options)
        return _response.data

    async def get_address_customer(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get address customer

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.addresses.get_address_customer()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_address_customer(request_options=request_options)
        return _response.data

    async def get_address_customer_relationship(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get address customer relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.addresses.get_address_customer_relationship()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_address_customer_relationship(request_options=request_options)
        return _response.data
