

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.procare_staff import ProcareStaff
from .raw_client import AsyncRawProcareStaffClient, RawProcareStaffClient


class ProcareStaffClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProcareStaffClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProcareStaffClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProcareStaffClient
        """
        return self._raw_client

    def get_procare_staff_v3(
        self, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ProcareStaff]]:
        """
        Requires school_id assigned to the session. Returns the school staff array directly, without pagination or X-Total-Count.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ProcareStaff]]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.procare_staff.get_procare_staff_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_procare_staff_v3(
            company_id=company_id, school_id=school_id, request_options=request_options
        )
        return _response.data

    def get_procare_staff_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcareStaff:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns the staff record directly. A missing record raises a data-layer error which this handler currently reports as HTTP 500.

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
        ProcareStaff
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.procare_staff.get_procare_staff_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_procare_staff_id_v3(id, company_id=company_id, request_options=request_options)
        return _response.data


class AsyncProcareStaffClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProcareStaffClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProcareStaffClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProcareStaffClient
        """
        return self._raw_client

    async def get_procare_staff_v3(
        self, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ProcareStaff]]:
        """
        Requires school_id assigned to the session. Returns the school staff array directly, without pagination or X-Total-Count.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ProcareStaff]]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.procare_staff.get_procare_staff_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_procare_staff_v3(
            company_id=company_id, school_id=school_id, request_options=request_options
        )
        return _response.data

    async def get_procare_staff_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcareStaff:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns the staff record directly. A missing record raises a data-layer error which this handler currently reports as HTTP 500.

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
        ProcareStaff
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.procare_staff.get_procare_staff_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_procare_staff_id_v3(
            id, company_id=company_id, request_options=request_options
        )
        return _response.data
