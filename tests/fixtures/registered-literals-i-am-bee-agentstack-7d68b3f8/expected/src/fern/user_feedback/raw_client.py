

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.paginated_result_user_feedback_response import PaginatedResultUserFeedbackResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserFeedbackClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_user_feedback(
        self,
        *,
        provider_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        after_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedResultUserFeedbackResponse]:
        """
        Parameters
        ----------
        provider_id : typing.Optional[str]

        limit : typing.Optional[int]

        after_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedResultUserFeedbackResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/user_feedback",
            method="GET",
            params={
                "provider_id": provider_id,
                "limit": limit,
                "after_cursor": after_cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultUserFeedbackResponse,
                    parse_obj_as(
                        type_=PaginatedResultUserFeedbackResponse,
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

    def user_feedback(
        self,
        *,
        provider_id: str,
        task_id: str,
        context_id: str,
        rating: int,
        message: str,
        comment_tags: typing.Optional[typing.Sequence[str]] = OMIT,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        provider_id : str

        task_id : str

        context_id : str

        rating : int
            Rating thats either 1 or -1

        message : str

        comment_tags : typing.Optional[typing.Sequence[str]]

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/user_feedback",
            method="POST",
            json={
                "provider_id": provider_id,
                "task_id": task_id,
                "context_id": context_id,
                "rating": rating,
                "message": message,
                "comment_tags": comment_tags,
                "comment": comment,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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


class AsyncRawUserFeedbackClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_user_feedback(
        self,
        *,
        provider_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        after_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedResultUserFeedbackResponse]:
        """
        Parameters
        ----------
        provider_id : typing.Optional[str]

        limit : typing.Optional[int]

        after_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedResultUserFeedbackResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/user_feedback",
            method="GET",
            params={
                "provider_id": provider_id,
                "limit": limit,
                "after_cursor": after_cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultUserFeedbackResponse,
                    parse_obj_as(
                        type_=PaginatedResultUserFeedbackResponse,
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

    async def user_feedback(
        self,
        *,
        provider_id: str,
        task_id: str,
        context_id: str,
        rating: int,
        message: str,
        comment_tags: typing.Optional[typing.Sequence[str]] = OMIT,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        provider_id : str

        task_id : str

        context_id : str

        rating : int
            Rating thats either 1 or -1

        message : str

        comment_tags : typing.Optional[typing.Sequence[str]]

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/user_feedback",
            method="POST",
            json={
                "provider_id": provider_id,
                "task_id": task_id,
                "context_id": context_id,
                "rating": rating,
                "message": message,
                "comment_tags": comment_tags,
                "comment": comment,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
