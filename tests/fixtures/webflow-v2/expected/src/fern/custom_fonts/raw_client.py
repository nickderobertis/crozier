

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
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from .types.batch_create_custom_fonts_request_items_item import BatchCreateCustomFontsRequestItemsItem
from .types.batch_create_custom_fonts_response import BatchCreateCustomFontsResponse
from .types.batch_delete_custom_fonts_request_items_item import BatchDeleteCustomFontsRequestItemsItem
from .types.batch_delete_custom_fonts_response import BatchDeleteCustomFontsResponse
from .types.create_custom_fonts_request_axes_item import CreateCustomFontsRequestAxesItem
from .types.create_custom_fonts_request_font_display import CreateCustomFontsRequestFontDisplay
from .types.create_custom_fonts_response import CreateCustomFontsResponse
from .types.get_custom_fonts_response import GetCustomFontsResponse
from .types.list_custom_fonts_response import ListCustomFontsResponse
from .types.replace_file_custom_fonts_request_axes_item import ReplaceFileCustomFontsRequestAxesItem
from .types.replace_file_custom_fonts_response import ReplaceFileCustomFontsResponse
from .types.update_custom_fonts_request_font_display import UpdateCustomFontsRequestFontDisplay
from .types.update_custom_fonts_response import UpdateCustomFontsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCustomFontsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        site_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCustomFontsResponse]:
        """
        List the custom fonts uploaded to a site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCustomFontsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCustomFontsResponse,
                    parse_obj_as(
                        type_=ListCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def create(
        self,
        site_id: str,
        *,
        file_name: str,
        file_hash: str,
        font_family: str,
        weight: int,
        italic: bool,
        font_display: CreateCustomFontsRequestFontDisplay,
        axes: typing.Optional[typing.Sequence[CreateCustomFontsRequestAxesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCustomFontsResponse]:
        """
        Register a custom font on a site and get a presigned S3 URL to upload the font binary.

        The response includes a `customFont` object and an `upload` object. Use the `upload.url` and `upload.fields`
        to POST the font binary directly to S3 as `multipart/form-data`. The binary must go in a field named `file`
        and must be the last field in the form (an AWS S3 requirement). S3 returns `201 Created` on a successful upload.

        To learn more, see [Custom fonts](/data/docs/custom-fonts).

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        file_name : str
            File name including extension. Accepted extensions are `.woff2`, `.woff`, `.ttf`, `.otf`, and `.eot`. Maximum 256 characters.

        file_hash : str
            Lowercase hex MD5 hash of the font binary (exactly 32 characters)

        font_family : str
            The CSS font-family name (1-256 characters). Commas are stripped server-side.

        weight : int
            CSS font-weight value (1-1000)

        italic : bool
            Whether the font is italic

        font_display : CreateCustomFontsRequestFontDisplay
            CSS font-display value

        axes : typing.Optional[typing.Sequence[CreateCustomFontsRequestAxesItem]]
            Variable font axes. Omit or pass an empty array for static fonts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateCustomFontsResponse]
            Font registered. Upload the binary to the presigned S3 URL in `upload` to complete the process.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "fileName": file_name,
                "fileHash": file_hash,
                "fontFamily": font_family,
                "weight": weight,
                "italic": italic,
                "fontDisplay": font_display,
                "axes": convert_and_respect_annotation_metadata(
                    object_=axes, annotation=typing.Sequence[CreateCustomFontsRequestAxesItem], direction="write"
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
                    CreateCustomFontsResponse,
                    parse_obj_as(
                        type_=CreateCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 409:
                raise ConflictError(
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def get(
        self, site_id: str, font_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetCustomFontsResponse]:
        """
        Get details about a custom font on a site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCustomFontsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/{encode_path_param(font_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomFontsResponse,
                    parse_obj_as(
                        type_=GetCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def delete(
        self, site_id: str, font_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a custom font from a site.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/{encode_path_param(font_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def update(
        self,
        site_id: str,
        font_id: str,
        *,
        font_family: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        italic: typing.Optional[bool] = OMIT,
        font_display: typing.Optional[UpdateCustomFontsRequestFontDisplay] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateCustomFontsResponse]:
        """
        Update the metadata of a custom font. The font binary is not changed by this endpoint.
        To replace the binary, use [Replace custom font file](#operation/replace-custom-font-file).

        The request body must include at least one of `fontFamily`, `weight`, `italic`, or `fontDisplay`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        font_family : typing.Optional[str]
            The CSS font-family name (1-256 characters)

        weight : typing.Optional[int]
            CSS font-weight value (1-1000)

        italic : typing.Optional[bool]
            Whether the font is italic

        font_display : typing.Optional[UpdateCustomFontsRequestFontDisplay]
            CSS font-display value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateCustomFontsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/{encode_path_param(font_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "fontFamily": font_family,
                "weight": weight,
                "italic": italic,
                "fontDisplay": font_display,
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
                    UpdateCustomFontsResponse,
                    parse_obj_as(
                        type_=UpdateCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def replace_file(
        self,
        site_id: str,
        font_id: str,
        *,
        file_name: str,
        file_hash: str,
        axes: typing.Optional[typing.Sequence[ReplaceFileCustomFontsRequestAxesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReplaceFileCustomFontsResponse]:
        """
        Replace the binary of an existing custom font while preserving its ID and any references to it.
        The upload handshake is identical to [Create custom font](#operation/create-custom-font).

        If the existing font has a non-empty `axes` array (a variable font), you must include an `axes` field
        in the request. Send `axes: []` to declare that the new binary is a static font, or send the new variable
        axes to declare it is still variable. Omitting `axes` when the existing font is variable returns `400`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        file_name : str
            File name including extension. Accepted extensions are `.woff2`, `.woff`, `.ttf`, `.otf`, and `.eot`. Maximum 256 characters.

        file_hash : str
            Lowercase hex MD5 hash of the font binary (exactly 32 characters)

        axes : typing.Optional[typing.Sequence[ReplaceFileCustomFontsRequestAxesItem]]
            Variable font axes for the replacement binary. Required when the existing font has a non-empty `axes` array.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReplaceFileCustomFontsResponse]
            File replacement initiated. Upload the binary to the presigned S3 URL in `upload` to complete the process.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/{encode_path_param(font_id)}/file",
            base_url=self._client_wrapper.get_environment().base,
            method="PUT",
            json={
                "fileName": file_name,
                "fileHash": file_hash,
                "axes": convert_and_respect_annotation_metadata(
                    object_=axes, annotation=typing.Sequence[ReplaceFileCustomFontsRequestAxesItem], direction="write"
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
                    ReplaceFileCustomFontsResponse,
                    parse_obj_as(
                        type_=ReplaceFileCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def batch_create(
        self,
        site_id: str,
        *,
        items: typing.Sequence[BatchCreateCustomFontsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchCreateCustomFontsResponse]:
        """
        Register 1–25 custom fonts in a single request and get a presigned S3 URL for each one.
        This collapses the registration step for a whole font family (for example, Regular, Bold,
        Italic, and Bold Italic) into one rate-limited request.

        Registration is batched, but the binary uploads are not: the response contains one `upload`
        object per registered font, and you must POST each font binary to its own presigned S3 URL
        exactly as you would for [Create custom font](#operation/create-custom-font). The Webflow API
        server never receives the raw font bytes.

        The response is `200 OK` for a valid request body. Per-font results are reported in the
        `created` and `failed` arrays. If the site's font limit is reached partway through the batch,
        the fonts that still fit are registered and returned in `created`, while the rest appear in
        `failed` with `name: "FontLimitReached"` — valid fonts are never discarded because a later
        font in the same batch could not be registered. Each presigned URL expires approximately
        15 minutes after issuance, so upload the binaries promptly.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        items : typing.Sequence[BatchCreateCustomFontsRequestItemsItem]
            The custom fonts to register. Each item uses the same shape as the single-font create request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchCreateCustomFontsResponse]
            Request was successful. Check the `created` and `failed` arrays for per-item results.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/batchCreate",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[BatchCreateCustomFontsRequestItemsItem], direction="write"
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
                    BatchCreateCustomFontsResponse,
                    parse_obj_as(
                        type_=BatchCreateCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def batch_delete(
        self,
        site_id: str,
        *,
        items: typing.Sequence[BatchDeleteCustomFontsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchDeleteCustomFontsResponse]:
        """
        Delete 1-100 custom fonts in a single request. The response is always `200 OK` for a valid request body.
        Per-font results are reported in the `deleted` and `failed` arrays.

        The endpoint is idempotent: fonts that do not exist appear in `failed` with `name: "NotFound"` rather than
        failing the entire request. You can safely retry a partial failure by re-sending only the IDs that did not
        appear in `deleted`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        items : typing.Sequence[BatchDeleteCustomFontsRequestItemsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchDeleteCustomFontsResponse]
            Request was successful. Check `deleted` and `failed` arrays for per-item results.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/batchDelete",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[BatchDeleteCustomFontsRequestItemsItem], direction="write"
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
                    BatchDeleteCustomFontsResponse,
                    parse_obj_as(
                        type_=BatchDeleteCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawCustomFontsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        site_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListCustomFontsResponse]:
        """
        List the custom fonts uploaded to a site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCustomFontsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCustomFontsResponse,
                    parse_obj_as(
                        type_=ListCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def create(
        self,
        site_id: str,
        *,
        file_name: str,
        file_hash: str,
        font_family: str,
        weight: int,
        italic: bool,
        font_display: CreateCustomFontsRequestFontDisplay,
        axes: typing.Optional[typing.Sequence[CreateCustomFontsRequestAxesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateCustomFontsResponse]:
        """
        Register a custom font on a site and get a presigned S3 URL to upload the font binary.

        The response includes a `customFont` object and an `upload` object. Use the `upload.url` and `upload.fields`
        to POST the font binary directly to S3 as `multipart/form-data`. The binary must go in a field named `file`
        and must be the last field in the form (an AWS S3 requirement). S3 returns `201 Created` on a successful upload.

        To learn more, see [Custom fonts](/data/docs/custom-fonts).

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        file_name : str
            File name including extension. Accepted extensions are `.woff2`, `.woff`, `.ttf`, `.otf`, and `.eot`. Maximum 256 characters.

        file_hash : str
            Lowercase hex MD5 hash of the font binary (exactly 32 characters)

        font_family : str
            The CSS font-family name (1-256 characters). Commas are stripped server-side.

        weight : int
            CSS font-weight value (1-1000)

        italic : bool
            Whether the font is italic

        font_display : CreateCustomFontsRequestFontDisplay
            CSS font-display value

        axes : typing.Optional[typing.Sequence[CreateCustomFontsRequestAxesItem]]
            Variable font axes. Omit or pass an empty array for static fonts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateCustomFontsResponse]
            Font registered. Upload the binary to the presigned S3 URL in `upload` to complete the process.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "fileName": file_name,
                "fileHash": file_hash,
                "fontFamily": font_family,
                "weight": weight,
                "italic": italic,
                "fontDisplay": font_display,
                "axes": convert_and_respect_annotation_metadata(
                    object_=axes, annotation=typing.Sequence[CreateCustomFontsRequestAxesItem], direction="write"
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
                    CreateCustomFontsResponse,
                    parse_obj_as(
                        type_=CreateCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 409:
                raise ConflictError(
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def get(
        self, site_id: str, font_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetCustomFontsResponse]:
        """
        Get details about a custom font on a site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCustomFontsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/{encode_path_param(font_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomFontsResponse,
                    parse_obj_as(
                        type_=GetCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def delete(
        self, site_id: str, font_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a custom font from a site.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/{encode_path_param(font_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def update(
        self,
        site_id: str,
        font_id: str,
        *,
        font_family: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        italic: typing.Optional[bool] = OMIT,
        font_display: typing.Optional[UpdateCustomFontsRequestFontDisplay] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateCustomFontsResponse]:
        """
        Update the metadata of a custom font. The font binary is not changed by this endpoint.
        To replace the binary, use [Replace custom font file](#operation/replace-custom-font-file).

        The request body must include at least one of `fontFamily`, `weight`, `italic`, or `fontDisplay`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        font_family : typing.Optional[str]
            The CSS font-family name (1-256 characters)

        weight : typing.Optional[int]
            CSS font-weight value (1-1000)

        italic : typing.Optional[bool]
            Whether the font is italic

        font_display : typing.Optional[UpdateCustomFontsRequestFontDisplay]
            CSS font-display value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateCustomFontsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/{encode_path_param(font_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "fontFamily": font_family,
                "weight": weight,
                "italic": italic,
                "fontDisplay": font_display,
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
                    UpdateCustomFontsResponse,
                    parse_obj_as(
                        type_=UpdateCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def replace_file(
        self,
        site_id: str,
        font_id: str,
        *,
        file_name: str,
        file_hash: str,
        axes: typing.Optional[typing.Sequence[ReplaceFileCustomFontsRequestAxesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReplaceFileCustomFontsResponse]:
        """
        Replace the binary of an existing custom font while preserving its ID and any references to it.
        The upload handshake is identical to [Create custom font](#operation/create-custom-font).

        If the existing font has a non-empty `axes` array (a variable font), you must include an `axes` field
        in the request. Send `axes: []` to declare that the new binary is a static font, or send the new variable
        axes to declare it is still variable. Omitting `axes` when the existing font is variable returns `400`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        file_name : str
            File name including extension. Accepted extensions are `.woff2`, `.woff`, `.ttf`, `.otf`, and `.eot`. Maximum 256 characters.

        file_hash : str
            Lowercase hex MD5 hash of the font binary (exactly 32 characters)

        axes : typing.Optional[typing.Sequence[ReplaceFileCustomFontsRequestAxesItem]]
            Variable font axes for the replacement binary. Required when the existing font has a non-empty `axes` array.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReplaceFileCustomFontsResponse]
            File replacement initiated. Upload the binary to the presigned S3 URL in `upload` to complete the process.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/{encode_path_param(font_id)}/file",
            base_url=self._client_wrapper.get_environment().base,
            method="PUT",
            json={
                "fileName": file_name,
                "fileHash": file_hash,
                "axes": convert_and_respect_annotation_metadata(
                    object_=axes, annotation=typing.Sequence[ReplaceFileCustomFontsRequestAxesItem], direction="write"
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
                    ReplaceFileCustomFontsResponse,
                    parse_obj_as(
                        type_=ReplaceFileCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def batch_create(
        self,
        site_id: str,
        *,
        items: typing.Sequence[BatchCreateCustomFontsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchCreateCustomFontsResponse]:
        """
        Register 1–25 custom fonts in a single request and get a presigned S3 URL for each one.
        This collapses the registration step for a whole font family (for example, Regular, Bold,
        Italic, and Bold Italic) into one rate-limited request.

        Registration is batched, but the binary uploads are not: the response contains one `upload`
        object per registered font, and you must POST each font binary to its own presigned S3 URL
        exactly as you would for [Create custom font](#operation/create-custom-font). The Webflow API
        server never receives the raw font bytes.

        The response is `200 OK` for a valid request body. Per-font results are reported in the
        `created` and `failed` arrays. If the site's font limit is reached partway through the batch,
        the fonts that still fit are registered and returned in `created`, while the rest appear in
        `failed` with `name: "FontLimitReached"` — valid fonts are never discarded because a later
        font in the same batch could not be registered. Each presigned URL expires approximately
        15 minutes after issuance, so upload the binaries promptly.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        items : typing.Sequence[BatchCreateCustomFontsRequestItemsItem]
            The custom fonts to register. Each item uses the same shape as the single-font create request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchCreateCustomFontsResponse]
            Request was successful. Check the `created` and `failed` arrays for per-item results.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/batchCreate",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[BatchCreateCustomFontsRequestItemsItem], direction="write"
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
                    BatchCreateCustomFontsResponse,
                    parse_obj_as(
                        type_=BatchCreateCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def batch_delete(
        self,
        site_id: str,
        *,
        items: typing.Sequence[BatchDeleteCustomFontsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchDeleteCustomFontsResponse]:
        """
        Delete 1-100 custom fonts in a single request. The response is always `200 OK` for a valid request body.
        Per-font results are reported in the `deleted` and `failed` arrays.

        The endpoint is idempotent: fonts that do not exist appear in `failed` with `name: "NotFound"` rather than
        failing the entire request. You can safely retry a partial failure by re-sending only the IDs that did not
        appear in `deleted`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        items : typing.Sequence[BatchDeleteCustomFontsRequestItemsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchDeleteCustomFontsResponse]
            Request was successful. Check `deleted` and `failed` arrays for per-item results.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/custom_fonts/batchDelete",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[BatchDeleteCustomFontsRequestItemsItem], direction="write"
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
                    BatchDeleteCustomFontsResponse,
                    parse_obj_as(
                        type_=BatchDeleteCustomFontsResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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
