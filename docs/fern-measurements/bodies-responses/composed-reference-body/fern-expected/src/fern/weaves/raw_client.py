

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
from ..types.knot import Knot
from ..types.weave import Weave
from ..types.weave_finish_delivery import WeaveFinishDelivery
from ..types.weave_plan_finish import WeavePlanFinish
from ..types.weave_plan_pattern import WeavePlanPattern
from ..types.weave_plan_threads_item import WeavePlanThreadsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWeavesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_weave(
        self, weave_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Weave]:
        """
        Parameters
        ----------
        weave_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Weave]
            The weave
        """
        _response = self._client_wrapper.httpx_client.request(
            f"weaves/{encode_path_param(weave_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Weave,
                    parse_obj_as(
                        type_=Weave,
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

    def start_weave(
        self,
        *,
        pattern: WeavePlanPattern,
        threads: typing.Sequence[WeavePlanThreadsItem],
        knots: typing.Sequence[Knot],
        finish: WeavePlanFinish,
        shelf_id: str,
        label: str,
        delivery: WeaveFinishDelivery,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Weave]:
        """
        Parameters
        ----------
        pattern : WeavePlanPattern
            The weave's pattern.

        threads : typing.Sequence[WeavePlanThreadsItem]
            The threads, in order.

        knots : typing.Sequence[Knot]
            The knots tied along the selvedge.

        finish : WeavePlanFinish
            How the cloth is finished.

        shelf_id : str
            The shelf the cloth goes to.

        label : str
            The cloth's label.

        delivery : WeaveFinishDelivery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Weave]
            Started
        """
        _response = self._client_wrapper.httpx_client.request(
            "weaves:start",
            method="POST",
            json={
                "pattern": convert_and_respect_annotation_metadata(
                    object_=pattern, annotation=WeavePlanPattern, direction="write"
                ),
                "threads": convert_and_respect_annotation_metadata(
                    object_=threads, annotation=typing.Sequence[WeavePlanThreadsItem], direction="write"
                ),
                "knots": convert_and_respect_annotation_metadata(
                    object_=knots, annotation=typing.Sequence[Knot], direction="write"
                ),
                "finish": finish,
                "shelfId": shelf_id,
                "label": label,
                "delivery": convert_and_respect_annotation_metadata(
                    object_=delivery, annotation=WeaveFinishDelivery, direction="write"
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
                    Weave,
                    parse_obj_as(
                        type_=Weave,
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

    def check_weave(
        self,
        *,
        pattern: WeavePlanPattern,
        threads: typing.Sequence[WeavePlanThreadsItem],
        knots: typing.Sequence[Knot],
        finish: WeavePlanFinish,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Weave]:
        """
        Parameters
        ----------
        pattern : WeavePlanPattern
            The weave's pattern.

        threads : typing.Sequence[WeavePlanThreadsItem]
            The threads, in order.

        knots : typing.Sequence[Knot]
            The knots tied along the selvedge.

        finish : WeavePlanFinish
            How the cloth is finished.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Weave]
            Checked
        """
        _response = self._client_wrapper.httpx_client.request(
            "weaves:check",
            method="POST",
            json={
                "pattern": convert_and_respect_annotation_metadata(
                    object_=pattern, annotation=WeavePlanPattern, direction="write"
                ),
                "threads": convert_and_respect_annotation_metadata(
                    object_=threads, annotation=typing.Sequence[WeavePlanThreadsItem], direction="write"
                ),
                "knots": convert_and_respect_annotation_metadata(
                    object_=knots, annotation=typing.Sequence[Knot], direction="write"
                ),
                "finish": finish,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Weave,
                    parse_obj_as(
                        type_=Weave,
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


class AsyncRawWeavesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_weave(
        self, weave_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Weave]:
        """
        Parameters
        ----------
        weave_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Weave]
            The weave
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"weaves/{encode_path_param(weave_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Weave,
                    parse_obj_as(
                        type_=Weave,
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

    async def start_weave(
        self,
        *,
        pattern: WeavePlanPattern,
        threads: typing.Sequence[WeavePlanThreadsItem],
        knots: typing.Sequence[Knot],
        finish: WeavePlanFinish,
        shelf_id: str,
        label: str,
        delivery: WeaveFinishDelivery,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Weave]:
        """
        Parameters
        ----------
        pattern : WeavePlanPattern
            The weave's pattern.

        threads : typing.Sequence[WeavePlanThreadsItem]
            The threads, in order.

        knots : typing.Sequence[Knot]
            The knots tied along the selvedge.

        finish : WeavePlanFinish
            How the cloth is finished.

        shelf_id : str
            The shelf the cloth goes to.

        label : str
            The cloth's label.

        delivery : WeaveFinishDelivery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Weave]
            Started
        """
        _response = await self._client_wrapper.httpx_client.request(
            "weaves:start",
            method="POST",
            json={
                "pattern": convert_and_respect_annotation_metadata(
                    object_=pattern, annotation=WeavePlanPattern, direction="write"
                ),
                "threads": convert_and_respect_annotation_metadata(
                    object_=threads, annotation=typing.Sequence[WeavePlanThreadsItem], direction="write"
                ),
                "knots": convert_and_respect_annotation_metadata(
                    object_=knots, annotation=typing.Sequence[Knot], direction="write"
                ),
                "finish": finish,
                "shelfId": shelf_id,
                "label": label,
                "delivery": convert_and_respect_annotation_metadata(
                    object_=delivery, annotation=WeaveFinishDelivery, direction="write"
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
                    Weave,
                    parse_obj_as(
                        type_=Weave,
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

    async def check_weave(
        self,
        *,
        pattern: WeavePlanPattern,
        threads: typing.Sequence[WeavePlanThreadsItem],
        knots: typing.Sequence[Knot],
        finish: WeavePlanFinish,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Weave]:
        """
        Parameters
        ----------
        pattern : WeavePlanPattern
            The weave's pattern.

        threads : typing.Sequence[WeavePlanThreadsItem]
            The threads, in order.

        knots : typing.Sequence[Knot]
            The knots tied along the selvedge.

        finish : WeavePlanFinish
            How the cloth is finished.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Weave]
            Checked
        """
        _response = await self._client_wrapper.httpx_client.request(
            "weaves:check",
            method="POST",
            json={
                "pattern": convert_and_respect_annotation_metadata(
                    object_=pattern, annotation=WeavePlanPattern, direction="write"
                ),
                "threads": convert_and_respect_annotation_metadata(
                    object_=threads, annotation=typing.Sequence[WeavePlanThreadsItem], direction="write"
                ),
                "knots": convert_and_respect_annotation_metadata(
                    object_=knots, annotation=typing.Sequence[Knot], direction="write"
                ),
                "finish": finish,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Weave,
                    parse_obj_as(
                        type_=Weave,
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
