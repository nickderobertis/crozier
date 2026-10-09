

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
from ..types.harbor_berth_assignment import HarborBerthAssignment
from ..types.harbor_event import HarborEvent
from ..types.harbor_voyage import HarborVoyage
from .types.create_mooring_permit_request_vessel import CreateMooringPermitRequestVessel
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawHarborClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_berth_assignment(
        self,
        harbor_id: str,
        *,
        harbor_berth_assignment_create_harbor_id: str,
        vessel_name: str,
        stay_hours: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HarborBerthAssignment]:
        """
        Parameters
        ----------
        harbor_id : str

        harbor_berth_assignment_create_harbor_id : str

        vessel_name : str

        stay_hours : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HarborBerthAssignment]
            The created berth assignment.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"harbor/{encode_path_param(harbor_id)}/berth-assignments",
            method="POST",
            json={
                "harbor_id": harbor_berth_assignment_create_harbor_id,
                "vessel_name": vessel_name,
                "stay_hours": stay_hours,
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
                    HarborBerthAssignment,
                    parse_obj_as(
                        type_=HarborBerthAssignment,
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

    def create_voyage(
        self,
        harbor_id: str,
        *,
        harbor_voyage_create_harbor_id: str,
        route: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HarborVoyage]:
        """
        Parameters
        ----------
        harbor_id : str

        harbor_voyage_create_harbor_id : str

        route : str

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HarborVoyage]
            The created voyage.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"harbor/{encode_path_param(harbor_id)}/voyages",
            method="POST",
            json={
                "harbor_id": harbor_voyage_create_harbor_id,
                "route": route,
                "tags": tags,
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
                    HarborVoyage,
                    parse_obj_as(
                        type_=HarborVoyage,
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

    def create_mooring_permit(
        self,
        harbor_id: str,
        *,
        mooring_permit_harbor_id: str,
        vessel: typing.Optional[CreateMooringPermitRequestVessel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HarborEvent]:
        """
        Parameters
        ----------
        harbor_id : str

        mooring_permit_harbor_id : str

        vessel : typing.Optional[CreateMooringPermitRequestVessel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HarborEvent]
            The created permit's events.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"harbor/{encode_path_param(harbor_id)}/mooring-permits",
            method="POST",
            json={
                "harbor_id": mooring_permit_harbor_id,
                "vessel": convert_and_respect_annotation_metadata(
                    object_=vessel, annotation=CreateMooringPermitRequestVessel, direction="write"
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
                    HarborEvent,
                    parse_obj_as(
                        type_=HarborEvent,
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

    def create_log_entry(
        self,
        harbor_id: str,
        *,
        log_entry_harbor_id: str,
        body: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        harbor_id : str

        log_entry_harbor_id : str

        body : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"harbor/{encode_path_param(harbor_id)}/log-entries",
            method="POST",
            data={
                "harbor_id": log_entry_harbor_id,
                "body": body,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawHarborClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_berth_assignment(
        self,
        harbor_id: str,
        *,
        harbor_berth_assignment_create_harbor_id: str,
        vessel_name: str,
        stay_hours: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HarborBerthAssignment]:
        """
        Parameters
        ----------
        harbor_id : str

        harbor_berth_assignment_create_harbor_id : str

        vessel_name : str

        stay_hours : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HarborBerthAssignment]
            The created berth assignment.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"harbor/{encode_path_param(harbor_id)}/berth-assignments",
            method="POST",
            json={
                "harbor_id": harbor_berth_assignment_create_harbor_id,
                "vessel_name": vessel_name,
                "stay_hours": stay_hours,
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
                    HarborBerthAssignment,
                    parse_obj_as(
                        type_=HarborBerthAssignment,
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

    async def create_voyage(
        self,
        harbor_id: str,
        *,
        harbor_voyage_create_harbor_id: str,
        route: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HarborVoyage]:
        """
        Parameters
        ----------
        harbor_id : str

        harbor_voyage_create_harbor_id : str

        route : str

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HarborVoyage]
            The created voyage.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"harbor/{encode_path_param(harbor_id)}/voyages",
            method="POST",
            json={
                "harbor_id": harbor_voyage_create_harbor_id,
                "route": route,
                "tags": tags,
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
                    HarborVoyage,
                    parse_obj_as(
                        type_=HarborVoyage,
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

    async def create_mooring_permit(
        self,
        harbor_id: str,
        *,
        mooring_permit_harbor_id: str,
        vessel: typing.Optional[CreateMooringPermitRequestVessel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HarborEvent]:
        """
        Parameters
        ----------
        harbor_id : str

        mooring_permit_harbor_id : str

        vessel : typing.Optional[CreateMooringPermitRequestVessel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HarborEvent]
            The created permit's events.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"harbor/{encode_path_param(harbor_id)}/mooring-permits",
            method="POST",
            json={
                "harbor_id": mooring_permit_harbor_id,
                "vessel": convert_and_respect_annotation_metadata(
                    object_=vessel, annotation=CreateMooringPermitRequestVessel, direction="write"
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
                    HarborEvent,
                    parse_obj_as(
                        type_=HarborEvent,
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

    async def create_log_entry(
        self,
        harbor_id: str,
        *,
        log_entry_harbor_id: str,
        body: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        harbor_id : str

        log_entry_harbor_id : str

        body : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"harbor/{encode_path_param(harbor_id)}/log-entries",
            method="POST",
            data={
                "harbor_id": log_entry_harbor_id,
                "body": body,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
