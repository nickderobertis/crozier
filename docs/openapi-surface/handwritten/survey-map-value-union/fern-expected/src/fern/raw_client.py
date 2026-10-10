

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.submit_response_request_answers import SubmitResponseRequestAnswers
from .types.submit_response_request_metadata import SubmitResponseRequestMetadata
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def submit_response(
        self,
        *,
        answers: SubmitResponseRequestAnswers,
        respondent: typing.Optional[str] = OMIT,
        metadata: typing.Optional[SubmitResponseRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        answers : SubmitResponseRequestAnswers

        respondent : typing.Optional[str]

        metadata : typing.Optional[SubmitResponseRequestMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "responses",
            method="POST",
            json={
                "respondent": respondent,
                "answers": convert_and_respect_annotation_metadata(
                    object_=answers, annotation=SubmitResponseRequestAnswers, direction="write"
                ),
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=SubmitResponseRequestMetadata, direction="write"
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
                return HttpResponse(response=_response, data=None)
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

    async def submit_response(
        self,
        *,
        answers: SubmitResponseRequestAnswers,
        respondent: typing.Optional[str] = OMIT,
        metadata: typing.Optional[SubmitResponseRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        answers : SubmitResponseRequestAnswers

        respondent : typing.Optional[str]

        metadata : typing.Optional[SubmitResponseRequestMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "responses",
            method="POST",
            json={
                "respondent": respondent,
                "answers": convert_and_respect_annotation_metadata(
                    object_=answers, annotation=SubmitResponseRequestAnswers, direction="write"
                ),
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=SubmitResponseRequestMetadata, direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
