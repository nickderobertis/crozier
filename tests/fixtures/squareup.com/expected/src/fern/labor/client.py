

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.break_type import BreakType
from ..types.create_break_type_response import CreateBreakTypeResponse
from ..types.create_shift_response import CreateShiftResponse
from ..types.delete_break_type_response import DeleteBreakTypeResponse
from ..types.delete_shift_response import DeleteShiftResponse
from ..types.get_break_type_response import GetBreakTypeResponse
from ..types.get_employee_wage_response import GetEmployeeWageResponse
from ..types.get_shift_response import GetShiftResponse
from ..types.get_team_member_wage_response import GetTeamMemberWageResponse
from ..types.list_break_types_response import ListBreakTypesResponse
from ..types.list_employee_wages_response import ListEmployeeWagesResponse
from ..types.list_team_member_wages_response import ListTeamMemberWagesResponse
from ..types.list_workweek_configs_response import ListWorkweekConfigsResponse
from ..types.search_shifts_response import SearchShiftsResponse
from ..types.shift import Shift
from ..types.shift_query import ShiftQuery
from ..types.update_break_type_response import UpdateBreakTypeResponse
from ..types.update_shift_response import UpdateShiftResponse
from ..types.update_workweek_config_response import UpdateWorkweekConfigResponse
from ..types.workweek_config import WorkweekConfig
from .raw_client import AsyncRawLaborClient, RawLaborClient


OMIT = typing.cast(typing.Any, ...)


class LaborClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLaborClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLaborClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLaborClient
        """
        return self._raw_client

    def list_break_types(
        self,
        *,
        location_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBreakTypesResponse:
        """
        Returns a paginated list of `BreakType` instances for a business.

        Parameters
        ----------
        location_id : typing.Optional[str]
            Filter the returned `BreakType` results to only those that are associated with the
            specified location.

        limit : typing.Optional[int]
            The maximum number of `BreakType` results to return per page. The number can range between 1
            and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `BreakType` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBreakTypesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.list_break_types()
        """
        _response = self._raw_client.list_break_types(
            location_id=location_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    def create_break_type(
        self,
        *,
        break_type: BreakType,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateBreakTypeResponse:
        """
        Creates a new `BreakType`.

        A `BreakType` is a template for creating `Break` objects.
        You must provide the following values in your request to this
        endpoint:

        - `location_id`
        - `break_name`
        - `expected_duration`
        - `is_paid`

        You can only have three `BreakType` instances per location. If you attempt to add a fourth
        `BreakType` for a location, an `INVALID_REQUEST_ERROR` "Exceeded limit of 3 breaks per location."
        is returned.

        Parameters
        ----------
        break_type : BreakType

        idempotency_key : typing.Optional[str]
            A unique string value to ensure the idempotency of the operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBreakTypeResponse
            Success

        Examples
        --------
        from fern import BreakType, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.create_break_type(
            break_type=BreakType(
                break_name="break_name",
                expected_duration="expected_duration",
                is_paid=True,
                location_id="location_id",
            ),
        )
        """
        _response = self._raw_client.create_break_type(
            break_type=break_type, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def get_break_type(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBreakTypeResponse:
        """
        Returns a single `BreakType` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `BreakType` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBreakTypeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.get_break_type(
            id="id",
        )
        """
        _response = self._raw_client.get_break_type(id, request_options=request_options)
        return _response.data

    def update_break_type(
        self, id: str, *, break_type: BreakType, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateBreakTypeResponse:
        """
        Updates an existing `BreakType`.

        Parameters
        ----------
        id : str
             The UUID for the `BreakType` being updated.

        break_type : BreakType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateBreakTypeResponse
            Success

        Examples
        --------
        from fern import BreakType, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.update_break_type(
            id="id",
            break_type=BreakType(
                break_name="break_name",
                expected_duration="expected_duration",
                is_paid=True,
                location_id="location_id",
            ),
        )
        """
        _response = self._raw_client.update_break_type(id, break_type=break_type, request_options=request_options)
        return _response.data

    def delete_break_type(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteBreakTypeResponse:
        """
        Deletes an existing `BreakType`.

        A `BreakType` can be deleted even if it is referenced from a `Shift`.

        Parameters
        ----------
        id : str
            The UUID for the `BreakType` being deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteBreakTypeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.delete_break_type(
            id="id",
        )
        """
        _response = self._raw_client.delete_break_type(id, request_options=request_options)
        return _response.data

    def list_employee_wages(
        self,
        *,
        employee_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEmployeeWagesResponse:
        """
        Returns a paginated list of `EmployeeWage` instances for a business.

        Parameters
        ----------
        employee_id : typing.Optional[str]
            Filter the returned wages to only those that are associated with the specified employee.

        limit : typing.Optional[int]
            The maximum number of `EmployeeWage` results to return per page. The number can range between
            1 and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `EmployeeWage` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEmployeeWagesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.list_employee_wages()
        """
        _response = self._raw_client.list_employee_wages(
            employee_id=employee_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    def get_employee_wage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEmployeeWageResponse:
        """
        Returns a single `EmployeeWage` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `EmployeeWage` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEmployeeWageResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.get_employee_wage(
            id="id",
        )
        """
        _response = self._raw_client.get_employee_wage(id, request_options=request_options)
        return _response.data

    def create_shift(
        self,
        *,
        shift: Shift,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateShiftResponse:
        """
        Creates a new `Shift`.

        A `Shift` represents a complete workday for a single employee.
        You must provide the following values in your request to this
        endpoint:

        - `location_id`
        - `employee_id`
        - `start_at`

        An attempt to create a new `Shift` can result in a `BAD_REQUEST` error when:
        - The `status` of the new `Shift` is `OPEN` and the employee has another
        shift with an `OPEN` status.
        - The `start_at` date is in the future.
        - The `start_at` or `end_at` date overlaps another shift for the same employee.
        - The `Break` instances are set in the request and a break `start_at`
        is before the `Shift.start_at`, a break `end_at` is after
        the `Shift.end_at`, or both.

        Parameters
        ----------
        shift : Shift

        idempotency_key : typing.Optional[str]
            A unique string value to ensure the idempotency of the operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateShiftResponse
            Success

        Examples
        --------
        from fern import FernApi, Shift

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.create_shift(
            shift=Shift(
                start_at="start_at",
            ),
        )
        """
        _response = self._raw_client.create_shift(
            shift=shift, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def search_shifts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[ShiftQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchShiftsResponse:
        """
        Returns a paginated list of `Shift` records for a business.
        The list to be returned can be filtered by:
        - Location IDs.
        - Employee IDs.
        - Shift status (`OPEN` and `CLOSED`).
        - Shift start.
        - Shift end.
        - Workday details.

        The list can be sorted by:
        - `start_at`.
        - `end_at`.
        - `created_at`.
        - `updated_at`.

        Parameters
        ----------
        cursor : typing.Optional[str]
            An opaque cursor for fetching the next page.

        limit : typing.Optional[int]
            The number of resources in a page (200 by default).

        query : typing.Optional[ShiftQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchShiftsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.search_shifts()
        """
        _response = self._raw_client.search_shifts(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def get_shift(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetShiftResponse:
        """
        Returns a single `Shift` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `Shift` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetShiftResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.get_shift(
            id="id",
        )
        """
        _response = self._raw_client.get_shift(id, request_options=request_options)
        return _response.data

    def update_shift(
        self, id: str, *, shift: Shift, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateShiftResponse:
        """
        Updates an existing `Shift`.

        When adding a `Break` to a `Shift`, any earlier `Break` instances in the `Shift` have
        the `end_at` property set to a valid RFC-3339 datetime string.

        When closing a `Shift`, all `Break` instances in the `Shift` must be complete with `end_at`
        set on each `Break`.

        Parameters
        ----------
        id : str
            The ID of the object being updated.

        shift : Shift

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateShiftResponse
            Success

        Examples
        --------
        from fern import FernApi, Shift

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.update_shift(
            id="id",
            shift=Shift(
                start_at="start_at",
            ),
        )
        """
        _response = self._raw_client.update_shift(id, shift=shift, request_options=request_options)
        return _response.data

    def delete_shift(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteShiftResponse:
        """
        Deletes a `Shift`.

        Parameters
        ----------
        id : str
            The UUID for the `Shift` being deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteShiftResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.delete_shift(
            id="id",
        )
        """
        _response = self._raw_client.delete_shift(id, request_options=request_options)
        return _response.data

    def list_team_member_wages(
        self,
        *,
        team_member_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTeamMemberWagesResponse:
        """
        Returns a paginated list of `TeamMemberWage` instances for a business.

        Parameters
        ----------
        team_member_id : typing.Optional[str]
            Filter the returned wages to only those that are associated with the
            specified team member.

        limit : typing.Optional[int]
            The maximum number of `TeamMemberWage` results to return per page. The number can range between
            1 and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `EmployeeWage` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTeamMemberWagesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.list_team_member_wages()
        """
        _response = self._raw_client.list_team_member_wages(
            team_member_id=team_member_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    def get_team_member_wage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTeamMemberWageResponse:
        """
        Returns a single `TeamMemberWage` specified by `id `.

        Parameters
        ----------
        id : str
            The UUID for the `TeamMemberWage` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTeamMemberWageResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.get_team_member_wage(
            id="id",
        )
        """
        _response = self._raw_client.get_team_member_wage(id, request_options=request_options)
        return _response.data

    def list_workweek_configs(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListWorkweekConfigsResponse:
        """
        Returns a list of `WorkweekConfig` instances for a business.

        Parameters
        ----------
        limit : typing.Optional[int]
            The maximum number of `WorkweekConfigs` results to return per page.

        cursor : typing.Optional[str]
            A pointer to the next page of `WorkweekConfig` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWorkweekConfigsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.list_workweek_configs()
        """
        _response = self._raw_client.list_workweek_configs(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    def update_workweek_config(
        self, id: str, *, workweek_config: WorkweekConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateWorkweekConfigResponse:
        """
        Updates a `WorkweekConfig`.

        Parameters
        ----------
        id : str
            The UUID for the `WorkweekConfig` object being updated.

        workweek_config : WorkweekConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWorkweekConfigResponse
            Success

        Examples
        --------
        from fern import FernApi, WorkweekConfig

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.labor.update_workweek_config(
            id="id",
            workweek_config=WorkweekConfig(
                start_of_day_local_time="start_of_day_local_time",
                start_of_week="start_of_week",
            ),
        )
        """
        _response = self._raw_client.update_workweek_config(
            id, workweek_config=workweek_config, request_options=request_options
        )
        return _response.data


class AsyncLaborClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLaborClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLaborClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLaborClient
        """
        return self._raw_client

    async def list_break_types(
        self,
        *,
        location_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBreakTypesResponse:
        """
        Returns a paginated list of `BreakType` instances for a business.

        Parameters
        ----------
        location_id : typing.Optional[str]
            Filter the returned `BreakType` results to only those that are associated with the
            specified location.

        limit : typing.Optional[int]
            The maximum number of `BreakType` results to return per page. The number can range between 1
            and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `BreakType` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBreakTypesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.list_break_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_break_types(
            location_id=location_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def create_break_type(
        self,
        *,
        break_type: BreakType,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateBreakTypeResponse:
        """
        Creates a new `BreakType`.

        A `BreakType` is a template for creating `Break` objects.
        You must provide the following values in your request to this
        endpoint:

        - `location_id`
        - `break_name`
        - `expected_duration`
        - `is_paid`

        You can only have three `BreakType` instances per location. If you attempt to add a fourth
        `BreakType` for a location, an `INVALID_REQUEST_ERROR` "Exceeded limit of 3 breaks per location."
        is returned.

        Parameters
        ----------
        break_type : BreakType

        idempotency_key : typing.Optional[str]
            A unique string value to ensure the idempotency of the operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBreakTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BreakType

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.create_break_type(
                break_type=BreakType(
                    break_name="break_name",
                    expected_duration="expected_duration",
                    is_paid=True,
                    location_id="location_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_break_type(
            break_type=break_type, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def get_break_type(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBreakTypeResponse:
        """
        Returns a single `BreakType` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `BreakType` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBreakTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.get_break_type(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_break_type(id, request_options=request_options)
        return _response.data

    async def update_break_type(
        self, id: str, *, break_type: BreakType, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateBreakTypeResponse:
        """
        Updates an existing `BreakType`.

        Parameters
        ----------
        id : str
             The UUID for the `BreakType` being updated.

        break_type : BreakType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateBreakTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BreakType

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.update_break_type(
                id="id",
                break_type=BreakType(
                    break_name="break_name",
                    expected_duration="expected_duration",
                    is_paid=True,
                    location_id="location_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_break_type(id, break_type=break_type, request_options=request_options)
        return _response.data

    async def delete_break_type(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteBreakTypeResponse:
        """
        Deletes an existing `BreakType`.

        A `BreakType` can be deleted even if it is referenced from a `Shift`.

        Parameters
        ----------
        id : str
            The UUID for the `BreakType` being deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteBreakTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.delete_break_type(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_break_type(id, request_options=request_options)
        return _response.data

    async def list_employee_wages(
        self,
        *,
        employee_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEmployeeWagesResponse:
        """
        Returns a paginated list of `EmployeeWage` instances for a business.

        Parameters
        ----------
        employee_id : typing.Optional[str]
            Filter the returned wages to only those that are associated with the specified employee.

        limit : typing.Optional[int]
            The maximum number of `EmployeeWage` results to return per page. The number can range between
            1 and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `EmployeeWage` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEmployeeWagesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.list_employee_wages()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_employee_wages(
            employee_id=employee_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def get_employee_wage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEmployeeWageResponse:
        """
        Returns a single `EmployeeWage` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `EmployeeWage` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEmployeeWageResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.get_employee_wage(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_employee_wage(id, request_options=request_options)
        return _response.data

    async def create_shift(
        self,
        *,
        shift: Shift,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateShiftResponse:
        """
        Creates a new `Shift`.

        A `Shift` represents a complete workday for a single employee.
        You must provide the following values in your request to this
        endpoint:

        - `location_id`
        - `employee_id`
        - `start_at`

        An attempt to create a new `Shift` can result in a `BAD_REQUEST` error when:
        - The `status` of the new `Shift` is `OPEN` and the employee has another
        shift with an `OPEN` status.
        - The `start_at` date is in the future.
        - The `start_at` or `end_at` date overlaps another shift for the same employee.
        - The `Break` instances are set in the request and a break `start_at`
        is before the `Shift.start_at`, a break `end_at` is after
        the `Shift.end_at`, or both.

        Parameters
        ----------
        shift : Shift

        idempotency_key : typing.Optional[str]
            A unique string value to ensure the idempotency of the operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateShiftResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Shift

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.create_shift(
                shift=Shift(
                    start_at="start_at",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_shift(
            shift=shift, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def search_shifts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[ShiftQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchShiftsResponse:
        """
        Returns a paginated list of `Shift` records for a business.
        The list to be returned can be filtered by:
        - Location IDs.
        - Employee IDs.
        - Shift status (`OPEN` and `CLOSED`).
        - Shift start.
        - Shift end.
        - Workday details.

        The list can be sorted by:
        - `start_at`.
        - `end_at`.
        - `created_at`.
        - `updated_at`.

        Parameters
        ----------
        cursor : typing.Optional[str]
            An opaque cursor for fetching the next page.

        limit : typing.Optional[int]
            The number of resources in a page (200 by default).

        query : typing.Optional[ShiftQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchShiftsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.search_shifts()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_shifts(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def get_shift(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetShiftResponse:
        """
        Returns a single `Shift` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `Shift` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetShiftResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.get_shift(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_shift(id, request_options=request_options)
        return _response.data

    async def update_shift(
        self, id: str, *, shift: Shift, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateShiftResponse:
        """
        Updates an existing `Shift`.

        When adding a `Break` to a `Shift`, any earlier `Break` instances in the `Shift` have
        the `end_at` property set to a valid RFC-3339 datetime string.

        When closing a `Shift`, all `Break` instances in the `Shift` must be complete with `end_at`
        set on each `Break`.

        Parameters
        ----------
        id : str
            The ID of the object being updated.

        shift : Shift

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateShiftResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Shift

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.update_shift(
                id="id",
                shift=Shift(
                    start_at="start_at",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_shift(id, shift=shift, request_options=request_options)
        return _response.data

    async def delete_shift(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteShiftResponse:
        """
        Deletes a `Shift`.

        Parameters
        ----------
        id : str
            The UUID for the `Shift` being deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteShiftResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.delete_shift(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_shift(id, request_options=request_options)
        return _response.data

    async def list_team_member_wages(
        self,
        *,
        team_member_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTeamMemberWagesResponse:
        """
        Returns a paginated list of `TeamMemberWage` instances for a business.

        Parameters
        ----------
        team_member_id : typing.Optional[str]
            Filter the returned wages to only those that are associated with the
            specified team member.

        limit : typing.Optional[int]
            The maximum number of `TeamMemberWage` results to return per page. The number can range between
            1 and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `EmployeeWage` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTeamMemberWagesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.list_team_member_wages()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_team_member_wages(
            team_member_id=team_member_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def get_team_member_wage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTeamMemberWageResponse:
        """
        Returns a single `TeamMemberWage` specified by `id `.

        Parameters
        ----------
        id : str
            The UUID for the `TeamMemberWage` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTeamMemberWageResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.get_team_member_wage(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_team_member_wage(id, request_options=request_options)
        return _response.data

    async def list_workweek_configs(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListWorkweekConfigsResponse:
        """
        Returns a list of `WorkweekConfig` instances for a business.

        Parameters
        ----------
        limit : typing.Optional[int]
            The maximum number of `WorkweekConfigs` results to return per page.

        cursor : typing.Optional[str]
            A pointer to the next page of `WorkweekConfig` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWorkweekConfigsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.list_workweek_configs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_workweek_configs(
            limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def update_workweek_config(
        self, id: str, *, workweek_config: WorkweekConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateWorkweekConfigResponse:
        """
        Updates a `WorkweekConfig`.

        Parameters
        ----------
        id : str
            The UUID for the `WorkweekConfig` object being updated.

        workweek_config : WorkweekConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWorkweekConfigResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WorkweekConfig

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.update_workweek_config(
                id="id",
                workweek_config=WorkweekConfig(
                    start_of_day_local_time="start_of_day_local_time",
                    start_of_week="start_of_week",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_workweek_config(
            id, workweek_config=workweek_config, request_options=request_options
        )
        return _response.data
