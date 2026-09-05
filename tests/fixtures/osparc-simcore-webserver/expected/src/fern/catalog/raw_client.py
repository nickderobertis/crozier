

import datetime as dt
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
from ..types.envelope_catalog_service_get import EnvelopeCatalogServiceGet
from ..types.envelope_dict_annotated_str_string_constraints_image_resources import (
    EnvelopeDictAnnotatedStrStringConstraintsImageResources,
)
from ..types.envelope_list_annotated_str_string_constraints import EnvelopeListAnnotatedStrStringConstraints
from ..types.envelope_list_service_input_get import EnvelopeListServiceInputGet
from ..types.envelope_list_service_output_get import EnvelopeListServiceOutputGet
from ..types.envelope_list_tag_get import EnvelopeListTagGet
from ..types.envelope_service_input_get import EnvelopeServiceInputGet
from ..types.envelope_service_pricing_plan_get import EnvelopeServicePricingPlanGet
from ..types.page_catalog_latest_service_get import PageCatalogLatestServiceGet
from ..types.service_group_access_rights_v2 import ServiceGroupAccessRightsV2
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCatalogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_services_latest(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageCatalogLatestServiceGet]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageCatalogLatestServiceGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/catalog/services/-/latest",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageCatalogLatestServiceGet,
                    parse_obj_as(
                        type_=PageCatalogLatestServiceGet,
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

    def get_service(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeCatalogServiceGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeCatalogServiceGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeCatalogServiceGet,
                    parse_obj_as(
                        type_=EnvelopeCatalogServiceGet,
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

    def update_service(
        self,
        service_key: str,
        service_version: str,
        *,
        name: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_ui: typing.Optional[bool] = OMIT,
        version_display: typing.Optional[str] = OMIT,
        deprecated: typing.Optional[dt.datetime] = OMIT,
        classifiers: typing.Optional[typing.Sequence[str]] = OMIT,
        quality: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        access_rights: typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]] = OMIT,
        release_notes_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeCatalogServiceGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        name : typing.Optional[str]

        thumbnail : typing.Optional[str]

        icon : typing.Optional[str]

        description : typing.Optional[str]

        description_ui : typing.Optional[bool]

        version_display : typing.Optional[str]

        deprecated : typing.Optional[dt.datetime]

        classifiers : typing.Optional[typing.Sequence[str]]

        quality : typing.Optional[typing.Dict[str, typing.Any]]

        access_rights : typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]]

        release_notes_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeCatalogServiceGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}",
            method="PATCH",
            json={
                "name": name,
                "thumbnail": thumbnail,
                "icon": icon,
                "description": description,
                "descriptionUi": description_ui,
                "versionDisplay": version_display,
                "deprecated": deprecated,
                "classifiers": classifiers,
                "quality": quality,
                "accessRights": convert_and_respect_annotation_metadata(
                    object_=access_rights,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]],
                    direction="write",
                ),
                "releaseNotesUrl": release_notes_url,
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
                    EnvelopeCatalogServiceGet,
                    parse_obj_as(
                        type_=EnvelopeCatalogServiceGet,
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

    def list_service_inputs(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListServiceInputGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListServiceInputGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/inputs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListServiceInputGet,
                    parse_obj_as(
                        type_=EnvelopeListServiceInputGet,
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

    def get_service_input(
        self,
        service_key: str,
        service_version: str,
        input_key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeServiceInputGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        input_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeServiceInputGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/inputs/{encode_path_param(input_key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeServiceInputGet,
                    parse_obj_as(
                        type_=EnvelopeServiceInputGet,
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

    def get_compatible_inputs_given_source_output(
        self,
        service_key: str,
        service_version: str,
        *,
        from_service: str,
        from_version: str,
        from_output: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeListAnnotatedStrStringConstraints]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        from_service : str

        from_version : str

        from_output : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListAnnotatedStrStringConstraints]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/inputs:match",
            method="GET",
            params={
                "fromService": from_service,
                "fromVersion": from_version,
                "fromOutput": from_output,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListAnnotatedStrStringConstraints,
                    parse_obj_as(
                        type_=EnvelopeListAnnotatedStrStringConstraints,
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

    def list_service_outputs(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListAnnotatedStrStringConstraints]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListAnnotatedStrStringConstraints]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/outputs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListAnnotatedStrStringConstraints,
                    parse_obj_as(
                        type_=EnvelopeListAnnotatedStrStringConstraints,
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

    def get_service_output(
        self,
        service_key: str,
        service_version: str,
        output_key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeListServiceOutputGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        output_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListServiceOutputGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/outputs/{encode_path_param(output_key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListServiceOutputGet,
                    parse_obj_as(
                        type_=EnvelopeListServiceOutputGet,
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

    def get_compatible_outputs_given_target_input(
        self,
        service_key: str,
        service_version: str,
        *,
        to_service: str,
        to_version: str,
        to_input: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeListAnnotatedStrStringConstraints]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        to_service : str

        to_version : str

        to_input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListAnnotatedStrStringConstraints]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/outputs:match",
            method="GET",
            params={
                "toService": to_service,
                "toVersion": to_version,
                "toInput": to_input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListAnnotatedStrStringConstraints,
                    parse_obj_as(
                        type_=EnvelopeListAnnotatedStrStringConstraints,
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

    def get_service_resources(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/resources",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictAnnotatedStrStringConstraintsImageResources,
                    parse_obj_as(
                        type_=EnvelopeDictAnnotatedStrStringConstraintsImageResources,
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

    def get_service_pricing_plan(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeServicePricingPlanGet]:
        """
        Retrieve default pricing plan for provided service

        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeServicePricingPlanGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/pricing-plan",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeServicePricingPlanGet,
                    parse_obj_as(
                        type_=EnvelopeServicePricingPlanGet,
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

    def list_service_tags(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListTagGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListTagGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/tags",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListTagGet,
                    parse_obj_as(
                        type_=EnvelopeListTagGet,
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

    def add_service_tag(
        self,
        service_key: str,
        service_version: str,
        tag_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeCatalogServiceGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeCatalogServiceGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/tags/{encode_path_param(tag_id)}:add",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeCatalogServiceGet,
                    parse_obj_as(
                        type_=EnvelopeCatalogServiceGet,
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

    def remove_service_tag(
        self,
        service_key: str,
        service_version: str,
        tag_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeCatalogServiceGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeCatalogServiceGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/tags/{encode_path_param(tag_id)}:remove",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeCatalogServiceGet,
                    parse_obj_as(
                        type_=EnvelopeCatalogServiceGet,
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


class AsyncRawCatalogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_services_latest(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageCatalogLatestServiceGet]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageCatalogLatestServiceGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/catalog/services/-/latest",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageCatalogLatestServiceGet,
                    parse_obj_as(
                        type_=PageCatalogLatestServiceGet,
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

    async def get_service(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeCatalogServiceGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeCatalogServiceGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeCatalogServiceGet,
                    parse_obj_as(
                        type_=EnvelopeCatalogServiceGet,
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

    async def update_service(
        self,
        service_key: str,
        service_version: str,
        *,
        name: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_ui: typing.Optional[bool] = OMIT,
        version_display: typing.Optional[str] = OMIT,
        deprecated: typing.Optional[dt.datetime] = OMIT,
        classifiers: typing.Optional[typing.Sequence[str]] = OMIT,
        quality: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        access_rights: typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]] = OMIT,
        release_notes_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeCatalogServiceGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        name : typing.Optional[str]

        thumbnail : typing.Optional[str]

        icon : typing.Optional[str]

        description : typing.Optional[str]

        description_ui : typing.Optional[bool]

        version_display : typing.Optional[str]

        deprecated : typing.Optional[dt.datetime]

        classifiers : typing.Optional[typing.Sequence[str]]

        quality : typing.Optional[typing.Dict[str, typing.Any]]

        access_rights : typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]]

        release_notes_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeCatalogServiceGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}",
            method="PATCH",
            json={
                "name": name,
                "thumbnail": thumbnail,
                "icon": icon,
                "description": description,
                "descriptionUi": description_ui,
                "versionDisplay": version_display,
                "deprecated": deprecated,
                "classifiers": classifiers,
                "quality": quality,
                "accessRights": convert_and_respect_annotation_metadata(
                    object_=access_rights,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]],
                    direction="write",
                ),
                "releaseNotesUrl": release_notes_url,
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
                    EnvelopeCatalogServiceGet,
                    parse_obj_as(
                        type_=EnvelopeCatalogServiceGet,
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

    async def list_service_inputs(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListServiceInputGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListServiceInputGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/inputs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListServiceInputGet,
                    parse_obj_as(
                        type_=EnvelopeListServiceInputGet,
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

    async def get_service_input(
        self,
        service_key: str,
        service_version: str,
        input_key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeServiceInputGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        input_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeServiceInputGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/inputs/{encode_path_param(input_key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeServiceInputGet,
                    parse_obj_as(
                        type_=EnvelopeServiceInputGet,
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

    async def get_compatible_inputs_given_source_output(
        self,
        service_key: str,
        service_version: str,
        *,
        from_service: str,
        from_version: str,
        from_output: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeListAnnotatedStrStringConstraints]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        from_service : str

        from_version : str

        from_output : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListAnnotatedStrStringConstraints]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/inputs:match",
            method="GET",
            params={
                "fromService": from_service,
                "fromVersion": from_version,
                "fromOutput": from_output,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListAnnotatedStrStringConstraints,
                    parse_obj_as(
                        type_=EnvelopeListAnnotatedStrStringConstraints,
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

    async def list_service_outputs(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListAnnotatedStrStringConstraints]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListAnnotatedStrStringConstraints]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/outputs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListAnnotatedStrStringConstraints,
                    parse_obj_as(
                        type_=EnvelopeListAnnotatedStrStringConstraints,
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

    async def get_service_output(
        self,
        service_key: str,
        service_version: str,
        output_key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeListServiceOutputGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        output_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListServiceOutputGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/outputs/{encode_path_param(output_key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListServiceOutputGet,
                    parse_obj_as(
                        type_=EnvelopeListServiceOutputGet,
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

    async def get_compatible_outputs_given_target_input(
        self,
        service_key: str,
        service_version: str,
        *,
        to_service: str,
        to_version: str,
        to_input: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeListAnnotatedStrStringConstraints]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        to_service : str

        to_version : str

        to_input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListAnnotatedStrStringConstraints]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/outputs:match",
            method="GET",
            params={
                "toService": to_service,
                "toVersion": to_version,
                "toInput": to_input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListAnnotatedStrStringConstraints,
                    parse_obj_as(
                        type_=EnvelopeListAnnotatedStrStringConstraints,
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

    async def get_service_resources(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/resources",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictAnnotatedStrStringConstraintsImageResources,
                    parse_obj_as(
                        type_=EnvelopeDictAnnotatedStrStringConstraintsImageResources,
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

    async def get_service_pricing_plan(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeServicePricingPlanGet]:
        """
        Retrieve default pricing plan for provided service

        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeServicePricingPlanGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/pricing-plan",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeServicePricingPlanGet,
                    parse_obj_as(
                        type_=EnvelopeServicePricingPlanGet,
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

    async def list_service_tags(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListTagGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListTagGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/tags",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListTagGet,
                    parse_obj_as(
                        type_=EnvelopeListTagGet,
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

    async def add_service_tag(
        self,
        service_key: str,
        service_version: str,
        tag_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeCatalogServiceGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeCatalogServiceGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/tags/{encode_path_param(tag_id)}:add",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeCatalogServiceGet,
                    parse_obj_as(
                        type_=EnvelopeCatalogServiceGet,
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

    async def remove_service_tag(
        self,
        service_key: str,
        service_version: str,
        tag_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeCatalogServiceGet]:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeCatalogServiceGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/catalog/services/{encode_path_param(service_key)}/{encode_path_param(service_version)}/tags/{encode_path_param(tag_id)}:remove",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeCatalogServiceGet,
                    parse_obj_as(
                        type_=EnvelopeCatalogServiceGet,
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
