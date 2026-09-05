

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
from ..types.envelope_list_pricing_plan_to_service_admin_get import EnvelopeListPricingPlanToServiceAdminGet
from ..types.envelope_pricing_plan_admin_get import EnvelopePricingPlanAdminGet
from ..types.envelope_pricing_plan_to_service_admin_get import EnvelopePricingPlanToServiceAdminGet
from ..types.envelope_pricing_unit_admin_get import EnvelopePricingUnitAdminGet
from ..types.page_pricing_plan_admin_get import PagePricingPlanAdminGet
from ..types.pricing_plan_classification import PricingPlanClassification
from ..types.pricing_unit_cost_update import PricingUnitCostUpdate
from ..types.specific_info import SpecificInfo
from .types.create_pricing_unit_body_params_cost_per_unit import CreatePricingUnitBodyParamsCostPerUnit
from .types.create_pricing_unit_body_params_unit_extra_info import CreatePricingUnitBodyParamsUnitExtraInfo
from .types.update_pricing_unit_body_params_unit_extra_info import UpdatePricingUnitBodyParamsUnitExtraInfo
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAdminClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_pricing_plans_for_admin_user(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PagePricingPlanAdminGet]:
        """
        To keep the listing lightweight, the pricingUnits field is None.

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagePricingPlanAdminGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/pricing-plans",
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
                    PagePricingPlanAdminGet,
                    parse_obj_as(
                        type_=PagePricingPlanAdminGet,
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

    def create_pricing_plan(
        self,
        *,
        display_name: str,
        description: str,
        classification: PricingPlanClassification,
        pricing_plan_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopePricingPlanAdminGet]:
        """
        Parameters
        ----------
        display_name : str

        description : str

        classification : PricingPlanClassification

        pricing_plan_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopePricingPlanAdminGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/pricing-plans",
            method="POST",
            json={
                "displayName": display_name,
                "description": description,
                "classification": classification,
                "pricingPlanKey": pricing_plan_key,
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
                    EnvelopePricingPlanAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingPlanAdminGet,
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

    def get_pricing_plan_for_admin_user(
        self, pricing_plan_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopePricingPlanAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopePricingPlanAdminGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopePricingPlanAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingPlanAdminGet,
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

    def update_pricing_plan(
        self,
        pricing_plan_id: int,
        *,
        display_name: str,
        description: str,
        is_active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopePricingPlanAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        display_name : str

        description : str

        is_active : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopePricingPlanAdminGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}",
            method="PUT",
            json={
                "displayName": display_name,
                "description": description,
                "isActive": is_active,
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
                    EnvelopePricingPlanAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingPlanAdminGet,
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

    def get_pricing_unit(
        self, pricing_plan_id: int, pricing_unit_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopePricingUnitAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        pricing_unit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopePricingUnitAdminGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}/pricing-units/{encode_path_param(pricing_unit_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopePricingUnitAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingUnitAdminGet,
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

    def update_pricing_unit(
        self,
        pricing_plan_id: int,
        pricing_unit_id: int,
        *,
        unit_name: str,
        unit_extra_info: UpdatePricingUnitBodyParamsUnitExtraInfo,
        default: bool,
        specific_info: SpecificInfo,
        pricing_unit_cost_update: typing.Optional[PricingUnitCostUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopePricingUnitAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        pricing_unit_id : int

        unit_name : str

        unit_extra_info : UpdatePricingUnitBodyParamsUnitExtraInfo

        default : bool

        specific_info : SpecificInfo

        pricing_unit_cost_update : typing.Optional[PricingUnitCostUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopePricingUnitAdminGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}/pricing-units/{encode_path_param(pricing_unit_id)}",
            method="PUT",
            json={
                "unitName": unit_name,
                "unitExtraInfo": convert_and_respect_annotation_metadata(
                    object_=unit_extra_info, annotation=UpdatePricingUnitBodyParamsUnitExtraInfo, direction="write"
                ),
                "default": default,
                "specificInfo": convert_and_respect_annotation_metadata(
                    object_=specific_info, annotation=SpecificInfo, direction="write"
                ),
                "pricingUnitCostUpdate": convert_and_respect_annotation_metadata(
                    object_=pricing_unit_cost_update,
                    annotation=typing.Optional[PricingUnitCostUpdate],
                    direction="write",
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
                    EnvelopePricingUnitAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingUnitAdminGet,
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

    def create_pricing_unit(
        self,
        pricing_plan_id: int,
        *,
        unit_name: str,
        unit_extra_info: CreatePricingUnitBodyParamsUnitExtraInfo,
        default: bool,
        specific_info: SpecificInfo,
        cost_per_unit: CreatePricingUnitBodyParamsCostPerUnit,
        comment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopePricingUnitAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        unit_name : str

        unit_extra_info : CreatePricingUnitBodyParamsUnitExtraInfo

        default : bool

        specific_info : SpecificInfo

        cost_per_unit : CreatePricingUnitBodyParamsCostPerUnit

        comment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopePricingUnitAdminGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}/pricing-units",
            method="POST",
            json={
                "unitName": unit_name,
                "unitExtraInfo": convert_and_respect_annotation_metadata(
                    object_=unit_extra_info, annotation=CreatePricingUnitBodyParamsUnitExtraInfo, direction="write"
                ),
                "default": default,
                "specificInfo": convert_and_respect_annotation_metadata(
                    object_=specific_info, annotation=SpecificInfo, direction="write"
                ),
                "costPerUnit": convert_and_respect_annotation_metadata(
                    object_=cost_per_unit, annotation=CreatePricingUnitBodyParamsCostPerUnit, direction="write"
                ),
                "comment": comment,
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
                    EnvelopePricingUnitAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingUnitAdminGet,
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

    def list_connected_services_to_pricing_plan(
        self, pricing_plan_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListPricingPlanToServiceAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListPricingPlanToServiceAdminGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}/billable-services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListPricingPlanToServiceAdminGet,
                    parse_obj_as(
                        type_=EnvelopeListPricingPlanToServiceAdminGet,
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

    def connect_service_to_pricing_plan(
        self,
        pricing_plan_id: int,
        *,
        service_key: str,
        service_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopePricingPlanToServiceAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopePricingPlanToServiceAdminGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}/billable-services",
            method="POST",
            json={
                "serviceKey": service_key,
                "serviceVersion": service_version,
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
                    EnvelopePricingPlanToServiceAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingPlanToServiceAdminGet,
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


class AsyncRawAdminClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_pricing_plans_for_admin_user(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PagePricingPlanAdminGet]:
        """
        To keep the listing lightweight, the pricingUnits field is None.

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagePricingPlanAdminGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/pricing-plans",
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
                    PagePricingPlanAdminGet,
                    parse_obj_as(
                        type_=PagePricingPlanAdminGet,
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

    async def create_pricing_plan(
        self,
        *,
        display_name: str,
        description: str,
        classification: PricingPlanClassification,
        pricing_plan_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopePricingPlanAdminGet]:
        """
        Parameters
        ----------
        display_name : str

        description : str

        classification : PricingPlanClassification

        pricing_plan_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopePricingPlanAdminGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/pricing-plans",
            method="POST",
            json={
                "displayName": display_name,
                "description": description,
                "classification": classification,
                "pricingPlanKey": pricing_plan_key,
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
                    EnvelopePricingPlanAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingPlanAdminGet,
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

    async def get_pricing_plan_for_admin_user(
        self, pricing_plan_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopePricingPlanAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopePricingPlanAdminGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopePricingPlanAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingPlanAdminGet,
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

    async def update_pricing_plan(
        self,
        pricing_plan_id: int,
        *,
        display_name: str,
        description: str,
        is_active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopePricingPlanAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        display_name : str

        description : str

        is_active : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopePricingPlanAdminGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}",
            method="PUT",
            json={
                "displayName": display_name,
                "description": description,
                "isActive": is_active,
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
                    EnvelopePricingPlanAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingPlanAdminGet,
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

    async def get_pricing_unit(
        self, pricing_plan_id: int, pricing_unit_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopePricingUnitAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        pricing_unit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopePricingUnitAdminGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}/pricing-units/{encode_path_param(pricing_unit_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopePricingUnitAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingUnitAdminGet,
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

    async def update_pricing_unit(
        self,
        pricing_plan_id: int,
        pricing_unit_id: int,
        *,
        unit_name: str,
        unit_extra_info: UpdatePricingUnitBodyParamsUnitExtraInfo,
        default: bool,
        specific_info: SpecificInfo,
        pricing_unit_cost_update: typing.Optional[PricingUnitCostUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopePricingUnitAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        pricing_unit_id : int

        unit_name : str

        unit_extra_info : UpdatePricingUnitBodyParamsUnitExtraInfo

        default : bool

        specific_info : SpecificInfo

        pricing_unit_cost_update : typing.Optional[PricingUnitCostUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopePricingUnitAdminGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}/pricing-units/{encode_path_param(pricing_unit_id)}",
            method="PUT",
            json={
                "unitName": unit_name,
                "unitExtraInfo": convert_and_respect_annotation_metadata(
                    object_=unit_extra_info, annotation=UpdatePricingUnitBodyParamsUnitExtraInfo, direction="write"
                ),
                "default": default,
                "specificInfo": convert_and_respect_annotation_metadata(
                    object_=specific_info, annotation=SpecificInfo, direction="write"
                ),
                "pricingUnitCostUpdate": convert_and_respect_annotation_metadata(
                    object_=pricing_unit_cost_update,
                    annotation=typing.Optional[PricingUnitCostUpdate],
                    direction="write",
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
                    EnvelopePricingUnitAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingUnitAdminGet,
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

    async def create_pricing_unit(
        self,
        pricing_plan_id: int,
        *,
        unit_name: str,
        unit_extra_info: CreatePricingUnitBodyParamsUnitExtraInfo,
        default: bool,
        specific_info: SpecificInfo,
        cost_per_unit: CreatePricingUnitBodyParamsCostPerUnit,
        comment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopePricingUnitAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        unit_name : str

        unit_extra_info : CreatePricingUnitBodyParamsUnitExtraInfo

        default : bool

        specific_info : SpecificInfo

        cost_per_unit : CreatePricingUnitBodyParamsCostPerUnit

        comment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopePricingUnitAdminGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}/pricing-units",
            method="POST",
            json={
                "unitName": unit_name,
                "unitExtraInfo": convert_and_respect_annotation_metadata(
                    object_=unit_extra_info, annotation=CreatePricingUnitBodyParamsUnitExtraInfo, direction="write"
                ),
                "default": default,
                "specificInfo": convert_and_respect_annotation_metadata(
                    object_=specific_info, annotation=SpecificInfo, direction="write"
                ),
                "costPerUnit": convert_and_respect_annotation_metadata(
                    object_=cost_per_unit, annotation=CreatePricingUnitBodyParamsCostPerUnit, direction="write"
                ),
                "comment": comment,
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
                    EnvelopePricingUnitAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingUnitAdminGet,
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

    async def list_connected_services_to_pricing_plan(
        self, pricing_plan_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListPricingPlanToServiceAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListPricingPlanToServiceAdminGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}/billable-services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListPricingPlanToServiceAdminGet,
                    parse_obj_as(
                        type_=EnvelopeListPricingPlanToServiceAdminGet,
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

    async def connect_service_to_pricing_plan(
        self,
        pricing_plan_id: int,
        *,
        service_key: str,
        service_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopePricingPlanToServiceAdminGet]:
        """
        Parameters
        ----------
        pricing_plan_id : int

        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopePricingPlanToServiceAdminGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/admin/pricing-plans/{encode_path_param(pricing_plan_id)}/billable-services",
            method="POST",
            json={
                "serviceKey": service_key,
                "serviceVersion": service_version,
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
                    EnvelopePricingPlanToServiceAdminGet,
                    parse_obj_as(
                        type_=EnvelopePricingPlanToServiceAdminGet,
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
