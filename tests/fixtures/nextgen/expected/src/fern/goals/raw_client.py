

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.bad_request1 import BadRequest1
from ..types.forbidden1 import Forbidden1
from ..types.ok17 import Ok17
from ..types.ok19 import Ok19
from ..types.ok20 import Ok20
from ..types.ok21 import Ok21
from ..types.ok22 import Ok22
from ..types.ok23 import Ok23
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGoalsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def base_url_persons_person_id_chart_care_plan_goals(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok17]:
        """
        Gets a patient's care plan goals.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose goals are being fetched

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok17]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/care-plan/goals",
            method="GET",
            params={
                "$top": top,
                "$filter": filter,
                "$orderby": orderby,
                "$skip": skip,
                "$inlinecount": inlinecount,
                "$count": count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok17,
                    parse_obj_as(
                        type_=Ok17,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok17]:
        """
        Gets a patient's care plan goals for a specified encounter and health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose goals are being fetched

        encounter_id : str
            (Required) (Required) The id of the patient encounter whose goals are being fetched

        health_concern_id : str
            (Required) (Required) The id of the health concern whose goals are being fetched

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok17]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals",
            method="GET",
            params={
                "$top": top,
                "$filter": filter,
                "$orderby": orderby,
                "$skip": skip,
                "$inlinecount": inlinecount,
                "$count": count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok17,
                    parse_obj_as(
                        type_=Ok17,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Creates a new care plan goal for a patient for specified encounter and health concern

        Parameters
        ----------
        person_id : str
            (Required) (Required) id of the Patient

        encounter_id : str
            (Required) (Required) id of the encounter

        health_concern_id : str
            (Required) (Required) id of Health Concern

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id1(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok19]:
        """
        Gets a patient's care plan goal details.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) The id of the goal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok19]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok19,
                    parse_obj_as(
                        type_=Ok19,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Update patient's careplan goal.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) Encounter id of the patient

        health_concern_id : str
            (Required) (Required) Care plan health concern id of the patient

        goal_id : str
            (Required) (Required) Care plan goal id of the patient

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete a Care Plan Goal

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok20]:
        """
        Returns a list of interventions for the specified person id, encounter id, health concern id and goal id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose interventions are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter whose interventions are being retrieved

        health_concern_id : str
            (Required) (Required) The id of the health concern whose interventions are being retrieved

        goal_id : str
            (Required) (Required) The id of the goal whose interventions are being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok20]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions",
            method="GET",
            params={
                "$top": top,
                "$filter": filter,
                "$orderby": orderby,
                "$skip": skip,
                "$inlinecount": inlinecount,
                "$count": count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok20,
                    parse_obj_as(
                        type_=Ok20,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Add new intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id1(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok21]:
        """
        Gets intervention details based on person id, encounter id, health concern id , goal id and intervention id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose intervention is being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter whose intervention is being retrieved

        health_concern_id : str
            (Required) (Required) The id of the health concern whose intervention is being retrieved

        goal_id : str
            (Required) (Required) The id of the goal whose intervention is being retrieved

        intervention_id : str
            (Required) (Required) The id of the intervention to be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok21]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok21,
                    parse_obj_as(
                        type_=Ok21,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Updates intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) The id of the patient encounter.

        health_concern_id : str
            (Required) (Required) The id of the health concern.

        goal_id : str
            (Required) (Required) Care plan goal id of patient.

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete Patient intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) The id of the goal

        intervention_id : str
            (Required) (Required) The id of the intervention

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok22]:
        """
        Returns a list of care plan outcomes for the specified person, encounter, concern, and goal after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care plan outcomes are being retrieved

        encounter_id : str
            (Required) (Required) Encounter id for outcome

        health_concern_id : str
            (Required) (Required) Care plan health concern id of patient

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok22]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}/outcomes",
            method="GET",
            params={
                "$top": top,
                "$filter": filter,
                "$orderby": orderby,
                "$skip": skip,
                "$inlinecount": inlinecount,
                "$count": count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok22,
                    parse_obj_as(
                        type_=Ok22,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Add new outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}/outcomes",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        expand: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok23]:
        """
        Gets the care plan outcome details for the given outcome id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care plan outcomes are being retrieved

        encounter_id : str
            (Required) (Required) Encounter id for outcome

        health_concern_id : str
            (Required) (Required) Care plan health concern id of patient

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

        outcome_id : str
            (Required) (Required) Care plan outcome id for patient

        expand : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok23]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}/outcomes/{encode_path_param(outcome_id)}",
            method="GET",
            params={
                "$expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok23,
                    parse_obj_as(
                        type_=Ok23,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Updates outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) The id of the patient encounter.

        health_concern_id : str
            (Required) (Required) The id of the health concern.

        goal_id : str
            (Required) (Required) Care plan goal id of patient.

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient.

        outcome_id : str
            (Required) (Required) Care plan outcome id for patient.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}/outcomes/{encode_path_param(outcome_id)}",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id of the patient

        outcome_id : str
            (Required) (Required) Care plan outcome of the patient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}/outcomes/{encode_path_param(outcome_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawGoalsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def base_url_persons_person_id_chart_care_plan_goals(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok17]:
        """
        Gets a patient's care plan goals.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose goals are being fetched

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok17]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/care-plan/goals",
            method="GET",
            params={
                "$top": top,
                "$filter": filter,
                "$orderby": orderby,
                "$skip": skip,
                "$inlinecount": inlinecount,
                "$count": count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok17,
                    parse_obj_as(
                        type_=Ok17,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok17]:
        """
        Gets a patient's care plan goals for a specified encounter and health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose goals are being fetched

        encounter_id : str
            (Required) (Required) The id of the patient encounter whose goals are being fetched

        health_concern_id : str
            (Required) (Required) The id of the health concern whose goals are being fetched

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok17]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals",
            method="GET",
            params={
                "$top": top,
                "$filter": filter,
                "$orderby": orderby,
                "$skip": skip,
                "$inlinecount": inlinecount,
                "$count": count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok17,
                    parse_obj_as(
                        type_=Ok17,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Creates a new care plan goal for a patient for specified encounter and health concern

        Parameters
        ----------
        person_id : str
            (Required) (Required) id of the Patient

        encounter_id : str
            (Required) (Required) id of the encounter

        health_concern_id : str
            (Required) (Required) id of Health Concern

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id1(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok19]:
        """
        Gets a patient's care plan goal details.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) The id of the goal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok19]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok19,
                    parse_obj_as(
                        type_=Ok19,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Update patient's careplan goal.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) Encounter id of the patient

        health_concern_id : str
            (Required) (Required) Care plan health concern id of the patient

        goal_id : str
            (Required) (Required) Care plan goal id of the patient

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete a Care Plan Goal

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok20]:
        """
        Returns a list of interventions for the specified person id, encounter id, health concern id and goal id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose interventions are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter whose interventions are being retrieved

        health_concern_id : str
            (Required) (Required) The id of the health concern whose interventions are being retrieved

        goal_id : str
            (Required) (Required) The id of the goal whose interventions are being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok20]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions",
            method="GET",
            params={
                "$top": top,
                "$filter": filter,
                "$orderby": orderby,
                "$skip": skip,
                "$inlinecount": inlinecount,
                "$count": count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok20,
                    parse_obj_as(
                        type_=Ok20,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Add new intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id1(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok21]:
        """
        Gets intervention details based on person id, encounter id, health concern id , goal id and intervention id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose intervention is being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter whose intervention is being retrieved

        health_concern_id : str
            (Required) (Required) The id of the health concern whose intervention is being retrieved

        goal_id : str
            (Required) (Required) The id of the goal whose intervention is being retrieved

        intervention_id : str
            (Required) (Required) The id of the intervention to be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok21]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok21,
                    parse_obj_as(
                        type_=Ok21,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Updates intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) The id of the patient encounter.

        health_concern_id : str
            (Required) (Required) The id of the health concern.

        goal_id : str
            (Required) (Required) Care plan goal id of patient.

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete Patient intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) The id of the goal

        intervention_id : str
            (Required) (Required) The id of the intervention

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok22]:
        """
        Returns a list of care plan outcomes for the specified person, encounter, concern, and goal after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care plan outcomes are being retrieved

        encounter_id : str
            (Required) (Required) Encounter id for outcome

        health_concern_id : str
            (Required) (Required) Care plan health concern id of patient

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok22]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}/outcomes",
            method="GET",
            params={
                "$top": top,
                "$filter": filter,
                "$orderby": orderby,
                "$skip": skip,
                "$inlinecount": inlinecount,
                "$count": count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok22,
                    parse_obj_as(
                        type_=Ok22,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Add new outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}/outcomes",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        expand: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok23]:
        """
        Gets the care plan outcome details for the given outcome id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care plan outcomes are being retrieved

        encounter_id : str
            (Required) (Required) Encounter id for outcome

        health_concern_id : str
            (Required) (Required) Care plan health concern id of patient

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

        outcome_id : str
            (Required) (Required) Care plan outcome id for patient

        expand : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok23]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}/outcomes/{encode_path_param(outcome_id)}",
            method="GET",
            params={
                "$expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok23,
                    parse_obj_as(
                        type_=Ok23,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Updates outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) The id of the patient encounter.

        health_concern_id : str
            (Required) (Required) The id of the health concern.

        goal_id : str
            (Required) (Required) Care plan goal id of patient.

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient.

        outcome_id : str
            (Required) (Required) Care plan outcome id for patient.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}/outcomes/{encode_path_param(outcome_id)}",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id of the patient

        outcome_id : str
            (Required) (Required) Care plan outcome of the patient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/care-plan/health-concerns/{encode_path_param(health_concern_id)}/goals/{encode_path_param(goal_id)}/interventions/{encode_path_param(intervention_id)}/outcomes/{encode_path_param(outcome_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest1,
                        parse_obj_as(
                            type_=BadRequest1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Forbidden1,
                        parse_obj_as(
                            type_=Forbidden1,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
