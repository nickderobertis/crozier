

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.data_refresh import DataRefresh
from ..types.school_refresh import SchoolRefresh
from .raw_client import AsyncRawDataRefreshClient, RawDataRefreshClient


class DataRefreshClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataRefreshClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataRefreshClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataRefreshClient
        """
        return self._raw_client

    def get_data_refresh_v3(
        self, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DataRefresh:
        """
        Returns the latest recorded company process. Returns 404 when no process is available. last_data_refresh_at is a display timestamp rather than an RFC3339 value.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataRefresh
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.data_refresh.get_data_refresh_v3(
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_data_refresh_v3(company_id=company_id, request_options=request_options)
        return _response.data

    def get_data_refresh_details_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SchoolRefresh]:
        """
        Returns the latest school process statuses grouped by school. An explicit school_id must be assigned to the session. Without school_id, the current process lookup requests company-wide statuses. The school-name lookup uses the session school assignments. Returns an array without pagination headers.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchoolRefresh]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.data_refresh.get_data_refresh_details_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_data_refresh_details_v3(
            company_id=company_id, school_id=school_id, request_options=request_options
        )
        return _response.data


class AsyncDataRefreshClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataRefreshClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataRefreshClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataRefreshClient
        """
        return self._raw_client

    async def get_data_refresh_v3(
        self, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DataRefresh:
        """
        Returns the latest recorded company process. Returns 404 when no process is available. last_data_refresh_at is a display timestamp rather than an RFC3339 value.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataRefresh
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.data_refresh.get_data_refresh_v3(
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_data_refresh_v3(company_id=company_id, request_options=request_options)
        return _response.data

    async def get_data_refresh_details_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SchoolRefresh]:
        """
        Returns the latest school process statuses grouped by school. An explicit school_id must be assigned to the session. Without school_id, the current process lookup requests company-wide statuses. The school-name lookup uses the session school assignments. Returns an array without pagination headers.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchoolRefresh]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.data_refresh.get_data_refresh_details_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_data_refresh_details_v3(
            company_id=company_id, school_id=school_id, request_options=request_options
        )
        return _response.data
