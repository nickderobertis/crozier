

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deleted import Deleted
from ..types.patch import Patch
from .raw_client import AsyncRawAuthConfigClient, RawAuthConfigClient
from .types.create_global_auth_module_request import CreateGlobalAuthModuleRequest
from .types.create_global_auth_module_response import CreateGlobalAuthModuleResponse
from .types.find_all_global_auth_modules_response_item import FindAllGlobalAuthModulesResponseItem
from .types.find_global_auth_module_by_id_response import FindGlobalAuthModuleByIdResponse
from .types.patch_global_auth_module_response import PatchGlobalAuthModuleResponse
from .types.update_global_auth_module_request_body import UpdateGlobalAuthModuleRequestBody
from .types.update_global_auth_module_response import UpdateGlobalAuthModuleResponse


OMIT = typing.cast(typing.Any, ...)


class AuthConfigClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthConfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthConfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthConfigClient
        """
        return self._raw_client

    def find_all_global_auth_modules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FindAllGlobalAuthModulesResponseItem]:
        """
        Get all global auth. module configs

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FindAllGlobalAuthModulesResponseItem]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_config.find_all_global_auth_modules()
        """
        _response = self._raw_client.find_all_global_auth_modules(request_options=request_options)
        return _response.data

    def create_global_auth_module(
        self, *, request: CreateGlobalAuthModuleRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateGlobalAuthModuleResponse:
        """
        Create one global auth. module config

        Parameters
        ----------
        request : CreateGlobalAuthModuleRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGlobalAuthModuleResponse
            Successful operation

        Examples
        --------
        from fern import FernApi, LdapAuthModuleConfig

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_config.create_global_auth_module(
            request=LdapAuthModuleConfig(
                admin_password="a string value",
                admin_username="a string value",
                desc="a string value",
                email_field="a string value",
                group_filter="a string value",
                id="a string value",
                name="a string value",
                name_field="a string value",
                search_base="a string value",
                search_filter="a string value",
                server_url="a string value",
                session_max_age=123123,
                type="a string value",
                user_base="a string value",
            ),
        )
        """
        _response = self._raw_client.create_global_auth_module(request=request, request_options=request_options)
        return _response.data

    def find_global_auth_module_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FindGlobalAuthModuleByIdResponse:
        """
        Get one global auth. module configs

        Parameters
        ----------
        id : str
            The auth. config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindGlobalAuthModuleByIdResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_config.find_global_auth_module_by_id(
            id="id",
        )
        """
        _response = self._raw_client.find_global_auth_module_by_id(id, request_options=request_options)
        return _response.data

    def update_global_auth_module(
        self,
        id: str,
        *,
        request: UpdateGlobalAuthModuleRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateGlobalAuthModuleResponse:
        """
        Update one global auth. module config

        Parameters
        ----------
        id : str
            The auth. config id

        request : UpdateGlobalAuthModuleRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateGlobalAuthModuleResponse
            Successful operation

        Examples
        --------
        from fern import FernApi, LdapAuthModuleConfig

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_config.update_global_auth_module(
            id="id",
            request=LdapAuthModuleConfig(
                admin_password="a string value",
                admin_username="a string value",
                desc="a string value",
                email_field="a string value",
                group_filter="a string value",
                id="a string value",
                name="a string value",
                name_field="a string value",
                search_base="a string value",
                search_filter="a string value",
                server_url="a string value",
                session_max_age=123123,
                type="a string value",
                user_base="a string value",
            ),
        )
        """
        _response = self._raw_client.update_global_auth_module(id, request=request, request_options=request_options)
        return _response.data

    def delete_global_auth_module(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deleted:
        """
        Delete one global auth. module config

        Parameters
        ----------
        id : str
            The auth. config id id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_config.delete_global_auth_module(
            id="id",
        )
        """
        _response = self._raw_client.delete_global_auth_module(id, request_options=request_options)
        return _response.data

    def patch_global_auth_module(
        self, id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> PatchGlobalAuthModuleResponse:
        """
        Update one global auth. module config

        Parameters
        ----------
        id : str
            The auth. config id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchGlobalAuthModuleResponse
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_config.patch_global_auth_module(
            id="id",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_global_auth_module(id, request=request, request_options=request_options)
        return _response.data


class AsyncAuthConfigClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthConfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthConfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthConfigClient
        """
        return self._raw_client

    async def find_all_global_auth_modules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FindAllGlobalAuthModulesResponseItem]:
        """
        Get all global auth. module configs

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FindAllGlobalAuthModulesResponseItem]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_config.find_all_global_auth_modules()


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all_global_auth_modules(request_options=request_options)
        return _response.data

    async def create_global_auth_module(
        self, *, request: CreateGlobalAuthModuleRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateGlobalAuthModuleResponse:
        """
        Create one global auth. module config

        Parameters
        ----------
        request : CreateGlobalAuthModuleRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGlobalAuthModuleResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LdapAuthModuleConfig

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_config.create_global_auth_module(
                request=LdapAuthModuleConfig(
                    admin_password="a string value",
                    admin_username="a string value",
                    desc="a string value",
                    email_field="a string value",
                    group_filter="a string value",
                    id="a string value",
                    name="a string value",
                    name_field="a string value",
                    search_base="a string value",
                    search_filter="a string value",
                    server_url="a string value",
                    session_max_age=123123,
                    type="a string value",
                    user_base="a string value",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_global_auth_module(request=request, request_options=request_options)
        return _response.data

    async def find_global_auth_module_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FindGlobalAuthModuleByIdResponse:
        """
        Get one global auth. module configs

        Parameters
        ----------
        id : str
            The auth. config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindGlobalAuthModuleByIdResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_config.find_global_auth_module_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_global_auth_module_by_id(id, request_options=request_options)
        return _response.data

    async def update_global_auth_module(
        self,
        id: str,
        *,
        request: UpdateGlobalAuthModuleRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateGlobalAuthModuleResponse:
        """
        Update one global auth. module config

        Parameters
        ----------
        id : str
            The auth. config id

        request : UpdateGlobalAuthModuleRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateGlobalAuthModuleResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LdapAuthModuleConfig

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_config.update_global_auth_module(
                id="id",
                request=LdapAuthModuleConfig(
                    admin_password="a string value",
                    admin_username="a string value",
                    desc="a string value",
                    email_field="a string value",
                    group_filter="a string value",
                    id="a string value",
                    name="a string value",
                    name_field="a string value",
                    search_base="a string value",
                    search_filter="a string value",
                    server_url="a string value",
                    session_max_age=123123,
                    type="a string value",
                    user_base="a string value",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_global_auth_module(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_global_auth_module(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete one global auth. module config

        Parameters
        ----------
        id : str
            The auth. config id id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_config.delete_global_auth_module(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_global_auth_module(id, request_options=request_options)
        return _response.data

    async def patch_global_auth_module(
        self, id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> PatchGlobalAuthModuleResponse:
        """
        Update one global auth. module config

        Parameters
        ----------
        id : str
            The auth. config id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchGlobalAuthModuleResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchItem, PatchItemOp

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_config.patch_global_auth_module(
                id="id",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_global_auth_module(
            id, request=request, request_options=request_options
        )
        return _response.data
