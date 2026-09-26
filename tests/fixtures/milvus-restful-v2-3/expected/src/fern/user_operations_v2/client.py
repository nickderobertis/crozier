

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUserOperationsV2Client, RawUserOperationsV2Client
from .types.post_v2vectordb_users_describe_response import PostV2VectordbUsersDescribeResponse
from .types.post_v2vectordb_users_list_response import PostV2VectordbUsersListResponse


OMIT = typing.cast(typing.Any, ...)


class UserOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserOperationsV2Client
        """
        return self._raw_client

    def create_user(
        self, *, user_name: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This operation creates a new user with a corresponding password.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        password : str
            The corresponding password to the new user to create.
            The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_operations_v2.create_user(
            user_name="userName",
            password="password",
        )
        """
        _response = self._raw_client.create_user(
            user_name=user_name, password=password, request_options=request_options
        )
        return _response.data

    def update_user_password(
        self,
        *,
        user_name: str,
        password: str,
        new_password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation updates the password for a specific user.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        password : str
            The corresponding password to the new user to create.
            The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        new_password : str
            The new password for the specified user.    The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_operations_v2.update_user_password(
            user_name="userName",
            password="password",
            new_password="newPassword",
        )
        """
        _response = self._raw_client.update_user_password(
            user_name=user_name, password=password, new_password=new_password, request_options=request_options
        )
        return _response.data

    def drop_user(self, *, user_name: str, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        This operation deletes an existing user.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_operations_v2.drop_user(
            user_name="userName",
        )
        """
        _response = self._raw_client.drop_user(user_name=user_name, request_options=request_options)
        return _response.data

    def describe_user(
        self, *, user_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbUsersDescribeResponse:
        """
        This operation describes the detailed information of a specific user.

        Parameters
        ----------
        user_name : str
              The name of the user to describe.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbUsersDescribeResponse
            成功

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_operations_v2.describe_user(
            user_name="userName",
        )
        """
        _response = self._raw_client.describe_user(user_name=user_name, request_options=request_options)
        return _response.data

    def list_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> PostV2VectordbUsersListResponse:
        """
        This operation lists the information of all existing users.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbUsersListResponse
            An object that contains contains the user information.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_operations_v2.list_users()
        """
        _response = self._raw_client.list_users(request_options=request_options)
        return _response.data

    def grant_role_to_user(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This operation grants a specified role to the current user. Once granted the role, the user gets permissions allowed for the current role and can perform certain operations.

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_operations_v2.grant_role_to_user(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.grant_role_to_user(request=request, request_options=request_options)
        return _response.data

    def revoker_role_from_user(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This operation revokes a privilege granted to the current role.
        > Notes
        > To complete this operation, you need to enable authentication on your Milvus instance. For details, refer to [Authenticate User Access](https://milvus.io/docs/authenticate.md).

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_operations_v2.revoker_role_from_user(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.revoker_role_from_user(request=request, request_options=request_options)
        return _response.data


class AsyncUserOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserOperationsV2Client
        """
        return self._raw_client

    async def create_user(
        self, *, user_name: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This operation creates a new user with a corresponding password.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        password : str
            The corresponding password to the new user to create.
            The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_operations_v2.create_user(
                user_name="userName",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            user_name=user_name, password=password, request_options=request_options
        )
        return _response.data

    async def update_user_password(
        self,
        *,
        user_name: str,
        password: str,
        new_password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation updates the password for a specific user.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        password : str
            The corresponding password to the new user to create.
            The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        new_password : str
            The new password for the specified user.    The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_operations_v2.update_user_password(
                user_name="userName",
                password="password",
                new_password="newPassword",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_password(
            user_name=user_name, password=password, new_password=new_password, request_options=request_options
        )
        return _response.data

    async def drop_user(self, *, user_name: str, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        This operation deletes an existing user.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_operations_v2.drop_user(
                user_name="userName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.drop_user(user_name=user_name, request_options=request_options)
        return _response.data

    async def describe_user(
        self, *, user_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbUsersDescribeResponse:
        """
        This operation describes the detailed information of a specific user.

        Parameters
        ----------
        user_name : str
              The name of the user to describe.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbUsersDescribeResponse
            成功

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_operations_v2.describe_user(
                user_name="userName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.describe_user(user_name=user_name, request_options=request_options)
        return _response.data

    async def list_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbUsersListResponse:
        """
        This operation lists the information of all existing users.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbUsersListResponse
            An object that contains contains the user information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_operations_v2.list_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users(request_options=request_options)
        return _response.data

    async def grant_role_to_user(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This operation grants a specified role to the current user. Once granted the role, the user gets permissions allowed for the current role and can perform certain operations.

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_operations_v2.grant_role_to_user(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.grant_role_to_user(request=request, request_options=request_options)
        return _response.data

    async def revoker_role_from_user(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This operation revokes a privilege granted to the current role.
        > Notes
        > To complete this operation, you need to enable authentication on your Milvus instance. For details, refer to [Authenticate User Access](https://milvus.io/docs/authenticate.md).

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_operations_v2.revoker_role_from_user(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoker_role_from_user(request=request, request_options=request_options)
        return _response.data
