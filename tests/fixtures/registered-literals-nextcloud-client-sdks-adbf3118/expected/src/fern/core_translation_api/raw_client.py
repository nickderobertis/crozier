

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_translation_api_languages200response import CoreTranslationApiLanguages200Response
from ..types.core_translation_api_translate200response import CoreTranslationApiTranslate200Response
from pydantic import ValidationError


class RawCoreTranslationApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def languages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreTranslationApiLanguages200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreTranslationApiLanguages200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/translation/languages",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreTranslationApiLanguages200Response,
                    parse_obj_as(
                        type_=CoreTranslationApiLanguages200Response,
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

    def translate(
        self,
        *,
        text: str,
        to_language: str,
        from_language: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreTranslationApiTranslate200Response]:
        """
        Parameters
        ----------
        text : str
            Text to be translated

        to_language : str
            Language to translate to

        from_language : typing.Optional[str]
            Language to translate from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreTranslationApiTranslate200Response]
            Translated text returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/translation/translate",
            method="POST",
            params={
                "text": text,
                "fromLanguage": from_language,
                "toLanguage": to_language,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreTranslationApiTranslate200Response,
                    parse_obj_as(
                        type_=CoreTranslationApiTranslate200Response,
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


class AsyncRawCoreTranslationApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def languages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreTranslationApiLanguages200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreTranslationApiLanguages200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/translation/languages",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreTranslationApiLanguages200Response,
                    parse_obj_as(
                        type_=CoreTranslationApiLanguages200Response,
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

    async def translate(
        self,
        *,
        text: str,
        to_language: str,
        from_language: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreTranslationApiTranslate200Response]:
        """
        Parameters
        ----------
        text : str
            Text to be translated

        to_language : str
            Language to translate to

        from_language : typing.Optional[str]
            Language to translate from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreTranslationApiTranslate200Response]
            Translated text returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/translation/translate",
            method="POST",
            params={
                "text": text,
                "fromLanguage": from_language,
                "toLanguage": to_language,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreTranslationApiTranslate200Response,
                    parse_obj_as(
                        type_=CoreTranslationApiTranslate200Response,
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
