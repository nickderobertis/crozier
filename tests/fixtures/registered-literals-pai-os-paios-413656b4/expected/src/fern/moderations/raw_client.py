

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.create_moderation_response import CreateModerationResponse
from .types.create_moderation_request_input import CreateModerationRequestInput
from .types.create_moderation_request_model import CreateModerationRequestModel
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawModerationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_moderation(
        self,
        *,
        input: CreateModerationRequestInput,
        model: typing.Optional[CreateModerationRequestModel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateModerationResponse]:
        """
        Parameters
        ----------
        input : CreateModerationRequestInput
            The input text to classify

        model : typing.Optional[CreateModerationRequestModel]
            Two content moderations models are available: `text-moderation-stable` and `text-moderation-latest`.

            The default is `text-moderation-latest` which will be automatically upgraded over time. This ensures you are always using our most accurate model. If you use `text-moderation-stable`, we will provide advanced notice before updating the model. Accuracy of `text-moderation-stable` may be slightly lower than for `text-moderation-latest`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateModerationResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "moderations",
            method="POST",
            json={
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=CreateModerationRequestInput, direction="write"
                ),
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=CreateModerationRequestModel, direction="write"
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
                    CreateModerationResponse,
                    parse_obj_as(
                        type_=CreateModerationResponse,
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


class AsyncRawModerationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_moderation(
        self,
        *,
        input: CreateModerationRequestInput,
        model: typing.Optional[CreateModerationRequestModel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateModerationResponse]:
        """
        Parameters
        ----------
        input : CreateModerationRequestInput
            The input text to classify

        model : typing.Optional[CreateModerationRequestModel]
            Two content moderations models are available: `text-moderation-stable` and `text-moderation-latest`.

            The default is `text-moderation-latest` which will be automatically upgraded over time. This ensures you are always using our most accurate model. If you use `text-moderation-stable`, we will provide advanced notice before updating the model. Accuracy of `text-moderation-stable` may be slightly lower than for `text-moderation-latest`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateModerationResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "moderations",
            method="POST",
            json={
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=CreateModerationRequestInput, direction="write"
                ),
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=CreateModerationRequestModel, direction="write"
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
                    CreateModerationResponse,
                    parse_obj_as(
                        type_=CreateModerationResponse,
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
