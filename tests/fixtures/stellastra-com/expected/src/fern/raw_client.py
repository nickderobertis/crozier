

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .errors.bad_request_error import BadRequestError
from .errors.forbidden_error import ForbiddenError
from .errors.unauthorized_error import UnauthorizedError
from .types.bad_request_error_body import BadRequestErrorBody
from .types.forbidden_error_body import ForbiddenErrorBody
from .types.post_post_review_response import PostPostReviewResponse
from .types.unauthorized_error_body import UnauthorizedErrorBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def posts_the_users_review_to_stellastra(
        self,
        *,
        user_email: str,
        rating: int,
        post_post_review_request_rating: int,
        post_post_review_request_user_email: str,
        user_name: typing.Optional[str] = None,
        post_post_review_request_user_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPostReviewResponse]:
        """
        Parameters
        ----------
        user_email : str
            User's email to which the review verification will be sent.

        rating : int
            The user's star rating, must be a single integer from [1, 2, 3, 4, 5]

        post_post_review_request_rating : int

        post_post_review_request_user_email : str

        user_name : typing.Optional[str]
            The user's name, defaults to empty string "".  Thus, if this is omitted, the email to the user will not use the user's name.

        post_post_review_request_user_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPostReviewResponse]
            A response code of 200 means the request was succesful, and the user has been sent an email confirming their review.
        """
        _response = self._client_wrapper.httpx_client.request(
            "post-review",
            method="POST",
            params={
                "user_email": user_email,
                "user_name": user_name,
                "rating": rating,
            },
            json={
                "rating": post_post_review_request_rating,
                "user_email": post_post_review_request_user_email,
                "user_name": post_post_review_request_user_name,
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
                    PostPostReviewResponse,
                    parse_obj_as(
                        type_=PostPostReviewResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def posts_the_users_review_to_stellastra(
        self,
        *,
        user_email: str,
        rating: int,
        post_post_review_request_rating: int,
        post_post_review_request_user_email: str,
        user_name: typing.Optional[str] = None,
        post_post_review_request_user_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPostReviewResponse]:
        """
        Parameters
        ----------
        user_email : str
            User's email to which the review verification will be sent.

        rating : int
            The user's star rating, must be a single integer from [1, 2, 3, 4, 5]

        post_post_review_request_rating : int

        post_post_review_request_user_email : str

        user_name : typing.Optional[str]
            The user's name, defaults to empty string "".  Thus, if this is omitted, the email to the user will not use the user's name.

        post_post_review_request_user_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPostReviewResponse]
            A response code of 200 means the request was succesful, and the user has been sent an email confirming their review.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "post-review",
            method="POST",
            params={
                "user_email": user_email,
                "user_name": user_name,
                "rating": rating,
            },
            json={
                "rating": post_post_review_request_rating,
                "user_email": post_post_review_request_user_email,
                "user_name": post_post_review_request_user_name,
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
                    PostPostReviewResponse,
                    parse_obj_as(
                        type_=PostPostReviewResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
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
