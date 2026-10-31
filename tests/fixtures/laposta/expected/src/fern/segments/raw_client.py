

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.segment_envelope import SegmentEnvelope
from ..types.segment_list import SegmentList
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSegmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def alle_segmenten_opvragen(
        self, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SegmentList]:
        """
        All segments of a list in an array of segment objects. The segment objects are included in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SegmentList]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "segment",
            method="GET",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SegmentList,
                    parse_obj_as(
                        type_=SegmentList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def segment_toevoegen(
        self, *, list_id: str, name: str, definition: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SegmentEnvelope]:
        """
        If there is something wrong with the provided parameters, an error code and message will be displayed. See above under Error Messages for what the codes mean.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : str
            The name of the segment

        definition : str
            The segment definition as JSON text. Note that a field name that does not exist is accepted and produces a segment that matches nobody.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SegmentEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "segment",
            method="POST",
            data={
                "list_id": list_id,
                "name": name,
                "definition": definition,
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
                    SegmentEnvelope,
                    parse_obj_as(
                        type_=SegmentEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def segment_opvragen(
        self, segment_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SegmentEnvelope]:
        """
        All information about a segment.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SegmentEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"segment/{encode_path_param(segment_id)}",
            method="GET",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SegmentEnvelope,
                    parse_obj_as(
                        type_=SegmentEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def segment_wijzigen(
        self,
        segment_id: str,
        *,
        list_id: str,
        name: typing.Optional[str] = OMIT,
        definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentEnvelope]:
        """
        You only need to include the fields that need to be changed in the request. Fields that are not mentioned retain their current value. Once a field is mentioned, it is checked and can therefore cause an error message. This error message will include a code and a message. See above under Error Messages for what the codes mean.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : typing.Optional[str]
            The name of the segment

        definition : typing.Optional[str]
            The definition of the segment (string in JSON format)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SegmentEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"segment/{encode_path_param(segment_id)}",
            method="POST",
            data={
                "list_id": list_id,
                "name": name,
                "definition": definition,
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
                    SegmentEnvelope,
                    parse_obj_as(
                        type_=SegmentEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def segment_verwijderen(
        self, segment_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SegmentEnvelope]:
        """
        This permanently deletes a segment. After this, the segment cannot be retrieved again.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SegmentEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"segment/{encode_path_param(segment_id)}",
            method="DELETE",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SegmentEnvelope,
                    parse_obj_as(
                        type_=SegmentEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawSegmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def alle_segmenten_opvragen(
        self, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SegmentList]:
        """
        All segments of a list in an array of segment objects. The segment objects are included in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SegmentList]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "segment",
            method="GET",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SegmentList,
                    parse_obj_as(
                        type_=SegmentList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def segment_toevoegen(
        self, *, list_id: str, name: str, definition: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SegmentEnvelope]:
        """
        If there is something wrong with the provided parameters, an error code and message will be displayed. See above under Error Messages for what the codes mean.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : str
            The name of the segment

        definition : str
            The segment definition as JSON text. Note that a field name that does not exist is accepted and produces a segment that matches nobody.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SegmentEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "segment",
            method="POST",
            data={
                "list_id": list_id,
                "name": name,
                "definition": definition,
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
                    SegmentEnvelope,
                    parse_obj_as(
                        type_=SegmentEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def segment_opvragen(
        self, segment_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SegmentEnvelope]:
        """
        All information about a segment.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SegmentEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"segment/{encode_path_param(segment_id)}",
            method="GET",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SegmentEnvelope,
                    parse_obj_as(
                        type_=SegmentEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def segment_wijzigen(
        self,
        segment_id: str,
        *,
        list_id: str,
        name: typing.Optional[str] = OMIT,
        definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SegmentEnvelope]:
        """
        You only need to include the fields that need to be changed in the request. Fields that are not mentioned retain their current value. Once a field is mentioned, it is checked and can therefore cause an error message. This error message will include a code and a message. See above under Error Messages for what the codes mean.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : typing.Optional[str]
            The name of the segment

        definition : typing.Optional[str]
            The definition of the segment (string in JSON format)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SegmentEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"segment/{encode_path_param(segment_id)}",
            method="POST",
            data={
                "list_id": list_id,
                "name": name,
                "definition": definition,
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
                    SegmentEnvelope,
                    parse_obj_as(
                        type_=SegmentEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def segment_verwijderen(
        self, segment_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SegmentEnvelope]:
        """
        This permanently deletes a segment. After this, the segment cannot be retrieved again.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SegmentEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"segment/{encode_path_param(segment_id)}",
            method="DELETE",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SegmentEnvelope,
                    parse_obj_as(
                        type_=SegmentEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
