

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.feedback import Feedback
from ..types.seldon_message import SeldonMessage
from ..types.seldon_message_list import SeldonMessageList
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def aggregate(
        self, *, body: SeldonMessageList, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        body : SeldonMessageList

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "aggregate",
            method="GET",
            params={
                "body": convert_and_respect_annotation_metadata(
                    object_=body, annotation=SeldonMessageList, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def aggregate2(
        self,
        *,
        json: typing.Optional[SeldonMessageList] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessageList]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "aggregate",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessageList, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def transform_input4(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "predict",
            method="GET",
            params={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def transform_input3(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "predict",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def route2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "route",
            method="GET",
            params={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def route(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "route",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def send_feedback2(
        self, *, json: Feedback, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : Feedback

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "send-feedback",
            method="GET",
            params={
                "json": convert_and_respect_annotation_metadata(object_=json, annotation=Feedback, direction="write"),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def send_feedback(
        self, *, json: typing.Optional[Feedback] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[Feedback]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "send-feedback",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(object_=json, annotation=Feedback, direction="write"),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def transform_input2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "transform-input",
            method="GET",
            params={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def transform_input(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "transform-input",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def transform_output2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "transform-output",
            method="GET",
            params={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    def transform_output(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeldonMessage]
            A successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "transform-output",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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


class AsyncRawInternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def aggregate(
        self, *, body: SeldonMessageList, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        body : SeldonMessageList

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "aggregate",
            method="GET",
            params={
                "body": convert_and_respect_annotation_metadata(
                    object_=body, annotation=SeldonMessageList, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def aggregate2(
        self,
        *,
        json: typing.Optional[SeldonMessageList] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessageList]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "aggregate",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessageList, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def transform_input4(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "predict",
            method="GET",
            params={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def transform_input3(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "predict",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def route2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "route",
            method="GET",
            params={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def route(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "route",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def send_feedback2(
        self, *, json: Feedback, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : Feedback

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "send-feedback",
            method="GET",
            params={
                "json": convert_and_respect_annotation_metadata(object_=json, annotation=Feedback, direction="write"),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def send_feedback(
        self, *, json: typing.Optional[Feedback] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[Feedback]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "send-feedback",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(object_=json, annotation=Feedback, direction="write"),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def transform_input2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transform-input",
            method="GET",
            params={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def transform_input(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transform-input",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def transform_output2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transform-output",
            method="GET",
            params={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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

    async def transform_output(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeldonMessage]:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeldonMessage]
            A successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transform-output",
            method="POST",
            data={
                "json": convert_and_respect_annotation_metadata(
                    object_=json, annotation=SeldonMessage, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeldonMessage,
                    parse_obj_as(
                        type_=SeldonMessage,
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
