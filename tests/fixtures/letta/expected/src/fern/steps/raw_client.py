

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.feedback_type import FeedbackType
from ..types.http_validation_error import HttpValidationError
from ..types.provider_trace import ProviderTrace
from ..types.step import Step
from ..types.step_metrics import StepMetrics
from .types.list_messages_for_step_request_order import ListMessagesForStepRequestOrder
from .types.list_messages_for_step_request_order_by import ListMessagesForStepRequestOrderBy
from .types.list_messages_for_step_response_item import ListMessagesForStepResponseItem
from .types.list_steps_request_feedback import ListStepsRequestFeedback
from .types.list_steps_request_order import ListStepsRequestOrder
from .types.list_steps_request_order_by import ListStepsRequestOrderBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStepsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_steps(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListStepsRequestOrder] = None,
        order_by: typing.Optional[ListStepsRequestOrderBy] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        trace_ids: typing.Optional[typing.Sequence[str]] = None,
        feedback: typing.Optional[ListStepsRequestFeedback] = None,
        has_feedback: typing.Optional[bool] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        project_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Step]]:
        """
        List steps with optional pagination and date filters.

        Parameters
        ----------
        before : typing.Optional[str]
            Return steps before this step ID

        after : typing.Optional[str]
            Return steps after this step ID

        limit : typing.Optional[int]
            Maximum number of steps to return

        order : typing.Optional[ListStepsRequestOrder]
            Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListStepsRequestOrderBy]
            Field to sort by

        start_date : typing.Optional[str]
            Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        end_date : typing.Optional[str]
            Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        model : typing.Optional[str]
            Filter by the name of the model used for the step

        agent_id : typing.Optional[str]
            Filter by the ID of the agent that performed the step

        trace_ids : typing.Optional[typing.Sequence[str]]
            Filter by trace ids returned by the server

        feedback : typing.Optional[ListStepsRequestFeedback]
            Filter by feedback

        has_feedback : typing.Optional[bool]
            Filter by whether steps have feedback (true) or not (false)

        tags : typing.Optional[typing.Sequence[str]]
            Filter by tags

        project_id : typing.Optional[str]
            Filter by the project ID that is associated with the step (cloud only).

        project : typing.Optional[str]
            Filter by project slug to associate with the group (cloud only).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Step]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/steps/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "start_date": start_date,
                "end_date": end_date,
                "model": model,
                "agent_id": agent_id,
                "trace_ids": trace_ids,
                "feedback": feedback,
                "has_feedback": has_feedback,
                "tags": tags,
                "project_id": project_id,
            },
            headers={
                "X-Project": str(project) if project is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Step],
                    parse_obj_as(
                        type_=typing.List[Step],
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

    def retrieve_step(
        self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Step]:
        """
        Get a step by ID.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Step]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/steps/{encode_path_param(step_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Step,
                    parse_obj_as(
                        type_=Step,
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

    def retrieve_metrics_for_step(
        self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StepMetrics]:
        """
        Get step metrics by step ID.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StepMetrics]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/steps/{encode_path_param(step_id)}/metrics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StepMetrics,
                    parse_obj_as(
                        type_=StepMetrics,
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

    def retrieve_trace_for_step(
        self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[ProviderTrace]]:
        """
        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[ProviderTrace]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/steps/{encode_path_param(step_id)}/trace",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ProviderTrace],
                    parse_obj_as(
                        type_=typing.Optional[ProviderTrace],
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

    def modify_feedback_for_step(
        self,
        step_id: str,
        *,
        feedback: typing.Optional[FeedbackType] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Step]:
        """
        Modify feedback for a given step.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        feedback : typing.Optional[FeedbackType]
            Whether this feedback is positive or negative

        tags : typing.Optional[typing.Sequence[str]]
            Feedback tags to add to the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Step]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/steps/{encode_path_param(step_id)}/feedback",
            method="PATCH",
            json={
                "feedback": feedback,
                "tags": tags,
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
                    Step,
                    parse_obj_as(
                        type_=Step,
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

    def list_messages_for_step(
        self,
        step_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForStepRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForStepRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ListMessagesForStepResponseItem]]:
        """
        List messages for a given step.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForStepRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForStepRequestOrderBy]
            Sort by field

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ListMessagesForStepResponseItem]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/steps/{encode_path_param(step_id)}/messages",
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
                    typing.List[ListMessagesForStepResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListMessagesForStepResponseItem],
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


class AsyncRawStepsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_steps(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListStepsRequestOrder] = None,
        order_by: typing.Optional[ListStepsRequestOrderBy] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        trace_ids: typing.Optional[typing.Sequence[str]] = None,
        feedback: typing.Optional[ListStepsRequestFeedback] = None,
        has_feedback: typing.Optional[bool] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        project_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Step]]:
        """
        List steps with optional pagination and date filters.

        Parameters
        ----------
        before : typing.Optional[str]
            Return steps before this step ID

        after : typing.Optional[str]
            Return steps after this step ID

        limit : typing.Optional[int]
            Maximum number of steps to return

        order : typing.Optional[ListStepsRequestOrder]
            Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListStepsRequestOrderBy]
            Field to sort by

        start_date : typing.Optional[str]
            Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        end_date : typing.Optional[str]
            Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        model : typing.Optional[str]
            Filter by the name of the model used for the step

        agent_id : typing.Optional[str]
            Filter by the ID of the agent that performed the step

        trace_ids : typing.Optional[typing.Sequence[str]]
            Filter by trace ids returned by the server

        feedback : typing.Optional[ListStepsRequestFeedback]
            Filter by feedback

        has_feedback : typing.Optional[bool]
            Filter by whether steps have feedback (true) or not (false)

        tags : typing.Optional[typing.Sequence[str]]
            Filter by tags

        project_id : typing.Optional[str]
            Filter by the project ID that is associated with the step (cloud only).

        project : typing.Optional[str]
            Filter by project slug to associate with the group (cloud only).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Step]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/steps/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "start_date": start_date,
                "end_date": end_date,
                "model": model,
                "agent_id": agent_id,
                "trace_ids": trace_ids,
                "feedback": feedback,
                "has_feedback": has_feedback,
                "tags": tags,
                "project_id": project_id,
            },
            headers={
                "X-Project": str(project) if project is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Step],
                    parse_obj_as(
                        type_=typing.List[Step],
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

    async def retrieve_step(
        self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Step]:
        """
        Get a step by ID.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Step]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/steps/{encode_path_param(step_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Step,
                    parse_obj_as(
                        type_=Step,
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

    async def retrieve_metrics_for_step(
        self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StepMetrics]:
        """
        Get step metrics by step ID.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StepMetrics]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/steps/{encode_path_param(step_id)}/metrics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StepMetrics,
                    parse_obj_as(
                        type_=StepMetrics,
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

    async def retrieve_trace_for_step(
        self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[ProviderTrace]]:
        """
        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[ProviderTrace]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/steps/{encode_path_param(step_id)}/trace",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ProviderTrace],
                    parse_obj_as(
                        type_=typing.Optional[ProviderTrace],
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

    async def modify_feedback_for_step(
        self,
        step_id: str,
        *,
        feedback: typing.Optional[FeedbackType] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Step]:
        """
        Modify feedback for a given step.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        feedback : typing.Optional[FeedbackType]
            Whether this feedback is positive or negative

        tags : typing.Optional[typing.Sequence[str]]
            Feedback tags to add to the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Step]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/steps/{encode_path_param(step_id)}/feedback",
            method="PATCH",
            json={
                "feedback": feedback,
                "tags": tags,
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
                    Step,
                    parse_obj_as(
                        type_=Step,
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

    async def list_messages_for_step(
        self,
        step_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForStepRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForStepRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ListMessagesForStepResponseItem]]:
        """
        List messages for a given step.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForStepRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForStepRequestOrderBy]
            Sort by field

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ListMessagesForStepResponseItem]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/steps/{encode_path_param(step_id)}/messages",
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
                    typing.List[ListMessagesForStepResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListMessagesForStepResponseItem],
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
