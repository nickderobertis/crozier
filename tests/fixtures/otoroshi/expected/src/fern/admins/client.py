

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.empty import Empty
from ..types.otoroshi_models_otoroshi_admin import OtoroshiModelsOtoroshiAdmin
from .raw_client import AsyncRawAdminsClient, RawAdminsClient


OMIT = typing.cast(typing.Any, ...)


class AdminsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdminsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdminsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdminsClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_create_from_template_simple(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsOtoroshiAdmin:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsOtoroshiAdmin
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_templates_controller_create_from_template_simple(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_create_from_template_simple(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsOtoroshiAdmin:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsOtoroshiAdmin
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_simple_admins(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_users_controller_simple_admins()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_simple_admins(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_register_simple_admin(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_users_controller_register_simple_admin(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_register_simple_admin(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_find_admin(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_users_controller_find_admin(
            username="username",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_find_admin(
            username, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_update_admin(
        self,
        username: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_users_controller_update_admin(
            username="username",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_update_admin(
            username, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_delete_admin(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_users_controller_delete_admin(
            username="username",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_delete_admin(
            username, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_web_authn_admins(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_users_controller_web_authn_admins()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_web_authn_admins(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_register_web_authn_admin(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_users_controller_register_web_authn_admin(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_register_web_authn_admin(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_find_web_authn_admin(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_users_controller_find_web_authn_admin(
            username="username",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_find_web_authn_admin(
            username, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_update_web_authn_admin(
        self,
        username: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_users_controller_update_web_authn_admin(
            username="username",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_update_web_authn_admin(
            username, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin(
        self, username: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        id : str
            the id parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin(
            username="username",
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin(
            username, id, request_options=request_options
        )
        return _response.data


class AsyncAdminsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdminsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdminsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdminsClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_create_from_template_simple(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsOtoroshiAdmin:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsOtoroshiAdmin
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
            await client.admins.otoroshi_controllers_adminapi_templates_controller_create_from_template_simple(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_templates_controller_create_from_template_simple(
                request=request, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsOtoroshiAdmin:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsOtoroshiAdmin
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
            await client.admins.otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn(
                request=request, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_simple_admins(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_users_controller_simple_admins()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_simple_admins(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_register_simple_admin(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_users_controller_register_simple_admin(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_register_simple_admin(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_find_admin(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_users_controller_find_admin(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_find_admin(
            username, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_update_admin(
        self,
        username: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_users_controller_update_admin(
                username="username",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_update_admin(
            username, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_delete_admin(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_users_controller_delete_admin(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_delete_admin(
            username, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_web_authn_admins(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_users_controller_web_authn_admins()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_web_authn_admins(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_register_web_authn_admin(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_users_controller_register_web_authn_admin(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_register_web_authn_admin(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_find_web_authn_admin(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_users_controller_find_web_authn_admin(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_find_web_authn_admin(
            username, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_update_web_authn_admin(
        self,
        username: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_users_controller_update_web_authn_admin(
                username="username",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_update_web_authn_admin(
            username, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin(
        self, username: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        username : str
            the username parameter

        id : str
            the id parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.admins.otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin(
                username="username",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin(
            username, id, request_options=request_options
        )
        return _response.data
