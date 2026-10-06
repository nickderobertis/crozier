

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deleted_user_response import DeletedUserResponse
from ..types.gender_value import GenderValue
from ..types.user_data_response import UserDataResponse
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.update_user_request_birthday import UpdateUserRequestBirthday
from .types.update_user_request_first_name import UpdateUserRequestFirstName
from .types.update_user_request_gender import UpdateUserRequestGender
from .types.update_user_request_last_name import UpdateUserRequestLastName


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

    def get_user(self, *, user_id: int, request_options: typing.Optional[RequestOptions] = None) -> UserDataResponse:
        """
        Получение данных о пользователе с помощью его id

        Parameters
        ----------
        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDataResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.get_user(
            user_id=1,
        )
        """
        _response = self._raw_client.get_user(user_id=user_id, request_options=request_options)
        return _response.data

    def create_user(
        self,
        *,
        authorization: str,
        first_name: str,
        last_name: str,
        gender: GenderValue,
        birthday: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserDataResponse:
        """
        Создание пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        first_name : str
            Имя пользователя

        last_name : str
            Фамилия пользователя

        gender : GenderValue
            Пол пользователя

        birthday : dt.date
            Дата рождения

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDataResponse
            Successful Response

        Examples
        --------
        import datetime

        from fern import FernApi, GenderValue

        client = FernApi()
        client.users.create_user(
            authorization="Authorization",
            first_name="first_name",
            last_name="last_name",
            gender=GenderValue.MALE,
            birthday=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._raw_client.create_user(
            authorization=authorization,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birthday=birthday,
            request_options=request_options,
        )
        return _response.data

    def update_user_info(
        self,
        *,
        authorization: str,
        first_name: typing.Optional[UpdateUserRequestFirstName] = OMIT,
        last_name: typing.Optional[UpdateUserRequestLastName] = OMIT,
        gender: typing.Optional[UpdateUserRequestGender] = OMIT,
        birthday: typing.Optional[UpdateUserRequestBirthday] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserDataResponse:
        """
        Обновление данных пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        first_name : typing.Optional[UpdateUserRequestFirstName]
            Имя

        last_name : typing.Optional[UpdateUserRequestLastName]
            Фамилия

        gender : typing.Optional[UpdateUserRequestGender]
            Пол

        birthday : typing.Optional[UpdateUserRequestBirthday]
            Дата

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDataResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.update_user_info(
            authorization="Authorization",
        )
        """
        _response = self._raw_client.update_user_info(
            authorization=authorization,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birthday=birthday,
            request_options=request_options,
        )
        return _response.data

    def delete_user(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletedUserResponse:
        """
        Удаление пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletedUserResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.delete_user(
            authorization="Authorization",
        )
        """
        _response = self._raw_client.delete_user(authorization=authorization, request_options=request_options)
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

    async def get_user(
        self, *, user_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> UserDataResponse:
        """
        Получение данных о пользователе с помощью его id

        Parameters
        ----------
        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDataResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.get_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(user_id=user_id, request_options=request_options)
        return _response.data

    async def create_user(
        self,
        *,
        authorization: str,
        first_name: str,
        last_name: str,
        gender: GenderValue,
        birthday: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserDataResponse:
        """
        Создание пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        first_name : str
            Имя пользователя

        last_name : str
            Фамилия пользователя

        gender : GenderValue
            Пол пользователя

        birthday : dt.date
            Дата рождения

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDataResponse
            Successful Response

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, GenderValue

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.create_user(
                authorization="Authorization",
                first_name="first_name",
                last_name="last_name",
                gender=GenderValue.MALE,
                birthday=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            authorization=authorization,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birthday=birthday,
            request_options=request_options,
        )
        return _response.data

    async def update_user_info(
        self,
        *,
        authorization: str,
        first_name: typing.Optional[UpdateUserRequestFirstName] = OMIT,
        last_name: typing.Optional[UpdateUserRequestLastName] = OMIT,
        gender: typing.Optional[UpdateUserRequestGender] = OMIT,
        birthday: typing.Optional[UpdateUserRequestBirthday] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserDataResponse:
        """
        Обновление данных пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        first_name : typing.Optional[UpdateUserRequestFirstName]
            Имя

        last_name : typing.Optional[UpdateUserRequestLastName]
            Фамилия

        gender : typing.Optional[UpdateUserRequestGender]
            Пол

        birthday : typing.Optional[UpdateUserRequestBirthday]
            Дата

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDataResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.update_user_info(
                authorization="Authorization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_info(
            authorization=authorization,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birthday=birthday,
            request_options=request_options,
        )
        return _response.data

    async def delete_user(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletedUserResponse:
        """
        Удаление пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletedUserResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.delete_user(
                authorization="Authorization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(authorization=authorization, request_options=request_options)
        return _response.data
