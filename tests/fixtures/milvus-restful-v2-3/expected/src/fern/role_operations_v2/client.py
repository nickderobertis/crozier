

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.privileges import Privileges
from .raw_client import AsyncRawRoleOperationsV2Client, RawRoleOperationsV2Client


OMIT = typing.cast(typing.Any, ...)


class RoleOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoleOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoleOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoleOperationsV2Client
        """
        return self._raw_client

    def list_roles(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        This operation lists the information about all existing roles.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            A RoleInfo object that contains a list of RoleItem objects.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.role_operations_v2.list_roles()
        """
        _response = self._raw_client.list_roles(request_options=request_options)
        return _response.data

    def describe_role(self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None) -> Privileges:
        """
        This operation describes the details of a specified role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Privileges
            An object that contains the detailed desription of a role.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.role_operations_v2.describe_role(
            role_name="roleName",
        )
        """
        _response = self._raw_client.describe_role(role_name=role_name, request_options=request_options)
        return _response.data

    def create_role(self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        This operation creates the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

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
        client.role_operations_v2.create_role(
            role_name="roleName",
        )
        """
        _response = self._raw_client.create_role(role_name=role_name, request_options=request_options)
        return _response.data

    def drop_role(self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        This operation drops an existing role. The operation will succeed if the specified role exists. Otherwise, this operation will fail.

        Parameters
        ----------
        role_name : str
            The name of the role.

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
        client.role_operations_v2.drop_role(
            role_name="roleName",
        )
        """
        _response = self._raw_client.drop_role(role_name=role_name, request_options=request_options)
        return _response.data

    def grant_privilege_to_role(
        self,
        *,
        role_name: str,
        object_type: str,
        object_name: str,
        privilege: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation grants a privilege to the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        object_type : str
             The type of the object to which the privilege belongs.

        object_name : str
             The name of the object to which the role is granted the specified privilege.

        privilege : str
             The privilege that is granted to the role.

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
        client.role_operations_v2.grant_privilege_to_role(
            role_name="roleName",
            object_type="objectType",
            object_name="objectName",
            privilege="privilege",
        )
        """
        _response = self._raw_client.grant_privilege_to_role(
            role_name=role_name,
            object_type=object_type,
            object_name=object_name,
            privilege=privilege,
            request_options=request_options,
        )
        return _response.data

    def revoke_privilege_from_role(
        self,
        *,
        role_name: str,
        object_type: str,
        object_name: str,
        privilege: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation revokes a privilege granted to the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        object_type : str
            The type of the object to which the privilege belongs.

        object_name : str
            The name of the object to which the role is granted the specified privilege.

        privilege : str
            The privilege that is granted to the role.

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
        client.role_operations_v2.revoke_privilege_from_role(
            role_name="roleName",
            object_type="objectType",
            object_name="objectName",
            privilege="privilege",
        )
        """
        _response = self._raw_client.revoke_privilege_from_role(
            role_name=role_name,
            object_type=object_type,
            object_name=object_name,
            privilege=privilege,
            request_options=request_options,
        )
        return _response.data


class AsyncRoleOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoleOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoleOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoleOperationsV2Client
        """
        return self._raw_client

    async def list_roles(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        This operation lists the information about all existing roles.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            A RoleInfo object that contains a list of RoleItem objects.

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
            await client.role_operations_v2.list_roles()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_roles(request_options=request_options)
        return _response.data

    async def describe_role(
        self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Privileges:
        """
        This operation describes the details of a specified role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Privileges
            An object that contains the detailed desription of a role.

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
            await client.role_operations_v2.describe_role(
                role_name="roleName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.describe_role(role_name=role_name, request_options=request_options)
        return _response.data

    async def create_role(
        self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This operation creates the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

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
            await client.role_operations_v2.create_role(
                role_name="roleName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_role(role_name=role_name, request_options=request_options)
        return _response.data

    async def drop_role(self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        This operation drops an existing role. The operation will succeed if the specified role exists. Otherwise, this operation will fail.

        Parameters
        ----------
        role_name : str
            The name of the role.

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
            await client.role_operations_v2.drop_role(
                role_name="roleName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.drop_role(role_name=role_name, request_options=request_options)
        return _response.data

    async def grant_privilege_to_role(
        self,
        *,
        role_name: str,
        object_type: str,
        object_name: str,
        privilege: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation grants a privilege to the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        object_type : str
             The type of the object to which the privilege belongs.

        object_name : str
             The name of the object to which the role is granted the specified privilege.

        privilege : str
             The privilege that is granted to the role.

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
            await client.role_operations_v2.grant_privilege_to_role(
                role_name="roleName",
                object_type="objectType",
                object_name="objectName",
                privilege="privilege",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.grant_privilege_to_role(
            role_name=role_name,
            object_type=object_type,
            object_name=object_name,
            privilege=privilege,
            request_options=request_options,
        )
        return _response.data

    async def revoke_privilege_from_role(
        self,
        *,
        role_name: str,
        object_type: str,
        object_name: str,
        privilege: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation revokes a privilege granted to the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        object_type : str
            The type of the object to which the privilege belongs.

        object_name : str
            The name of the object to which the role is granted the specified privilege.

        privilege : str
            The privilege that is granted to the role.

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
            await client.role_operations_v2.revoke_privilege_from_role(
                role_name="roleName",
                object_type="objectType",
                object_name="objectName",
                privilege="privilege",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_privilege_from_role(
            role_name=role_name,
            object_type=object_type,
            object_name=object_name,
            privilege=privilege,
            request_options=request_options,
        )
        return _response.data
