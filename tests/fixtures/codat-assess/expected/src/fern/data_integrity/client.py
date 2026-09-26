

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.details import Details
from ..types.status import Status
from ..types.summaries import Summaries
from .raw_client import AsyncRawDataIntegrityClient, RawDataIntegrityClient
from .types.get_data_integrity_details_request_data_type import GetDataIntegrityDetailsRequestDataType
from .types.get_data_integrity_status_request_data_type import GetDataIntegrityStatusRequestDataType
from .types.get_data_integrity_summaries_request_data_type import GetDataIntegritySummariesRequestDataType


class DataIntegrityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataIntegrityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataIntegrityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataIntegrityClient
        """
        return self._raw_client

    def get_data_integrity_details(
        self,
        company_id: str,
        data_type: GetDataIntegrityDetailsRequestDataType,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Details:
        """
        Gets record-by-record match results for a given company and datatype, optionally restricted by a Codat query string.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegrityDetailsRequestDataType
            A key for a Codat data type.

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        order_by : typing.Optional[str]
            Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Details
            OK

        Examples
        --------
        from fern.data_integrity import GetDataIntegrityDetailsRequestDataType

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_integrity.get_data_integrity_details(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            data_type=GetDataIntegrityDetailsRequestDataType.BANKING_ACCOUNTS,
            page=1,
            page_size=100,
            order_by="-modifiedDate",
        )
        """
        _response = self._raw_client.get_data_integrity_details(
            company_id,
            data_type,
            page=page,
            page_size=page_size,
            query=query,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def get_data_integrity_status(
        self,
        company_id: str,
        data_type: GetDataIntegrityStatusRequestDataType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Status:
        """
        Gets match status for a given company and datatype.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegrityStatusRequestDataType
            A key for a Codat data type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Status
            OK

        Examples
        --------
        from fern.data_integrity import GetDataIntegrityStatusRequestDataType

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_integrity.get_data_integrity_status(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            data_type=GetDataIntegrityStatusRequestDataType.BANKING_ACCOUNTS,
        )
        """
        _response = self._raw_client.get_data_integrity_status(company_id, data_type, request_options=request_options)
        return _response.data

    def get_data_integrity_summaries(
        self,
        company_id: str,
        data_type: GetDataIntegritySummariesRequestDataType,
        *,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Summaries:
        """
        Gets match summary for a given company and datatype, optionally restricted by a Codat query string.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegritySummariesRequestDataType
            A key for a Codat data type.

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Summaries
            OK

        Examples
        --------
        from fern.data_integrity import GetDataIntegritySummariesRequestDataType

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_integrity.get_data_integrity_summaries(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            data_type=GetDataIntegritySummariesRequestDataType.BANKING_ACCOUNTS,
        )
        """
        _response = self._raw_client.get_data_integrity_summaries(
            company_id, data_type, query=query, request_options=request_options
        )
        return _response.data


class AsyncDataIntegrityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataIntegrityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataIntegrityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataIntegrityClient
        """
        return self._raw_client

    async def get_data_integrity_details(
        self,
        company_id: str,
        data_type: GetDataIntegrityDetailsRequestDataType,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Details:
        """
        Gets record-by-record match results for a given company and datatype, optionally restricted by a Codat query string.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegrityDetailsRequestDataType
            A key for a Codat data type.

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        order_by : typing.Optional[str]
            Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Details
            OK

        Examples
        --------
        import asyncio

        from fern.data_integrity import GetDataIntegrityDetailsRequestDataType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_integrity.get_data_integrity_details(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                data_type=GetDataIntegrityDetailsRequestDataType.BANKING_ACCOUNTS,
                page=1,
                page_size=100,
                order_by="-modifiedDate",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_data_integrity_details(
            company_id,
            data_type,
            page=page,
            page_size=page_size,
            query=query,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def get_data_integrity_status(
        self,
        company_id: str,
        data_type: GetDataIntegrityStatusRequestDataType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Status:
        """
        Gets match status for a given company and datatype.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegrityStatusRequestDataType
            A key for a Codat data type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Status
            OK

        Examples
        --------
        import asyncio

        from fern.data_integrity import GetDataIntegrityStatusRequestDataType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_integrity.get_data_integrity_status(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                data_type=GetDataIntegrityStatusRequestDataType.BANKING_ACCOUNTS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_data_integrity_status(
            company_id, data_type, request_options=request_options
        )
        return _response.data

    async def get_data_integrity_summaries(
        self,
        company_id: str,
        data_type: GetDataIntegritySummariesRequestDataType,
        *,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Summaries:
        """
        Gets match summary for a given company and datatype, optionally restricted by a Codat query string.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegritySummariesRequestDataType
            A key for a Codat data type.

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Summaries
            OK

        Examples
        --------
        import asyncio

        from fern.data_integrity import GetDataIntegritySummariesRequestDataType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_integrity.get_data_integrity_summaries(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                data_type=GetDataIntegritySummariesRequestDataType.BANKING_ACCOUNTS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_data_integrity_summaries(
            company_id, data_type, query=query, request_options=request_options
        )
        return _response.data
