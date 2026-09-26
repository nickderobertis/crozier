

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.selling_point_in import SellingPointIn
from ..types.sku_meta_in import SkuMetaIn
from ..types.spec_response import SpecResponse
from .types.spec_request_locale import SpecRequestLocale
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCopywriterClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_spec(
        self,
        kit_id: str,
        *,
        locale: SpecRequestLocale,
        selling_points: typing.Sequence[SellingPointIn],
        sku_meta: SkuMetaIn,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SpecResponse]:
        """
        Generate the marketing spec for *kit_id* under the requested locale.

        Parameters
        ----------
        kit_id : str

        locale : SpecRequestLocale

        selling_points : typing.Sequence[SellingPointIn]

        sku_meta : SkuMetaIn

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SpecResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(kit_id)}/spec",
            method="POST",
            json={
                "locale": locale,
                "selling_points": convert_and_respect_annotation_metadata(
                    object_=selling_points, annotation=typing.Sequence[SellingPointIn], direction="write"
                ),
                "sku_meta": convert_and_respect_annotation_metadata(
                    object_=sku_meta, annotation=SkuMetaIn, direction="write"
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
                    SpecResponse,
                    parse_obj_as(
                        type_=SpecResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawCopywriterClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_spec(
        self,
        kit_id: str,
        *,
        locale: SpecRequestLocale,
        selling_points: typing.Sequence[SellingPointIn],
        sku_meta: SkuMetaIn,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SpecResponse]:
        """
        Generate the marketing spec for *kit_id* under the requested locale.

        Parameters
        ----------
        kit_id : str

        locale : SpecRequestLocale

        selling_points : typing.Sequence[SellingPointIn]

        sku_meta : SkuMetaIn

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SpecResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(kit_id)}/spec",
            method="POST",
            json={
                "locale": locale,
                "selling_points": convert_and_respect_annotation_metadata(
                    object_=selling_points, annotation=typing.Sequence[SellingPointIn], direction="write"
                ),
                "sku_meta": convert_and_respect_annotation_metadata(
                    object_=sku_meta, annotation=SkuMetaIn, direction="write"
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
                    SpecResponse,
                    parse_obj_as(
                        type_=SpecResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
