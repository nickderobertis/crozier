

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_annotated_union_registered_project_function_get_registered_solver_function_get_field_info_annotation_none_type_required_true_discriminator_function_class import (
    EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
)
from ..types.envelope_dict_new_type_function_group_access_rights_get import (
    EnvelopeDictNewTypeFunctionGroupAccessRightsGet,
)
from ..types.envelope_function_group_access_rights_get import EnvelopeFunctionGroupAccessRightsGet
from ..types.envelope_list_annotated_union_registered_project_function_get_registered_solver_function_get_field_info_annotation_none_type_required_true_discriminator_function_class import (
    EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
)
from ..types.group_id_int import GroupIdInt
from .raw_client import AsyncRawFunctionsClient, RawFunctionsClient
from .types.register_function_request import RegisterFunctionRequest


OMIT = typing.cast(typing.Any, ...)


class FunctionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFunctionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFunctionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFunctionsClient
        """
        return self._raw_client

    def list_functions(
        self,
        *,
        include_extras: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass:
        """
        Parameters
        ----------
        include_extras : typing.Optional[bool]

        search : typing.Optional[str]

        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.functions.list_functions()
        """
        _response = self._raw_client.list_functions(
            include_extras=include_extras,
            search=search,
            filters=filters,
            order_by=order_by,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def register_function(
        self, *, request: RegisterFunctionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass:
        """
        Parameters
        ----------
        request : RegisterFunctionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
            Successful Response

        Examples
        --------
        from fern.functions import RegisterFunctionRequest_Project

        from fern import (
            FernApi,
            ProjectFunctionToRegisterInputSchema_ApplicationSchemaJson,
            ProjectFunctionToRegisterOutputSchema_ApplicationSchemaJson,
        )

        client = FernApi()
        client.functions.register_function(
            request=RegisterFunctionRequest_Project(
                input_schema=ProjectFunctionToRegisterInputSchema_ApplicationSchemaJson(),
                output_schema=ProjectFunctionToRegisterOutputSchema_ApplicationSchemaJson(),
                project_id="projectId",
            ),
        )
        """
        _response = self._raw_client.register_function(request=request, request_options=request_options)
        return _response.data

    def get_function(
        self,
        function_id: str,
        *,
        include_extras: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass:
        """
        Parameters
        ----------
        function_id : str

        include_extras : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.functions.get_function(
            function_id="function_id",
        )
        """
        _response = self._raw_client.get_function(
            function_id, include_extras=include_extras, request_options=request_options
        )
        return _response.data

    def delete_function(
        self,
        function_id: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        function_id : str

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.functions.delete_function(
            function_id="function_id",
        )
        """
        _response = self._raw_client.delete_function(function_id, force=force, request_options=request_options)
        return _response.data

    def update_function(
        self,
        function_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass:
        """
        Parameters
        ----------
        function_id : str

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.functions.update_function(
            function_id="function_id",
        )
        """
        _response = self._raw_client.update_function(
            function_id, title=title, description=description, request_options=request_options
        )
        return _response.data

    def get_function_groups(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictNewTypeFunctionGroupAccessRightsGet:
        """
        Parameters
        ----------
        function_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictNewTypeFunctionGroupAccessRightsGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.functions.get_function_groups(
            function_id="function_id",
        )
        """
        _response = self._raw_client.get_function_groups(function_id, request_options=request_options)
        return _response.data

    def create_or_update_function_group(
        self,
        function_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        execute: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeFunctionGroupAccessRightsGet:
        """
        Parameters
        ----------
        function_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        execute : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFunctionGroupAccessRightsGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.functions.create_or_update_function_group(
            function_id="function_id",
            group_id=1,
            read=True,
            write=True,
            execute=True,
        )
        """
        _response = self._raw_client.create_or_update_function_group(
            function_id, group_id, read=read, write=write, execute=execute, request_options=request_options
        )
        return _response.data

    def delete_function_group(
        self, function_id: str, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        function_id : str

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.functions.delete_function_group(
            function_id="function_id",
            group_id=1,
        )
        """
        _response = self._raw_client.delete_function_group(function_id, group_id, request_options=request_options)
        return _response.data


class AsyncFunctionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFunctionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFunctionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFunctionsClient
        """
        return self._raw_client

    async def list_functions(
        self,
        *,
        include_extras: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass:
        """
        Parameters
        ----------
        include_extras : typing.Optional[bool]

        search : typing.Optional[str]

        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.functions.list_functions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_functions(
            include_extras=include_extras,
            search=search,
            filters=filters,
            order_by=order_by,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def register_function(
        self, *, request: RegisterFunctionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass:
        """
        Parameters
        ----------
        request : RegisterFunctionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
            Successful Response

        Examples
        --------
        import asyncio

        from fern.functions import RegisterFunctionRequest_Project

        from fern import (
            AsyncFernApi,
            ProjectFunctionToRegisterInputSchema_ApplicationSchemaJson,
            ProjectFunctionToRegisterOutputSchema_ApplicationSchemaJson,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.functions.register_function(
                request=RegisterFunctionRequest_Project(
                    input_schema=ProjectFunctionToRegisterInputSchema_ApplicationSchemaJson(),
                    output_schema=ProjectFunctionToRegisterOutputSchema_ApplicationSchemaJson(),
                    project_id="projectId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_function(request=request, request_options=request_options)
        return _response.data

    async def get_function(
        self,
        function_id: str,
        *,
        include_extras: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass:
        """
        Parameters
        ----------
        function_id : str

        include_extras : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.functions.get_function(
                function_id="function_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_function(
            function_id, include_extras=include_extras, request_options=request_options
        )
        return _response.data

    async def delete_function(
        self,
        function_id: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        function_id : str

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.functions.delete_function(
                function_id="function_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_function(function_id, force=force, request_options=request_options)
        return _response.data

    async def update_function(
        self,
        function_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass:
        """
        Parameters
        ----------
        function_id : str

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.functions.update_function(
                function_id="function_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_function(
            function_id, title=title, description=description, request_options=request_options
        )
        return _response.data

    async def get_function_groups(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictNewTypeFunctionGroupAccessRightsGet:
        """
        Parameters
        ----------
        function_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictNewTypeFunctionGroupAccessRightsGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.functions.get_function_groups(
                function_id="function_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_function_groups(function_id, request_options=request_options)
        return _response.data

    async def create_or_update_function_group(
        self,
        function_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        execute: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeFunctionGroupAccessRightsGet:
        """
        Parameters
        ----------
        function_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        execute : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFunctionGroupAccessRightsGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.functions.create_or_update_function_group(
                function_id="function_id",
                group_id=1,
                read=True,
                write=True,
                execute=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update_function_group(
            function_id, group_id, read=read, write=write, execute=execute, request_options=request_options
        )
        return _response.data

    async def delete_function_group(
        self, function_id: str, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        function_id : str

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.functions.delete_function_group(
                function_id="function_id",
                group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_function_group(function_id, group_id, request_options=request_options)
        return _response.data
