

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
from ..types.coat import Coat
from ..types.pot import Pot
from ..types.pot_outer_coat import PotOuterCoat
from .types.recoat_pot_request_coat import RecoatPotRequestCoat
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def record_pot(
        self,
        *,
        potter: str,
        outer_coat: PotOuterCoat,
        inner_coat: typing.Optional[Coat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Pot]:
        """
        Parameters
        ----------
        potter : str

        outer_coat : PotOuterCoat
            The coat on the pot's outer wall.

        inner_coat : typing.Optional[Coat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Pot]
            The recorded pot.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pots",
            method="POST",
            json={
                "potter": potter,
                "outerCoat": convert_and_respect_annotation_metadata(
                    object_=outer_coat, annotation=PotOuterCoat, direction="write"
                ),
                "innerCoat": convert_and_respect_annotation_metadata(
                    object_=inner_coat, annotation=Coat, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pot,
                    parse_obj_as(
                        type_=Pot,
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

    def recoat_pot(
        self,
        pot_id: str,
        *,
        coat: RecoatPotRequestCoat,
        previous_coat: typing.Optional[Coat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Pot]:
        """
        Parameters
        ----------
        pot_id : str

        coat : RecoatPotRequestCoat
            The fresh coat to apply.

        previous_coat : typing.Optional[Coat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Pot]
            The recoated pot.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pots/{encode_path_param(pot_id)}/recoat",
            method="POST",
            json={
                "coat": convert_and_respect_annotation_metadata(
                    object_=coat, annotation=RecoatPotRequestCoat, direction="write"
                ),
                "previousCoat": convert_and_respect_annotation_metadata(
                    object_=previous_coat, annotation=Coat, direction="write"
                ),
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
                    Pot,
                    parse_obj_as(
                        type_=Pot,
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


class AsyncRawPotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def record_pot(
        self,
        *,
        potter: str,
        outer_coat: PotOuterCoat,
        inner_coat: typing.Optional[Coat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Pot]:
        """
        Parameters
        ----------
        potter : str

        outer_coat : PotOuterCoat
            The coat on the pot's outer wall.

        inner_coat : typing.Optional[Coat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Pot]
            The recorded pot.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pots",
            method="POST",
            json={
                "potter": potter,
                "outerCoat": convert_and_respect_annotation_metadata(
                    object_=outer_coat, annotation=PotOuterCoat, direction="write"
                ),
                "innerCoat": convert_and_respect_annotation_metadata(
                    object_=inner_coat, annotation=Coat, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pot,
                    parse_obj_as(
                        type_=Pot,
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

    async def recoat_pot(
        self,
        pot_id: str,
        *,
        coat: RecoatPotRequestCoat,
        previous_coat: typing.Optional[Coat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Pot]:
        """
        Parameters
        ----------
        pot_id : str

        coat : RecoatPotRequestCoat
            The fresh coat to apply.

        previous_coat : typing.Optional[Coat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Pot]
            The recoated pot.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pots/{encode_path_param(pot_id)}/recoat",
            method="POST",
            json={
                "coat": convert_and_respect_annotation_metadata(
                    object_=coat, annotation=RecoatPotRequestCoat, direction="write"
                ),
                "previousCoat": convert_and_respect_annotation_metadata(
                    object_=previous_coat, annotation=Coat, direction="write"
                ),
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
                    Pot,
                    parse_obj_as(
                        type_=Pot,
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
