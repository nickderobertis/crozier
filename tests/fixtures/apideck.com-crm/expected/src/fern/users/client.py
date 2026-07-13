

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.create_user_response import CreateUserResponse
from ..types.delete_user_response import DeleteUserResponse
from ..types.email import Email
from ..types.first_name import FirstName
from ..types.get_user_response import GetUserResponse
from ..types.get_users_response import GetUsersResponse
from ..types.last_name import LastName
from ..types.phone_number import PhoneNumber
from ..types.update_user_response import UpdateUserResponse
from .raw_client import AsyncRawUsersClient, RawUsersClient


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUsersResponse:
        """
        List users

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUsersResponse
            Users

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.users.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    def add(
        self,
        *,
        emails: typing.Sequence[Email],
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        division: typing.Optional[str] = OMIT,
        employee_number: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateUserResponse:
        """
        Create user

        Parameters
        ----------
        emails : typing.Sequence[Email]

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_name : typing.Optional[str]
            The name of the company.

        created_at : typing.Optional[str]

        department : typing.Optional[str]
            The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.

        description : typing.Optional[str]
            A description of the object.

        division : typing.Optional[str]
            The division the person is currently in. Usually a collection of departments or teams or regions.

        employee_number : typing.Optional[str]
            An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[LastName]

        parent_id : typing.Optional[str]

        password : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[str]

        title : typing.Optional[str]
            The job title of the person.

        updated_at : typing.Optional[str]

        username : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUserResponse
            User created

        Examples
        --------
        from fern import Email, FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.users.add(
            emails=[
                Email(
                    email="elon@musk.com",
                )
            ],
        )
        """
        _response = self._raw_client.add(
            emails=emails,
            raw=raw,
            addresses=addresses,
            company_name=company_name,
            created_at=created_at,
            department=department,
            description=description,
            division=division,
            employee_number=employee_number,
            first_name=first_name,
            id=id,
            image=image,
            language=language,
            last_name=last_name,
            parent_id=parent_id,
            password=password,
            phone_numbers=phone_numbers,
            status=status,
            title=title,
            updated_at=updated_at,
            username=username,
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
    ) -> GetUserResponse:
        """
        Get user

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
        GetUserResponse
            User

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.users.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteUserResponse:
        """
        Delete user

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
        DeleteUserResponse
            User deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.users.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        emails: typing.Sequence[Email],
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        division: typing.Optional[str] = OMIT,
        employee_number: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateUserResponse:
        """
        Update user

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        emails : typing.Sequence[Email]

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_name : typing.Optional[str]
            The name of the company.

        created_at : typing.Optional[str]

        department : typing.Optional[str]
            The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.

        description : typing.Optional[str]
            A description of the object.

        division : typing.Optional[str]
            The division the person is currently in. Usually a collection of departments or teams or regions.

        employee_number : typing.Optional[str]
            An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[LastName]

        parent_id : typing.Optional[str]

        password : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[str]

        title : typing.Optional[str]
            The job title of the person.

        updated_at : typing.Optional[str]

        username : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateUserResponse
            User updated

        Examples
        --------
        from fern import Email, FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.users.update(
            id_="id",
            emails=[
                Email(
                    email="elon@musk.com",
                )
            ],
        )
        """
        _response = self._raw_client.update(
            id_,
            emails=emails,
            raw=raw,
            addresses=addresses,
            company_name=company_name,
            created_at=created_at,
            department=department,
            description=description,
            division=division,
            employee_number=employee_number,
            first_name=first_name,
            id=id,
            image=image,
            language=language,
            last_name=last_name,
            parent_id=parent_id,
            password=password,
            phone_numbers=phone_numbers,
            status=status,
            title=title,
            updated_at=updated_at,
            username=username,
            request_options=request_options,
        )
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUsersResponse:
        """
        List users

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUsersResponse
            Users

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    async def add(
        self,
        *,
        emails: typing.Sequence[Email],
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        division: typing.Optional[str] = OMIT,
        employee_number: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateUserResponse:
        """
        Create user

        Parameters
        ----------
        emails : typing.Sequence[Email]

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_name : typing.Optional[str]
            The name of the company.

        created_at : typing.Optional[str]

        department : typing.Optional[str]
            The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.

        description : typing.Optional[str]
            A description of the object.

        division : typing.Optional[str]
            The division the person is currently in. Usually a collection of departments or teams or regions.

        employee_number : typing.Optional[str]
            An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[LastName]

        parent_id : typing.Optional[str]

        password : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[str]

        title : typing.Optional[str]
            The job title of the person.

        updated_at : typing.Optional[str]

        username : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUserResponse
            User created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Email

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.add(
                emails=[
                    Email(
                        email="elon@musk.com",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            emails=emails,
            raw=raw,
            addresses=addresses,
            company_name=company_name,
            created_at=created_at,
            department=department,
            description=description,
            division=division,
            employee_number=employee_number,
            first_name=first_name,
            id=id,
            image=image,
            language=language,
            last_name=last_name,
            parent_id=parent_id,
            password=password,
            phone_numbers=phone_numbers,
            status=status,
            title=title,
            updated_at=updated_at,
            username=username,
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
    ) -> GetUserResponse:
        """
        Get user

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
        GetUserResponse
            User

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteUserResponse:
        """
        Delete user

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
        DeleteUserResponse
            User deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.delete(
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
        emails: typing.Sequence[Email],
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        division: typing.Optional[str] = OMIT,
        employee_number: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateUserResponse:
        """
        Update user

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        emails : typing.Sequence[Email]

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_name : typing.Optional[str]
            The name of the company.

        created_at : typing.Optional[str]

        department : typing.Optional[str]
            The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.

        description : typing.Optional[str]
            A description of the object.

        division : typing.Optional[str]
            The division the person is currently in. Usually a collection of departments or teams or regions.

        employee_number : typing.Optional[str]
            An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[LastName]

        parent_id : typing.Optional[str]

        password : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[str]

        title : typing.Optional[str]
            The job title of the person.

        updated_at : typing.Optional[str]

        username : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateUserResponse
            User updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Email

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.update(
                id_="id",
                emails=[
                    Email(
                        email="elon@musk.com",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            emails=emails,
            raw=raw,
            addresses=addresses,
            company_name=company_name,
            created_at=created_at,
            department=department,
            description=description,
            division=division,
            employee_number=employee_number,
            first_name=first_name,
            id=id,
            image=image,
            language=language,
            last_name=last_name,
            parent_id=parent_id,
            password=password,
            phone_numbers=phone_numbers,
            status=status,
            title=title,
            updated_at=updated_at,
            username=username,
            request_options=request_options,
        )
        return _response.data
