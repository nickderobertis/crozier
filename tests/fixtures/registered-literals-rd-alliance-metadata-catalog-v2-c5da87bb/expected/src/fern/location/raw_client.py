

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.mscid import Mscid
from ..types.response_item_vocabulary_term import ResponseItemVocabularyTerm
from ..types.response_page_vocabulary_term import ResponsePageVocabularyTerm
from ..types.response_success_vocabulary_term import ResponseSuccessVocabularyTerm
from ..types.uri import Uri
from ..types.vocabulary_term_applies_item import VocabularyTermAppliesItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLocationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_registered_location_url_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponsePageVocabularyTerm]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponsePageVocabularyTerm]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/location",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageVocabularyTerm,
                    parse_obj_as(
                        type_=ResponsePageVocabularyTerm,
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

    def submit_a_new_location_url_type(
        self,
        *,
        id: str,
        label: str,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        applies: typing.Optional[typing.Sequence[VocabularyTermAppliesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessVocabularyTerm]:
        """
        Parameters
        ----------
        id : str
            String used to identify this term in records.

        label : str
            Human-readable descriptor for this term.

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        applies : typing.Optional[typing.Sequence[VocabularyTermAppliesItem]]
            Entities for which this term may be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessVocabularyTerm]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/location",
            method="POST",
            json={
                "id": id,
                "mscid": mscid,
                "uri": uri,
                "label": label,
                "applies": applies,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessVocabularyTerm,
                    parse_obj_as(
                        type_=ResponseSuccessVocabularyTerm,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def retrieve_an_existing_location_url_type_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponseItemVocabularyTerm]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseItemVocabularyTerm]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/location{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemVocabularyTerm,
                    parse_obj_as(
                        type_=ResponseItemVocabularyTerm,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def modify_an_existing_location_url_type_record(
        self,
        int_: int,
        *,
        label: str,
        id: typing.Optional[str] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        applies: typing.Optional[typing.Sequence[VocabularyTermAppliesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessVocabularyTerm]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        label : str
            Human-readable descriptor for this term.

        id : typing.Optional[str]
            String used to identify this term in records.

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        applies : typing.Optional[typing.Sequence[VocabularyTermAppliesItem]]
            Entities for which this term may be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessVocabularyTerm]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/location{encode_path_param(int_)}",
            method="PUT",
            json={
                "id": id,
                "mscid": mscid,
                "uri": uri,
                "label": label,
                "applies": applies,
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
                    ResponseSuccessVocabularyTerm,
                    parse_obj_as(
                        type_=ResponseSuccessVocabularyTerm,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_an_existing_location_url_type_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/location{encode_path_param(int_)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawLocationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_registered_location_url_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponsePageVocabularyTerm]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponsePageVocabularyTerm]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/location",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageVocabularyTerm,
                    parse_obj_as(
                        type_=ResponsePageVocabularyTerm,
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

    async def submit_a_new_location_url_type(
        self,
        *,
        id: str,
        label: str,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        applies: typing.Optional[typing.Sequence[VocabularyTermAppliesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessVocabularyTerm]:
        """
        Parameters
        ----------
        id : str
            String used to identify this term in records.

        label : str
            Human-readable descriptor for this term.

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        applies : typing.Optional[typing.Sequence[VocabularyTermAppliesItem]]
            Entities for which this term may be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessVocabularyTerm]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/location",
            method="POST",
            json={
                "id": id,
                "mscid": mscid,
                "uri": uri,
                "label": label,
                "applies": applies,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessVocabularyTerm,
                    parse_obj_as(
                        type_=ResponseSuccessVocabularyTerm,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def retrieve_an_existing_location_url_type_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponseItemVocabularyTerm]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseItemVocabularyTerm]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/location{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemVocabularyTerm,
                    parse_obj_as(
                        type_=ResponseItemVocabularyTerm,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def modify_an_existing_location_url_type_record(
        self,
        int_: int,
        *,
        label: str,
        id: typing.Optional[str] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        applies: typing.Optional[typing.Sequence[VocabularyTermAppliesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessVocabularyTerm]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        label : str
            Human-readable descriptor for this term.

        id : typing.Optional[str]
            String used to identify this term in records.

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        applies : typing.Optional[typing.Sequence[VocabularyTermAppliesItem]]
            Entities for which this term may be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessVocabularyTerm]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/location{encode_path_param(int_)}",
            method="PUT",
            json={
                "id": id,
                "mscid": mscid,
                "uri": uri,
                "label": label,
                "applies": applies,
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
                    ResponseSuccessVocabularyTerm,
                    parse_obj_as(
                        type_=ResponseSuccessVocabularyTerm,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_an_existing_location_url_type_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/location{encode_path_param(int_)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
