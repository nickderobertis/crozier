

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.action_result import ActionResult
from .raw_client import AsyncRawActionsClient, RawActionsClient


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

    def run_action(
        self,
        *,
        action: str,
        kiln_token: typing.Optional[str] = None,
        run_action_request_kiln_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionResult:
        """
        Parameters
        ----------
        action : str

        kiln_token : typing.Optional[str]

        run_action_request_kiln_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionResult
            Ran.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.actions.run_action(
            action="action",
        )
        """
        _response = self._raw_client.run_action(
            action=action,
            kiln_token=kiln_token,
            run_action_request_kiln_token=run_action_request_kiln_token,
            request_options=request_options,
        )
        return _response.data

    def queue_action(
        self,
        *,
        batch_label: str,
        action: str,
        queue_action_request_batch_label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionResult:
        """
        Parameters
        ----------
        batch_label : str

        action : str

        queue_action_request_batch_label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionResult
            Queued.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.actions.queue_action(
            batch_label="batchLabel",
            action="action",
        )
        """
        _response = self._raw_client.queue_action(
            batch_label=batch_label,
            action=action,
            queue_action_request_batch_label=queue_action_request_batch_label,
            request_options=request_options,
        )
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

    async def run_action(
        self,
        *,
        action: str,
        kiln_token: typing.Optional[str] = None,
        run_action_request_kiln_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionResult:
        """
        Parameters
        ----------
        action : str

        kiln_token : typing.Optional[str]

        run_action_request_kiln_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionResult
            Ran.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.actions.run_action(
                action="action",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_action(
            action=action,
            kiln_token=kiln_token,
            run_action_request_kiln_token=run_action_request_kiln_token,
            request_options=request_options,
        )
        return _response.data

    async def queue_action(
        self,
        *,
        batch_label: str,
        action: str,
        queue_action_request_batch_label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionResult:
        """
        Parameters
        ----------
        batch_label : str

        action : str

        queue_action_request_batch_label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionResult
            Queued.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.actions.queue_action(
                batch_label="batchLabel",
                action="action",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.queue_action(
            batch_label=batch_label,
            action=action,
            queue_action_request_batch_label=queue_action_request_batch_label,
            request_options=request_options,
        )
        return _response.data
