

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawActionsClient, RawActionsClient
from .types.call_action_response import CallActionResponse
from .types.get_action_status_response_item import GetActionStatusResponseItem
from .types.get_actions_response import GetActionsResponse
from .types.set_actions_request_actions_item import SetActionsRequestActionsItem
from .types.set_actions_request_const_value import SetActionsRequestConstValue
from .types.set_actions_response import SetActionsResponse


OMIT = typing.cast(typing.Any, ...)


class ActionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActionsClient
        """
        return self._raw_client

    def get_actions(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetActionsResponse:
        """
        Returns the current actions definition used by the device to trigger HTTP or Modbus requests.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetActionsResponse
            Current actions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.actions.get_actions()
        """
        _response = self._raw_client.get_actions(request_options=request_options)
        return _response.data

    def set_actions(
        self,
        *,
        const: typing.Optional[typing.Dict[str, SetActionsRequestConstValue]] = OMIT,
        actions: typing.Optional[typing.Sequence[SetActionsRequestActionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SetActionsResponse:
        """
        Replaces the actions definition. Large definitions may be rejected.

        Parameters
        ----------
        const : typing.Optional[typing.Dict[str, SetActionsRequestConstValue]]
            Constants for substitution; nulls may be ignored by firmware

        actions : typing.Optional[typing.Sequence[SetActionsRequestActionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetActionsResponse
            Actions saved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.actions.set_actions()
        """
        _response = self._raw_client.set_actions(const=const, actions=actions, request_options=request_options)
        return _response.data

    def delete_actions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the current actions definition.

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.actions.delete_actions()
        """
        _response = self._raw_client.delete_actions(request_options=request_options)
        return _response.data

    def call_action(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> CallActionResponse:
        """
        Queues execution of an action by ID. Returns status IDs to poll.

        Parameters
        ----------
        id : str
            Action ID to execute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CallActionResponse
            Queued for execution

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.actions.call_action(
            id="id",
        )
        """
        _response = self._raw_client.call_action(id=id, request_options=request_options)
        return _response.data

    def get_action_status(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetActionStatusResponseItem]:
        """
        Retrieves execution status by status IDs. Code is HTTP status for HTTP actions

        Parameters
        ----------
        id : str
            Comma-separated list of status IDs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetActionStatusResponseItem]
            Array of status records

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.actions.get_action_status(
            id="id",
        )
        """
        _response = self._raw_client.get_action_status(id=id, request_options=request_options)
        return _response.data


class AsyncActionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActionsClient
        """
        return self._raw_client

    async def get_actions(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetActionsResponse:
        """
        Returns the current actions definition used by the device to trigger HTTP or Modbus requests.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetActionsResponse
            Current actions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.actions.get_actions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_actions(request_options=request_options)
        return _response.data

    async def set_actions(
        self,
        *,
        const: typing.Optional[typing.Dict[str, SetActionsRequestConstValue]] = OMIT,
        actions: typing.Optional[typing.Sequence[SetActionsRequestActionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SetActionsResponse:
        """
        Replaces the actions definition. Large definitions may be rejected.

        Parameters
        ----------
        const : typing.Optional[typing.Dict[str, SetActionsRequestConstValue]]
            Constants for substitution; nulls may be ignored by firmware

        actions : typing.Optional[typing.Sequence[SetActionsRequestActionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetActionsResponse
            Actions saved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.actions.set_actions()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_actions(const=const, actions=actions, request_options=request_options)
        return _response.data

    async def delete_actions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the current actions definition.

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.actions.delete_actions()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_actions(request_options=request_options)
        return _response.data

    async def call_action(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CallActionResponse:
        """
        Queues execution of an action by ID. Returns status IDs to poll.

        Parameters
        ----------
        id : str
            Action ID to execute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CallActionResponse
            Queued for execution

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.actions.call_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.call_action(id=id, request_options=request_options)
        return _response.data

    async def get_action_status(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetActionStatusResponseItem]:
        """
        Retrieves execution status by status IDs. Code is HTTP status for HTTP actions

        Parameters
        ----------
        id : str
            Comma-separated list of status IDs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetActionStatusResponseItem]
            Array of status records

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.actions.get_action_status(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_action_status(id=id, request_options=request_options)
        return _response.data
