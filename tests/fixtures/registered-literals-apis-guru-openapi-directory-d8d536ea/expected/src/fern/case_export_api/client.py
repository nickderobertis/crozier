

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.case_export_callback import CaseExportCallback
from ..types.case_export_callback_list_response import CaseExportCallbackListResponse
from .raw_client import AsyncRawCaseExportApiClient, RawCaseExportApiClient
from .types.get_case_export_callbacks_request_status import GetCaseExportCallbacksRequestStatus


class CaseExportApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCaseExportApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCaseExportApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCaseExportApiClient
        """
        return self._raw_client

    def get_case_export_callbacks(
        self,
        *,
        date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCaseExportCallbacksRequestStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseExportCallbackListResponse:
        """
        Retrieve callbacks according to the specified criteria.

        Parameters
        ----------
        date : typing.Optional[dt.datetime]
            The date for which callbacks are to be retrieved.

        status : typing.Optional[GetCaseExportCallbacksRequestStatus]
            The status code of the callbacks to be retrieved.

        page_number : typing.Optional[int]
            The page number of the callbacks to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseExportCallbackListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_export_api.get_case_export_callbacks(
            page_number=1,
        )
        """
        _response = self._raw_client.get_case_export_callbacks(
            date=date, status=status, page_number=page_number, request_options=request_options
        )
        return _response.data

    def get_case_export_callback_by_id(
        self, case_export_callback_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseExportCallback:
        """
        Retrieve the specified case export callback object.

        Parameters
        ----------
        case_export_callback_id : str
            The caseExportCallbackId value of the case export callback object to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseExportCallback
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_export_api.get_case_export_callback_by_id(
            case_export_callback_id="CBCEG63f4e233eXqD1",
        )
        """
        _response = self._raw_client.get_case_export_callback_by_id(
            case_export_callback_id, request_options=request_options
        )
        return _response.data

    def export_case(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseExportCallback:
        """
        Retrieve information about the specified case export.

        Parameters
        ----------
        case_id : str
            The caseId value of the case for which case export information is to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseExportCallback
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_export_api.export_case(
            case_id="CASEhq2c3224900a48",
        )
        """
        _response = self._raw_client.export_case(case_id, request_options=request_options)
        return _response.data


class AsyncCaseExportApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCaseExportApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCaseExportApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCaseExportApiClient
        """
        return self._raw_client

    async def get_case_export_callbacks(
        self,
        *,
        date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCaseExportCallbacksRequestStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseExportCallbackListResponse:
        """
        Retrieve callbacks according to the specified criteria.

        Parameters
        ----------
        date : typing.Optional[dt.datetime]
            The date for which callbacks are to be retrieved.

        status : typing.Optional[GetCaseExportCallbacksRequestStatus]
            The status code of the callbacks to be retrieved.

        page_number : typing.Optional[int]
            The page number of the callbacks to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseExportCallbackListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_export_api.get_case_export_callbacks(
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_export_callbacks(
            date=date, status=status, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def get_case_export_callback_by_id(
        self, case_export_callback_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseExportCallback:
        """
        Retrieve the specified case export callback object.

        Parameters
        ----------
        case_export_callback_id : str
            The caseExportCallbackId value of the case export callback object to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseExportCallback
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_export_api.get_case_export_callback_by_id(
                case_export_callback_id="CBCEG63f4e233eXqD1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_export_callback_by_id(
            case_export_callback_id, request_options=request_options
        )
        return _response.data

    async def export_case(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseExportCallback:
        """
        Retrieve information about the specified case export.

        Parameters
        ----------
        case_id : str
            The caseId value of the case for which case export information is to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseExportCallback
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_export_api.export_case(
                case_id="CASEhq2c3224900a48",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_case(case_id, request_options=request_options)
        return _response.data
