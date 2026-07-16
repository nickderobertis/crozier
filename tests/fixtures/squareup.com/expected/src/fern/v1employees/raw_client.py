

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.v1employee import V1Employee
from ..types.v1employee_role import V1EmployeeRole
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawV1EmployeesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_employees(
        self,
        *,
        order: typing.Optional[str] = None,
        begin_updated_at: typing.Optional[str] = None,
        end_updated_at: typing.Optional[str] = None,
        begin_created_at: typing.Optional[str] = None,
        end_created_at: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Employee]]:
        """
        Provides summary information for all of a business's employees.

        Parameters
        ----------
        order : typing.Optional[str]
            The order in which employees are listed in the response, based on their created_at field.      Default value: ASC

        begin_updated_at : typing.Optional[str]
            If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format

        end_updated_at : typing.Optional[str]
            If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format.

        begin_created_at : typing.Optional[str]
            If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format.

        end_created_at : typing.Optional[str]
            If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format.

        status : typing.Optional[str]
            If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE).

        external_id : typing.Optional[str]
            If provided, the endpoint returns only employee entities with the specified external_id.

        limit : typing.Optional[int]
            The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Employee]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/me/employees",
            method="GET",
            params={
                "order": order,
                "begin_updated_at": begin_updated_at,
                "end_updated_at": end_updated_at,
                "begin_created_at": begin_created_at,
                "end_created_at": end_created_at,
                "status": status,
                "external_id": external_id,
                "limit": limit,
                "batch_token": batch_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Employee],
                    parse_obj_as(
                        type_=typing.List[V1Employee],
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

    def create_employee(
        self,
        *,
        first_name: str,
        last_name: str,
        authorized_location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        external_id: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        role_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        status: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Employee]:
        """
         Use the CreateEmployee endpoint to add an employee to a Square
        account. Employees created with the Connect API have an initial status
        of `INACTIVE`. Inactive employees cannot sign in to Square Point of Sale
        until they are activated from the Square Dashboard. Employee status
        cannot be changed with the Connect API.

        Employee entities cannot be deleted. To disable employee profiles,
        set the employee's status to <code>INACTIVE</code>

        Parameters
        ----------
        first_name : str
            The employee's first name.

        last_name : str
            The employee's last name.

        authorized_location_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the locations the employee is allowed to clock in at.

        created_at : typing.Optional[str]
            The time when the employee entity was created, in ISO 8601 format.

        email : typing.Optional[str]
            The employee's email address.

        external_id : typing.Optional[str]
            An ID the merchant can set to associate the employee with an entity in another system.

        id : typing.Optional[str]
            The employee's unique ID.

        role_ids : typing.Optional[typing.Sequence[str]]
            The ids of the employee's associated roles. Currently, you can specify only one or zero roles per employee.

        status : typing.Optional[str]
            Whether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard.

        updated_at : typing.Optional[str]
            The time when the employee entity was most recently updated, in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Employee]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/me/employees",
            method="POST",
            json={
                "authorized_location_ids": authorized_location_ids,
                "created_at": created_at,
                "email": email,
                "external_id": external_id,
                "first_name": first_name,
                "id": id,
                "last_name": last_name,
                "role_ids": role_ids,
                "status": status,
                "updated_at": updated_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Employee,
                    parse_obj_as(
                        type_=V1Employee,
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

    def retrieve_employee(
        self, employee_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Employee]:
        """
        Provides the details for a single employee.

        Parameters
        ----------
        employee_id : str
            The employee's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Employee]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/me/employees/{encode_path_param(employee_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Employee,
                    parse_obj_as(
                        type_=V1Employee,
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
        first_name: str,
        last_name: str,
        authorized_location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        external_id: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        role_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        status: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Employee]:
        """


        Parameters
        ----------
        employee_id : str
            The ID of the role to modify.

        first_name : str
            The employee's first name.

        last_name : str
            The employee's last name.

        authorized_location_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the locations the employee is allowed to clock in at.

        created_at : typing.Optional[str]
            The time when the employee entity was created, in ISO 8601 format.

        email : typing.Optional[str]
            The employee's email address.

        external_id : typing.Optional[str]
            An ID the merchant can set to associate the employee with an entity in another system.

        id : typing.Optional[str]
            The employee's unique ID.

        role_ids : typing.Optional[typing.Sequence[str]]
            The ids of the employee's associated roles. Currently, you can specify only one or zero roles per employee.

        status : typing.Optional[str]
            Whether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard.

        updated_at : typing.Optional[str]
            The time when the employee entity was most recently updated, in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Employee]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/me/employees/{encode_path_param(employee_id)}",
            method="PUT",
            json={
                "authorized_location_ids": authorized_location_ids,
                "created_at": created_at,
                "email": email,
                "external_id": external_id,
                "first_name": first_name,
                "id": id,
                "last_name": last_name,
                "role_ids": role_ids,
                "status": status,
                "updated_at": updated_at,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Employee,
                    parse_obj_as(
                        type_=V1Employee,
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

    def list_employee_roles(
        self,
        *,
        order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1EmployeeRole]]:
        """
        Provides summary information for all of a business's employee roles.

        Parameters
        ----------
        order : typing.Optional[str]
            The order in which employees are listed in the response, based on their created_at field.Default value: ASC

        limit : typing.Optional[int]
            The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1EmployeeRole]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/me/roles",
            method="GET",
            params={
                "order": order,
                "limit": limit,
                "batch_token": batch_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1EmployeeRole],
                    parse_obj_as(
                        type_=typing.List[V1EmployeeRole],
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

    def create_employee_role(
        self,
        *,
        name: str,
        permissions: typing.Sequence[str],
        created_at: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_owner: typing.Optional[bool] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1EmployeeRole]:
        """
        Creates an employee role you can then assign to employees.

        Square accounts can include any number of roles that can be assigned to
        employees. These roles define the actions and permissions granted to an
        employee with that role. For example, an employee with a "Shift Manager"
        role might be able to issue refunds in Square Point of Sale, whereas an
        employee with a "Clerk" role might not.

        Roles are assigned with the [V1UpdateEmployee](https://developer.squareup.com/reference/square_2021-08-18/v1-employees-api/update-employee-role)
        endpoint. An employee can have only one role at a time.

        If an employee has no role, they have none of the permissions associated
        with roles. All employees can accept payments with Square Point of Sale.

        Parameters
        ----------
        name : str
            The role's merchant-defined name.

        permissions : typing.Sequence[str]
            The role's permissions.

        created_at : typing.Optional[str]
            The time when the employee entity was created, in ISO 8601 format. Is set by Square when the Role is created.

        id : typing.Optional[str]
            The role's unique ID, Can only be set by Square.

        is_owner : typing.Optional[bool]
            If true, employees with this role have all permissions, regardless of the values indicated in permissions.

        updated_at : typing.Optional[str]
            The time when the employee entity was most recently updated, in ISO 8601 format. Is set by Square when the Role updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1EmployeeRole]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/me/roles",
            method="POST",
            json={
                "created_at": created_at,
                "id": id,
                "is_owner": is_owner,
                "name": name,
                "permissions": permissions,
                "updated_at": updated_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1EmployeeRole,
                    parse_obj_as(
                        type_=V1EmployeeRole,
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

    def retrieve_employee_role(
        self, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1EmployeeRole]:
        """
        Provides the details for a single employee role.

        Parameters
        ----------
        role_id : str
            The role's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1EmployeeRole]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/me/roles/{encode_path_param(role_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1EmployeeRole,
                    parse_obj_as(
                        type_=V1EmployeeRole,
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

    def update_employee_role(
        self,
        role_id: str,
        *,
        name: str,
        permissions: typing.Sequence[str],
        created_at: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_owner: typing.Optional[bool] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1EmployeeRole]:
        """
        Modifies the details of an employee role.

        Parameters
        ----------
        role_id : str
            The ID of the role to modify.

        name : str
            The role's merchant-defined name.

        permissions : typing.Sequence[str]
            The role's permissions.

        created_at : typing.Optional[str]
            The time when the employee entity was created, in ISO 8601 format. Is set by Square when the Role is created.

        id : typing.Optional[str]
            The role's unique ID, Can only be set by Square.

        is_owner : typing.Optional[bool]
            If true, employees with this role have all permissions, regardless of the values indicated in permissions.

        updated_at : typing.Optional[str]
            The time when the employee entity was most recently updated, in ISO 8601 format. Is set by Square when the Role updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1EmployeeRole]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/me/roles/{encode_path_param(role_id)}",
            method="PUT",
            json={
                "created_at": created_at,
                "id": id,
                "is_owner": is_owner,
                "name": name,
                "permissions": permissions,
                "updated_at": updated_at,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1EmployeeRole,
                    parse_obj_as(
                        type_=V1EmployeeRole,
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


class AsyncRawV1EmployeesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_employees(
        self,
        *,
        order: typing.Optional[str] = None,
        begin_updated_at: typing.Optional[str] = None,
        end_updated_at: typing.Optional[str] = None,
        begin_created_at: typing.Optional[str] = None,
        end_created_at: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Employee]]:
        """
        Provides summary information for all of a business's employees.

        Parameters
        ----------
        order : typing.Optional[str]
            The order in which employees are listed in the response, based on their created_at field.      Default value: ASC

        begin_updated_at : typing.Optional[str]
            If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format

        end_updated_at : typing.Optional[str]
            If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format.

        begin_created_at : typing.Optional[str]
            If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format.

        end_created_at : typing.Optional[str]
            If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format.

        status : typing.Optional[str]
            If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE).

        external_id : typing.Optional[str]
            If provided, the endpoint returns only employee entities with the specified external_id.

        limit : typing.Optional[int]
            The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Employee]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/me/employees",
            method="GET",
            params={
                "order": order,
                "begin_updated_at": begin_updated_at,
                "end_updated_at": end_updated_at,
                "begin_created_at": begin_created_at,
                "end_created_at": end_created_at,
                "status": status,
                "external_id": external_id,
                "limit": limit,
                "batch_token": batch_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Employee],
                    parse_obj_as(
                        type_=typing.List[V1Employee],
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

    async def create_employee(
        self,
        *,
        first_name: str,
        last_name: str,
        authorized_location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        external_id: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        role_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        status: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Employee]:
        """
         Use the CreateEmployee endpoint to add an employee to a Square
        account. Employees created with the Connect API have an initial status
        of `INACTIVE`. Inactive employees cannot sign in to Square Point of Sale
        until they are activated from the Square Dashboard. Employee status
        cannot be changed with the Connect API.

        Employee entities cannot be deleted. To disable employee profiles,
        set the employee's status to <code>INACTIVE</code>

        Parameters
        ----------
        first_name : str
            The employee's first name.

        last_name : str
            The employee's last name.

        authorized_location_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the locations the employee is allowed to clock in at.

        created_at : typing.Optional[str]
            The time when the employee entity was created, in ISO 8601 format.

        email : typing.Optional[str]
            The employee's email address.

        external_id : typing.Optional[str]
            An ID the merchant can set to associate the employee with an entity in another system.

        id : typing.Optional[str]
            The employee's unique ID.

        role_ids : typing.Optional[typing.Sequence[str]]
            The ids of the employee's associated roles. Currently, you can specify only one or zero roles per employee.

        status : typing.Optional[str]
            Whether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard.

        updated_at : typing.Optional[str]
            The time when the employee entity was most recently updated, in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Employee]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/me/employees",
            method="POST",
            json={
                "authorized_location_ids": authorized_location_ids,
                "created_at": created_at,
                "email": email,
                "external_id": external_id,
                "first_name": first_name,
                "id": id,
                "last_name": last_name,
                "role_ids": role_ids,
                "status": status,
                "updated_at": updated_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Employee,
                    parse_obj_as(
                        type_=V1Employee,
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

    async def retrieve_employee(
        self, employee_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Employee]:
        """
        Provides the details for a single employee.

        Parameters
        ----------
        employee_id : str
            The employee's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Employee]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/me/employees/{encode_path_param(employee_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Employee,
                    parse_obj_as(
                        type_=V1Employee,
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
        first_name: str,
        last_name: str,
        authorized_location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        external_id: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        role_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        status: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Employee]:
        """


        Parameters
        ----------
        employee_id : str
            The ID of the role to modify.

        first_name : str
            The employee's first name.

        last_name : str
            The employee's last name.

        authorized_location_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the locations the employee is allowed to clock in at.

        created_at : typing.Optional[str]
            The time when the employee entity was created, in ISO 8601 format.

        email : typing.Optional[str]
            The employee's email address.

        external_id : typing.Optional[str]
            An ID the merchant can set to associate the employee with an entity in another system.

        id : typing.Optional[str]
            The employee's unique ID.

        role_ids : typing.Optional[typing.Sequence[str]]
            The ids of the employee's associated roles. Currently, you can specify only one or zero roles per employee.

        status : typing.Optional[str]
            Whether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard.

        updated_at : typing.Optional[str]
            The time when the employee entity was most recently updated, in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Employee]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/me/employees/{encode_path_param(employee_id)}",
            method="PUT",
            json={
                "authorized_location_ids": authorized_location_ids,
                "created_at": created_at,
                "email": email,
                "external_id": external_id,
                "first_name": first_name,
                "id": id,
                "last_name": last_name,
                "role_ids": role_ids,
                "status": status,
                "updated_at": updated_at,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Employee,
                    parse_obj_as(
                        type_=V1Employee,
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

    async def list_employee_roles(
        self,
        *,
        order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1EmployeeRole]]:
        """
        Provides summary information for all of a business's employee roles.

        Parameters
        ----------
        order : typing.Optional[str]
            The order in which employees are listed in the response, based on their created_at field.Default value: ASC

        limit : typing.Optional[int]
            The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1EmployeeRole]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/me/roles",
            method="GET",
            params={
                "order": order,
                "limit": limit,
                "batch_token": batch_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1EmployeeRole],
                    parse_obj_as(
                        type_=typing.List[V1EmployeeRole],
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

    async def create_employee_role(
        self,
        *,
        name: str,
        permissions: typing.Sequence[str],
        created_at: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_owner: typing.Optional[bool] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1EmployeeRole]:
        """
        Creates an employee role you can then assign to employees.

        Square accounts can include any number of roles that can be assigned to
        employees. These roles define the actions and permissions granted to an
        employee with that role. For example, an employee with a "Shift Manager"
        role might be able to issue refunds in Square Point of Sale, whereas an
        employee with a "Clerk" role might not.

        Roles are assigned with the [V1UpdateEmployee](https://developer.squareup.com/reference/square_2021-08-18/v1-employees-api/update-employee-role)
        endpoint. An employee can have only one role at a time.

        If an employee has no role, they have none of the permissions associated
        with roles. All employees can accept payments with Square Point of Sale.

        Parameters
        ----------
        name : str
            The role's merchant-defined name.

        permissions : typing.Sequence[str]
            The role's permissions.

        created_at : typing.Optional[str]
            The time when the employee entity was created, in ISO 8601 format. Is set by Square when the Role is created.

        id : typing.Optional[str]
            The role's unique ID, Can only be set by Square.

        is_owner : typing.Optional[bool]
            If true, employees with this role have all permissions, regardless of the values indicated in permissions.

        updated_at : typing.Optional[str]
            The time when the employee entity was most recently updated, in ISO 8601 format. Is set by Square when the Role updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1EmployeeRole]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/me/roles",
            method="POST",
            json={
                "created_at": created_at,
                "id": id,
                "is_owner": is_owner,
                "name": name,
                "permissions": permissions,
                "updated_at": updated_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1EmployeeRole,
                    parse_obj_as(
                        type_=V1EmployeeRole,
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

    async def retrieve_employee_role(
        self, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1EmployeeRole]:
        """
        Provides the details for a single employee role.

        Parameters
        ----------
        role_id : str
            The role's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1EmployeeRole]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/me/roles/{encode_path_param(role_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1EmployeeRole,
                    parse_obj_as(
                        type_=V1EmployeeRole,
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

    async def update_employee_role(
        self,
        role_id: str,
        *,
        name: str,
        permissions: typing.Sequence[str],
        created_at: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_owner: typing.Optional[bool] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1EmployeeRole]:
        """
        Modifies the details of an employee role.

        Parameters
        ----------
        role_id : str
            The ID of the role to modify.

        name : str
            The role's merchant-defined name.

        permissions : typing.Sequence[str]
            The role's permissions.

        created_at : typing.Optional[str]
            The time when the employee entity was created, in ISO 8601 format. Is set by Square when the Role is created.

        id : typing.Optional[str]
            The role's unique ID, Can only be set by Square.

        is_owner : typing.Optional[bool]
            If true, employees with this role have all permissions, regardless of the values indicated in permissions.

        updated_at : typing.Optional[str]
            The time when the employee entity was most recently updated, in ISO 8601 format. Is set by Square when the Role updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1EmployeeRole]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/me/roles/{encode_path_param(role_id)}",
            method="PUT",
            json={
                "created_at": created_at,
                "id": id,
                "is_owner": is_owner,
                "name": name,
                "permissions": permissions,
                "updated_at": updated_at,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1EmployeeRole,
                    parse_obj_as(
                        type_=V1EmployeeRole,
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
