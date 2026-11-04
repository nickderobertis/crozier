

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
from ..errors.bad_request_error import BadRequestError
from ..types.named_ref import NamedRef
from ..types.source_response import SourceResponse
from .types.post_api_sources_signals_verify_response import PostApiSourcesSignalsVerifyResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def returns_all_available_sources(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[SourceResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SourceResponse]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/sources",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SourceResponse],
                    parse_obj_as(
                        type_=typing.List[SourceResponse],
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

    def creates_new_source(
        self,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        connection: typing.Optional[NamedRef] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        connection : typing.Optional[NamedRef]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/sources",
            method="POST",
            json={
                "name": name,
                "description": description,
                "type": type,
                "schema": schema,
                "connection": convert_and_respect_annotation_metadata(
                    object_=connection, annotation=NamedRef, direction="write"
                ),
                "vaults": convert_and_respect_annotation_metadata(
                    object_=vaults, annotation=typing.Sequence[NamedRef], direction="write"
                ),
                "config": config,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def verify_that_signal_data_collection_is_configured_correctly(
        self,
        *,
        connection_id: int,
        fully_qualified_table_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostApiSourcesSignalsVerifyResponse]:
        """
        Parameters
        ----------
        connection_id : int

        fully_qualified_table_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostApiSourcesSignalsVerifyResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/sources/signals/verify",
            method="POST",
            json={
                "connectionId": connection_id,
                "fullyQualifiedTableName": fully_qualified_table_name,
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
                    PostApiSourcesSignalsVerifyResponse,
                    parse_obj_as(
                        type_=PostApiSourcesSignalsVerifyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def returns_a_source_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SourceResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SourceResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/sources/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SourceResponse,
                    parse_obj_as(
                        type_=SourceResponse,
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

    def updates_an_existing_source(
        self,
        id: int,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        connection: typing.Optional[NamedRef] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SourceResponse]:
        """
        Parameters
        ----------
        id : int

        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        connection : typing.Optional[NamedRef]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SourceResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/sources/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
                "description": description,
                "type": type,
                "schema": schema,
                "connection": convert_and_respect_annotation_metadata(
                    object_=connection, annotation=NamedRef, direction="write"
                ),
                "vaults": convert_and_respect_annotation_metadata(
                    object_=vaults, annotation=typing.Sequence[NamedRef], direction="write"
                ),
                "config": config,
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
                    SourceResponse,
                    parse_obj_as(
                        type_=SourceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def deletes_an_existing_source(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/sources/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
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


class AsyncRawSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def returns_all_available_sources(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[SourceResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SourceResponse]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/sources",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SourceResponse],
                    parse_obj_as(
                        type_=typing.List[SourceResponse],
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

    async def creates_new_source(
        self,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        connection: typing.Optional[NamedRef] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        connection : typing.Optional[NamedRef]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/sources",
            method="POST",
            json={
                "name": name,
                "description": description,
                "type": type,
                "schema": schema,
                "connection": convert_and_respect_annotation_metadata(
                    object_=connection, annotation=NamedRef, direction="write"
                ),
                "vaults": convert_and_respect_annotation_metadata(
                    object_=vaults, annotation=typing.Sequence[NamedRef], direction="write"
                ),
                "config": config,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def verify_that_signal_data_collection_is_configured_correctly(
        self,
        *,
        connection_id: int,
        fully_qualified_table_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostApiSourcesSignalsVerifyResponse]:
        """
        Parameters
        ----------
        connection_id : int

        fully_qualified_table_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostApiSourcesSignalsVerifyResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/sources/signals/verify",
            method="POST",
            json={
                "connectionId": connection_id,
                "fullyQualifiedTableName": fully_qualified_table_name,
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
                    PostApiSourcesSignalsVerifyResponse,
                    parse_obj_as(
                        type_=PostApiSourcesSignalsVerifyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def returns_a_source_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SourceResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SourceResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/sources/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SourceResponse,
                    parse_obj_as(
                        type_=SourceResponse,
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

    async def updates_an_existing_source(
        self,
        id: int,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        connection: typing.Optional[NamedRef] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SourceResponse]:
        """
        Parameters
        ----------
        id : int

        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        connection : typing.Optional[NamedRef]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SourceResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/sources/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
                "description": description,
                "type": type,
                "schema": schema,
                "connection": convert_and_respect_annotation_metadata(
                    object_=connection, annotation=NamedRef, direction="write"
                ),
                "vaults": convert_and_respect_annotation_metadata(
                    object_=vaults, annotation=typing.Sequence[NamedRef], direction="write"
                ),
                "config": config,
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
                    SourceResponse,
                    parse_obj_as(
                        type_=SourceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def deletes_an_existing_source(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/sources/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
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
