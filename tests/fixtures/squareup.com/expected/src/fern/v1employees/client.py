

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1employee import V1Employee
from ..types.v1employee_role import V1EmployeeRole
from .raw_client import AsyncRawV1EmployeesClient, RawV1EmployeesClient


OMIT = typing.cast(typing.Any, ...)


class V1EmployeesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV1EmployeesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV1EmployeesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV1EmployeesClient
        """
        return self._raw_client

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
    ) -> typing.List[V1Employee]:
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
        typing.List[V1Employee]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1employees.list_employees()
        """
        _response = self._raw_client.list_employees(
            order=order,
            begin_updated_at=begin_updated_at,
            end_updated_at=end_updated_at,
            begin_created_at=begin_created_at,
            end_created_at=end_created_at,
            status=status,
            external_id=external_id,
            limit=limit,
            batch_token=batch_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> V1Employee:
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
        V1Employee
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1employees.create_employee(
            first_name="first_name",
            last_name="last_name",
        )
        """
        _response = self._raw_client.create_employee(
            first_name=first_name,
            last_name=last_name,
            authorized_location_ids=authorized_location_ids,
            created_at=created_at,
            email=email,
            external_id=external_id,
            id=id,
            role_ids=role_ids,
            status=status,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    def retrieve_employee(
        self, employee_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Employee:
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
        V1Employee
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1employees.retrieve_employee(
            employee_id="employee_id",
        )
        """
        _response = self._raw_client.retrieve_employee(employee_id, request_options=request_options)
        return _response.data

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
    ) -> V1Employee:
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
        V1Employee
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1employees.update_employee(
            employee_id="employee_id",
            first_name="first_name",
            last_name="last_name",
        )
        """
        _response = self._raw_client.update_employee(
            employee_id,
            first_name=first_name,
            last_name=last_name,
            authorized_location_ids=authorized_location_ids,
            created_at=created_at,
            email=email,
            external_id=external_id,
            id=id,
            role_ids=role_ids,
            status=status,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    def list_employee_roles(
        self,
        *,
        order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1EmployeeRole]:
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
        typing.List[V1EmployeeRole]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1employees.list_employee_roles()
        """
        _response = self._raw_client.list_employee_roles(
            order=order, limit=limit, batch_token=batch_token, request_options=request_options
        )
        return _response.data

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
    ) -> V1EmployeeRole:
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
        V1EmployeeRole
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1employees.create_employee_role(
            name="name",
            permissions=["permissions"],
        )
        """
        _response = self._raw_client.create_employee_role(
            name=name,
            permissions=permissions,
            created_at=created_at,
            id=id,
            is_owner=is_owner,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    def retrieve_employee_role(
        self, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1EmployeeRole:
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
        V1EmployeeRole
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1employees.retrieve_employee_role(
            role_id="role_id",
        )
        """
        _response = self._raw_client.retrieve_employee_role(role_id, request_options=request_options)
        return _response.data

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
    ) -> V1EmployeeRole:
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
        V1EmployeeRole
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1employees.update_employee_role(
            role_id="role_id",
            name="name",
            permissions=["permissions"],
        )
        """
        _response = self._raw_client.update_employee_role(
            role_id,
            name=name,
            permissions=permissions,
            created_at=created_at,
            id=id,
            is_owner=is_owner,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data


class AsyncV1EmployeesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV1EmployeesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV1EmployeesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV1EmployeesClient
        """
        return self._raw_client

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
    ) -> typing.List[V1Employee]:
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
        typing.List[V1Employee]
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
            await client.v1employees.list_employees()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_employees(
            order=order,
            begin_updated_at=begin_updated_at,
            end_updated_at=end_updated_at,
            begin_created_at=begin_created_at,
            end_created_at=end_created_at,
            status=status,
            external_id=external_id,
            limit=limit,
            batch_token=batch_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> V1Employee:
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
        V1Employee
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
            await client.v1employees.create_employee(
                first_name="first_name",
                last_name="last_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_employee(
            first_name=first_name,
            last_name=last_name,
            authorized_location_ids=authorized_location_ids,
            created_at=created_at,
            email=email,
            external_id=external_id,
            id=id,
            role_ids=role_ids,
            status=status,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_employee(
        self, employee_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Employee:
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
        V1Employee
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
            await client.v1employees.retrieve_employee(
                employee_id="employee_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_employee(employee_id, request_options=request_options)
        return _response.data

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
    ) -> V1Employee:
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
        V1Employee
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
            await client.v1employees.update_employee(
                employee_id="employee_id",
                first_name="first_name",
                last_name="last_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_employee(
            employee_id,
            first_name=first_name,
            last_name=last_name,
            authorized_location_ids=authorized_location_ids,
            created_at=created_at,
            email=email,
            external_id=external_id,
            id=id,
            role_ids=role_ids,
            status=status,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    async def list_employee_roles(
        self,
        *,
        order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1EmployeeRole]:
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
        typing.List[V1EmployeeRole]
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
            await client.v1employees.list_employee_roles()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_employee_roles(
            order=order, limit=limit, batch_token=batch_token, request_options=request_options
        )
        return _response.data

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
    ) -> V1EmployeeRole:
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
        V1EmployeeRole
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
            await client.v1employees.create_employee_role(
                name="name",
                permissions=["permissions"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_employee_role(
            name=name,
            permissions=permissions,
            created_at=created_at,
            id=id,
            is_owner=is_owner,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_employee_role(
        self, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1EmployeeRole:
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
        V1EmployeeRole
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
            await client.v1employees.retrieve_employee_role(
                role_id="role_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_employee_role(role_id, request_options=request_options)
        return _response.data

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
    ) -> V1EmployeeRole:
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
        V1EmployeeRole
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
            await client.v1employees.update_employee_role(
                role_id="role_id",
                name="name",
                permissions=["permissions"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_employee_role(
            role_id,
            name=name,
            permissions=permissions,
            created_at=created_at,
            id=id,
            is_owner=is_owner,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data
