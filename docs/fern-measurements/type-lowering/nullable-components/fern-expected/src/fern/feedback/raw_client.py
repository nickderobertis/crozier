

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.feedback_query import FeedbackQuery
from ..types.feedback_settings import FeedbackSettings
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFeedbackClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def send_feedback(
        self,
        *,
        queries: typing.Sequence[FeedbackQuery],
        primary: typing.Optional[FeedbackQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedbackSettings]:
        """
        Parameters
        ----------
        queries : typing.Sequence[FeedbackQuery]

        primary : typing.Optional[FeedbackQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedbackSettings]
            Accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            "feedback",
            method="POST",
            json={
                "queries": convert_and_respect_annotation_metadata(
                    object_=queries, annotation=typing.Sequence[FeedbackQuery], direction="write"
                ),
                "primary": convert_and_respect_annotation_metadata(
                    object_=primary, annotation=FeedbackQuery, direction="write"
                ),
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
                    FeedbackSettings,
                    parse_obj_as(
                        type_=FeedbackSettings,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFeedbackClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def send_feedback(
        self,
        *,
        queries: typing.Sequence[FeedbackQuery],
        primary: typing.Optional[FeedbackQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedbackSettings]:
        """
        Parameters
        ----------
        queries : typing.Sequence[FeedbackQuery]

        primary : typing.Optional[FeedbackQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedbackSettings]
            Accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "feedback",
            method="POST",
            json={
                "queries": convert_and_respect_annotation_metadata(
                    object_=queries, annotation=typing.Sequence[FeedbackQuery], direction="write"
                ),
                "primary": convert_and_respect_annotation_metadata(
                    object_=primary, annotation=FeedbackQuery, direction="write"
                ),
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
                    FeedbackSettings,
                    parse_obj_as(
                        type_=FeedbackSettings,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
