

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_time_off_request_response import CreateTimeOffRequestResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.delete_time_off_request_response import DeleteTimeOffRequestResponse
from ..types.get_time_off_request_response import GetTimeOffRequestResponse
from ..types.get_time_off_requests_response import GetTimeOffRequestsResponse
from ..types.id import Id
from ..types.time_off_request_notes import TimeOffRequestNotes
from ..types.time_off_request_request_type import TimeOffRequestRequestType
from ..types.time_off_request_status import TimeOffRequestStatus
from ..types.time_off_request_units import TimeOffRequestUnits
from ..types.time_off_requests_filter import TimeOffRequestsFilter
from ..types.update_time_off_request_response import UpdateTimeOffRequestResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from .raw_client import AsyncRawTimeOffRequestsClient, RawTimeOffRequestsClient


OMIT = typing.cast(typing.Any, ...)


class TimeOffRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTimeOffRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTimeOffRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTimeOffRequestsClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[TimeOffRequestsFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTimeOffRequestsResponse:
        """
        List Time Off Requests

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[TimeOffRequestsFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTimeOffRequestsResponse
            TimeOffRequests

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.time_off_requests.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, filter=filter, fields=fields, request_options=request_options
        )
        return _response.data

    def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        amount: typing.Optional[float] = OMIT,
        approval_date: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        employee_id: typing.Optional[str] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[Id] = OMIT,
        notes: typing.Optional[TimeOffRequestNotes] = OMIT,
        policy_id: typing.Optional[str] = OMIT,
        request_date: typing.Optional[str] = OMIT,
        request_type: typing.Optional[TimeOffRequestRequestType] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[TimeOffRequestStatus] = OMIT,
        units: typing.Optional[TimeOffRequestUnits] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTimeOffRequestResponse:
        """
        Create Time Off Request

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        amount : typing.Optional[float]
            The amount of time off requested.

        approval_date : typing.Optional[str]
            The date the request was approved

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            Description of the time off request.

        employee_id : typing.Optional[str]
            ID of the employee

        end_date : typing.Optional[str]
            The end date of the time off request.

        id : typing.Optional[Id]

        notes : typing.Optional[TimeOffRequestNotes]

        policy_id : typing.Optional[str]
            ID of the policy

        request_date : typing.Optional[str]
            The date the request was made.

        request_type : typing.Optional[TimeOffRequestRequestType]
            The type of request

        start_date : typing.Optional[str]
            The start date of the time off request.

        status : typing.Optional[TimeOffRequestStatus]
            The status of the time off request.

        units : typing.Optional[TimeOffRequestUnits]
            The unit of time off requested. Possible values include: `hours`, `days`, or `other`.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTimeOffRequestResponse
            TimeOffRequests

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.time_off_requests.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            amount=amount,
            approval_date=approval_date,
            created_at=created_at,
            created_by=created_by,
            description=description,
            employee_id=employee_id,
            end_date=end_date,
            id=id,
            notes=notes,
            policy_id=policy_id,
            request_date=request_date,
            request_type=request_type,
            start_date=start_date,
            status=status,
            units=units,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTimeOffRequestResponse:
        """
        Get Time Off Request

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTimeOffRequestResponse
            TimeOffRequests

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.time_off_requests.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTimeOffRequestResponse:
        """
        Delete Time Off Request

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTimeOffRequestResponse
            TimeOffRequests

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.time_off_requests.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        amount: typing.Optional[float] = OMIT,
        approval_date: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        employee_id: typing.Optional[str] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[Id] = OMIT,
        notes: typing.Optional[TimeOffRequestNotes] = OMIT,
        policy_id: typing.Optional[str] = OMIT,
        request_date: typing.Optional[str] = OMIT,
        request_type: typing.Optional[TimeOffRequestRequestType] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[TimeOffRequestStatus] = OMIT,
        units: typing.Optional[TimeOffRequestUnits] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTimeOffRequestResponse:
        """
        Update Time Off Request

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        amount : typing.Optional[float]
            The amount of time off requested.

        approval_date : typing.Optional[str]
            The date the request was approved

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            Description of the time off request.

        employee_id : typing.Optional[str]
            ID of the employee

        end_date : typing.Optional[str]
            The end date of the time off request.

        id : typing.Optional[Id]

        notes : typing.Optional[TimeOffRequestNotes]

        policy_id : typing.Optional[str]
            ID of the policy

        request_date : typing.Optional[str]
            The date the request was made.

        request_type : typing.Optional[TimeOffRequestRequestType]
            The type of request

        start_date : typing.Optional[str]
            The start date of the time off request.

        status : typing.Optional[TimeOffRequestStatus]
            The status of the time off request.

        units : typing.Optional[TimeOffRequestUnits]
            The unit of time off requested. Possible values include: `hours`, `days`, or `other`.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTimeOffRequestResponse
            TimeOffRequests

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.time_off_requests.update(
            id_="id",
        )
        """
        _response = self._raw_client.update(
            id_,
            raw=raw,
            amount=amount,
            approval_date=approval_date,
            created_at=created_at,
            created_by=created_by,
            description=description,
            employee_id=employee_id,
            end_date=end_date,
            id=id,
            notes=notes,
            policy_id=policy_id,
            request_date=request_date,
            request_type=request_type,
            start_date=start_date,
            status=status,
            units=units,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data


class AsyncTimeOffRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTimeOffRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTimeOffRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTimeOffRequestsClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[TimeOffRequestsFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTimeOffRequestsResponse:
        """
        List Time Off Requests

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[TimeOffRequestsFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTimeOffRequestsResponse
            TimeOffRequests

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.time_off_requests.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, filter=filter, fields=fields, request_options=request_options
        )
        return _response.data

    async def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        amount: typing.Optional[float] = OMIT,
        approval_date: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        employee_id: typing.Optional[str] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[Id] = OMIT,
        notes: typing.Optional[TimeOffRequestNotes] = OMIT,
        policy_id: typing.Optional[str] = OMIT,
        request_date: typing.Optional[str] = OMIT,
        request_type: typing.Optional[TimeOffRequestRequestType] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[TimeOffRequestStatus] = OMIT,
        units: typing.Optional[TimeOffRequestUnits] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTimeOffRequestResponse:
        """
        Create Time Off Request

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        amount : typing.Optional[float]
            The amount of time off requested.

        approval_date : typing.Optional[str]
            The date the request was approved

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            Description of the time off request.

        employee_id : typing.Optional[str]
            ID of the employee

        end_date : typing.Optional[str]
            The end date of the time off request.

        id : typing.Optional[Id]

        notes : typing.Optional[TimeOffRequestNotes]

        policy_id : typing.Optional[str]
            ID of the policy

        request_date : typing.Optional[str]
            The date the request was made.

        request_type : typing.Optional[TimeOffRequestRequestType]
            The type of request

        start_date : typing.Optional[str]
            The start date of the time off request.

        status : typing.Optional[TimeOffRequestStatus]
            The status of the time off request.

        units : typing.Optional[TimeOffRequestUnits]
            The unit of time off requested. Possible values include: `hours`, `days`, or `other`.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTimeOffRequestResponse
            TimeOffRequests

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.time_off_requests.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            amount=amount,
            approval_date=approval_date,
            created_at=created_at,
            created_by=created_by,
            description=description,
            employee_id=employee_id,
            end_date=end_date,
            id=id,
            notes=notes,
            policy_id=policy_id,
            request_date=request_date,
            request_type=request_type,
            start_date=start_date,
            status=status,
            units=units,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTimeOffRequestResponse:
        """
        Get Time Off Request

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTimeOffRequestResponse
            TimeOffRequests

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.time_off_requests.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTimeOffRequestResponse:
        """
        Delete Time Off Request

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTimeOffRequestResponse
            TimeOffRequests

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.time_off_requests.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        amount: typing.Optional[float] = OMIT,
        approval_date: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        employee_id: typing.Optional[str] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[Id] = OMIT,
        notes: typing.Optional[TimeOffRequestNotes] = OMIT,
        policy_id: typing.Optional[str] = OMIT,
        request_date: typing.Optional[str] = OMIT,
        request_type: typing.Optional[TimeOffRequestRequestType] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[TimeOffRequestStatus] = OMIT,
        units: typing.Optional[TimeOffRequestUnits] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTimeOffRequestResponse:
        """
        Update Time Off Request

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        amount : typing.Optional[float]
            The amount of time off requested.

        approval_date : typing.Optional[str]
            The date the request was approved

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            Description of the time off request.

        employee_id : typing.Optional[str]
            ID of the employee

        end_date : typing.Optional[str]
            The end date of the time off request.

        id : typing.Optional[Id]

        notes : typing.Optional[TimeOffRequestNotes]

        policy_id : typing.Optional[str]
            ID of the policy

        request_date : typing.Optional[str]
            The date the request was made.

        request_type : typing.Optional[TimeOffRequestRequestType]
            The type of request

        start_date : typing.Optional[str]
            The start date of the time off request.

        status : typing.Optional[TimeOffRequestStatus]
            The status of the time off request.

        units : typing.Optional[TimeOffRequestUnits]
            The unit of time off requested. Possible values include: `hours`, `days`, or `other`.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTimeOffRequestResponse
            TimeOffRequests

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.time_off_requests.update(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            raw=raw,
            amount=amount,
            approval_date=approval_date,
            created_at=created_at,
            created_by=created_by,
            description=description,
            employee_id=employee_id,
            end_date=end_date,
            id=id,
            notes=notes,
            policy_id=policy_id,
            request_date=request_date,
            request_type=request_type,
            start_date=start_date,
            status=status,
            units=units,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data
