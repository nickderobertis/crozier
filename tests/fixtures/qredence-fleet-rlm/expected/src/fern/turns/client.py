

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.skill_selection_request import SkillSelectionRequest
from .raw_client import AsyncRawTurnsClient, RawTurnsClient


OMIT = typing.cast(typing.Any, ...)


class TurnsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTurnsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTurnsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTurnsClient
        """
        return self._raw_client

    def create_turn(
        self,
        session_id: str,
        *,
        idempotency_key: str,
        text: str,
        attachment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        skill_selections: typing.Optional[typing.Sequence[SkillSelectionRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        Stream one Turn, opening claim and preparation inside the SSE generator.

        Parameters
        ----------
        session_id : str

        idempotency_key : str

        text : str

        attachment_ids : typing.Optional[typing.Sequence[str]]

        skill_selections : typing.Optional[typing.Sequence[SkillSelectionRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            AI SDK UI v1 UIMessage SSE stream. It opens immediately with a transient data-status prelude (phase=preparation) that repeats every runtime heartbeat until the Turn is claimed and prepared. Claim or preparation failures no longer change the HTTP status: they project closed error + finish chunks inside the stream, and cancellation projects one abort chunk.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.turns.create_turn(
            session_id="session_id",
            idempotency_key="Idempotency-Key",
            text="text",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.create_turn(
            session_id,
            idempotency_key=idempotency_key,
            text=text,
            attachment_ids=attachment_ids,
            skill_selections=skill_selections,
            request_options=request_options,
        ) as r:
            yield from r.data


class AsyncTurnsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTurnsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTurnsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTurnsClient
        """
        return self._raw_client

    async def create_turn(
        self,
        session_id: str,
        *,
        idempotency_key: str,
        text: str,
        attachment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        skill_selections: typing.Optional[typing.Sequence[SkillSelectionRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        Stream one Turn, opening claim and preparation inside the SSE generator.

        Parameters
        ----------
        session_id : str

        idempotency_key : str

        text : str

        attachment_ids : typing.Optional[typing.Sequence[str]]

        skill_selections : typing.Optional[typing.Sequence[SkillSelectionRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            AI SDK UI v1 UIMessage SSE stream. It opens immediately with a transient data-status prelude (phase=preparation) that repeats every runtime heartbeat until the Turn is claimed and prepared. Claim or preparation failures no longer change the HTTP status: they project closed error + finish chunks inside the stream, and cancellation projects one abort chunk.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.turns.create_turn(
                session_id="session_id",
                idempotency_key="Idempotency-Key",
                text="text",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.create_turn(
            session_id,
            idempotency_key=idempotency_key,
            text=text,
            attachment_ids=attachment_ids,
            skill_selections=skill_selections,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk
