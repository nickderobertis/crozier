

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.analysis import Analysis
from ..types.info import Info
from ..types.token_request_token_scope import TokenRequestTokenScope
from ..types.user import User
from ..types.user_access_level import UserAccessLevel
from .raw_client import AsyncRawUserClient, RawUserClient
from .types.create_rest_api_token_response import CreateRestApiTokenResponse
from .types.create_user_request_default_visibility import CreateUserRequestDefaultVisibility
from .types.get_self_response import GetSelfResponse
from .types.get_tokens_by_type_request_type import GetTokensByTypeRequestType
from .types.get_tokens_by_type_response import GetTokensByTypeResponse
from .types.modify_user_by_id_request_default_visibility import ModifyUserByIdRequestDefaultVisibility


OMIT = typing.cast(typing.Any, ...)


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserClient
        """
        return self._raw_client

    def get_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[User]:
        """
        Get the registered users

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.get_users()
        """
        _response = self._raw_client.get_users(request_options=request_options)
        return _response.data

    def create_user(
        self,
        *,
        name: str,
        id: int,
        user_pass: typing.Optional[str] = OMIT,
        default_visibility: typing.Optional[CreateUserRequestDefaultVisibility] = OMIT,
        description: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        access_level: typing.Optional[UserAccessLevel] = OMIT,
        root_folder_id: typing.Optional[float] = OMIT,
        email_notification: typing.Optional[bool] = OMIT,
        default_group: typing.Optional[int] = OMIT,
        agents: typing.Optional[Analysis] = OMIT,
        default_bucketpool: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Create a new user

        Parameters
        ----------
        name : str
            Unique username

        id : int
            ID of the user

        user_pass : typing.Optional[str]

        default_visibility : typing.Optional[CreateUserRequestDefaultVisibility]

        description : typing.Optional[str]
            Description of the user

        email : typing.Optional[str]
            Email of the user, needs to be unique and is required

        access_level : typing.Optional[UserAccessLevel]

        root_folder_id : typing.Optional[float]
            root folder id of the user

        email_notification : typing.Optional[bool]
            enable email notification when upload scan completes

        default_group : typing.Optional[int]
            Default group id of the user

        agents : typing.Optional[Analysis]

        default_bucketpool : typing.Optional[int]
            Default bucket pool id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.create_user(
            id=1,
            name="name",
        )
        """
        _response = self._raw_client.create_user(
            name=name,
            id=id,
            user_pass=user_pass,
            default_visibility=default_visibility,
            description=description,
            email=email,
            access_level=access_level,
            root_folder_id=root_folder_id,
            email_notification=email_notification,
            default_group=default_group,
            agents=agents,
            default_bucketpool=default_bucketpool,
            request_options=request_options,
        )
        return _response.data

    def get_user_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get one single user by id

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User with the given id

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.get_user_by_id(
            id=1,
        )
        """
        _response = self._raw_client.get_user_by_id(id, request_options=request_options)
        return _response.data

    def modify_user_by_id(
        self,
        id_path_param: int,
        *,
        id: int,
        user_pass: typing.Optional[str] = OMIT,
        default_folder_id: typing.Optional[int] = OMIT,
        default_visibility: typing.Optional[ModifyUserByIdRequestDefaultVisibility] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        access_level: typing.Optional[UserAccessLevel] = OMIT,
        root_folder_id: typing.Optional[float] = OMIT,
        email_notification: typing.Optional[bool] = OMIT,
        default_group: typing.Optional[int] = OMIT,
        agents: typing.Optional[Analysis] = OMIT,
        default_bucketpool: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Edit user details by id

        Parameters
        ----------
        id_path_param : int

        id : int
            ID of the user

        user_pass : typing.Optional[str]

        default_folder_id : typing.Optional[int]

        default_visibility : typing.Optional[ModifyUserByIdRequestDefaultVisibility]

        name : typing.Optional[str]
            Unique username

        description : typing.Optional[str]
            Description of the user

        email : typing.Optional[str]
            Email of the user, needs to be unique and is required

        access_level : typing.Optional[UserAccessLevel]

        root_folder_id : typing.Optional[float]
            root folder id of the user

        email_notification : typing.Optional[bool]
            enable email notification when upload scan completes

        default_group : typing.Optional[int]
            Default group id of the user

        agents : typing.Optional[Analysis]

        default_bucketpool : typing.Optional[int]
            Default bucket pool id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.modify_user_by_id(
            id_path_param=1,
            id=1,
        )
        """
        _response = self._raw_client.modify_user_by_id(
            id_path_param,
            id=id,
            user_pass=user_pass,
            default_folder_id=default_folder_id,
            default_visibility=default_visibility,
            name=name,
            description=description,
            email=email,
            access_level=access_level,
            root_folder_id=root_folder_id,
            email_notification=email_notification,
            default_group=default_group,
            agents=agents,
            default_bucketpool=default_bucketpool,
            request_options=request_options,
        )
        return _response.data

    def delete_user_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Info:
        """
        Delete a single user by id

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User will be deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.delete_user_by_id(
            id=1,
        )
        """
        _response = self._raw_client.delete_user_by_id(id, request_options=request_options)
        return _response.data

    def get_self(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetSelfResponse:
        """
        Get the information about logged in user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSelfResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.get_self()
        """
        _response = self._raw_client.get_self(request_options=request_options)
        return _response.data

    def create_rest_api_token(
        self,
        *,
        token_name: str,
        token_scope: TokenRequestTokenScope,
        token_expire: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateRestApiTokenResponse:
        """
        Create a new REST API Token

        Parameters
        ----------
        token_name : str
            Friendly name of the token

        token_scope : TokenRequestTokenScope
            The scope of the token.

        token_expire : dt.date
            Date when the token must expire (default max 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRestApiTokenResponse
            Token created successfully

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.create_rest_api_token(
            token_name="token_name",
            token_scope="read",
            token_expire=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._raw_client.create_rest_api_token(
            token_name=token_name, token_scope=token_scope, token_expire=token_expire, request_options=request_options
        )
        return _response.data

    def get_tokens_by_type(
        self, type: GetTokensByTypeRequestType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTokensByTypeResponse:
        """
        Get all the REST API tokens (active | expired)

        Parameters
        ----------
        type : GetTokensByTypeRequestType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTokensByTypeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.get_tokens_by_type(
            type="active",
        )
        """
        _response = self._raw_client.get_tokens_by_type(type, request_options=request_options)
        return _response.data

    def update_permission_by_group_id_and_user_id(
        self,
        id: int,
        user_id: int,
        *,
        perm: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Update User's permission in group.

        Parameters
        ----------
        id : int
            Id of the group

        user_id : int
            user id of the member

        perm : typing.Optional[int]
            New user permission in the group.
            0: User
            1: Admin
            2: Advisor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User's permission will be updated.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.update_permission_by_group_id_and_user_id(
            id=1,
            user_id=1,
        )
        """
        _response = self._raw_client.update_permission_by_group_id_and_user_id(
            id, user_id, perm=perm, request_options=request_options
        )
        return _response.data


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserClient
        """
        return self._raw_client

    async def get_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[User]:
        """
        Get the registered users

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(request_options=request_options)
        return _response.data

    async def create_user(
        self,
        *,
        name: str,
        id: int,
        user_pass: typing.Optional[str] = OMIT,
        default_visibility: typing.Optional[CreateUserRequestDefaultVisibility] = OMIT,
        description: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        access_level: typing.Optional[UserAccessLevel] = OMIT,
        root_folder_id: typing.Optional[float] = OMIT,
        email_notification: typing.Optional[bool] = OMIT,
        default_group: typing.Optional[int] = OMIT,
        agents: typing.Optional[Analysis] = OMIT,
        default_bucketpool: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Create a new user

        Parameters
        ----------
        name : str
            Unique username

        id : int
            ID of the user

        user_pass : typing.Optional[str]

        default_visibility : typing.Optional[CreateUserRequestDefaultVisibility]

        description : typing.Optional[str]
            Description of the user

        email : typing.Optional[str]
            Email of the user, needs to be unique and is required

        access_level : typing.Optional[UserAccessLevel]

        root_folder_id : typing.Optional[float]
            root folder id of the user

        email_notification : typing.Optional[bool]
            enable email notification when upload scan completes

        default_group : typing.Optional[int]
            Default group id of the user

        agents : typing.Optional[Analysis]

        default_bucketpool : typing.Optional[int]
            Default bucket pool id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.create_user(
                id=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            name=name,
            id=id,
            user_pass=user_pass,
            default_visibility=default_visibility,
            description=description,
            email=email,
            access_level=access_level,
            root_folder_id=root_folder_id,
            email_notification=email_notification,
            default_group=default_group,
            agents=agents,
            default_bucketpool=default_bucketpool,
            request_options=request_options,
        )
        return _response.data

    async def get_user_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get one single user by id

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User with the given id

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.get_user_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_by_id(id, request_options=request_options)
        return _response.data

    async def modify_user_by_id(
        self,
        id_path_param: int,
        *,
        id: int,
        user_pass: typing.Optional[str] = OMIT,
        default_folder_id: typing.Optional[int] = OMIT,
        default_visibility: typing.Optional[ModifyUserByIdRequestDefaultVisibility] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        access_level: typing.Optional[UserAccessLevel] = OMIT,
        root_folder_id: typing.Optional[float] = OMIT,
        email_notification: typing.Optional[bool] = OMIT,
        default_group: typing.Optional[int] = OMIT,
        agents: typing.Optional[Analysis] = OMIT,
        default_bucketpool: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Edit user details by id

        Parameters
        ----------
        id_path_param : int

        id : int
            ID of the user

        user_pass : typing.Optional[str]

        default_folder_id : typing.Optional[int]

        default_visibility : typing.Optional[ModifyUserByIdRequestDefaultVisibility]

        name : typing.Optional[str]
            Unique username

        description : typing.Optional[str]
            Description of the user

        email : typing.Optional[str]
            Email of the user, needs to be unique and is required

        access_level : typing.Optional[UserAccessLevel]

        root_folder_id : typing.Optional[float]
            root folder id of the user

        email_notification : typing.Optional[bool]
            enable email notification when upload scan completes

        default_group : typing.Optional[int]
            Default group id of the user

        agents : typing.Optional[Analysis]

        default_bucketpool : typing.Optional[int]
            Default bucket pool id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.modify_user_by_id(
                id_path_param=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_user_by_id(
            id_path_param,
            id=id,
            user_pass=user_pass,
            default_folder_id=default_folder_id,
            default_visibility=default_visibility,
            name=name,
            description=description,
            email=email,
            access_level=access_level,
            root_folder_id=root_folder_id,
            email_notification=email_notification,
            default_group=default_group,
            agents=agents,
            default_bucketpool=default_bucketpool,
            request_options=request_options,
        )
        return _response.data

    async def delete_user_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Info:
        """
        Delete a single user by id

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User will be deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.delete_user_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_by_id(id, request_options=request_options)
        return _response.data

    async def get_self(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetSelfResponse:
        """
        Get the information about logged in user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSelfResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.get_self()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_self(request_options=request_options)
        return _response.data

    async def create_rest_api_token(
        self,
        *,
        token_name: str,
        token_scope: TokenRequestTokenScope,
        token_expire: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateRestApiTokenResponse:
        """
        Create a new REST API Token

        Parameters
        ----------
        token_name : str
            Friendly name of the token

        token_scope : TokenRequestTokenScope
            The scope of the token.

        token_expire : dt.date
            Date when the token must expire (default max 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRestApiTokenResponse
            Token created successfully

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.create_rest_api_token(
                token_name="token_name",
                token_scope="read",
                token_expire=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_rest_api_token(
            token_name=token_name, token_scope=token_scope, token_expire=token_expire, request_options=request_options
        )
        return _response.data

    async def get_tokens_by_type(
        self, type: GetTokensByTypeRequestType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTokensByTypeResponse:
        """
        Get all the REST API tokens (active | expired)

        Parameters
        ----------
        type : GetTokensByTypeRequestType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTokensByTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.get_tokens_by_type(
                type="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tokens_by_type(type, request_options=request_options)
        return _response.data

    async def update_permission_by_group_id_and_user_id(
        self,
        id: int,
        user_id: int,
        *,
        perm: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Update User's permission in group.

        Parameters
        ----------
        id : int
            Id of the group

        user_id : int
            user id of the member

        perm : typing.Optional[int]
            New user permission in the group.
            0: User
            1: Admin
            2: Advisor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User's permission will be updated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.update_permission_by_group_id_and_user_id(
                id=1,
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_permission_by_group_id_and_user_id(
            id, user_id, perm=perm, request_options=request_options
        )
        return _response.data
