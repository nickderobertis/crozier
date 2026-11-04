

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key_presentation import ApiKeyPresentation
from ..types.paginated_response_of_api_key_presentation import PaginatedResponseOfApiKeyPresentation
from ..types.paginated_response_of_api_key_privilege import PaginatedResponseOfApiKeyPrivilege
from ..types.paginated_response_of_api_key_privilege_info import PaginatedResponseOfApiKeyPrivilegeInfo
from ..types.paginated_response_of_id4n_presentation import PaginatedResponseOfId4NPresentation
from .raw_client import AsyncRawApiKeysClient, RawApiKeysClient


OMIT = typing.cast(typing.Any, ...)


class ApiKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApiKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApiKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApiKeysClient
        """
        return self._raw_client

    def list_all_api_keys_of_organization(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfApiKeyPresentation:
        """
        Finding all API key assigned to the specified organization in a paginated manner.

        Parameters
        ----------
        organization_id : typing.Optional[str]
            The namespace of the organization to search in.

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfApiKeyPresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.list_all_api_keys_of_organization()
        """
        _response = self._raw_client.list_all_api_keys_of_organization(
            organization_id=organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def create_new_api_key(
        self, *, label: str, organization_id: str, secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyPresentation:
        """
        Creation of a new API key.

        Parameters
        ----------
        label : str

        organization_id : str

        secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyPresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.create_new_api_key(
            label="label",
            organization_id="de.acme",
            secret="secret",
        )
        """
        _response = self._raw_client.create_new_api_key(
            label=label, organization_id=organization_id, secret=secret, request_options=request_options
        )
        return _response.data

    def list_all_api_key_privileges(
        self,
        *,
        id4n_concerning: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfApiKeyPrivilegeInfo:
        """
        Listing all possible API key privileges.

        Parameters
        ----------
        id4n_concerning : typing.Optional[bool]
            id4nConcerning

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfApiKeyPrivilegeInfo
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.list_all_api_key_privileges()
        """
        _response = self._raw_client.list_all_api_key_privileges(
            id4n_concerning=id4n_concerning, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def get_api_key(self, key: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKeyPresentation:
        """
        Showing the details of an API key.

        Parameters
        ----------
        key : str
            The API key to show.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyPresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.get_api_key(
            key="key",
        )
        """
        _response = self._raw_client.get_api_key(key, request_options=request_options)
        return _response.data

    def update_api_key(
        self,
        key: str,
        *,
        new_label: str,
        active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        API keys can be updated with new labels, and be activated and deactivated. The secret or UUID cannot be changed.

        Parameters
        ----------
        key : str
            The API key to be updated.

        new_label : str

        active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.update_api_key(
            key="key",
            new_label="newLabel",
        )
        """
        _response = self._raw_client.update_api_key(
            key, new_label=new_label, active=active, request_options=request_options
        )
        return _response.data

    def delete_api_key(self, key: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletion of an API key.

        Parameters
        ----------
        key : str
            The API key to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.delete_api_key(
            key="key",
        )
        """
        _response = self._raw_client.delete_api_key(key, request_options=request_options)
        return _response.data

    def list_api_key_privileges(
        self,
        key: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfApiKeyPrivilege:
        """
        Parameters
        ----------
        key : str
            key

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfApiKeyPrivilege
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.list_api_key_privileges(
            key="key",
        )
        """
        _response = self._raw_client.list_api_key_privileges(
            key, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def add_api_key_privilege(
        self, key: str, *, privilege: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        key : str
            key

        privilege : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.add_api_key_privilege(
            key="key",
            privilege="privilege",
        )
        """
        _response = self._raw_client.add_api_key_privilege(key, privilege=privilege, request_options=request_options)
        return _response.data

    def remove_api_key_privilege(
        self, key: str, *, privilege: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        key : str
            key

        privilege : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.remove_api_key_privilege(
            key="key",
            privilege="privilege",
        )
        """
        _response = self._raw_client.remove_api_key_privilege(key, privilege=privilege, request_options=request_options)
        return _response.data

    def list_id4ns(
        self,
        key: str,
        privilege: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfId4NPresentation:
        """
        Listing ID4ns of a id4n concerning privilege

        Parameters
        ----------
        key : str
            key

        privilege : str
            privilege

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfId4NPresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.list_id4ns(
            key="key",
            privilege="privilege",
        )
        """
        _response = self._raw_client.list_id4ns(
            key, privilege, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def add_api_key_privilege_for_id4ns(
        self,
        key: str,
        privilege: str,
        *,
        id4ns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        key : str
            key

        privilege : str
            privilege

        id4ns : typing.Optional[typing.Sequence[str]]
            A list of id4ns.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.add_api_key_privilege_for_id4ns(
            key="key",
            privilege="privilege",
        )
        """
        _response = self._raw_client.add_api_key_privilege_for_id4ns(
            key, privilege, id4ns=id4ns, request_options=request_options
        )
        return _response.data

    def remove_api_key_privilege_for_id4ns(
        self,
        key: str,
        privilege: str,
        *,
        id4ns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        key : str
            key

        privilege : str
            privilege

        id4ns : typing.Optional[typing.Sequence[str]]
            A list of id4ns.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.api_keys.remove_api_key_privilege_for_id4ns(
            key="key",
            privilege="privilege",
        )
        """
        _response = self._raw_client.remove_api_key_privilege_for_id4ns(
            key, privilege, id4ns=id4ns, request_options=request_options
        )
        return _response.data


class AsyncApiKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApiKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApiKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApiKeysClient
        """
        return self._raw_client

    async def list_all_api_keys_of_organization(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfApiKeyPresentation:
        """
        Finding all API key assigned to the specified organization in a paginated manner.

        Parameters
        ----------
        organization_id : typing.Optional[str]
            The namespace of the organization to search in.

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfApiKeyPresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.list_all_api_keys_of_organization()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_api_keys_of_organization(
            organization_id=organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_new_api_key(
        self, *, label: str, organization_id: str, secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyPresentation:
        """
        Creation of a new API key.

        Parameters
        ----------
        label : str

        organization_id : str

        secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyPresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.create_new_api_key(
                label="label",
                organization_id="de.acme",
                secret="secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_new_api_key(
            label=label, organization_id=organization_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def list_all_api_key_privileges(
        self,
        *,
        id4n_concerning: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfApiKeyPrivilegeInfo:
        """
        Listing all possible API key privileges.

        Parameters
        ----------
        id4n_concerning : typing.Optional[bool]
            id4nConcerning

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfApiKeyPrivilegeInfo
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.list_all_api_key_privileges()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_api_key_privileges(
            id4n_concerning=id4n_concerning, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_api_key(
        self, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyPresentation:
        """
        Showing the details of an API key.

        Parameters
        ----------
        key : str
            The API key to show.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyPresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.get_api_key(
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_key(key, request_options=request_options)
        return _response.data

    async def update_api_key(
        self,
        key: str,
        *,
        new_label: str,
        active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        API keys can be updated with new labels, and be activated and deactivated. The secret or UUID cannot be changed.

        Parameters
        ----------
        key : str
            The API key to be updated.

        new_label : str

        active : typing.Optional[bool]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.update_api_key(
                key="key",
                new_label="newLabel",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_api_key(
            key, new_label=new_label, active=active, request_options=request_options
        )
        return _response.data

    async def delete_api_key(self, key: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletion of an API key.

        Parameters
        ----------
        key : str
            The API key to delete.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.delete_api_key(
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_key(key, request_options=request_options)
        return _response.data

    async def list_api_key_privileges(
        self,
        key: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfApiKeyPrivilege:
        """
        Parameters
        ----------
        key : str
            key

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfApiKeyPrivilege
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.list_api_key_privileges(
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_api_key_privileges(
            key, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def add_api_key_privilege(
        self, key: str, *, privilege: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        key : str
            key

        privilege : str

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.add_api_key_privilege(
                key="key",
                privilege="privilege",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_api_key_privilege(
            key, privilege=privilege, request_options=request_options
        )
        return _response.data

    async def remove_api_key_privilege(
        self, key: str, *, privilege: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        key : str
            key

        privilege : str

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.remove_api_key_privilege(
                key="key",
                privilege="privilege",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_api_key_privilege(
            key, privilege=privilege, request_options=request_options
        )
        return _response.data

    async def list_id4ns(
        self,
        key: str,
        privilege: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfId4NPresentation:
        """
        Listing ID4ns of a id4n concerning privilege

        Parameters
        ----------
        key : str
            key

        privilege : str
            privilege

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfId4NPresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.list_id4ns(
                key="key",
                privilege="privilege",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_id4ns(
            key, privilege, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def add_api_key_privilege_for_id4ns(
        self,
        key: str,
        privilege: str,
        *,
        id4ns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        key : str
            key

        privilege : str
            privilege

        id4ns : typing.Optional[typing.Sequence[str]]
            A list of id4ns.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.add_api_key_privilege_for_id4ns(
                key="key",
                privilege="privilege",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_api_key_privilege_for_id4ns(
            key, privilege, id4ns=id4ns, request_options=request_options
        )
        return _response.data

    async def remove_api_key_privilege_for_id4ns(
        self,
        key: str,
        privilege: str,
        *,
        id4ns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        key : str
            key

        privilege : str
            privilege

        id4ns : typing.Optional[typing.Sequence[str]]
            A list of id4ns.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_keys.remove_api_key_privilege_for_id4ns(
                key="key",
                privilege="privilege",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_api_key_privilege_for_id4ns(
            key, privilege, id4ns=id4ns, request_options=request_options
        )
        return _response.data
