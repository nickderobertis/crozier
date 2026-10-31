

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.consent_record import ConsentRecord
from ..types.error import Error
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConsentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_consent_record(
        self,
        *,
        citizen_identity: str,
        scopes: typing.Sequence[str],
        synthesis_consent: bool,
        expires_at: dt.datetime,
        dpa_reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConsentRecord]:
        """
        Citizen-signed consent artifact. MUST include `dpa_reference` whenever any requested
        scope touches a PII-bound tool (PIPA §26 위탁 documentation gap closure).
        MUST include `synthesis_consent` as a separate boolean reflecting the LLM-synthesis
        controller-level carve-out.

        Parameters
        ----------
        citizen_identity : str
            Opaque citizen identifier bound by PASS/공동인증서 at collection time.

        scopes : typing.Sequence[str]
            Scope entries shaped as `<tool_id>:<verb>[:resource]`.

        synthesis_consent : bool
            Separate consent for the LLM-synthesis controller-level carve-out (FR-015).

        expires_at : dt.datetime

        dpa_reference : typing.Optional[str]
            Non-null when any scope is PII-bound (FR-014).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConsentRecord]
            Consent recorded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "consent",
            method="POST",
            json={
                "citizen_identity": citizen_identity,
                "scopes": scopes,
                "dpa_reference": dpa_reference,
                "synthesis_consent": synthesis_consent,
                "expires_at": expires_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsentRecord,
                    parse_obj_as(
                        type_=ConsentRecord,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawConsentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_consent_record(
        self,
        *,
        citizen_identity: str,
        scopes: typing.Sequence[str],
        synthesis_consent: bool,
        expires_at: dt.datetime,
        dpa_reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConsentRecord]:
        """
        Citizen-signed consent artifact. MUST include `dpa_reference` whenever any requested
        scope touches a PII-bound tool (PIPA §26 위탁 documentation gap closure).
        MUST include `synthesis_consent` as a separate boolean reflecting the LLM-synthesis
        controller-level carve-out.

        Parameters
        ----------
        citizen_identity : str
            Opaque citizen identifier bound by PASS/공동인증서 at collection time.

        scopes : typing.Sequence[str]
            Scope entries shaped as `<tool_id>:<verb>[:resource]`.

        synthesis_consent : bool
            Separate consent for the LLM-synthesis controller-level carve-out (FR-015).

        expires_at : dt.datetime

        dpa_reference : typing.Optional[str]
            Non-null when any scope is PII-bound (FR-014).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConsentRecord]
            Consent recorded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "consent",
            method="POST",
            json={
                "citizen_identity": citizen_identity,
                "scopes": scopes,
                "dpa_reference": dpa_reference,
                "synthesis_consent": synthesis_consent,
                "expires_at": expires_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsentRecord,
                    parse_obj_as(
                        type_=ConsentRecord,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
