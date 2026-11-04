

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
from ..types.api_key import ApiKey
from ..types.count_of import CountOf
from ..types.find_credentials import FindCredentials
from ..types.product_create_modify import ProductCreateModify
from ..types.product_view import ProductView
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProductsapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def patchproduct2(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ProductsApi",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ProductCreateModify], direction="write"
            ),
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

    def patchproduct(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ProductsApi",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ProductCreateModify], direction="write"
            ),
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

    def count(
        self, *, request: typing.Optional[ApiKey] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[CountOf]]:
        """
        Parameters
        ----------
        request : typing.Optional[ApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[CountOf]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ProductsApi/Count",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ApiKey], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CountOf],
                    parse_obj_as(
                        type_=typing.Optional[CountOf],
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

    def find(
        self,
        *,
        page: typing.Optional[int] = None,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[ProductView]]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[ProductView]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ProductsApi/Find",
            method="POST",
            params={
                "page": page,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[FindCredentials], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ProductView],
                    parse_obj_as(
                        type_=typing.Optional[ProductView],
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

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        request: typing.Optional[ApiKey] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[ProductView]]]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request : typing.Optional[ApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ProductView]]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ProductsApi/List",
            method="POST",
            params={
                "page": page,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ApiKey], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ProductView]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ProductView]],
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

    def save(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[ProductView]]:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[ProductView]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ProductsApi/Save",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ProductCreateModify], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ProductView],
                    parse_obj_as(
                        type_=typing.Optional[ProductView],
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

    def deleteproduct2(
        self, serial: str, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ProductsApi/{encode_path_param(serial)}",
            method="POST",
            headers={
                "X-Api-Key": str(api_key) if api_key is not None else None,
            },
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

    def deleteproduct(
        self, serial: str, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ProductsApi/{encode_path_param(serial)}",
            method="DELETE",
            headers={
                "X-Api-Key": str(api_key) if api_key is not None else None,
            },
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


class AsyncRawProductsapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def patchproduct2(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ProductsApi",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ProductCreateModify], direction="write"
            ),
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

    async def patchproduct(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ProductsApi",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ProductCreateModify], direction="write"
            ),
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

    async def count(
        self, *, request: typing.Optional[ApiKey] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[CountOf]]:
        """
        Parameters
        ----------
        request : typing.Optional[ApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[CountOf]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ProductsApi/Count",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ApiKey], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CountOf],
                    parse_obj_as(
                        type_=typing.Optional[CountOf],
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

    async def find(
        self,
        *,
        page: typing.Optional[int] = None,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[ProductView]]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[ProductView]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ProductsApi/Find",
            method="POST",
            params={
                "page": page,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[FindCredentials], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ProductView],
                    parse_obj_as(
                        type_=typing.Optional[ProductView],
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

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        request: typing.Optional[ApiKey] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ProductView]]]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request : typing.Optional[ApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ProductView]]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ProductsApi/List",
            method="POST",
            params={
                "page": page,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ApiKey], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ProductView]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ProductView]],
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

    async def save(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[ProductView]]:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[ProductView]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ProductsApi/Save",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ProductCreateModify], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ProductView],
                    parse_obj_as(
                        type_=typing.Optional[ProductView],
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

    async def deleteproduct2(
        self, serial: str, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ProductsApi/{encode_path_param(serial)}",
            method="POST",
            headers={
                "X-Api-Key": str(api_key) if api_key is not None else None,
            },
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

    async def deleteproduct(
        self, serial: str, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ProductsApi/{encode_path_param(serial)}",
            method="DELETE",
            headers={
                "X-Api-Key": str(api_key) if api_key is not None else None,
            },
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
