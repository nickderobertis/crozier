

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.metadata import Metadata
from ..types.role import Role
from .raw_client import AsyncRawRolesClient, RawRolesClient
from .types.list_merchant_roles_response import ListMerchantRolesResponse


OMIT = typing.cast(typing.Any, ...)


class RolesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRolesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRolesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRolesClient
        """
        return self._raw_client

    def list_merchant_roles(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListMerchantRolesResponse:
        """
        List merchant's custom roles.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMerchantRolesResponse
            Returns a list of Role objects.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.list_merchant_roles(
            merchant_code="MK10CL2A",
        )
        """
        _response = self._raw_client.list_merchant_roles(merchant_code, request_options=request_options)
        return _response.data

    def create_merchant_role(
        self,
        merchant_code: str,
        *,
        name: str,
        permissions: typing.Sequence[str],
        metadata: typing.Optional[Metadata] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Create a custom role for the merchant. Roles are defined by the set of permissions that they grant to the members that they are assigned to.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        name : str
            User-defined name of the role.

        permissions : typing.Sequence[str]
            User's permissions.

        metadata : typing.Optional[Metadata]

        description : typing.Optional[str]
            User-defined description of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the Role object after successful custom role creation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.create_merchant_role(
            merchant_code="MK10CL2A",
            name="Senior Shop Manager II",
            permissions=["catalog_access", "taxes_access", "members_access"],
        )
        """
        _response = self._raw_client.create_merchant_role(
            merchant_code,
            name=name,
            permissions=permissions,
            metadata=metadata,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def get_merchant_role(
        self, merchant_code: str, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Role:
        """
        Retrieve a custom role by ID.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the Role object for a valid identifier.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.get_merchant_role(
            merchant_code="MK10CL2A",
            role_id="role_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
        )
        """
        _response = self._raw_client.get_merchant_role(merchant_code, role_id, request_options=request_options)
        return _response.data

    def delete_merchant_role(
        self, merchant_code: str, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a custom role.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.delete_merchant_role(
            merchant_code="MK10CL2A",
            role_id="role_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
        )
        """
        _response = self._raw_client.delete_merchant_role(merchant_code, role_id, request_options=request_options)
        return _response.data

    def update_merchant_role(
        self,
        merchant_code: str,
        role_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        permissions: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Updates a custom role's name, description, or permissions and returns the updated role.

        Providing `permissions` replaces the role's permission list and changes the access granted to members assigned to that role. Omitted fields remain unchanged.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        name : typing.Optional[str]
            User-defined name of the role.

        permissions : typing.Optional[typing.Sequence[str]]
            User's permissions.

        description : typing.Optional[str]
            User-defined description of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the updated Role object if the update succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.update_merchant_role(
            merchant_code="MK10CL2A",
            role_id="role_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
            name="Senior Shop Manager III",
            permissions=["catalog_edit", "taxes_access", "members_edit"],
        )
        """
        _response = self._raw_client.update_merchant_role(
            merchant_code,
            role_id,
            name=name,
            permissions=permissions,
            description=description,
            request_options=request_options,
        )
        return _response.data


class AsyncRolesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRolesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRolesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRolesClient
        """
        return self._raw_client

    async def list_merchant_roles(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListMerchantRolesResponse:
        """
        List merchant's custom roles.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMerchantRolesResponse
            Returns a list of Role objects.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.list_merchant_roles(
                merchant_code="MK10CL2A",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_merchant_roles(merchant_code, request_options=request_options)
        return _response.data

    async def create_merchant_role(
        self,
        merchant_code: str,
        *,
        name: str,
        permissions: typing.Sequence[str],
        metadata: typing.Optional[Metadata] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Create a custom role for the merchant. Roles are defined by the set of permissions that they grant to the members that they are assigned to.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        name : str
            User-defined name of the role.

        permissions : typing.Sequence[str]
            User's permissions.

        metadata : typing.Optional[Metadata]

        description : typing.Optional[str]
            User-defined description of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the Role object after successful custom role creation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.create_merchant_role(
                merchant_code="MK10CL2A",
                name="Senior Shop Manager II",
                permissions=["catalog_access", "taxes_access", "members_access"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_merchant_role(
            merchant_code,
            name=name,
            permissions=permissions,
            metadata=metadata,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def get_merchant_role(
        self, merchant_code: str, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Role:
        """
        Retrieve a custom role by ID.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the Role object for a valid identifier.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.get_merchant_role(
                merchant_code="MK10CL2A",
                role_id="role_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_merchant_role(merchant_code, role_id, request_options=request_options)
        return _response.data

    async def delete_merchant_role(
        self, merchant_code: str, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a custom role.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.delete_merchant_role(
                merchant_code="MK10CL2A",
                role_id="role_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_merchant_role(merchant_code, role_id, request_options=request_options)
        return _response.data

    async def update_merchant_role(
        self,
        merchant_code: str,
        role_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        permissions: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Updates a custom role's name, description, or permissions and returns the updated role.

        Providing `permissions` replaces the role's permission list and changes the access granted to members assigned to that role. Omitted fields remain unchanged.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        name : typing.Optional[str]
            User-defined name of the role.

        permissions : typing.Optional[typing.Sequence[str]]
            User's permissions.

        description : typing.Optional[str]
            User-defined description of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the updated Role object if the update succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.update_merchant_role(
                merchant_code="MK10CL2A",
                role_id="role_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
                name="Senior Shop Manager III",
                permissions=["catalog_edit", "taxes_access", "members_edit"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_merchant_role(
            merchant_code,
            role_id,
            name=name,
            permissions=permissions,
            description=description,
            request_options=request_options,
        )
        return _response.data
