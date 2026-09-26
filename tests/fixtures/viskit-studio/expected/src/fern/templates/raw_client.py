

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
from ..types.preview_response import PreviewResponse
from ..types.scheme_slot import SchemeSlot
from ..types.scheme_summary import SchemeSummary
from ..types.template_summary import TemplateSummary
from .types.list_schemes_api_templates_schemes_get_request_locale import ListSchemesApiTemplatesSchemesGetRequestLocale
from .types.preview_request_locale import PreviewRequestLocale
from .types.scheme_payload_locale import SchemePayloadLocale
from .types.template_payload_category import TemplatePayloadCategory
from .types.template_payload_locale import TemplatePayloadLocale
from .types.template_update_category import TemplateUpdateCategory
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TemplateSummary]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TemplateSummary]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/templates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TemplateSummary],
                    parse_obj_as(
                        type_=typing.List[TemplateSummary],
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

    def create_template(
        self,
        *,
        locale: TemplatePayloadLocale,
        name: str,
        prompt_template: typing.Dict[str, str],
        category: typing.Optional[TemplatePayloadCategory] = OMIT,
        category_tips: typing.Optional[typing.Dict[str, str]] = OMIT,
        defaults: typing.Optional[typing.Dict[str, str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        examples: typing.Optional[typing.Sequence[str]] = OMIT,
        supports_image_reference: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        variants: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TemplateSummary]:
        """
        Parameters
        ----------
        locale : TemplatePayloadLocale

        name : str

        prompt_template : typing.Dict[str, str]

        category : typing.Optional[TemplatePayloadCategory]

        category_tips : typing.Optional[typing.Dict[str, str]]

        defaults : typing.Optional[typing.Dict[str, str]]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        examples : typing.Optional[typing.Sequence[str]]

        supports_image_reference : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        variants : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TemplateSummary]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/templates",
            method="POST",
            json={
                "category": category,
                "category_tips": category_tips,
                "defaults": defaults,
                "description": description,
                "enabled": enabled,
                "examples": examples,
                "locale": locale,
                "name": name,
                "prompt_template": prompt_template,
                "supports_image_reference": supports_image_reference,
                "tags": tags,
                "variants": variants,
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
                    TemplateSummary,
                    parse_obj_as(
                        type_=TemplateSummary,
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

    def copy_template(
        self,
        *,
        source_ref: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TemplateSummary]:
        """
        Parameters
        ----------
        source_ref : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TemplateSummary]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/templates/copy",
            method="POST",
            json={
                "name": name,
                "source_ref": source_ref,
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
                    TemplateSummary,
                    parse_obj_as(
                        type_=TemplateSummary,
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

    def get_managed_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TemplateSummary]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TemplateSummary]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/templates/managed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TemplateSummary],
                    parse_obj_as(
                        type_=typing.List[TemplateSummary],
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

    def preview_template(
        self,
        *,
        locale: PreviewRequestLocale,
        template_ref: str,
        brand_color_hex: typing.Optional[str] = OMIT,
        copy: typing.Optional[str] = OMIT,
        design_note: typing.Optional[str] = OMIT,
        sample_brand: typing.Optional[str] = OMIT,
        sample_category: typing.Optional[str] = OMIT,
        sample_name: typing.Optional[str] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        visual: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PreviewResponse]:
        """
        Parameters
        ----------
        locale : PreviewRequestLocale

        template_ref : str

        brand_color_hex : typing.Optional[str]

        copy : typing.Optional[str]

        design_note : typing.Optional[str]

        sample_brand : typing.Optional[str]

        sample_category : typing.Optional[str]

        sample_name : typing.Optional[str]

        style_prompt : typing.Optional[str]

        visual : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PreviewResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/templates/preview",
            method="POST",
            json={
                "brand_color_hex": brand_color_hex,
                "copy": copy,
                "design_note": design_note,
                "locale": locale,
                "sample_brand": sample_brand,
                "sample_category": sample_category,
                "sample_name": sample_name,
                "style_prompt": style_prompt,
                "template_ref": template_ref,
                "visual": visual,
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
                    PreviewResponse,
                    parse_obj_as(
                        type_=PreviewResponse,
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

    def list_schemes(
        self,
        *,
        locale: typing.Optional[ListSchemesApiTemplatesSchemesGetRequestLocale] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[SchemeSummary]]:
        """
        Parameters
        ----------
        locale : typing.Optional[ListSchemesApiTemplatesSchemesGetRequestLocale]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SchemeSummary]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/templates/schemes",
            method="GET",
            params={
                "locale": locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SchemeSummary],
                    parse_obj_as(
                        type_=typing.List[SchemeSummary],
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

    def create_scheme(
        self,
        *,
        locale: SchemePayloadLocale,
        name: str,
        slots: typing.Sequence[SchemeSlot],
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchemeSummary]:
        """
        Parameters
        ----------
        locale : SchemePayloadLocale

        name : str

        slots : typing.Sequence[SchemeSlot]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchemeSummary]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/templates/schemes",
            method="POST",
            json={
                "description": description,
                "enabled": enabled,
                "locale": locale,
                "name": name,
                "slots": convert_and_respect_annotation_metadata(
                    object_=slots, annotation=typing.Sequence[SchemeSlot], direction="write"
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
                    SchemeSummary,
                    parse_obj_as(
                        type_=SchemeSummary,
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

    def delete_template(
        self, template_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, bool]]:
        """
        Parameters
        ----------
        template_ref : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, bool]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/templates/{encode_path_param(template_ref)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, bool],
                    parse_obj_as(
                        type_=typing.Dict[str, bool],
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

    def update_template(
        self,
        template_ref: str,
        *,
        category: typing.Optional[TemplateUpdateCategory] = OMIT,
        category_tips: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        defaults: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        examples: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        supports_image_reference: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        variants: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TemplateSummary]:
        """
        Parameters
        ----------
        template_ref : str

        category : typing.Optional[TemplateUpdateCategory]

        category_tips : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        defaults : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        examples : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        prompt_template : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        supports_image_reference : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        variants : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TemplateSummary]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/templates/{encode_path_param(template_ref)}",
            method="PATCH",
            json={
                "category": category,
                "category_tips": category_tips,
                "defaults": defaults,
                "description": description,
                "enabled": enabled,
                "examples": examples,
                "name": name,
                "prompt_template": prompt_template,
                "supports_image_reference": supports_image_reference,
                "tags": tags,
                "variants": variants,
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
                    TemplateSummary,
                    parse_obj_as(
                        type_=TemplateSummary,
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


class AsyncRawTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TemplateSummary]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TemplateSummary]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/templates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TemplateSummary],
                    parse_obj_as(
                        type_=typing.List[TemplateSummary],
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

    async def create_template(
        self,
        *,
        locale: TemplatePayloadLocale,
        name: str,
        prompt_template: typing.Dict[str, str],
        category: typing.Optional[TemplatePayloadCategory] = OMIT,
        category_tips: typing.Optional[typing.Dict[str, str]] = OMIT,
        defaults: typing.Optional[typing.Dict[str, str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        examples: typing.Optional[typing.Sequence[str]] = OMIT,
        supports_image_reference: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        variants: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TemplateSummary]:
        """
        Parameters
        ----------
        locale : TemplatePayloadLocale

        name : str

        prompt_template : typing.Dict[str, str]

        category : typing.Optional[TemplatePayloadCategory]

        category_tips : typing.Optional[typing.Dict[str, str]]

        defaults : typing.Optional[typing.Dict[str, str]]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        examples : typing.Optional[typing.Sequence[str]]

        supports_image_reference : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        variants : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TemplateSummary]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/templates",
            method="POST",
            json={
                "category": category,
                "category_tips": category_tips,
                "defaults": defaults,
                "description": description,
                "enabled": enabled,
                "examples": examples,
                "locale": locale,
                "name": name,
                "prompt_template": prompt_template,
                "supports_image_reference": supports_image_reference,
                "tags": tags,
                "variants": variants,
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
                    TemplateSummary,
                    parse_obj_as(
                        type_=TemplateSummary,
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

    async def copy_template(
        self,
        *,
        source_ref: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TemplateSummary]:
        """
        Parameters
        ----------
        source_ref : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TemplateSummary]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/templates/copy",
            method="POST",
            json={
                "name": name,
                "source_ref": source_ref,
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
                    TemplateSummary,
                    parse_obj_as(
                        type_=TemplateSummary,
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

    async def get_managed_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TemplateSummary]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TemplateSummary]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/templates/managed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TemplateSummary],
                    parse_obj_as(
                        type_=typing.List[TemplateSummary],
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

    async def preview_template(
        self,
        *,
        locale: PreviewRequestLocale,
        template_ref: str,
        brand_color_hex: typing.Optional[str] = OMIT,
        copy: typing.Optional[str] = OMIT,
        design_note: typing.Optional[str] = OMIT,
        sample_brand: typing.Optional[str] = OMIT,
        sample_category: typing.Optional[str] = OMIT,
        sample_name: typing.Optional[str] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        visual: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PreviewResponse]:
        """
        Parameters
        ----------
        locale : PreviewRequestLocale

        template_ref : str

        brand_color_hex : typing.Optional[str]

        copy : typing.Optional[str]

        design_note : typing.Optional[str]

        sample_brand : typing.Optional[str]

        sample_category : typing.Optional[str]

        sample_name : typing.Optional[str]

        style_prompt : typing.Optional[str]

        visual : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PreviewResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/templates/preview",
            method="POST",
            json={
                "brand_color_hex": brand_color_hex,
                "copy": copy,
                "design_note": design_note,
                "locale": locale,
                "sample_brand": sample_brand,
                "sample_category": sample_category,
                "sample_name": sample_name,
                "style_prompt": style_prompt,
                "template_ref": template_ref,
                "visual": visual,
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
                    PreviewResponse,
                    parse_obj_as(
                        type_=PreviewResponse,
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

    async def list_schemes(
        self,
        *,
        locale: typing.Optional[ListSchemesApiTemplatesSchemesGetRequestLocale] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[SchemeSummary]]:
        """
        Parameters
        ----------
        locale : typing.Optional[ListSchemesApiTemplatesSchemesGetRequestLocale]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SchemeSummary]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/templates/schemes",
            method="GET",
            params={
                "locale": locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SchemeSummary],
                    parse_obj_as(
                        type_=typing.List[SchemeSummary],
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

    async def create_scheme(
        self,
        *,
        locale: SchemePayloadLocale,
        name: str,
        slots: typing.Sequence[SchemeSlot],
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchemeSummary]:
        """
        Parameters
        ----------
        locale : SchemePayloadLocale

        name : str

        slots : typing.Sequence[SchemeSlot]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchemeSummary]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/templates/schemes",
            method="POST",
            json={
                "description": description,
                "enabled": enabled,
                "locale": locale,
                "name": name,
                "slots": convert_and_respect_annotation_metadata(
                    object_=slots, annotation=typing.Sequence[SchemeSlot], direction="write"
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
                    SchemeSummary,
                    parse_obj_as(
                        type_=SchemeSummary,
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

    async def delete_template(
        self, template_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, bool]]:
        """
        Parameters
        ----------
        template_ref : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, bool]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/templates/{encode_path_param(template_ref)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, bool],
                    parse_obj_as(
                        type_=typing.Dict[str, bool],
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

    async def update_template(
        self,
        template_ref: str,
        *,
        category: typing.Optional[TemplateUpdateCategory] = OMIT,
        category_tips: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        defaults: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        examples: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        supports_image_reference: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        variants: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TemplateSummary]:
        """
        Parameters
        ----------
        template_ref : str

        category : typing.Optional[TemplateUpdateCategory]

        category_tips : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        defaults : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        examples : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        prompt_template : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        supports_image_reference : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        variants : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TemplateSummary]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/templates/{encode_path_param(template_ref)}",
            method="PATCH",
            json={
                "category": category,
                "category_tips": category_tips,
                "defaults": defaults,
                "description": description,
                "enabled": enabled,
                "examples": examples,
                "name": name,
                "prompt_template": prompt_template,
                "supports_image_reference": supports_image_reference,
                "tags": tags,
                "variants": variants,
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
                    TemplateSummary,
                    parse_obj_as(
                        type_=TemplateSummary,
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
