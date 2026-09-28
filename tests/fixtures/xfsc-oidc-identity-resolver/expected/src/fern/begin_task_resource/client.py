

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.any_type import AnyType
from ..types.begin_response import BeginResponse
from .raw_client import AsyncRawBeginTaskResourceClient, RawBeginTaskResourceClient


OMIT = typing.cast(typing.Any, ...)


class BeginTaskResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBeginTaskResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBeginTaskResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBeginTaskResourceClient
        """
        return self._raw_client

    def post_session(
        self,
        *,
        failure: str,
        profile_id: str,
        success: str,
        task_name: str,
        request: AnyType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BeginResponse:
        """
        Parameters
        ----------
        failure : str

        profile_id : str

        success : str

        task_name : str

        request : AnyType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BeginResponse
            A redirect and a cancel URL.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.begin_task_resource.post_session(
            failure="failure",
            profile_id="profileId",
            success="success",
            task_name="taskName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_session(
            failure=failure,
            profile_id=profile_id,
            success=success,
            task_name=task_name,
            request=request,
            request_options=request_options,
        )
        return _response.data


class AsyncBeginTaskResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBeginTaskResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBeginTaskResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBeginTaskResourceClient
        """
        return self._raw_client

    async def post_session(
        self,
        *,
        failure: str,
        profile_id: str,
        success: str,
        task_name: str,
        request: AnyType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BeginResponse:
        """
        Parameters
        ----------
        failure : str

        profile_id : str

        success : str

        task_name : str

        request : AnyType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BeginResponse
            A redirect and a cancel URL.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.begin_task_resource.post_session(
                failure="failure",
                profile_id="profileId",
                success="success",
                task_name="taskName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_session(
            failure=failure,
            profile_id=profile_id,
            success=success,
            task_name=task_name,
            request=request,
            request_options=request_options,
        )
        return _response.data
