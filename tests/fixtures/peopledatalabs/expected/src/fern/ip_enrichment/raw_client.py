

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.ip import Ip
from pydantic import ValidationError


class RawIpEnrichmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def ip_enrich(
        self,
        *,
        ip: str,
        return_ip_location: typing.Optional[bool] = None,
        return_ip_metadata: typing.Optional[bool] = None,
        return_person: typing.Optional[bool] = None,
        return_if_unmatched: typing.Optional[bool] = None,
        titlecase: typing.Optional[bool] = None,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ip]:
        """
        Parameters
        ----------
        ip : str
            IP that will be enriched.

        return_ip_location : typing.Optional[bool]
            IP responses will not include location data for the IP by default.  Setting to `true` will return IP specific location info.

        return_ip_metadata : typing.Optional[bool]
            IP responses will not include metadata for the IP by default.  Setting to `true` will return IP specific metadata.

        return_person : typing.Optional[bool]
            Setting to `true` will return person fields associated with the IP.

        return_if_unmatched : typing.Optional[bool]
            Setting to `true` will return IP specific metadata or location data regardless of a company match.

        titlecase : typing.Optional[bool]
            Setting to `true` will titlecase any records returned.

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ip]
            IP enrich completed.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v5/ip/enrich",
            method="GET",
            params={
                "ip": ip,
                "return_ip_location": return_ip_location,
                "return_ip_metadata": return_ip_metadata,
                "return_person": return_person,
                "return_if_unmatched": return_if_unmatched,
                "titlecase": titlecase,
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ip,
                    parse_obj_as(
                        type_=Ip,
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
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
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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


class AsyncRawIpEnrichmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def ip_enrich(
        self,
        *,
        ip: str,
        return_ip_location: typing.Optional[bool] = None,
        return_ip_metadata: typing.Optional[bool] = None,
        return_person: typing.Optional[bool] = None,
        return_if_unmatched: typing.Optional[bool] = None,
        titlecase: typing.Optional[bool] = None,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ip]:
        """
        Parameters
        ----------
        ip : str
            IP that will be enriched.

        return_ip_location : typing.Optional[bool]
            IP responses will not include location data for the IP by default.  Setting to `true` will return IP specific location info.

        return_ip_metadata : typing.Optional[bool]
            IP responses will not include metadata for the IP by default.  Setting to `true` will return IP specific metadata.

        return_person : typing.Optional[bool]
            Setting to `true` will return person fields associated with the IP.

        return_if_unmatched : typing.Optional[bool]
            Setting to `true` will return IP specific metadata or location data regardless of a company match.

        titlecase : typing.Optional[bool]
            Setting to `true` will titlecase any records returned.

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ip]
            IP enrich completed.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v5/ip/enrich",
            method="GET",
            params={
                "ip": ip,
                "return_ip_location": return_ip_location,
                "return_ip_metadata": return_ip_metadata,
                "return_person": return_person,
                "return_if_unmatched": return_if_unmatched,
                "titlecase": titlecase,
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ip,
                    parse_obj_as(
                        type_=Ip,
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
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
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
