

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_module import ExportModule
from ..types.module import Module
from ..types.preview_module import PreviewModule
from ..types.publish_module import PublishModule
from ..types.validate_module import ValidateModule
from .raw_client import AsyncRawModulesClient, RawModulesClient


OMIT = typing.cast(typing.Any, ...)


class ModulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawModulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawModulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawModulesClient
        """
        return self._raw_client

    def return_a_list_of_all_modules(
        self,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Module:
        """
        Returns all modules. Only users with the Standard Registry and Installer role are allowed to make the request.

        Parameters
        ----------
        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Module
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.return_a_list_of_all_modules()
        """
        _response = self._raw_client.return_a_list_of_all_modules(
            page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    def creates_a_new_module(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[str] = OMIT,
        creator: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        code_version: typing.Optional[str] = OMIT,
        create_date: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new module. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        status : typing.Optional[str]

        creator : typing.Optional[str]

        owner : typing.Optional[str]

        topic_id : typing.Optional[str]

        message_id : typing.Optional[str]

        code_version : typing.Optional[str]

        create_date : typing.Optional[str]

        type : typing.Optional[str]

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
        client.modules.creates_a_new_module()
        """
        _response = self._raw_client.creates_a_new_module(
            id=id,
            uuid_=uuid_,
            name=name,
            description=description,
            config=config,
            status=status,
            creator=creator,
            owner=owner,
            topic_id=topic_id,
            message_id=message_id,
            code_version=code_version,
            create_date=create_date,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def modules_api_get_module_schemas(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
        client.modules.modules_api_get_module_schemas()
        """
        _response = self._raw_client.modules_api_get_module_schemas(request_options=request_options)
        return _response.data

    def modules_api_post_schemas(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
        client.modules.modules_api_post_schemas()
        """
        _response = self._raw_client.modules_api_post_schemas(request_options=request_options)
        return _response.data

    def retrieves_module_configuration(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Module:
        """
        Retrieves module configuration for the specified module ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid_ : str
            Selected module ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Module
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.retrieves_module_configuration(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.retrieves_module_configuration(uuid_, request_options=request_options)
        return _response.data

    def updates_module_configuration(
        self,
        uuid__: str,
        *,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[str] = OMIT,
        creator: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        code_version: typing.Optional[str] = OMIT,
        create_date: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Module:
        """
        Updates module configuration for the specified module ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid__ : str
            Selected module ID.

        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        status : typing.Optional[str]

        creator : typing.Optional[str]

        owner : typing.Optional[str]

        topic_id : typing.Optional[str]

        message_id : typing.Optional[str]

        code_version : typing.Optional[str]

        create_date : typing.Optional[str]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Module
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.updates_module_configuration(
            uuid__="uuid",
        )
        """
        _response = self._raw_client.updates_module_configuration(
            uuid__,
            id=id,
            uuid_=uuid_,
            name=name,
            description=description,
            config=config,
            status=status,
            creator=creator,
            owner=owner,
            topic_id=topic_id,
            message_id=message_id,
            code_version=code_version,
            create_date=create_date,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def deletes_the_module(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Deletes the module with the provided module ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid_ : str
            Module ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.deletes_the_module(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.deletes_the_module(uuid_, request_options=request_options)
        return _response.data

    def return_a_list_of_modules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Module]:
        """
        Returns modules menu. Only users with the Standard Registry and Installer role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Module]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.return_a_list_of_modules()
        """
        _response = self._raw_client.return_a_list_of_modules(request_options=request_options)
        return _response.data

    def return_module_and_its_artifacts_in_a_zip_file_format_for_the_specified_module(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a zip file containing the published module and all associated artifacts, i.e. schemas and VCs. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid_ : str
            Selected module ID.

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
        client.modules.return_module_and_its_artifacts_in_a_zip_file_format_for_the_specified_module(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.return_module_and_its_artifacts_in_a_zip_file_format_for_the_specified_module(
            uuid_, request_options=request_options
        )
        return _response.data

    def return_heder_message_id_for_the_specified_published_module(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportModule:
        """
        Returns the Hedera message ID for the specified module published onto IPFS. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid_ : str
            Selected module ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportModule
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.return_heder_message_id_for_the_specified_published_module(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.return_heder_message_id_for_the_specified_published_module(
            uuid_, request_options=request_options
        )
        return _response.data

    def imports_new_module_from_ipfs(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Module:
        """
        Imports new module and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Module
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.imports_new_module_from_ipfs()
        """
        _response = self._raw_client.imports_new_module_from_ipfs(
            message_id=message_id, request_options=request_options
        )
        return _response.data

    def imports_new_module_from_a_zip_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> Module:
        """
        Imports new module and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Module
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.imports_new_module_from_a_zip_file()
        """
        _response = self._raw_client.imports_new_module_from_a_zip_file(request_options=request_options)
        return _response.data

    def module_preview_from_ipfs(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> PreviewModule:
        """
        Previews the module from IPFS without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewModule
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.module_preview_from_ipfs()
        """
        _response = self._raw_client.module_preview_from_ipfs(message_id=message_id, request_options=request_options)
        return _response.data

    def module_preview_from_a_zip_file(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreviewModule:
        """
        Previews the module from a zip file without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewModule
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.module_preview_from_a_zip_file()
        """
        _response = self._raw_client.module_preview_from_a_zip_file(request_options=request_options)
        return _response.data

    def publishes_the_module_onto_ipfs(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublishModule:
        """
        Publishes the module with the specified (internal) module ID onto IPFS, sends a message featuring its IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid_ : str
            Selected module ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishModule
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.publishes_the_module_onto_ipfs(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.publishes_the_module_onto_ipfs(uuid_, request_options=request_options)
        return _response.data

    def validates_module(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[str] = OMIT,
        creator: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        code_version: typing.Optional[str] = OMIT,
        create_date: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidateModule:
        """
        Validates selected module. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        status : typing.Optional[str]

        creator : typing.Optional[str]

        owner : typing.Optional[str]

        topic_id : typing.Optional[str]

        message_id : typing.Optional[str]

        code_version : typing.Optional[str]

        create_date : typing.Optional[str]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidateModule
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.modules.validates_module()
        """
        _response = self._raw_client.validates_module(
            id=id,
            uuid_=uuid_,
            name=name,
            description=description,
            config=config,
            status=status,
            creator=creator,
            owner=owner,
            topic_id=topic_id,
            message_id=message_id,
            code_version=code_version,
            create_date=create_date,
            type=type,
            request_options=request_options,
        )
        return _response.data


class AsyncModulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawModulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawModulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawModulesClient
        """
        return self._raw_client

    async def return_a_list_of_all_modules(
        self,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Module:
        """
        Returns all modules. Only users with the Standard Registry and Installer role are allowed to make the request.

        Parameters
        ----------
        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Module
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.return_a_list_of_all_modules()


        asyncio.run(main())
        """
        _response = await self._raw_client.return_a_list_of_all_modules(
            page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def creates_a_new_module(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[str] = OMIT,
        creator: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        code_version: typing.Optional[str] = OMIT,
        create_date: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new module. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        status : typing.Optional[str]

        creator : typing.Optional[str]

        owner : typing.Optional[str]

        topic_id : typing.Optional[str]

        message_id : typing.Optional[str]

        code_version : typing.Optional[str]

        create_date : typing.Optional[str]

        type : typing.Optional[str]

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
            await client.modules.creates_a_new_module()


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_a_new_module(
            id=id,
            uuid_=uuid_,
            name=name,
            description=description,
            config=config,
            status=status,
            creator=creator,
            owner=owner,
            topic_id=topic_id,
            message_id=message_id,
            code_version=code_version,
            create_date=create_date,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def modules_api_get_module_schemas(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.modules.modules_api_get_module_schemas()


        asyncio.run(main())
        """
        _response = await self._raw_client.modules_api_get_module_schemas(request_options=request_options)
        return _response.data

    async def modules_api_post_schemas(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.modules.modules_api_post_schemas()


        asyncio.run(main())
        """
        _response = await self._raw_client.modules_api_post_schemas(request_options=request_options)
        return _response.data

    async def retrieves_module_configuration(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Module:
        """
        Retrieves module configuration for the specified module ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid_ : str
            Selected module ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Module
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.retrieves_module_configuration(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieves_module_configuration(uuid_, request_options=request_options)
        return _response.data

    async def updates_module_configuration(
        self,
        uuid__: str,
        *,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[str] = OMIT,
        creator: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        code_version: typing.Optional[str] = OMIT,
        create_date: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Module:
        """
        Updates module configuration for the specified module ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid__ : str
            Selected module ID.

        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        status : typing.Optional[str]

        creator : typing.Optional[str]

        owner : typing.Optional[str]

        topic_id : typing.Optional[str]

        message_id : typing.Optional[str]

        code_version : typing.Optional[str]

        create_date : typing.Optional[str]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Module
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.updates_module_configuration(
                uuid__="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_module_configuration(
            uuid__,
            id=id,
            uuid_=uuid_,
            name=name,
            description=description,
            config=config,
            status=status,
            creator=creator,
            owner=owner,
            topic_id=topic_id,
            message_id=message_id,
            code_version=code_version,
            create_date=create_date,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def deletes_the_module(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Deletes the module with the provided module ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid_ : str
            Module ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.deletes_the_module(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_module(uuid_, request_options=request_options)
        return _response.data

    async def return_a_list_of_modules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Module]:
        """
        Returns modules menu. Only users with the Standard Registry and Installer role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Module]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.return_a_list_of_modules()


        asyncio.run(main())
        """
        _response = await self._raw_client.return_a_list_of_modules(request_options=request_options)
        return _response.data

    async def return_module_and_its_artifacts_in_a_zip_file_format_for_the_specified_module(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a zip file containing the published module and all associated artifacts, i.e. schemas and VCs. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid_ : str
            Selected module ID.

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
            await client.modules.return_module_and_its_artifacts_in_a_zip_file_format_for_the_specified_module(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.return_module_and_its_artifacts_in_a_zip_file_format_for_the_specified_module(
                uuid_, request_options=request_options
            )
        )
        return _response.data

    async def return_heder_message_id_for_the_specified_published_module(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportModule:
        """
        Returns the Hedera message ID for the specified module published onto IPFS. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid_ : str
            Selected module ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportModule
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.return_heder_message_id_for_the_specified_published_module(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_heder_message_id_for_the_specified_published_module(
            uuid_, request_options=request_options
        )
        return _response.data

    async def imports_new_module_from_ipfs(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Module:
        """
        Imports new module and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Module
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.imports_new_module_from_ipfs()


        asyncio.run(main())
        """
        _response = await self._raw_client.imports_new_module_from_ipfs(
            message_id=message_id, request_options=request_options
        )
        return _response.data

    async def imports_new_module_from_a_zip_file(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Module:
        """
        Imports new module and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Module
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.imports_new_module_from_a_zip_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.imports_new_module_from_a_zip_file(request_options=request_options)
        return _response.data

    async def module_preview_from_ipfs(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> PreviewModule:
        """
        Previews the module from IPFS without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewModule
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.module_preview_from_ipfs()


        asyncio.run(main())
        """
        _response = await self._raw_client.module_preview_from_ipfs(
            message_id=message_id, request_options=request_options
        )
        return _response.data

    async def module_preview_from_a_zip_file(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreviewModule:
        """
        Previews the module from a zip file without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewModule
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.module_preview_from_a_zip_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.module_preview_from_a_zip_file(request_options=request_options)
        return _response.data

    async def publishes_the_module_onto_ipfs(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublishModule:
        """
        Publishes the module with the specified (internal) module ID onto IPFS, sends a message featuring its IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        uuid_ : str
            Selected module ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishModule
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.publishes_the_module_onto_ipfs(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publishes_the_module_onto_ipfs(uuid_, request_options=request_options)
        return _response.data

    async def validates_module(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[str] = OMIT,
        creator: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        code_version: typing.Optional[str] = OMIT,
        create_date: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidateModule:
        """
        Validates selected module. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        status : typing.Optional[str]

        creator : typing.Optional[str]

        owner : typing.Optional[str]

        topic_id : typing.Optional[str]

        message_id : typing.Optional[str]

        code_version : typing.Optional[str]

        create_date : typing.Optional[str]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidateModule
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.modules.validates_module()


        asyncio.run(main())
        """
        _response = await self._raw_client.validates_module(
            id=id,
            uuid_=uuid_,
            name=name,
            description=description,
            config=config,
            status=status,
            creator=creator,
            owner=owner,
            topic_id=topic_id,
            message_id=message_id,
            code_version=code_version,
            create_date=create_date,
            type=type,
            request_options=request_options,
        )
        return _response.data
