

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_script_script import OtoroshiScriptScript
from .raw_client import AsyncRawScriptsClient, RawScriptsClient


OMIT = typing.cast(typing.Any, ...)


class ScriptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScriptsClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_initiate_script(
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
        client.scripts.otoroshi_controllers_adminapi_templates_controller_initiate_script()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_script(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list(
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
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_compile_script(
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
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_compile_script(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_compile_script(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiScriptScript], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiScriptScript]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiScriptScript

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_bulk_create_action(
            request=[OtoroshiScriptScript()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiScriptScript], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiScriptScript]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiScriptScript

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_bulk_update_action(
            request=[OtoroshiScriptScript()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiScriptScript:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiScriptScript
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_update_entity_action(
        self,
        id_: str,
        *,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        desc: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiScriptScript:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        name : typing.Optional[str]
            The name of the script

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        loc : typing.Optional[typing.Any]

        desc : typing.Optional[str]
            The description of the script

        code : typing.Optional[str]
            The code of the script

        id : typing.Optional[str]
            The id of the script

        type : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiScriptScript
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_update_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_update_entity_action(
            id_,
            name=name,
            metadata=metadata,
            tags=tags,
            loc=loc,
            desc=desc,
            code=code,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiScriptScript:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiScriptScript
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_patch_entity_action(
        self,
        id_: str,
        *,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        desc: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiScriptScript:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        name : typing.Optional[str]
            The name of the script

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        loc : typing.Optional[typing.Any]

        desc : typing.Optional[str]
            The description of the script

        code : typing.Optional[str]
            The code of the script

        id : typing.Optional[str]
            The id of the script

        type : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiScriptScript
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_patch_entity_action(
            id_,
            name=name,
            metadata=metadata,
            tags=tags,
            loc=loc,
            desc=desc,
            code=code,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiScriptScript]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiScriptScript]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_script_api_controller_create_action(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        desc: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiScriptScript:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            The name of the script

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        loc : typing.Optional[typing.Any]

        desc : typing.Optional[str]
            The description of the script

        code : typing.Optional[str]
            The code of the script

        id : typing.Optional[str]
            The id of the script

        type : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiScriptScript
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.otoroshi_controllers_adminapi_script_api_controller_create_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_script_api_controller_create_action(
            name=name,
            metadata=metadata,
            tags=tags,
            loc=loc,
            desc=desc,
            code=code,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data


class AsyncScriptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScriptsClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_initiate_script(
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
            await client.scripts.otoroshi_controllers_adminapi_templates_controller_initiate_script()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_script(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list(
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
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_compile_script(
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
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_compile_script(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_compile_script(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiScriptScript], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiScriptScript]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiScriptScript

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_bulk_create_action(
                request=[OtoroshiScriptScript()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiScriptScript], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiScriptScript]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiScriptScript

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_bulk_update_action(
                request=[OtoroshiScriptScript()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
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
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
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
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiScriptScript:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiScriptScript
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
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_update_entity_action(
        self,
        id_: str,
        *,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        desc: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiScriptScript:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        name : typing.Optional[str]
            The name of the script

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        loc : typing.Optional[typing.Any]

        desc : typing.Optional[str]
            The description of the script

        code : typing.Optional[str]
            The code of the script

        id : typing.Optional[str]
            The id of the script

        type : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiScriptScript
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
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_update_entity_action(
            id_,
            name=name,
            metadata=metadata,
            tags=tags,
            loc=loc,
            desc=desc,
            code=code,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiScriptScript:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiScriptScript
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
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_patch_entity_action(
        self,
        id_: str,
        *,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        desc: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiScriptScript:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        name : typing.Optional[str]
            The name of the script

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        loc : typing.Optional[typing.Any]

        desc : typing.Optional[str]
            The description of the script

        code : typing.Optional[str]
            The code of the script

        id : typing.Optional[str]
            The id of the script

        type : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiScriptScript
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
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_patch_entity_action(
            id_,
            name=name,
            metadata=metadata,
            tags=tags,
            loc=loc,
            desc=desc,
            code=code,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiScriptScript]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiScriptScript]
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
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_script_api_controller_create_action(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        desc: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiScriptScript:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            The name of the script

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        loc : typing.Optional[typing.Any]

        desc : typing.Optional[str]
            The description of the script

        code : typing.Optional[str]
            The code of the script

        id : typing.Optional[str]
            The id of the script

        type : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiScriptScript
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
            await client.scripts.otoroshi_controllers_adminapi_script_api_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_script_api_controller_create_action(
            name=name,
            metadata=metadata,
            tags=tags,
            loc=loc,
            desc=desc,
            code=code,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data
