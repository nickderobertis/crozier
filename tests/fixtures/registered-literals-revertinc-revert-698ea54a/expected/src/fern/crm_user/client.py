

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.crm_create_or_update_user_response import CrmCreateOrUpdateUserResponse
from ..types.crm_get_user_response import CrmGetUserResponse
from ..types.crm_get_users_response import CrmGetUsersResponse
from .raw_client import AsyncRawCrmUserClient, RawCrmUserClient


OMIT = typing.cast(typing.Any, ...)


class CrmUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmUserClient
        """
        return self._raw_client

    def crm_user_get_user(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetUserResponse:
        """
        Get details of a user

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetUserResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_user.crm_user_get_user(
            id="id",
        )
        """
        _response = self._raw_client.crm_user_get_user(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_user_get_users(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetUsersResponse:
        """
        Get all the users

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetUsersResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_user.crm_user_get_users()
        """
        _response = self._raw_client.crm_user_get_users(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_user_create_user(
        self,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateUserResponse:
        """
        Create a new user

        Parameters
        ----------
        additional : typing.Any

        first_name : str
            The first name of a user in a CRM.

        last_name : str
            The last name of a user in a CRM.

        phone : str
            The phone number of a user in a CRM.

        email : str
            The email of a user in a CRM.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateUserResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_user.crm_user_create_user(
            additional={"key": "value"},
            first_name="firstName",
            last_name="lastName",
            phone="phone",
            email="email",
        )
        """
        _response = self._raw_client.crm_user_create_user(
            additional=additional,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            request_options=request_options,
        )
        return _response.data


class AsyncCrmUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmUserClient
        """
        return self._raw_client

    async def crm_user_get_user(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetUserResponse:
        """
        Get details of a user

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetUserResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_user.crm_user_get_user(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_user_get_user(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_user_get_users(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetUsersResponse:
        """
        Get all the users

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetUsersResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_user.crm_user_get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_user_get_users(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_user_create_user(
        self,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateUserResponse:
        """
        Create a new user

        Parameters
        ----------
        additional : typing.Any

        first_name : str
            The first name of a user in a CRM.

        last_name : str
            The last name of a user in a CRM.

        phone : str
            The phone number of a user in a CRM.

        email : str
            The email of a user in a CRM.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateUserResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_user.crm_user_create_user(
                additional={"key": "value"},
                first_name="firstName",
                last_name="lastName",
                phone="phone",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_user_create_user(
            additional=additional,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            request_options=request_options,
        )
        return _response.data
