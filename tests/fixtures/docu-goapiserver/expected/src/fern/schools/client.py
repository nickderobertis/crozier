

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.school import School
from .raw_client import AsyncRawSchoolsClient, RawSchoolsClient


OMIT = typing.cast(typing.Any, ...)


class SchoolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSchoolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSchoolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSchoolsClient
        """
        return self._raw_client

    def get_schools_v3(
        self,
        *,
        company_id: str,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        only_active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[School]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns an unpaginated array; school_ids and only_active are optional filters.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Restrict to these school UUIDs. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        only_active : typing.Optional[bool]
            Return active schools only. Only true/1 enables the filter; other values disable it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[School]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schools.get_schools_v3(
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_schools_v3(
            company_id=company_id, school_ids=school_ids, only_active=only_active, request_options=request_options
        )
        return _response.data

    def get_schools_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> School:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns 404 when the school does not exist for the requested company.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        School
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schools.get_schools_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_schools_id_v3(id, company_id=company_id, request_options=request_options)
        return _response.data

    def patch_schools_id_v3(
        self, id: str, *, company_id: str, capacity: int, request_options: typing.Optional[RequestOptions] = None
    ) -> School:
        """
        Requires company_id, an authenticated session with schools assigned, and the target school in those assignments. Updates capacity, then reads the school in the requested company. A failed subsequent read can return 404 or 500 after the write has executed.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        capacity : int
            New school capacity; must be greater than zero.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        School
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schools.patch_schools_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
            capacity=120,
        )
        """
        _response = self._raw_client.patch_schools_id_v3(
            id, company_id=company_id, capacity=capacity, request_options=request_options
        )
        return _response.data


class AsyncSchoolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSchoolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSchoolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSchoolsClient
        """
        return self._raw_client

    async def get_schools_v3(
        self,
        *,
        company_id: str,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        only_active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[School]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns an unpaginated array; school_ids and only_active are optional filters.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Restrict to these school UUIDs. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        only_active : typing.Optional[bool]
            Return active schools only. Only true/1 enables the filter; other values disable it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[School]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schools.get_schools_v3(
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schools_v3(
            company_id=company_id, school_ids=school_ids, only_active=only_active, request_options=request_options
        )
        return _response.data

    async def get_schools_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> School:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns 404 when the school does not exist for the requested company.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        School
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schools.get_schools_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schools_id_v3(id, company_id=company_id, request_options=request_options)
        return _response.data

    async def patch_schools_id_v3(
        self, id: str, *, company_id: str, capacity: int, request_options: typing.Optional[RequestOptions] = None
    ) -> School:
        """
        Requires company_id, an authenticated session with schools assigned, and the target school in those assignments. Updates capacity, then reads the school in the requested company. A failed subsequent read can return 404 or 500 after the write has executed.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        capacity : int
            New school capacity; must be greater than zero.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        School
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schools.patch_schools_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
                capacity=120,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_schools_id_v3(
            id, company_id=company_id, capacity=capacity, request_options=request_options
        )
        return _response.data
