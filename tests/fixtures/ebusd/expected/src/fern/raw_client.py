

import contextlib
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .errors.bad_request_error import BadRequestError
from .errors.forbidden_error import ForbiddenError
from .errors.internal_server_error import InternalServerError
from .errors.not_found_error import NotFoundError
from .types.data import Data
from .types.data_types import DataTypes
from .types.field_value import FieldValue
from .types.raw_messages import RawMessages
from .types.seconds import Seconds
from .types.templates import Templates
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all_messages_of_all_circuits(
        self,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Data]:
        """
        Parameters
        ----------
        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Data]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "data",
            method="GET",
            params={
                "since": since,
                "poll": poll,
                "verbose": verbose,
                "indexed": indexed,
                "numeric": numeric,
                "valuename": valuename,
                "full": full,
                "required": required,
                "write": write,
                "raw": raw,
                "def": def_,
                "user": user,
                "secret": secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Data,
                    parse_obj_as(
                        type_=Data,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_all_messages_of_a_particular_circuit(
        self,
        circuit: str,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        exact: typing.Optional[bool] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Data]:
        """
        Parameters
        ----------
        circuit : str

        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        exact : typing.Optional[bool]
            exact search for circuit/message name.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Data]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/{encode_path_param(circuit)}",
            method="GET",
            params={
                "since": since,
                "poll": poll,
                "exact": exact,
                "verbose": verbose,
                "indexed": indexed,
                "numeric": numeric,
                "valuename": valuename,
                "full": full,
                "required": required,
                "write": write,
                "raw": raw,
                "def": def_,
                "user": user,
                "secret": secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Data,
                    parse_obj_as(
                        type_=Data,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_a_particular_message_of_a_particular_circuit(
        self,
        circuit: str,
        message: str,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        exact: typing.Optional[bool] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        define: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Data]:
        """
        Parameters
        ----------
        circuit : str

        message : str

        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        exact : typing.Optional[bool]
            exact search for circuit/message name.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        define : typing.Optional[str]
            update/replace a message definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Data]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/{encode_path_param(circuit)}/{encode_path_param(message)}",
            method="GET",
            params={
                "since": since,
                "poll": poll,
                "exact": exact,
                "verbose": verbose,
                "indexed": indexed,
                "numeric": numeric,
                "valuename": valuename,
                "full": full,
                "required": required,
                "write": write,
                "raw": raw,
                "def": def_,
                "define": define,
                "user": user,
                "secret": secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Data,
                    parse_obj_as(
                        type_=Data,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_all_known_field_data_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DataTypes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DataTypes]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "datatypes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataTypes,
                    parse_obj_as(
                        type_=DataTypes,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_all_known_field_templates_for_the_root(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Templates]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Templates]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "templates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Templates,
                    parse_obj_as(
                        type_=Templates,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_all_known_field_templates_for_the_path(
        self, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Templates]:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Templates]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"templates/{encode_path_param(path)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Templates,
                    parse_obj_as(
                        type_=Templates,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def retrieve_raw_data_from_grabbed_and_or_decoded_messages(
        self, *, since: typing.Optional[Seconds] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RawMessages]:
        """
        Parameters
        ----------
        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RawMessages]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "raw",
            method="GET",
            params={
                "since": since,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RawMessages,
                    parse_obj_as(
                        type_=RawMessages,
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

    def decode_raw_data_with_the_specified_field_defintion(
        self, *, def_: str, raw: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[FieldValue]]:
        """
        Parameters
        ----------
        def_ : str
            the field definition (starting with type).

        raw : str
            the raw symbols to decode as hex sequence.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[FieldValue]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "decode",
            method="GET",
            params={
                "def": def_,
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[FieldValue],
                    parse_obj_as(
                        type_=typing.Optional[FieldValue],
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

    @contextlib.contextmanager
    def retrieve_a_particular_file(
        self, file: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        file : str
            the file to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Success
        """
        with self._client_wrapper.httpx_client.stream(
            f"{encode_path_param(file)}",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
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
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all_messages_of_all_circuits(
        self,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Data]:
        """
        Parameters
        ----------
        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Data]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "data",
            method="GET",
            params={
                "since": since,
                "poll": poll,
                "verbose": verbose,
                "indexed": indexed,
                "numeric": numeric,
                "valuename": valuename,
                "full": full,
                "required": required,
                "write": write,
                "raw": raw,
                "def": def_,
                "user": user,
                "secret": secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Data,
                    parse_obj_as(
                        type_=Data,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_all_messages_of_a_particular_circuit(
        self,
        circuit: str,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        exact: typing.Optional[bool] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Data]:
        """
        Parameters
        ----------
        circuit : str

        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        exact : typing.Optional[bool]
            exact search for circuit/message name.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Data]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/{encode_path_param(circuit)}",
            method="GET",
            params={
                "since": since,
                "poll": poll,
                "exact": exact,
                "verbose": verbose,
                "indexed": indexed,
                "numeric": numeric,
                "valuename": valuename,
                "full": full,
                "required": required,
                "write": write,
                "raw": raw,
                "def": def_,
                "user": user,
                "secret": secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Data,
                    parse_obj_as(
                        type_=Data,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_a_particular_message_of_a_particular_circuit(
        self,
        circuit: str,
        message: str,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        exact: typing.Optional[bool] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        define: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Data]:
        """
        Parameters
        ----------
        circuit : str

        message : str

        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        exact : typing.Optional[bool]
            exact search for circuit/message name.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        define : typing.Optional[str]
            update/replace a message definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Data]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/{encode_path_param(circuit)}/{encode_path_param(message)}",
            method="GET",
            params={
                "since": since,
                "poll": poll,
                "exact": exact,
                "verbose": verbose,
                "indexed": indexed,
                "numeric": numeric,
                "valuename": valuename,
                "full": full,
                "required": required,
                "write": write,
                "raw": raw,
                "def": def_,
                "define": define,
                "user": user,
                "secret": secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Data,
                    parse_obj_as(
                        type_=Data,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_all_known_field_data_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DataTypes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DataTypes]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "datatypes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataTypes,
                    parse_obj_as(
                        type_=DataTypes,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_all_known_field_templates_for_the_root(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Templates]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Templates]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "templates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Templates,
                    parse_obj_as(
                        type_=Templates,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_all_known_field_templates_for_the_path(
        self, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Templates]:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Templates]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"templates/{encode_path_param(path)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Templates,
                    parse_obj_as(
                        type_=Templates,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def retrieve_raw_data_from_grabbed_and_or_decoded_messages(
        self, *, since: typing.Optional[Seconds] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RawMessages]:
        """
        Parameters
        ----------
        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RawMessages]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "raw",
            method="GET",
            params={
                "since": since,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RawMessages,
                    parse_obj_as(
                        type_=RawMessages,
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

    async def decode_raw_data_with_the_specified_field_defintion(
        self, *, def_: str, raw: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[FieldValue]]:
        """
        Parameters
        ----------
        def_ : str
            the field definition (starting with type).

        raw : str
            the raw symbols to decode as hex sequence.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[FieldValue]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "decode",
            method="GET",
            params={
                "def": def_,
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[FieldValue],
                    parse_obj_as(
                        type_=typing.Optional[FieldValue],
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

    @contextlib.asynccontextmanager
    async def retrieve_a_particular_file(
        self, file: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        file : str
            the file to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Success
        """
        async with self._client_wrapper.httpx_client.stream(
            f"{encode_path_param(file)}",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
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
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
