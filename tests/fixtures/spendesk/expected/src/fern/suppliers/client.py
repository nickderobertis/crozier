

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.supplier_input import SupplierInput
from .raw_client import AsyncRawSuppliersClient, RawSuppliersClient
from .types.updatesupplierstatus_request_status import UpdatesupplierstatusRequestStatus


OMIT = typing.cast(typing.Any, ...)


class SuppliersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSuppliersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSuppliersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSuppliersClient
        """
        return self._raw_client

    def listsuppliers(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        per_page : typing.Optional[int]

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
        client.suppliers.listsuppliers()
        """
        _response = self._raw_client.listsuppliers(page=page, per_page=per_page, request_options=request_options)
        return _response.data

    def createsupplier(
        self,
        *,
        name: str,
        vat_number: typing.Optional[str] = OMIT,
        iban: typing.Optional[str] = OMIT,
        address: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str

        vat_number : typing.Optional[str]

        iban : typing.Optional[str]

        address : typing.Optional[typing.Dict[str, typing.Any]]

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
        client.suppliers.createsupplier(
            name="name",
        )
        """
        _response = self._raw_client.createsupplier(
            name=name, vat_number=vat_number, iban=iban, address=address, request_options=request_options
        )
        return _response.data

    def updatesuppliers(
        self, *, request: typing.Sequence[SupplierInput], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Sequence[SupplierInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, SupplierInput

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.suppliers.updatesuppliers(
            request=[
                SupplierInput(
                    name="name",
                )
            ],
        )
        """
        _response = self._raw_client.updatesuppliers(request=request, request_options=request_options)
        return _response.data

    def getsupplier(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
        client.suppliers.getsupplier(
            id="id",
        )
        """
        _response = self._raw_client.getsupplier(id, request_options=request_options)
        return _response.data

    def updatesupplierstatus(
        self,
        id: str,
        *,
        status: UpdatesupplierstatusRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        status : UpdatesupplierstatusRequestStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.suppliers import UpdatesupplierstatusRequestStatus

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.suppliers.updatesupplierstatus(
            id="id",
            status=UpdatesupplierstatusRequestStatus.ACTIVE,
        )
        """
        _response = self._raw_client.updatesupplierstatus(id, status=status, request_options=request_options)
        return _response.data


class AsyncSuppliersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSuppliersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSuppliersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSuppliersClient
        """
        return self._raw_client

    async def listsuppliers(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        per_page : typing.Optional[int]

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
            await client.suppliers.listsuppliers()


        asyncio.run(main())
        """
        _response = await self._raw_client.listsuppliers(page=page, per_page=per_page, request_options=request_options)
        return _response.data

    async def createsupplier(
        self,
        *,
        name: str,
        vat_number: typing.Optional[str] = OMIT,
        iban: typing.Optional[str] = OMIT,
        address: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str

        vat_number : typing.Optional[str]

        iban : typing.Optional[str]

        address : typing.Optional[typing.Dict[str, typing.Any]]

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
            await client.suppliers.createsupplier(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createsupplier(
            name=name, vat_number=vat_number, iban=iban, address=address, request_options=request_options
        )
        return _response.data

    async def updatesuppliers(
        self, *, request: typing.Sequence[SupplierInput], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Sequence[SupplierInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SupplierInput

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.suppliers.updatesuppliers(
                request=[
                    SupplierInput(
                        name="name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatesuppliers(request=request, request_options=request_options)
        return _response.data

    async def getsupplier(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            await client.suppliers.getsupplier(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getsupplier(id, request_options=request_options)
        return _response.data

    async def updatesupplierstatus(
        self,
        id: str,
        *,
        status: UpdatesupplierstatusRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        status : UpdatesupplierstatusRequestStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.suppliers import UpdatesupplierstatusRequestStatus

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.suppliers.updatesupplierstatus(
                id="id",
                status=UpdatesupplierstatusRequestStatus.ACTIVE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatesupplierstatus(id, status=status, request_options=request_options)
        return _response.data
