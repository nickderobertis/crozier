

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.deduction_type import DeductionType
from ..types.earnings_rate import EarningsRate
from ..types.employee import Employee
from ..types.employees import Employees
from ..types.leave_application import LeaveApplication
from ..types.leave_applications import LeaveApplications
from ..types.leave_type import LeaveType
from ..types.pay_items import PayItems
from ..types.pay_run import PayRun
from ..types.pay_runs import PayRuns
from ..types.payroll_calendar import PayrollCalendar
from ..types.payroll_calendars import PayrollCalendars
from ..types.payslip_lines import PayslipLines
from ..types.payslip_object import PayslipObject
from ..types.payslips import Payslips
from ..types.reimbursement_type import ReimbursementType
from ..types.settings_object import SettingsObject
from ..types.super_fund import SuperFund
from ..types.super_fund_products import SuperFundProducts
from ..types.super_funds import SuperFunds
from ..types.timesheet import Timesheet
from ..types.timesheet_object import TimesheetObject
from ..types.timesheets import Timesheets
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPayrollAuClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_employees(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Employees]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 employees will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Employees]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            "Employees",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Employees,
                    parse_obj_as(
                        type_=Employees,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_employee(
        self, *, request: typing.Sequence[Employee], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Employees]:
        """
        Parameters
        ----------
        request : typing.Sequence[Employee]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Employees]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            "Employees",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[Employee], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Employees,
                    parse_obj_as(
                        type_=Employees,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_employee(
        self, employee_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Employees]:
        """
        Parameters
        ----------
        employee_id : str
            Employee id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Employees]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Employees/{encode_path_param(employee_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Employees,
                    parse_obj_as(
                        type_=Employees,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_employee(
        self,
        employee_id: str,
        *,
        request: typing.Sequence[Employee],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Employees]:
        """
        Update properties on a single employee

        Parameters
        ----------
        employee_id : str
            Employee id for single object

        request : typing.Sequence[Employee]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Employees]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Employees/{encode_path_param(employee_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[Employee], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Employees,
                    parse_obj_as(
                        type_=Employees,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_leave_applications(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LeaveApplications]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LeaveApplications]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            "LeaveApplications",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LeaveApplications,
                    parse_obj_as(
                        type_=LeaveApplications,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_leave_application(
        self, *, request: typing.Sequence[LeaveApplication], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LeaveApplications]:
        """
        Parameters
        ----------
        request : typing.Sequence[LeaveApplication]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LeaveApplications]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            "LeaveApplications",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[LeaveApplication], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LeaveApplications,
                    parse_obj_as(
                        type_=LeaveApplications,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_leave_application(
        self, leave_application_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LeaveApplications]:
        """
        Parameters
        ----------
        leave_application_id : str
            Leave Application id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LeaveApplications]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            f"LeaveApplications/{encode_path_param(leave_application_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LeaveApplications,
                    parse_obj_as(
                        type_=LeaveApplications,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_leave_application(
        self,
        leave_application_id: str,
        *,
        request: typing.Sequence[LeaveApplication],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LeaveApplications]:
        """
        Parameters
        ----------
        leave_application_id : str
            Leave Application id for single object

        request : typing.Sequence[LeaveApplication]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LeaveApplications]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            f"LeaveApplications/{encode_path_param(leave_application_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[LeaveApplication], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LeaveApplications,
                    parse_obj_as(
                        type_=LeaveApplications,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_pay_items(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PayItems]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PayItems]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            "PayItems",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayItems,
                    parse_obj_as(
                        type_=PayItems,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_pay_item(
        self,
        *,
        deduction_types: typing.Optional[typing.Sequence[DeductionType]] = OMIT,
        earnings_rates: typing.Optional[typing.Sequence[EarningsRate]] = OMIT,
        leave_types: typing.Optional[typing.Sequence[LeaveType]] = OMIT,
        reimbursement_types: typing.Optional[typing.Sequence[ReimbursementType]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PayItems]:
        """
        Parameters
        ----------
        deduction_types : typing.Optional[typing.Sequence[DeductionType]]

        earnings_rates : typing.Optional[typing.Sequence[EarningsRate]]

        leave_types : typing.Optional[typing.Sequence[LeaveType]]

        reimbursement_types : typing.Optional[typing.Sequence[ReimbursementType]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PayItems]
            A successful request - currently returns empty array for JSON
        """
        _response = self._client_wrapper.httpx_client.request(
            "PayItems",
            method="POST",
            json={
                "DeductionTypes": convert_and_respect_annotation_metadata(
                    object_=deduction_types, annotation=typing.Sequence[DeductionType], direction="write"
                ),
                "EarningsRates": convert_and_respect_annotation_metadata(
                    object_=earnings_rates, annotation=typing.Sequence[EarningsRate], direction="write"
                ),
                "LeaveTypes": convert_and_respect_annotation_metadata(
                    object_=leave_types, annotation=typing.Sequence[LeaveType], direction="write"
                ),
                "ReimbursementTypes": convert_and_respect_annotation_metadata(
                    object_=reimbursement_types, annotation=typing.Sequence[ReimbursementType], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayItems,
                    parse_obj_as(
                        type_=PayItems,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_pay_runs(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PayRuns]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 PayRuns will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PayRuns]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            "PayRuns",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayRuns,
                    parse_obj_as(
                        type_=PayRuns,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_pay_run(
        self, *, request: typing.Sequence[PayRun], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PayRuns]:
        """
        Parameters
        ----------
        request : typing.Sequence[PayRun]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PayRuns]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            "PayRuns",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PayRun], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayRuns,
                    parse_obj_as(
                        type_=PayRuns,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_pay_run(
        self, pay_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PayRuns]:
        """
        Parameters
        ----------
        pay_run_id : str
            PayRun id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PayRuns]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            f"PayRuns/{encode_path_param(pay_run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayRuns,
                    parse_obj_as(
                        type_=PayRuns,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_pay_run(
        self,
        pay_run_id: str,
        *,
        request: typing.Sequence[PayRun],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PayRuns]:
        """
        Update properties on a single PayRun

        Parameters
        ----------
        pay_run_id : str
            PayRun id for single object

        request : typing.Sequence[PayRun]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PayRuns]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            f"PayRuns/{encode_path_param(pay_run_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PayRun], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayRuns,
                    parse_obj_as(
                        type_=PayRuns,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_payroll_calendars(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PayrollCalendars]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PayrollCalendars]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            "PayrollCalendars",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayrollCalendars,
                    parse_obj_as(
                        type_=PayrollCalendars,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_payroll_calendar(
        self, *, request: typing.Sequence[PayrollCalendar], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PayrollCalendars]:
        """
        Parameters
        ----------
        request : typing.Sequence[PayrollCalendar]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PayrollCalendars]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            "PayrollCalendars",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PayrollCalendar], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayrollCalendars,
                    parse_obj_as(
                        type_=PayrollCalendars,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_payroll_calendar(
        self, payroll_calendar_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PayrollCalendars]:
        """
        Parameters
        ----------
        payroll_calendar_id : str
            Payroll Calendar id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PayrollCalendars]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            f"PayrollCalendars/{encode_path_param(payroll_calendar_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayrollCalendars,
                    parse_obj_as(
                        type_=PayrollCalendars,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_payslip(
        self, payslip_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PayslipObject]:
        """
        Parameters
        ----------
        payslip_id : str
            Payslip id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PayslipObject]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Payslip/{encode_path_param(payslip_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayslipObject,
                    parse_obj_as(
                        type_=PayslipObject,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_payslip(
        self,
        payslip_id: str,
        *,
        request: typing.Sequence[PayslipLines],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Payslips]:
        """
        Update lines on a single payslips

        Parameters
        ----------
        payslip_id : str
            Payslip id for single object

        request : typing.Sequence[PayslipLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Payslips]
            A successful request - currently returns empty array for JSON
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Payslip/{encode_path_param(payslip_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PayslipLines], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Payslips,
                    parse_obj_as(
                        type_=Payslips,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[SettingsObject]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SettingsObject]
            payroll settings
        """
        _response = self._client_wrapper.httpx_client.request(
            "Settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SettingsObject,
                    parse_obj_as(
                        type_=SettingsObject,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_superfund_products(
        self,
        *,
        abn: typing.Optional[str] = None,
        usi: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuperFundProducts]:
        """
        Parameters
        ----------
        abn : typing.Optional[str]
            The ABN of the Regulated SuperFund

        usi : typing.Optional[str]
            The USI of the Regulated SuperFund

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuperFundProducts]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            "SuperfundProducts",
            method="GET",
            params={
                "ABN": abn,
                "USI": usi,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuperFundProducts,
                    parse_obj_as(
                        type_=SuperFundProducts,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_superfunds(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuperFunds]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuperFunds]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            "Superfunds",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuperFunds,
                    parse_obj_as(
                        type_=SuperFunds,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_superfund(
        self, *, request: typing.Sequence[SuperFund], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuperFunds]:
        """
        Parameters
        ----------
        request : typing.Sequence[SuperFund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuperFunds]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            "Superfunds",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[SuperFund], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuperFunds,
                    parse_obj_as(
                        type_=SuperFunds,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_superfund(
        self, super_fund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuperFunds]:
        """
        Parameters
        ----------
        super_fund_id : str
            Superfund id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuperFunds]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Superfunds/{encode_path_param(super_fund_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuperFunds,
                    parse_obj_as(
                        type_=SuperFunds,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_superfund(
        self,
        super_fund_id: str,
        *,
        request: typing.Sequence[SuperFund],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuperFunds]:
        """
        Update properties on a single Superfund

        Parameters
        ----------
        super_fund_id : str
            Superfund id for single object

        request : typing.Sequence[SuperFund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuperFunds]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Superfunds/{encode_path_param(super_fund_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[SuperFund], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuperFunds,
                    parse_obj_as(
                        type_=SuperFunds,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_timesheets(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Timesheets]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 timesheets will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Timesheets]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            "Timesheets",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Timesheets,
                    parse_obj_as(
                        type_=Timesheets,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_timesheet(
        self, *, request: typing.Sequence[Timesheet], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Timesheets]:
        """
        Parameters
        ----------
        request : typing.Sequence[Timesheet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Timesheets]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            "Timesheets",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[Timesheet], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Timesheets,
                    parse_obj_as(
                        type_=Timesheets,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_timesheet(
        self, timesheet_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TimesheetObject]:
        """
        Parameters
        ----------
        timesheet_id : str
            Timesheet id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TimesheetObject]
            search results matching criteria
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Timesheets/{encode_path_param(timesheet_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TimesheetObject,
                    parse_obj_as(
                        type_=TimesheetObject,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_timesheet(
        self,
        timesheet_id: str,
        *,
        request: typing.Sequence[Timesheet],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Timesheets]:
        """
        Update properties on a single timesheet

        Parameters
        ----------
        timesheet_id : str
            Timesheet id for single object

        request : typing.Sequence[Timesheet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Timesheets]
            A successful request
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Timesheets/{encode_path_param(timesheet_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[Timesheet], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Timesheets,
                    parse_obj_as(
                        type_=Timesheets,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPayrollAuClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_employees(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Employees]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 employees will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Employees]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Employees",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Employees,
                    parse_obj_as(
                        type_=Employees,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_employee(
        self, *, request: typing.Sequence[Employee], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Employees]:
        """
        Parameters
        ----------
        request : typing.Sequence[Employee]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Employees]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Employees",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[Employee], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Employees,
                    parse_obj_as(
                        type_=Employees,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_employee(
        self, employee_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Employees]:
        """
        Parameters
        ----------
        employee_id : str
            Employee id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Employees]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Employees/{encode_path_param(employee_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Employees,
                    parse_obj_as(
                        type_=Employees,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_employee(
        self,
        employee_id: str,
        *,
        request: typing.Sequence[Employee],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Employees]:
        """
        Update properties on a single employee

        Parameters
        ----------
        employee_id : str
            Employee id for single object

        request : typing.Sequence[Employee]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Employees]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Employees/{encode_path_param(employee_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[Employee], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Employees,
                    parse_obj_as(
                        type_=Employees,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_leave_applications(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LeaveApplications]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LeaveApplications]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            "LeaveApplications",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LeaveApplications,
                    parse_obj_as(
                        type_=LeaveApplications,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_leave_application(
        self, *, request: typing.Sequence[LeaveApplication], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LeaveApplications]:
        """
        Parameters
        ----------
        request : typing.Sequence[LeaveApplication]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LeaveApplications]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            "LeaveApplications",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[LeaveApplication], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LeaveApplications,
                    parse_obj_as(
                        type_=LeaveApplications,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_leave_application(
        self, leave_application_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LeaveApplications]:
        """
        Parameters
        ----------
        leave_application_id : str
            Leave Application id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LeaveApplications]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"LeaveApplications/{encode_path_param(leave_application_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LeaveApplications,
                    parse_obj_as(
                        type_=LeaveApplications,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_leave_application(
        self,
        leave_application_id: str,
        *,
        request: typing.Sequence[LeaveApplication],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LeaveApplications]:
        """
        Parameters
        ----------
        leave_application_id : str
            Leave Application id for single object

        request : typing.Sequence[LeaveApplication]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LeaveApplications]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"LeaveApplications/{encode_path_param(leave_application_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[LeaveApplication], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LeaveApplications,
                    parse_obj_as(
                        type_=LeaveApplications,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_pay_items(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PayItems]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PayItems]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PayItems",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayItems,
                    parse_obj_as(
                        type_=PayItems,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_pay_item(
        self,
        *,
        deduction_types: typing.Optional[typing.Sequence[DeductionType]] = OMIT,
        earnings_rates: typing.Optional[typing.Sequence[EarningsRate]] = OMIT,
        leave_types: typing.Optional[typing.Sequence[LeaveType]] = OMIT,
        reimbursement_types: typing.Optional[typing.Sequence[ReimbursementType]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PayItems]:
        """
        Parameters
        ----------
        deduction_types : typing.Optional[typing.Sequence[DeductionType]]

        earnings_rates : typing.Optional[typing.Sequence[EarningsRate]]

        leave_types : typing.Optional[typing.Sequence[LeaveType]]

        reimbursement_types : typing.Optional[typing.Sequence[ReimbursementType]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PayItems]
            A successful request - currently returns empty array for JSON
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PayItems",
            method="POST",
            json={
                "DeductionTypes": convert_and_respect_annotation_metadata(
                    object_=deduction_types, annotation=typing.Sequence[DeductionType], direction="write"
                ),
                "EarningsRates": convert_and_respect_annotation_metadata(
                    object_=earnings_rates, annotation=typing.Sequence[EarningsRate], direction="write"
                ),
                "LeaveTypes": convert_and_respect_annotation_metadata(
                    object_=leave_types, annotation=typing.Sequence[LeaveType], direction="write"
                ),
                "ReimbursementTypes": convert_and_respect_annotation_metadata(
                    object_=reimbursement_types, annotation=typing.Sequence[ReimbursementType], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayItems,
                    parse_obj_as(
                        type_=PayItems,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_pay_runs(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PayRuns]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 PayRuns will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PayRuns]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PayRuns",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayRuns,
                    parse_obj_as(
                        type_=PayRuns,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_pay_run(
        self, *, request: typing.Sequence[PayRun], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PayRuns]:
        """
        Parameters
        ----------
        request : typing.Sequence[PayRun]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PayRuns]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PayRuns",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PayRun], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayRuns,
                    parse_obj_as(
                        type_=PayRuns,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_pay_run(
        self, pay_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PayRuns]:
        """
        Parameters
        ----------
        pay_run_id : str
            PayRun id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PayRuns]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"PayRuns/{encode_path_param(pay_run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayRuns,
                    parse_obj_as(
                        type_=PayRuns,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_pay_run(
        self,
        pay_run_id: str,
        *,
        request: typing.Sequence[PayRun],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PayRuns]:
        """
        Update properties on a single PayRun

        Parameters
        ----------
        pay_run_id : str
            PayRun id for single object

        request : typing.Sequence[PayRun]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PayRuns]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"PayRuns/{encode_path_param(pay_run_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PayRun], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayRuns,
                    parse_obj_as(
                        type_=PayRuns,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_payroll_calendars(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PayrollCalendars]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PayrollCalendars]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PayrollCalendars",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayrollCalendars,
                    parse_obj_as(
                        type_=PayrollCalendars,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_payroll_calendar(
        self, *, request: typing.Sequence[PayrollCalendar], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PayrollCalendars]:
        """
        Parameters
        ----------
        request : typing.Sequence[PayrollCalendar]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PayrollCalendars]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PayrollCalendars",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PayrollCalendar], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayrollCalendars,
                    parse_obj_as(
                        type_=PayrollCalendars,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_payroll_calendar(
        self, payroll_calendar_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PayrollCalendars]:
        """
        Parameters
        ----------
        payroll_calendar_id : str
            Payroll Calendar id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PayrollCalendars]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"PayrollCalendars/{encode_path_param(payroll_calendar_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayrollCalendars,
                    parse_obj_as(
                        type_=PayrollCalendars,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_payslip(
        self, payslip_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PayslipObject]:
        """
        Parameters
        ----------
        payslip_id : str
            Payslip id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PayslipObject]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Payslip/{encode_path_param(payslip_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PayslipObject,
                    parse_obj_as(
                        type_=PayslipObject,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_payslip(
        self,
        payslip_id: str,
        *,
        request: typing.Sequence[PayslipLines],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Payslips]:
        """
        Update lines on a single payslips

        Parameters
        ----------
        payslip_id : str
            Payslip id for single object

        request : typing.Sequence[PayslipLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Payslips]
            A successful request - currently returns empty array for JSON
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Payslip/{encode_path_param(payslip_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PayslipLines], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Payslips,
                    parse_obj_as(
                        type_=Payslips,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SettingsObject]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SettingsObject]
            payroll settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SettingsObject,
                    parse_obj_as(
                        type_=SettingsObject,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_superfund_products(
        self,
        *,
        abn: typing.Optional[str] = None,
        usi: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuperFundProducts]:
        """
        Parameters
        ----------
        abn : typing.Optional[str]
            The ABN of the Regulated SuperFund

        usi : typing.Optional[str]
            The USI of the Regulated SuperFund

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuperFundProducts]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            "SuperfundProducts",
            method="GET",
            params={
                "ABN": abn,
                "USI": usi,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuperFundProducts,
                    parse_obj_as(
                        type_=SuperFundProducts,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_superfunds(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuperFunds]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuperFunds]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Superfunds",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuperFunds,
                    parse_obj_as(
                        type_=SuperFunds,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_superfund(
        self, *, request: typing.Sequence[SuperFund], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuperFunds]:
        """
        Parameters
        ----------
        request : typing.Sequence[SuperFund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuperFunds]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Superfunds",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[SuperFund], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuperFunds,
                    parse_obj_as(
                        type_=SuperFunds,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_superfund(
        self, super_fund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuperFunds]:
        """
        Parameters
        ----------
        super_fund_id : str
            Superfund id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuperFunds]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Superfunds/{encode_path_param(super_fund_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuperFunds,
                    parse_obj_as(
                        type_=SuperFunds,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_superfund(
        self,
        super_fund_id: str,
        *,
        request: typing.Sequence[SuperFund],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuperFunds]:
        """
        Update properties on a single Superfund

        Parameters
        ----------
        super_fund_id : str
            Superfund id for single object

        request : typing.Sequence[SuperFund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuperFunds]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Superfunds/{encode_path_param(super_fund_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[SuperFund], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuperFunds,
                    parse_obj_as(
                        type_=SuperFunds,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_timesheets(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Timesheets]:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 timesheets will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Timesheets]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Timesheets",
            method="GET",
            params={
                "where": where,
                "order": order,
                "page": page,
            },
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Timesheets,
                    parse_obj_as(
                        type_=Timesheets,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_timesheet(
        self, *, request: typing.Sequence[Timesheet], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Timesheets]:
        """
        Parameters
        ----------
        request : typing.Sequence[Timesheet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Timesheets]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Timesheets",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[Timesheet], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Timesheets,
                    parse_obj_as(
                        type_=Timesheets,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_timesheet(
        self, timesheet_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TimesheetObject]:
        """
        Parameters
        ----------
        timesheet_id : str
            Timesheet id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TimesheetObject]
            search results matching criteria
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Timesheets/{encode_path_param(timesheet_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TimesheetObject,
                    parse_obj_as(
                        type_=TimesheetObject,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_timesheet(
        self,
        timesheet_id: str,
        *,
        request: typing.Sequence[Timesheet],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Timesheets]:
        """
        Update properties on a single timesheet

        Parameters
        ----------
        timesheet_id : str
            Timesheet id for single object

        request : typing.Sequence[Timesheet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Timesheets]
            A successful request
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Timesheets/{encode_path_param(timesheet_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[Timesheet], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Timesheets,
                    parse_obj_as(
                        type_=Timesheets,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
