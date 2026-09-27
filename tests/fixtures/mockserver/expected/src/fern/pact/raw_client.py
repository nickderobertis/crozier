

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_acceptable_error import NotAcceptableError
from ..types.expectation import Expectation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPactClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def export_active_expectations_as_a_pact_contract(
        self,
        *,
        consumer: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Exports the current active expectations as a Pact consumer-driven contract (JSON). The optional 'consumer' and 'provider' query parameters set the contract's consumer and provider names.

        Parameters
        ----------
        consumer : typing.Optional[str]
            consumer name to record in the exported Pact contract

        provider : typing.Optional[str]
            provider name to record in the exported Pact contract

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Pact contract exported
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/pact",
            method="PUT",
            params={
                "consumer": consumer,
                "provider": provider,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def verify_active_expectations_against_a_pact_contract(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Verifies the supplied Pact contract (JSON) against the current expectations and returns the verification result. Returns 202 when verification passes and 406 when it fails.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Pact verification passed
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/pact/verify",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            if _response.status_code == 406:
                raise NotAcceptableError(
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

    def import_a_pact_contract_as_expectations(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        redact_sensitive_data: typing.Optional[bool] = None,
        additional_redacted_headers: typing.Optional[str] = None,
        additional_redacted_body_fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Expectation]]:
        """
        Parses a Pact v3 consumer-driven contract and adds the interactions it describes to the active expectation set. Redaction is applied on import so credentials present in the contract are not retained.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        redact_sensitive_data : typing.Optional[bool]
            redact credentials found in the imported contract

        additional_redacted_headers : typing.Optional[str]
            comma-separated additional header names to redact

        additional_redacted_body_fields : typing.Optional[str]
            comma-separated additional body field names to redact

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Expectation]]
            Pact contract imported as expectations
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/pact/import",
            method="PUT",
            params={
                "redactSensitiveData": redact_sensitive_data,
                "additionalRedactedHeaders": additional_redacted_headers,
                "additionalRedactedBodyFields": additional_redacted_body_fields,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Expectation],
                    parse_obj_as(
                        type_=typing.List[Expectation],
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


class AsyncRawPactClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def export_active_expectations_as_a_pact_contract(
        self,
        *,
        consumer: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Exports the current active expectations as a Pact consumer-driven contract (JSON). The optional 'consumer' and 'provider' query parameters set the contract's consumer and provider names.

        Parameters
        ----------
        consumer : typing.Optional[str]
            consumer name to record in the exported Pact contract

        provider : typing.Optional[str]
            provider name to record in the exported Pact contract

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Pact contract exported
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/pact",
            method="PUT",
            params={
                "consumer": consumer,
                "provider": provider,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def verify_active_expectations_against_a_pact_contract(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Verifies the supplied Pact contract (JSON) against the current expectations and returns the verification result. Returns 202 when verification passes and 406 when it fails.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Pact verification passed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/pact/verify",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            if _response.status_code == 406:
                raise NotAcceptableError(
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

    async def import_a_pact_contract_as_expectations(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        redact_sensitive_data: typing.Optional[bool] = None,
        additional_redacted_headers: typing.Optional[str] = None,
        additional_redacted_body_fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Expectation]]:
        """
        Parses a Pact v3 consumer-driven contract and adds the interactions it describes to the active expectation set. Redaction is applied on import so credentials present in the contract are not retained.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        redact_sensitive_data : typing.Optional[bool]
            redact credentials found in the imported contract

        additional_redacted_headers : typing.Optional[str]
            comma-separated additional header names to redact

        additional_redacted_body_fields : typing.Optional[str]
            comma-separated additional body field names to redact

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Expectation]]
            Pact contract imported as expectations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/pact/import",
            method="PUT",
            params={
                "redactSensitiveData": redact_sensitive_data,
                "additionalRedactedHeaders": additional_redacted_headers,
                "additionalRedactedBodyFields": additional_redacted_body_fields,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Expectation],
                    parse_obj_as(
                        type_=typing.List[Expectation],
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
