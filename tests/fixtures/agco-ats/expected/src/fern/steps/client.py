

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_build_system_shared_dto_step import ApiPagedResponseBuildSystemSharedDtoStep
from ..types.build_system_shared_dto_parameter import BuildSystemSharedDtoParameter
from ..types.build_system_shared_dto_step import BuildSystemSharedDtoStep
from .raw_client import AsyncRawStepsClient, RawStepsClient


OMIT = typing.cast(typing.Any, ...)


class StepsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStepsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStepsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStepsClient
        """
        return self._raw_client

    def getsteps(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoStep:
        """
        Gets a collection of Steps. When successful, the response is a PagedResponse of Steps.
                    If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        include_deleted : typing.Optional[bool]
            Does it include deleted step, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoStep
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.steps.getsteps()
        """
        _response = self._raw_client.getsteps(
            limit=limit, offset=offset, include_deleted=include_deleted, request_options=request_options
        )
        return _response.data

    def poststep(
        self,
        *,
        config_required: bool,
        implementation_id: str,
        name: str,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        step_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        config_required : bool
            Indicates if the step requires configuration values to be provided by the build agent

        implementation_id : str
            The implementation ID used to lookup the step implementation when it is executed

        name : str
            The name of the step

        deleted : typing.Optional[bool]
            Read Only.  Indicates if the record is deleted.

        description : typing.Optional[str]
            A description of the step to be presented to a user

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this step

        step_id : typing.Optional[int]
            The ID of the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.steps.poststep(
            config_required=True,
            implementation_id="ImplementationID",
            name="Name",
        )
        """
        _response = self._raw_client.poststep(
            config_required=config_required,
            implementation_id=implementation_id,
            name=name,
            deleted=deleted,
            description=description,
            parameters=parameters,
            step_id=step_id,
            request_options=request_options,
        )
        return _response.data

    def getstep(
        self,
        step_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildSystemSharedDtoStep:
        """
        Gets a Step by ID. When successful, the response is the requested Step.
                    If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

        Parameters
        ----------
        step_id : int
            The ID of the Step to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted step, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoStep
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.steps.getstep(
            step_id=1,
        )
        """
        _response = self._raw_client.getstep(
            step_id, is_include_deleted=is_include_deleted, request_options=request_options
        )
        return _response.data

    def putstep(
        self,
        step_id_: int,
        *,
        config_required: bool,
        implementation_id: str,
        name: str,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        step_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        step_id_ : int
            The step ID of the step to update

        config_required : bool
            Indicates if the step requires configuration values to be provided by the build agent

        implementation_id : str
            The implementation ID used to lookup the step implementation when it is executed

        name : str
            The name of the step

        deleted : typing.Optional[bool]
            Read Only.  Indicates if the record is deleted.

        description : typing.Optional[str]
            A description of the step to be presented to a user

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this step

        step_id : typing.Optional[int]
            The ID of the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.steps.putstep(
            step_id_=1,
            config_required=True,
            implementation_id="ImplementationID",
            name="Name",
        )
        """
        _response = self._raw_client.putstep(
            step_id_,
            config_required=config_required,
            implementation_id=implementation_id,
            name=name,
            deleted=deleted,
            description=description,
            parameters=parameters,
            step_id=step_id,
            request_options=request_options,
        )
        return _response.data


class AsyncStepsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStepsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStepsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStepsClient
        """
        return self._raw_client

    async def getsteps(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoStep:
        """
        Gets a collection of Steps. When successful, the response is a PagedResponse of Steps.
                    If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        include_deleted : typing.Optional[bool]
            Does it include deleted step, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoStep
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.steps.getsteps()


        asyncio.run(main())
        """
        _response = await self._raw_client.getsteps(
            limit=limit, offset=offset, include_deleted=include_deleted, request_options=request_options
        )
        return _response.data

    async def poststep(
        self,
        *,
        config_required: bool,
        implementation_id: str,
        name: str,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        step_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        config_required : bool
            Indicates if the step requires configuration values to be provided by the build agent

        implementation_id : str
            The implementation ID used to lookup the step implementation when it is executed

        name : str
            The name of the step

        deleted : typing.Optional[bool]
            Read Only.  Indicates if the record is deleted.

        description : typing.Optional[str]
            A description of the step to be presented to a user

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this step

        step_id : typing.Optional[int]
            The ID of the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.steps.poststep(
                config_required=True,
                implementation_id="ImplementationID",
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.poststep(
            config_required=config_required,
            implementation_id=implementation_id,
            name=name,
            deleted=deleted,
            description=description,
            parameters=parameters,
            step_id=step_id,
            request_options=request_options,
        )
        return _response.data

    async def getstep(
        self,
        step_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildSystemSharedDtoStep:
        """
        Gets a Step by ID. When successful, the response is the requested Step.
                    If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

        Parameters
        ----------
        step_id : int
            The ID of the Step to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted step, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoStep
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.steps.getstep(
                step_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getstep(
            step_id, is_include_deleted=is_include_deleted, request_options=request_options
        )
        return _response.data

    async def putstep(
        self,
        step_id_: int,
        *,
        config_required: bool,
        implementation_id: str,
        name: str,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        step_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        step_id_ : int
            The step ID of the step to update

        config_required : bool
            Indicates if the step requires configuration values to be provided by the build agent

        implementation_id : str
            The implementation ID used to lookup the step implementation when it is executed

        name : str
            The name of the step

        deleted : typing.Optional[bool]
            Read Only.  Indicates if the record is deleted.

        description : typing.Optional[str]
            A description of the step to be presented to a user

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this step

        step_id : typing.Optional[int]
            The ID of the step

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
            await client.steps.putstep(
                step_id_=1,
                config_required=True,
                implementation_id="ImplementationID",
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putstep(
            step_id_,
            config_required=config_required,
            implementation_id=implementation_id,
            name=name,
            deleted=deleted,
            description=description,
            parameters=parameters,
            step_id=step_id,
            request_options=request_options,
        )
        return _response.data
