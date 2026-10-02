

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.procare_message_created import ProcareMessageCreated
from ..types.procare_message_status import ProcareMessageStatus
from ..types.procare_message_task import ProcareMessageTask
from .raw_client import AsyncRawProcareMessagesClient, RawProcareMessagesClient
from .types.create_procare_message_request_type import CreateProcareMessageRequestType
from .types.get_procare_messages_v3request_status import GetProcareMessagesV3RequestStatus


OMIT = typing.cast(typing.Any, ...)


class ProcareMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProcareMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProcareMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProcareMessagesClient
        """
        return self._raw_client

    def get_procare_messages_v3(
        self,
        *,
        status: GetProcareMessagesV3RequestStatus,
        last_n_hours: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProcareMessageTask]:
        """
        Lists incomplete tasks in the global message queue. Tasks are not scoped to a company or school. status=incomplete is required; completed-task history is not available from this operation. last_n_hours defaults to 6 and accepts positive fractional hours. Returns an unpaginated array.

        Parameters
        ----------
        status : GetProcareMessagesV3RequestStatus
            Required queue selection; case-insensitive.

        last_n_hours : typing.Optional[float]
            Look back this many hours; must be greater than zero.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProcareMessageTask]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.procare_messages.get_procare_messages_v3(
            status="incomplete",
        )
        """
        _response = self._raw_client.get_procare_messages_v3(
            status=status, last_n_hours=last_n_hours, request_options=request_options
        )
        return _response.data

    def post_procare_messages_v3(
        self,
        *,
        type: CreateProcareMessageRequestType,
        students_ids: typing.Sequence[str],
        message: str,
        username: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcareMessageCreated:
        """
        Queues office_chat or classroom_chat delivery through the configured message service. Requires authentication but does not take company_id or enforce a company/school scope here. HTTP 202 means the task was accepted, not that delivery has finished. Poll the relative URL in Location for status. Non-2xx upstream responses other than 404 become 502.

        Parameters
        ----------
        type : CreateProcareMessageRequestType
            Case-insensitive; surrounding whitespace is ignored.

        students_ids : typing.Sequence[str]

        message : str

        username : typing.Optional[str]
            Procare username forwarded to the message service; not required by the V3 handler.

        password : typing.Optional[str]
            Procare password forwarded to the message service; not required by the V3 handler.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcareMessageCreated
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.procare_messages.post_procare_messages_v3(
            type="office_chat",
            username="example.user",
            password="<procare-password>",
            students_ids=["33333333-3333-4333-8333-333333333333"],
            message="Example reminder.",
        )
        """
        _response = self._raw_client.post_procare_messages_v3(
            type=type,
            students_ids=students_ids,
            message=message,
            username=username,
            password=password,
            request_options=request_options,
        )
        return _response.data

    def get_procare_messages_task_id_v3(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ProcareMessageStatus]:
        """
        Reads a task in the global queue. No company/school filter is applied. A service-side 404 becomes a JSON 404; other unsuccessful or malformed upstream responses become 502. The bundled service returns HTTP 200 with JSON null for an unknown task; V3 preserves that result.

        Parameters
        ----------
        task_id : str
            Task identifier returned by POST /procare_messages; not required to be a UUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProcareMessageStatus]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.procare_messages.get_procare_messages_task_id_v3(
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_procare_messages_task_id_v3(task_id, request_options=request_options)
        return _response.data


class AsyncProcareMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProcareMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProcareMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProcareMessagesClient
        """
        return self._raw_client

    async def get_procare_messages_v3(
        self,
        *,
        status: GetProcareMessagesV3RequestStatus,
        last_n_hours: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProcareMessageTask]:
        """
        Lists incomplete tasks in the global message queue. Tasks are not scoped to a company or school. status=incomplete is required; completed-task history is not available from this operation. last_n_hours defaults to 6 and accepts positive fractional hours. Returns an unpaginated array.

        Parameters
        ----------
        status : GetProcareMessagesV3RequestStatus
            Required queue selection; case-insensitive.

        last_n_hours : typing.Optional[float]
            Look back this many hours; must be greater than zero.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProcareMessageTask]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.procare_messages.get_procare_messages_v3(
                status="incomplete",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_procare_messages_v3(
            status=status, last_n_hours=last_n_hours, request_options=request_options
        )
        return _response.data

    async def post_procare_messages_v3(
        self,
        *,
        type: CreateProcareMessageRequestType,
        students_ids: typing.Sequence[str],
        message: str,
        username: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcareMessageCreated:
        """
        Queues office_chat or classroom_chat delivery through the configured message service. Requires authentication but does not take company_id or enforce a company/school scope here. HTTP 202 means the task was accepted, not that delivery has finished. Poll the relative URL in Location for status. Non-2xx upstream responses other than 404 become 502.

        Parameters
        ----------
        type : CreateProcareMessageRequestType
            Case-insensitive; surrounding whitespace is ignored.

        students_ids : typing.Sequence[str]

        message : str

        username : typing.Optional[str]
            Procare username forwarded to the message service; not required by the V3 handler.

        password : typing.Optional[str]
            Procare password forwarded to the message service; not required by the V3 handler.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcareMessageCreated
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.procare_messages.post_procare_messages_v3(
                type="office_chat",
                username="example.user",
                password="<procare-password>",
                students_ids=["33333333-3333-4333-8333-333333333333"],
                message="Example reminder.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_procare_messages_v3(
            type=type,
            students_ids=students_ids,
            message=message,
            username=username,
            password=password,
            request_options=request_options,
        )
        return _response.data

    async def get_procare_messages_task_id_v3(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ProcareMessageStatus]:
        """
        Reads a task in the global queue. No company/school filter is applied. A service-side 404 becomes a JSON 404; other unsuccessful or malformed upstream responses become 502. The bundled service returns HTTP 200 with JSON null for an unknown task; V3 preserves that result.

        Parameters
        ----------
        task_id : str
            Task identifier returned by POST /procare_messages; not required to be a UUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProcareMessageStatus]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.procare_messages.get_procare_messages_task_id_v3(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_procare_messages_task_id_v3(task_id, request_options=request_options)
        return _response.data
