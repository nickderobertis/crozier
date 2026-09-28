

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.expectation import Expectation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSamlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def mock_saml_provider(
        self,
        *,
        idp_entity_id: typing.Optional[str] = OMIT,
        sp_entity_id: typing.Optional[str] = OMIT,
        signing_certificate_pem: typing.Optional[str] = OMIT,
        signing_private_key_pem: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Expectation]]:
        """
        Generates a set of expectations that emulate a SAML 2.0 identity provider (metadata, single sign-on and single logout endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        idp_entity_id : typing.Optional[str]
            identity provider entity ID advertised in metadata

        sp_entity_id : typing.Optional[str]
            service provider entity ID the assertions are issued for

        signing_certificate_pem : typing.Optional[str]
            PEM-encoded X.509 certificate used to verify signed assertions

        signing_private_key_pem : typing.Optional[str]
            PEM-encoded private key used to sign assertions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Expectation]]
            SAML provider expectations created
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/saml",
            method="PUT",
            json={
                "idpEntityId": idp_entity_id,
                "spEntityId": sp_entity_id,
                "signingCertificatePem": signing_certificate_pem,
                "signingPrivateKeyPem": signing_private_key_pem,
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


class AsyncRawSamlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def mock_saml_provider(
        self,
        *,
        idp_entity_id: typing.Optional[str] = OMIT,
        sp_entity_id: typing.Optional[str] = OMIT,
        signing_certificate_pem: typing.Optional[str] = OMIT,
        signing_private_key_pem: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Expectation]]:
        """
        Generates a set of expectations that emulate a SAML 2.0 identity provider (metadata, single sign-on and single logout endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        idp_entity_id : typing.Optional[str]
            identity provider entity ID advertised in metadata

        sp_entity_id : typing.Optional[str]
            service provider entity ID the assertions are issued for

        signing_certificate_pem : typing.Optional[str]
            PEM-encoded X.509 certificate used to verify signed assertions

        signing_private_key_pem : typing.Optional[str]
            PEM-encoded private key used to sign assertions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Expectation]]
            SAML provider expectations created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/saml",
            method="PUT",
            json={
                "idpEntityId": idp_entity_id,
                "spEntityId": sp_entity_id,
                "signingCertificatePem": signing_certificate_pem,
                "signingPrivateKeyPem": signing_private_key_pem,
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
