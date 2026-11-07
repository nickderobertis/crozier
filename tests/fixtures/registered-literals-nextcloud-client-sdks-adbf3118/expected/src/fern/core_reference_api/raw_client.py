

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_reference_api_get_providers_info200response import CoreReferenceApiGetProvidersInfo200Response
from ..types.core_reference_api_resolve_one200response import CoreReferenceApiResolveOne200Response
from ..types.core_reference_api_touch_provider200response import CoreReferenceApiTouchProvider200Response
from pydantic import ValidationError


class RawCoreReferenceApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def resolve_one(
        self, *, reference: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreReferenceApiResolveOne200Response]:
        """
        Parameters
        ----------
        reference : str
            Reference to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreReferenceApiResolveOne200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/references/resolve",
            method="GET",
            params={
                "reference": reference,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiResolveOne200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiResolveOne200Response,
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

    def resolve(
        self,
        *,
        references: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreReferenceApiResolveOne200Response]:
        """
        Parameters
        ----------
        references : str
            References to resolve

        limit : typing.Optional[int]
            Maximum amount of references to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreReferenceApiResolveOne200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/references/resolve",
            method="POST",
            params={
                "references": references,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiResolveOne200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiResolveOne200Response,
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

    def extract(
        self,
        *,
        text: str,
        resolve: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreReferenceApiResolveOne200Response]:
        """
        Parameters
        ----------
        text : str
            Text to extract from

        resolve : typing.Optional[int]
            Resolve the references

        limit : typing.Optional[int]
            Maximum amount of references to extract

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreReferenceApiResolveOne200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/references/extract",
            method="POST",
            params={
                "text": text,
                "resolve": resolve,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiResolveOne200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiResolveOne200Response,
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

    def get_providers_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreReferenceApiGetProvidersInfo200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreReferenceApiGetProvidersInfo200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/references/providers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiGetProvidersInfo200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiGetProvidersInfo200Response,
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

    def touch_provider(
        self,
        provider_id: str,
        *,
        timestamp: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreReferenceApiTouchProvider200Response]:
        """
        Parameters
        ----------
        provider_id : str
            ID of the provider

        timestamp : typing.Optional[int]
            Timestamp of the last usage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreReferenceApiTouchProvider200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/references/provider/{encode_path_param(provider_id)}",
            method="PUT",
            params={
                "timestamp": timestamp,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiTouchProvider200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiTouchProvider200Response,
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


class AsyncRawCoreReferenceApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def resolve_one(
        self, *, reference: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreReferenceApiResolveOne200Response]:
        """
        Parameters
        ----------
        reference : str
            Reference to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreReferenceApiResolveOne200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/references/resolve",
            method="GET",
            params={
                "reference": reference,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiResolveOne200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiResolveOne200Response,
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

    async def resolve(
        self,
        *,
        references: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreReferenceApiResolveOne200Response]:
        """
        Parameters
        ----------
        references : str
            References to resolve

        limit : typing.Optional[int]
            Maximum amount of references to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreReferenceApiResolveOne200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/references/resolve",
            method="POST",
            params={
                "references": references,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiResolveOne200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiResolveOne200Response,
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

    async def extract(
        self,
        *,
        text: str,
        resolve: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreReferenceApiResolveOne200Response]:
        """
        Parameters
        ----------
        text : str
            Text to extract from

        resolve : typing.Optional[int]
            Resolve the references

        limit : typing.Optional[int]
            Maximum amount of references to extract

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreReferenceApiResolveOne200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/references/extract",
            method="POST",
            params={
                "text": text,
                "resolve": resolve,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiResolveOne200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiResolveOne200Response,
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

    async def get_providers_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreReferenceApiGetProvidersInfo200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreReferenceApiGetProvidersInfo200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/references/providers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiGetProvidersInfo200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiGetProvidersInfo200Response,
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

    async def touch_provider(
        self,
        provider_id: str,
        *,
        timestamp: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreReferenceApiTouchProvider200Response]:
        """
        Parameters
        ----------
        provider_id : str
            ID of the provider

        timestamp : typing.Optional[int]
            Timestamp of the last usage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreReferenceApiTouchProvider200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/references/provider/{encode_path_param(provider_id)}",
            method="PUT",
            params={
                "timestamp": timestamp,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiTouchProvider200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiTouchProvider200Response,
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
