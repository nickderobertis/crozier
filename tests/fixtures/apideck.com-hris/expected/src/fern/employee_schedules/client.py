

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_employee_schedules_response import GetEmployeeSchedulesResponse
from .raw_client import AsyncRawEmployeeSchedulesClient, RawEmployeeSchedulesClient


class EmployeeSchedulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmployeeSchedulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmployeeSchedulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmployeeSchedulesClient
        """
        return self._raw_client

    def all_(
        self,
        employee_id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEmployeeSchedulesResponse:
        """
        List schedules for employee, a schedule is a work pattern, not the actual worked hours, for an employee.

        Parameters
        ----------
        employee_id : str
            ID of the employee you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEmployeeSchedulesResponse
            EmployeeSchedules

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.employee_schedules.all_(
            employee_id="employee_id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(employee_id, raw=raw, fields=fields, request_options=request_options)
        return _response.data


class AsyncEmployeeSchedulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmployeeSchedulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmployeeSchedulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmployeeSchedulesClient
        """
        return self._raw_client

    async def all_(
        self,
        employee_id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEmployeeSchedulesResponse:
        """
        List schedules for employee, a schedule is a work pattern, not the actual worked hours, for an employee.

        Parameters
        ----------
        employee_id : str
            ID of the employee you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEmployeeSchedulesResponse
            EmployeeSchedules

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
            await client.employee_schedules.all_(
                employee_id="employee_id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(employee_id, raw=raw, fields=fields, request_options=request_options)
        return _response.data
