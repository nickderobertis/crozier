

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.users import Users
from ..types.users_upsert_confirmation import UsersUpsertConfirmation
from ..types.userss import Userss
from ..types.where import Where
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.delete_users_response import DeleteUsersResponse
from .types.patch_users_response import PatchUsersResponse


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

    def find_paginated_users(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Userss:
        """
        Find paginated Users

        Parameters
        ----------
        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Userss
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.find_paginated_users()
        """
        _response = self._raw_client.find_paginated_users(
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            sort=sort,
            where=where,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def create_a_new_user(
        self,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersUpsertConfirmation:
        """
        Create a new User

        Parameters
        ----------
        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersUpsertConfirmation
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.create_a_new_user(
            id="id",
            updated_at="updatedAt",
            created_at="createdAt",
        )
        """
        _response = self._raw_client.create_a_new_user(
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            email=email,
            reset_password_token=reset_password_token,
            reset_password_expiration=reset_password_expiration,
            salt=salt,
            hash=hash,
            login_attempts=login_attempts,
            lock_until=lock_until,
            password=password,
            request_options=request_options,
        )
        return _response.data

    def delete_multiple_users(
        self,
        *,
        where: Where,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteUsersResponse:
        """
        Delete all Users matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteUsersResponse
            ok

        Examples
        --------
        from fern import FernApi, Where

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.delete_multiple_users(
            where=Where(),
        )
        """
        _response = self._raw_client.delete_multiple_users(
            where=where,
            sort=sort,
            limit=limit,
            page=page,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            request_options=request_options,
        )
        return _response.data

    def update_multiple_users(
        self,
        *,
        where: Where,
        id: str,
        updated_at: str,
        created_at: str,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchUsersResponse:
        """
        Update all Users matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        id : str

        updated_at : str

        created_at : str

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchUsersResponse
            ok

        Examples
        --------
        from fern import FernApi, Where

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.update_multiple_users(
            where=Where(),
            id="id",
            updated_at="updatedAt",
            created_at="createdAt",
        )
        """
        _response = self._raw_client.update_multiple_users(
            where=where,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            sort=sort,
            limit=limit,
            page=page,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            email=email,
            reset_password_token=reset_password_token,
            reset_password_expiration=reset_password_expiration,
            salt=salt,
            hash=hash,
            login_attempts=login_attempts,
            lock_until=lock_until,
            password=password,
            request_options=request_options,
        )
        return _response.data

    def get_a_single_user_by_its_id(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Users:
        """
        Get a single User by its id

        Parameters
        ----------
        id : str
            id of the User

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Users
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_a_single_user_by_its_id(
            id="id",
        )
        """
        _response = self._raw_client.get_a_single_user_by_its_id(
            id,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            sort=sort,
            where=where,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def deletes_an_existing_user(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersUpsertConfirmation:
        """
        Deletes an existing User

        Parameters
        ----------
        id : str
            id of the User

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersUpsertConfirmation
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.deletes_an_existing_user(
            id="id",
        )
        """
        _response = self._raw_client.deletes_an_existing_user(
            id, depth=depth, locale=locale, fallback_locale=fallback_locale, request_options=request_options
        )
        return _response.data

    def updates_a_user(
        self,
        id_: str,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersUpsertConfirmation:
        """
        Updates a User

        Parameters
        ----------
        id_ : str
            id of the User

        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersUpsertConfirmation
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.updates_a_user(
            id_="id",
            id="id",
            updated_at="updatedAt",
            created_at="createdAt",
        )
        """
        _response = self._raw_client.updates_a_user(
            id_,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            email=email,
            reset_password_token=reset_password_token,
            reset_password_expiration=reset_password_expiration,
            salt=salt,
            hash=hash,
            login_attempts=login_attempts,
            lock_until=lock_until,
            password=password,
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

    async def find_paginated_users(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Userss:
        """
        Find paginated Users

        Parameters
        ----------
        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Userss
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.find_paginated_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.find_paginated_users(
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            sort=sort,
            where=where,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def create_a_new_user(
        self,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersUpsertConfirmation:
        """
        Create a new User

        Parameters
        ----------
        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersUpsertConfirmation
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.create_a_new_user(
                id="id",
                updated_at="updatedAt",
                created_at="createdAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_user(
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            email=email,
            reset_password_token=reset_password_token,
            reset_password_expiration=reset_password_expiration,
            salt=salt,
            hash=hash,
            login_attempts=login_attempts,
            lock_until=lock_until,
            password=password,
            request_options=request_options,
        )
        return _response.data

    async def delete_multiple_users(
        self,
        *,
        where: Where,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteUsersResponse:
        """
        Delete all Users matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteUsersResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Where

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.delete_multiple_users(
                where=Where(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_multiple_users(
            where=where,
            sort=sort,
            limit=limit,
            page=page,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            request_options=request_options,
        )
        return _response.data

    async def update_multiple_users(
        self,
        *,
        where: Where,
        id: str,
        updated_at: str,
        created_at: str,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchUsersResponse:
        """
        Update all Users matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        id : str

        updated_at : str

        created_at : str

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchUsersResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Where

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.update_multiple_users(
                where=Where(),
                id="id",
                updated_at="updatedAt",
                created_at="createdAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_multiple_users(
            where=where,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            sort=sort,
            limit=limit,
            page=page,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            email=email,
            reset_password_token=reset_password_token,
            reset_password_expiration=reset_password_expiration,
            salt=salt,
            hash=hash,
            login_attempts=login_attempts,
            lock_until=lock_until,
            password=password,
            request_options=request_options,
        )
        return _response.data

    async def get_a_single_user_by_its_id(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Users:
        """
        Get a single User by its id

        Parameters
        ----------
        id : str
            id of the User

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Users
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_a_single_user_by_its_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_single_user_by_its_id(
            id,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            sort=sort,
            where=where,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def deletes_an_existing_user(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersUpsertConfirmation:
        """
        Deletes an existing User

        Parameters
        ----------
        id : str
            id of the User

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersUpsertConfirmation
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.deletes_an_existing_user(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_an_existing_user(
            id, depth=depth, locale=locale, fallback_locale=fallback_locale, request_options=request_options
        )
        return _response.data

    async def updates_a_user(
        self,
        id_: str,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersUpsertConfirmation:
        """
        Updates a User

        Parameters
        ----------
        id_ : str
            id of the User

        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersUpsertConfirmation
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.updates_a_user(
                id_="id",
                id="id",
                updated_at="updatedAt",
                created_at="createdAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_a_user(
            id_,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            email=email,
            reset_password_token=reset_password_token,
            reset_password_expiration=reset_password_expiration,
            salt=salt,
            hash=hash,
            login_attempts=login_attempts,
            lock_until=lock_until,
            password=password,
            request_options=request_options,
        )
        return _response.data
