

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.get_map_test_response import GetMapTestResponse
from .types.get_nested_collections_response import GetNestedCollectionsResponse
from .types.get_obj_no_type_response import GetObjNoTypeResponse
from .types.get_set_test_response import GetSetTestResponse
from .types.map_allof_oneof_stringified import MapAllofOneofStringified
from .types.mapnested_allof_oneof_nullable import MapnestedAllofOneofNullable
from .types.mapnested_schema import MapnestedSchema
from .types.setnested_schema import SetnestedSchema
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def test_for_objects_that_have_no_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetObjNoTypeResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetObjNoTypeResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "obj_no_type",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetObjNoTypeResponse,
                    parse_obj_as(
                        type_=GetObjNoTypeResponse,
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

    def test_for_nested_collections_list_within_a_list_set_within_a_list_map_within_a_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetNestedCollectionsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetNestedCollectionsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "nested_collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNestedCollectionsResponse,
                    parse_obj_as(
                        type_=GetNestedCollectionsResponse,
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

    def test_for_map_nested_attributes_and_map_attributes_in_a_data_source(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMapTestResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMapTestResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "map_test",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMapTestResponse,
                    parse_obj_as(
                        type_=GetMapTestResponse,
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

    def test_for_map_nested_attributes_and_map_attributes_in_a_resource(
        self,
        *,
        mapnested_prop: MapnestedSchema,
        mapnested_nullable: typing.Optional[MapnestedAllofOneofNullable] = OMIT,
        map_prop: typing.Optional[typing.Dict[str, str]] = OMIT,
        map_stringified: typing.Optional[MapAllofOneofStringified] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        mapnested_prop : MapnestedSchema

        mapnested_nullable : typing.Optional[MapnestedAllofOneofNullable]

        map_prop : typing.Optional[typing.Dict[str, str]]
            This is a map of strings

        map_stringified : typing.Optional[MapAllofOneofStringified]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "map_test",
            method="POST",
            json={
                "mapnested_prop": convert_and_respect_annotation_metadata(
                    object_=mapnested_prop, annotation=MapnestedSchema, direction="write"
                ),
                "mapnested_nullable": convert_and_respect_annotation_metadata(
                    object_=mapnested_nullable, annotation=MapnestedAllofOneofNullable, direction="write"
                ),
                "map_prop": map_prop,
                "map_stringified": convert_and_respect_annotation_metadata(
                    object_=map_stringified, annotation=MapAllofOneofStringified, direction="write"
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

    def test_for_set_nested_attributes_and_set_attributes_in_a_data_source(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSetTestResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSetTestResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "set_test",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSetTestResponse,
                    parse_obj_as(
                        type_=GetSetTestResponse,
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

    def test_for_set_nested_attributes_and_set_attributes_in_a_resource(
        self,
        *,
        setnested_prop: SetnestedSchema,
        set_prop: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        setnested_prop : SetnestedSchema

        set_prop : typing.Optional[typing.Sequence[str]]
            This is a set of strings

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "set_test",
            method="POST",
            json={
                "setnested_prop": convert_and_respect_annotation_metadata(
                    object_=setnested_prop, annotation=SetnestedSchema, direction="write"
                ),
                "set_prop": set_prop,
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

    async def test_for_objects_that_have_no_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetObjNoTypeResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetObjNoTypeResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "obj_no_type",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetObjNoTypeResponse,
                    parse_obj_as(
                        type_=GetObjNoTypeResponse,
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

    async def test_for_nested_collections_list_within_a_list_set_within_a_list_map_within_a_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetNestedCollectionsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetNestedCollectionsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "nested_collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNestedCollectionsResponse,
                    parse_obj_as(
                        type_=GetNestedCollectionsResponse,
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

    async def test_for_map_nested_attributes_and_map_attributes_in_a_data_source(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMapTestResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMapTestResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "map_test",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMapTestResponse,
                    parse_obj_as(
                        type_=GetMapTestResponse,
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

    async def test_for_map_nested_attributes_and_map_attributes_in_a_resource(
        self,
        *,
        mapnested_prop: MapnestedSchema,
        mapnested_nullable: typing.Optional[MapnestedAllofOneofNullable] = OMIT,
        map_prop: typing.Optional[typing.Dict[str, str]] = OMIT,
        map_stringified: typing.Optional[MapAllofOneofStringified] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        mapnested_prop : MapnestedSchema

        mapnested_nullable : typing.Optional[MapnestedAllofOneofNullable]

        map_prop : typing.Optional[typing.Dict[str, str]]
            This is a map of strings

        map_stringified : typing.Optional[MapAllofOneofStringified]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "map_test",
            method="POST",
            json={
                "mapnested_prop": convert_and_respect_annotation_metadata(
                    object_=mapnested_prop, annotation=MapnestedSchema, direction="write"
                ),
                "mapnested_nullable": convert_and_respect_annotation_metadata(
                    object_=mapnested_nullable, annotation=MapnestedAllofOneofNullable, direction="write"
                ),
                "map_prop": map_prop,
                "map_stringified": convert_and_respect_annotation_metadata(
                    object_=map_stringified, annotation=MapAllofOneofStringified, direction="write"
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

    async def test_for_set_nested_attributes_and_set_attributes_in_a_data_source(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSetTestResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSetTestResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "set_test",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSetTestResponse,
                    parse_obj_as(
                        type_=GetSetTestResponse,
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

    async def test_for_set_nested_attributes_and_set_attributes_in_a_resource(
        self,
        *,
        setnested_prop: SetnestedSchema,
        set_prop: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        setnested_prop : SetnestedSchema

        set_prop : typing.Optional[typing.Sequence[str]]
            This is a set of strings

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "set_test",
            method="POST",
            json={
                "setnested_prop": convert_and_respect_annotation_metadata(
                    object_=setnested_prop, annotation=SetnestedSchema, direction="write"
                ),
                "set_prop": set_prop,
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
