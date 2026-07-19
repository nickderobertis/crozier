

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.batch_job import BatchJob
from ..types.http_validation_error import HttpValidationError
from ..types.letta_batch_messages import LettaBatchMessages
from ..types.letta_batch_request import LettaBatchRequest
from ..types.letta_message_union import LettaMessageUnion
from .types.list_all_messages_request_order import ListAllMessagesRequestOrder
from .types.list_batches_request_order import ListBatchesRequestOrder
from .types.list_batches_request_order_by import ListBatchesRequestOrderBy
from .types.list_messages_for_batch_request_order import ListMessagesForBatchRequestOrder
from .types.list_messages_for_batch_request_order_by import ListMessagesForBatchRequestOrderBy
from .types.search_all_messages_request_search_mode import SearchAllMessagesRequestSearchMode
from .types.search_all_messages_response_item import SearchAllMessagesResponseItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_messages(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAllMessagesRequestOrder] = None,
        conversation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[LettaMessageUnion]]:
        """
        List messages across all agents for the current user.

        Parameters
        ----------
        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListAllMessagesRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        conversation_id : typing.Optional[str]
            Conversation ID to filter messages by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LettaMessageUnion]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/messages/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "conversation_id": conversation_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LettaMessageUnion],
                    parse_obj_as(
                        type_=typing.List[LettaMessageUnion],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_all_messages(
        self,
        *,
        query: str,
        search_mode: typing.Optional[SearchAllMessagesRequestSearchMode] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        conversation_id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[SearchAllMessagesResponseItem]]:
        """
        Search messages across the organization with optional agent filtering.
        Returns messages with FTS/vector ranks and total RRF score.

        This is a cloud-only feature.

        Parameters
        ----------
        query : str
            Text query for full-text search

        search_mode : typing.Optional[SearchAllMessagesRequestSearchMode]
            Search mode to use

        agent_id : typing.Optional[str]
            Filter messages by agent ID

        conversation_id : typing.Optional[str]
            Filter messages by conversation ID

        limit : typing.Optional[int]
            Maximum number of results to return

        start_date : typing.Optional[dt.datetime]
            Filter messages created after this date

        end_date : typing.Optional[dt.datetime]
            Filter messages created on or before this date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SearchAllMessagesResponseItem]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/messages/search",
            method="POST",
            json={
                "query": query,
                "search_mode": search_mode,
                "agent_id": agent_id,
                "conversation_id": conversation_id,
                "limit": limit,
                "start_date": start_date,
                "end_date": end_date,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SearchAllMessagesResponseItem],
                    parse_obj_as(
                        type_=typing.List[SearchAllMessagesResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_batches(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListBatchesRequestOrder] = None,
        order_by: typing.Optional[ListBatchesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[BatchJob]]:
        """
        List all batch runs.

        Parameters
        ----------
        before : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come before this job ID in the specified sort order

        after : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come after this job ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of jobs to return

        order : typing.Optional[ListBatchesRequestOrder]
            Sort order for jobs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListBatchesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[BatchJob]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/messages/batches",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BatchJob],
                    parse_obj_as(
                        type_=typing.List[BatchJob],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_batch(
        self,
        *,
        requests: typing.Sequence[LettaBatchRequest],
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchJob]:
        """
        Submit a batch of agent runs for asynchronous processing.

        Creates a job that will fan out messages to all listed agents and process them in parallel.
        The request will be rejected if it exceeds 256MB.

        Parameters
        ----------
        requests : typing.Sequence[LettaBatchRequest]
            List of requests to be processed in batch.

        callback_url : typing.Optional[str]
            Optional URL to call via POST when the batch completes. The callback payload will be a JSON object with the following fields: {'job_id': string, 'status': string, 'completed_at': string}. Where 'job_id' is the unique batch job identifier, 'status' is the final batch status (e.g., 'completed', 'failed'), and 'completed_at' is an ISO 8601 timestamp indicating when the batch job completed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchJob]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/messages/batches",
            method="POST",
            json={
                "requests": convert_and_respect_annotation_metadata(
                    object_=requests, annotation=typing.Sequence[LettaBatchRequest], direction="write"
                ),
                "callback_url": callback_url,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchJob,
                    parse_obj_as(
                        type_=BatchJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_batch(
        self, batch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BatchJob]:
        """
        Retrieve the status and details of a batch run.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchJob]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/messages/batches/{encode_path_param(batch_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchJob,
                    parse_obj_as(
                        type_=BatchJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_messages_for_batch(
        self,
        batch_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForBatchRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForBatchRequestOrderBy] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LettaBatchMessages]:
        """
        Get response messages for a specific batch job.

        Parameters
        ----------
        batch_id : str

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForBatchRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForBatchRequestOrderBy]
            Field to sort by

        agent_id : typing.Optional[str]
            Filter messages by agent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LettaBatchMessages]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/messages/batches/{encode_path_param(batch_id)}/messages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "agent_id": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LettaBatchMessages,
                    parse_obj_as(
                        type_=LettaBatchMessages,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_batch(
        self, batch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Cancel a batch run.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/messages/batches/{encode_path_param(batch_id)}/cancel",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_message(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[LettaMessageUnion]]:
        """
        Retrieve a message by ID.

        Parameters
        ----------
        message_id : str
            The ID of the message in the format 'message-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LettaMessageUnion]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LettaMessageUnion],
                    parse_obj_as(
                        type_=typing.List[LettaMessageUnion],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_messages(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAllMessagesRequestOrder] = None,
        conversation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[LettaMessageUnion]]:
        """
        List messages across all agents for the current user.

        Parameters
        ----------
        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListAllMessagesRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        conversation_id : typing.Optional[str]
            Conversation ID to filter messages by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LettaMessageUnion]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/messages/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "conversation_id": conversation_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LettaMessageUnion],
                    parse_obj_as(
                        type_=typing.List[LettaMessageUnion],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_all_messages(
        self,
        *,
        query: str,
        search_mode: typing.Optional[SearchAllMessagesRequestSearchMode] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        conversation_id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[SearchAllMessagesResponseItem]]:
        """
        Search messages across the organization with optional agent filtering.
        Returns messages with FTS/vector ranks and total RRF score.

        This is a cloud-only feature.

        Parameters
        ----------
        query : str
            Text query for full-text search

        search_mode : typing.Optional[SearchAllMessagesRequestSearchMode]
            Search mode to use

        agent_id : typing.Optional[str]
            Filter messages by agent ID

        conversation_id : typing.Optional[str]
            Filter messages by conversation ID

        limit : typing.Optional[int]
            Maximum number of results to return

        start_date : typing.Optional[dt.datetime]
            Filter messages created after this date

        end_date : typing.Optional[dt.datetime]
            Filter messages created on or before this date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SearchAllMessagesResponseItem]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/messages/search",
            method="POST",
            json={
                "query": query,
                "search_mode": search_mode,
                "agent_id": agent_id,
                "conversation_id": conversation_id,
                "limit": limit,
                "start_date": start_date,
                "end_date": end_date,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SearchAllMessagesResponseItem],
                    parse_obj_as(
                        type_=typing.List[SearchAllMessagesResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_batches(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListBatchesRequestOrder] = None,
        order_by: typing.Optional[ListBatchesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[BatchJob]]:
        """
        List all batch runs.

        Parameters
        ----------
        before : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come before this job ID in the specified sort order

        after : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come after this job ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of jobs to return

        order : typing.Optional[ListBatchesRequestOrder]
            Sort order for jobs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListBatchesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[BatchJob]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/messages/batches",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BatchJob],
                    parse_obj_as(
                        type_=typing.List[BatchJob],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_batch(
        self,
        *,
        requests: typing.Sequence[LettaBatchRequest],
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchJob]:
        """
        Submit a batch of agent runs for asynchronous processing.

        Creates a job that will fan out messages to all listed agents and process them in parallel.
        The request will be rejected if it exceeds 256MB.

        Parameters
        ----------
        requests : typing.Sequence[LettaBatchRequest]
            List of requests to be processed in batch.

        callback_url : typing.Optional[str]
            Optional URL to call via POST when the batch completes. The callback payload will be a JSON object with the following fields: {'job_id': string, 'status': string, 'completed_at': string}. Where 'job_id' is the unique batch job identifier, 'status' is the final batch status (e.g., 'completed', 'failed'), and 'completed_at' is an ISO 8601 timestamp indicating when the batch job completed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchJob]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/messages/batches",
            method="POST",
            json={
                "requests": convert_and_respect_annotation_metadata(
                    object_=requests, annotation=typing.Sequence[LettaBatchRequest], direction="write"
                ),
                "callback_url": callback_url,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchJob,
                    parse_obj_as(
                        type_=BatchJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_batch(
        self, batch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BatchJob]:
        """
        Retrieve the status and details of a batch run.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchJob]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/messages/batches/{encode_path_param(batch_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchJob,
                    parse_obj_as(
                        type_=BatchJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_messages_for_batch(
        self,
        batch_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForBatchRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForBatchRequestOrderBy] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LettaBatchMessages]:
        """
        Get response messages for a specific batch job.

        Parameters
        ----------
        batch_id : str

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForBatchRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForBatchRequestOrderBy]
            Field to sort by

        agent_id : typing.Optional[str]
            Filter messages by agent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LettaBatchMessages]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/messages/batches/{encode_path_param(batch_id)}/messages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "agent_id": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LettaBatchMessages,
                    parse_obj_as(
                        type_=LettaBatchMessages,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_batch(
        self, batch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Cancel a batch run.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/messages/batches/{encode_path_param(batch_id)}/cancel",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_message(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[LettaMessageUnion]]:
        """
        Retrieve a message by ID.

        Parameters
        ----------
        message_id : str
            The ID of the message in the format 'message-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LettaMessageUnion]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LettaMessageUnion],
                    parse_obj_as(
                        type_=typing.List[LettaMessageUnion],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
