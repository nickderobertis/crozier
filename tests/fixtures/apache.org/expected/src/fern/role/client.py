

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.action_resource import ActionResource
from ..types.role import Role
from ..types.role_collection import RoleCollection
from .raw_client import AsyncRawRoleClient, RawRoleClient


OMIT = typing.cast(typing.Any, ...)


class RoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoleClient
        """
        return self._raw_client

    def get_roles(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RoleCollection:
        """
        Get a list of roles.

        *New in version 2.1.0*

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoleCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.role.get_roles()
        """
        _response = self._raw_client.get_roles(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    def post_role(
        self,
        *,
        actions: typing.Optional[typing.Sequence[ActionResource]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Create a new role.

        *New in version 2.1.0*

        Parameters
        ----------
        actions : typing.Optional[typing.Sequence[ActionResource]]

        name : typing.Optional[str]
            The name of the role

            *Changed in version 2.3.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.role.post_role()
        """
        _response = self._raw_client.post_role(actions=actions, name=name, request_options=request_options)
        return _response.data

    def get_role(self, role_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """
        Get a role.

        *New in version 2.1.0*

        Parameters
        ----------
        role_name : str
            The role name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.role.get_role(
            role_name="role_name",
        )
        """
        _response = self._raw_client.get_role(role_name, request_options=request_options)
        return _response.data

    def delete_role(self, role_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a role.

        *New in version 2.1.0*

        Parameters
        ----------
        role_name : str
            The role name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.role.delete_role(
            role_name="role_name",
        )
        """
        _response = self._raw_client.delete_role(role_name, request_options=request_options)
        return _response.data

    def patch_role(
        self,
        role_name: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        actions: typing.Optional[typing.Sequence[ActionResource]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Update a role.

        *New in version 2.1.0*

        Parameters
        ----------
        role_name : str
            The role name

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        actions : typing.Optional[typing.Sequence[ActionResource]]

        name : typing.Optional[str]
            The name of the role

            *Changed in version 2.3.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.role.patch_role(
            role_name="role_name",
        )
        """
        _response = self._raw_client.patch_role(
            role_name, update_mask=update_mask, actions=actions, name=name, request_options=request_options
        )
        return _response.data


class AsyncRoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoleClient
        """
        return self._raw_client

    async def get_roles(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RoleCollection:
        """
        Get a list of roles.

        *New in version 2.1.0*

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoleCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.role.get_roles()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_roles(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    async def post_role(
        self,
        *,
        actions: typing.Optional[typing.Sequence[ActionResource]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Create a new role.

        *New in version 2.1.0*

        Parameters
        ----------
        actions : typing.Optional[typing.Sequence[ActionResource]]

        name : typing.Optional[str]
            The name of the role

            *Changed in version 2.3.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.role.post_role()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_role(actions=actions, name=name, request_options=request_options)
        return _response.data

    async def get_role(self, role_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """
        Get a role.

        *New in version 2.1.0*

        Parameters
        ----------
        role_name : str
            The role name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.role.get_role(
                role_name="role_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_role(role_name, request_options=request_options)
        return _response.data

    async def delete_role(self, role_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a role.

        *New in version 2.1.0*

        Parameters
        ----------
        role_name : str
            The role name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.role.delete_role(
                role_name="role_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_role(role_name, request_options=request_options)
        return _response.data

    async def patch_role(
        self,
        role_name: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        actions: typing.Optional[typing.Sequence[ActionResource]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Update a role.

        *New in version 2.1.0*

        Parameters
        ----------
        role_name : str
            The role name

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        actions : typing.Optional[typing.Sequence[ActionResource]]

        name : typing.Optional[str]
            The name of the role

            *Changed in version 2.3.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.role.patch_role(
                role_name="role_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_role(
            role_name, update_mask=update_mask, actions=actions, name=name, request_options=request_options
        )
        return _response.data
