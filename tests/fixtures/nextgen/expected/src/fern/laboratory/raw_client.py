

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
from ..types.ok41 import Ok41
from ..types.ok53 import Ok53
from ..types.ok54 import Ok54
from ..types.ok56 import Ok56
from ..types.ok57 import Ok57
from ..types.ok58 import Ok58
from ..types.ok59 import Ok59
from ..types.ok60 import Ok60
from ..types.ok61 import Ok61
from ..types.ok63 import Ok63
from ..types.ok64 import Ok64
from ..types.ok65 import Ok65
from ..types.ok66 import Ok66
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLaboratoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def base_url_persons_person_id_chart_encounters_encounter_id_lab_orders(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok53]:
        """
        Adds a new lab order for the given person id and encounter id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient to add the new lab order for.

        encounter_id : str
            (Required) (Required) The id of the encounter to add the new lab order to.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok53]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/lab/orders",
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
                    Ok53,
                    parse_obj_as(
                        type_=Ok53,
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

    def base_url_persons_person_id_chart_lab_orders(
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
    ) -> HttpResponse[Ok54]:
        """
        Gets a list of lab order summaries for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose lab orders are being retrieved

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
        HttpResponse[Ok54]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders",
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
                    Ok54,
                    parse_obj_as(
                        type_=Ok54,
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

    def base_url_persons_person_id_chart_lab_orders_order_id1(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Ok53]:
        """
        Gets the lab order details for the given person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose lab orders are being retrieved

        order_id : str
            (Required) (Required) The id of the lab order being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok53]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok53,
                    parse_obj_as(
                        type_=Ok53,
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

    def put_base_url_persons_person_id_chart_lab_orders_order_id(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Update the specified lab order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is to be updated.

        order_id : str
            (Required) (Required) The id of the order that is to be updated.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}",
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

    def base_url_persons_person_id_chart_lab_orders_order_id(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete the specified order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is to be deleted.

        order_id : str
            (Required) (Required) The id of the order that is to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}",
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

    def base_url_persons_person_id_chart_lab_orders_order_id_insurances(
        self,
        person_id: str,
        order_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok56]:
        """
        Get a list of insurances that are associated with the specified person Id and order Id after apply additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom the order insurances are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order for which the insurances are being retrieved.

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
        HttpResponse[Ok56]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/insurances",
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
                    Ok56,
                    parse_obj_as(
                        type_=Ok56,
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

    def base_url_persons_person_id_chart_lab_orders_order_id_schedule(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Ok57]:
        """
        Get the schedule details for the specified person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order schedule is being retrieved.

        order_id : str
            (Required) (Required) The id of the order whose schedule is being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok57]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/schedule",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok57,
                    parse_obj_as(
                        type_=Ok57,
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

    def post_base_url_persons_person_id_chart_lab_orders_order_id_schedule(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Set the schedule for the specified person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is being scheduled.

        order_id : str
            (Required) (Required) The id of the order that is being scheduled.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/schedule",
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

    def base_url_persons_person_id_chart_lab_orders_order_id_send(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds a record to the interface queue with the provided order Id and lab interface agent information that is determined based on the order's lab Id. This route does not control when the order will be processed and sent out to the lab which is controlled by the interface.

        Parameters
        ----------
        person_id : str
            (Required) (Required) Id of the person whose order is being sent to interface

        order_id : str
            (Required) (Required) Id of the lab order which is being sent to interface

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/send",
            method="POST",
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

    def base_url_persons_person_id_chart_lab_orders_order_id_tests(
        self,
        person_id: str,
        order_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok58]:
        """
        Gets a list of ordered test summaries for the specified person id and order id after apply additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose ordered tests are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order for which the ordered tests are being retrieved.

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
        HttpResponse[Ok58]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests",
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
                    Ok58,
                    parse_obj_as(
                        type_=Ok58,
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

    def post_base_url_persons_person_id_chart_lab_orders_order_id_tests(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Add a lab test to the specified order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person where the new lab test will be added to the order.

        order_id : str
            (Required) (Required) The id of the order where the new lab test will be added.

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests",
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

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id1(
        self, person_id: str, order_id: str, test_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Ok59]:
        """
        Gets the ordered test for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient to retrieve the ordered test for.

        order_id : str
            (Required) (Required) The id of the lab order which contains the test that were ordered.

        test_id : str
            (Required) (Required) The id of the ordered test being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok59]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok59,
                    parse_obj_as(
                        type_=Ok59,
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

    def put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Updates the specified order test for the specified person and order.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered test is to be updated.

        order_id : str
            (Required) (Required) The id of the order whose ordered test is to be updated.

        test_id : str
            (Required) (Required) The id of the ordered test that is to be updated.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}",
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

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
        self, person_id: str, order_id: str, test_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Deletes the specified ordered test for the person and order.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered test will be deleted.

        order_id : str
            (Required) (Required) The id of the order whose ordered test will be deleted.

        test_id : str
            (Required) (Required) The id of the order test to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}",
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

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok60]:
        """
        Gets a list of order entry answers for the specified person id, order id and test id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answers are being retrieved.

        order_id : str
            (Required) (Required) The id of the order whose order entry answers are being retrieved.

        test_id : str
            (Required) (Required) The id of the ordered test whose order entry answers are being retrieved.

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
        HttpResponse[Ok60]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/order-entry-answers",
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
                    Ok60,
                    parse_obj_as(
                        type_=Ok60,
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

    def post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds an answer to an order entry question for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) This id of the person whose order entry answer is to be added.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is to be added.

        test_id : str
            (Required) (Required) The id of the ordered test whose order entry answer is to be added.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/order-entry-answers",
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

    def put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        answer_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Updates the specifed order entry answer for the specified person id, order id, test id and answer id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answer is being updated.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is being updated.

        test_id : str
            (Required) (Required) The id of the ordered test id whose order entry answer is being udpated.

        answer_id : str
            (Required) (Required) The id of the order entry answer to update.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/order-entry-answers/{encode_path_param(answer_id)}",
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

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        answer_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete the specified order entry answer for the specified person id, order id and ordered test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answer is being deleted.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is being deleted.

        test_id : str
            (Required) (Required) The id of the ordered test id whose order entry answer is being deleted.

        answer_id : str
            (Required) (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/order-entry-answers/{encode_path_param(answer_id)}",
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

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ok61]:
        """
        Get a list of suspected diagnosis for the specified ordered test id after applying addition OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose suspected diagnoses are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order which contains the test whose suspected diagnosis are beign retrieved.

        test_id : str
            (Required) (Required) The id of the ordered test whose suspected diagnosis are being retrieved.

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
        HttpResponse[Ok61]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/suspected-diagnoses",
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
                    Ok61,
                    parse_obj_as(
                        type_=Ok61,
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

    def post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds a suspected diagnosis for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the suspected diagnosis will be added.

        order_id : str
            (Required) (Required) The id of the order for which the suspected diagnosis will be added.

        test_id : str
            (Required) (Required) The id of the ordered test for which the suspected diagnosis will be added.

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/suspected-diagnoses",
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

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_diagnosis_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        diagnosis_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete the specified suspected diagnosis for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose suspected diagnosis is to be deleted.

        order_id : str
            (Required) (Required) The id of the order whose suspected diagnosis is to be deleted.

        test_id : str
            (Required) (Required) The id of the ordered test whose suspected diagnosis is to be deleted.

        diagnosis_id : str
            (Required) (Required) The id of the suspected diagnosis to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/suspected-diagnoses/{encode_path_param(diagnosis_id)}",
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

    def base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Ok41]:
        """
        Gets a list of tracking comments for the given person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to

        order_id : str
            (Required) (Required) The id of the order whose tracking comments are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok41]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tracking-comments",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok41,
                    parse_obj_as(
                        type_=Ok41,
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

    def post_base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds a tracking comment for the given person id and lab order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to.

        order_id : str
            (Required) (Required) The id of the lab order which the tracking comment will be added for.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tracking-comments",
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

    def base_url_persons_person_id_chart_lab_panels(
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
    ) -> HttpResponse[Ok63]:
        """
        Gets a list of observation panels for the specified person id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom the observation panels are being retrieved.

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
        HttpResponse[Ok63]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels",
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
                    Ok63,
                    parse_obj_as(
                        type_=Ok63,
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

    def post_base_url_persons_person_id_chart_lab_panels(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds an observation panel the specified person.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person to add the observation panel for.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels",
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

    def base_url_persons_person_id_chart_lab_panels_panel_id1(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Ok64]:
        """
        Gets an observation panel for the specified person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is being retrieved.

        panel_id : str
            (Required) (Required) The id of the observation panel being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok64]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok64,
                    parse_obj_as(
                        type_=Ok64,
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

    def put_base_url_persons_person_id_chart_lab_panels_panel_id(
        self,
        person_id: str,
        panel_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Update the specified observation panel for the specified personId.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is to be updated.

        panel_id : str
            (Required) (Required) The id of the panel to be updated.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}",
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

    def base_url_persons_person_id_chart_lab_panels_panel_id(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete the specified observation panel for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is to be deleted.

        panel_id : str
            (Required) (Required) The id of the observation panel to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}",
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

    def base_url_persons_person_id_chart_lab_panels_panel_id_results(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Ok65]:
        """
        Gets a list of observation results for the specified person id and observation panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation results are being retrieved.

        panel_id : str
            (Required) (Required) The id of the observation panel for whose observation results are being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ok65]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}/results",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok65,
                    parse_obj_as(
                        type_=Ok65,
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

    def post_base_url_persons_person_id_chart_lab_panels_panel_id_results(
        self,
        person_id: str,
        panel_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds observation results for the specified person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person to add observation results for.

        panel_id : str
            (Required) (Required) The id of the observation panel to add results to.

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}/results",
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

    def put_base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
        self,
        person_id: str,
        panel_id: str,
        sequence_number: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Update the specified observation result for the specifed person id, panel id and sequenceNumber.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of person whose observation result is to be updated.

        panel_id : str
            (Required) (Required) The id of the panel whose observation result is to be updated.

        sequence_number : str
            (Required) (Required) The observation result sequence number that is to be updated.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}/results/{encode_path_param(sequence_number)}",
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

    def base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
        self,
        person_id: str,
        panel_id: str,
        sequence_number: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete the specified observation result for the specifed person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of person whose observation result is to be deleted.

        panel_id : str
            (Required) (Required) The id of the panel whose observation result is to be deleted.

        sequence_number : str
            (Required) (Required) The observation result sequence number that is to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}/results/{encode_path_param(sequence_number)}",
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

    def base_url_persons_person_id_chart_lab_results(
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
    ) -> HttpResponse[Ok66]:
        """
        Gets a list of observation results for the specified person id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation results are being retrieved.

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
        HttpResponse[Ok66]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/results",
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
                    Ok66,
                    parse_obj_as(
                        type_=Ok66,
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


class AsyncRawLaboratoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def base_url_persons_person_id_chart_encounters_encounter_id_lab_orders(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok53]:
        """
        Adds a new lab order for the given person id and encounter id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient to add the new lab order for.

        encounter_id : str
            (Required) (Required) The id of the encounter to add the new lab order to.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok53]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/encounters/{encode_path_param(encounter_id)}/lab/orders",
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
                    Ok53,
                    parse_obj_as(
                        type_=Ok53,
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

    async def base_url_persons_person_id_chart_lab_orders(
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
    ) -> AsyncHttpResponse[Ok54]:
        """
        Gets a list of lab order summaries for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose lab orders are being retrieved

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
        AsyncHttpResponse[Ok54]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders",
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
                    Ok54,
                    parse_obj_as(
                        type_=Ok54,
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

    async def base_url_persons_person_id_chart_lab_orders_order_id1(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Ok53]:
        """
        Gets the lab order details for the given person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose lab orders are being retrieved

        order_id : str
            (Required) (Required) The id of the lab order being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok53]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok53,
                    parse_obj_as(
                        type_=Ok53,
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

    async def put_base_url_persons_person_id_chart_lab_orders_order_id(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Update the specified lab order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is to be updated.

        order_id : str
            (Required) (Required) The id of the order that is to be updated.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete the specified order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is to be deleted.

        order_id : str
            (Required) (Required) The id of the order that is to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_insurances(
        self,
        person_id: str,
        order_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok56]:
        """
        Get a list of insurances that are associated with the specified person Id and order Id after apply additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom the order insurances are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order for which the insurances are being retrieved.

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
        AsyncHttpResponse[Ok56]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/insurances",
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
                    Ok56,
                    parse_obj_as(
                        type_=Ok56,
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_schedule(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Ok57]:
        """
        Get the schedule details for the specified person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order schedule is being retrieved.

        order_id : str
            (Required) (Required) The id of the order whose schedule is being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok57]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/schedule",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok57,
                    parse_obj_as(
                        type_=Ok57,
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

    async def post_base_url_persons_person_id_chart_lab_orders_order_id_schedule(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Set the schedule for the specified person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is being scheduled.

        order_id : str
            (Required) (Required) The id of the order that is being scheduled.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/schedule",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_send(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds a record to the interface queue with the provided order Id and lab interface agent information that is determined based on the order's lab Id. This route does not control when the order will be processed and sent out to the lab which is controlled by the interface.

        Parameters
        ----------
        person_id : str
            (Required) (Required) Id of the person whose order is being sent to interface

        order_id : str
            (Required) (Required) Id of the lab order which is being sent to interface

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/send",
            method="POST",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests(
        self,
        person_id: str,
        order_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok58]:
        """
        Gets a list of ordered test summaries for the specified person id and order id after apply additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose ordered tests are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order for which the ordered tests are being retrieved.

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
        AsyncHttpResponse[Ok58]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests",
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
                    Ok58,
                    parse_obj_as(
                        type_=Ok58,
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

    async def post_base_url_persons_person_id_chart_lab_orders_order_id_tests(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Add a lab test to the specified order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person where the new lab test will be added to the order.

        order_id : str
            (Required) (Required) The id of the order where the new lab test will be added.

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id1(
        self, person_id: str, order_id: str, test_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Ok59]:
        """
        Gets the ordered test for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient to retrieve the ordered test for.

        order_id : str
            (Required) (Required) The id of the lab order which contains the test that were ordered.

        test_id : str
            (Required) (Required) The id of the ordered test being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok59]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok59,
                    parse_obj_as(
                        type_=Ok59,
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

    async def put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Updates the specified order test for the specified person and order.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered test is to be updated.

        order_id : str
            (Required) (Required) The id of the order whose ordered test is to be updated.

        test_id : str
            (Required) (Required) The id of the ordered test that is to be updated.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
        self, person_id: str, order_id: str, test_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Deletes the specified ordered test for the person and order.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered test will be deleted.

        order_id : str
            (Required) (Required) The id of the order whose ordered test will be deleted.

        test_id : str
            (Required) (Required) The id of the order test to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok60]:
        """
        Gets a list of order entry answers for the specified person id, order id and test id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answers are being retrieved.

        order_id : str
            (Required) (Required) The id of the order whose order entry answers are being retrieved.

        test_id : str
            (Required) (Required) The id of the ordered test whose order entry answers are being retrieved.

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
        AsyncHttpResponse[Ok60]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/order-entry-answers",
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
                    Ok60,
                    parse_obj_as(
                        type_=Ok60,
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

    async def post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds an answer to an order entry question for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) This id of the person whose order entry answer is to be added.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is to be added.

        test_id : str
            (Required) (Required) The id of the ordered test whose order entry answer is to be added.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/order-entry-answers",
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

    async def put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        answer_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Updates the specifed order entry answer for the specified person id, order id, test id and answer id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answer is being updated.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is being updated.

        test_id : str
            (Required) (Required) The id of the ordered test id whose order entry answer is being udpated.

        answer_id : str
            (Required) (Required) The id of the order entry answer to update.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/order-entry-answers/{encode_path_param(answer_id)}",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        answer_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete the specified order entry answer for the specified person id, order id and ordered test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answer is being deleted.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is being deleted.

        test_id : str
            (Required) (Required) The id of the ordered test id whose order entry answer is being deleted.

        answer_id : str
            (Required) (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/order-entry-answers/{encode_path_param(answer_id)}",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ok61]:
        """
        Get a list of suspected diagnosis for the specified ordered test id after applying addition OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose suspected diagnoses are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order which contains the test whose suspected diagnosis are beign retrieved.

        test_id : str
            (Required) (Required) The id of the ordered test whose suspected diagnosis are being retrieved.

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
        AsyncHttpResponse[Ok61]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/suspected-diagnoses",
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
                    Ok61,
                    parse_obj_as(
                        type_=Ok61,
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

    async def post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds a suspected diagnosis for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the suspected diagnosis will be added.

        order_id : str
            (Required) (Required) The id of the order for which the suspected diagnosis will be added.

        test_id : str
            (Required) (Required) The id of the ordered test for which the suspected diagnosis will be added.

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/suspected-diagnoses",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_diagnosis_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        diagnosis_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete the specified suspected diagnosis for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose suspected diagnosis is to be deleted.

        order_id : str
            (Required) (Required) The id of the order whose suspected diagnosis is to be deleted.

        test_id : str
            (Required) (Required) The id of the ordered test whose suspected diagnosis is to be deleted.

        diagnosis_id : str
            (Required) (Required) The id of the suspected diagnosis to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tests/{encode_path_param(test_id)}/suspected-diagnoses/{encode_path_param(diagnosis_id)}",
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

    async def base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Ok41]:
        """
        Gets a list of tracking comments for the given person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to

        order_id : str
            (Required) (Required) The id of the order whose tracking comments are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok41]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tracking-comments",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok41,
                    parse_obj_as(
                        type_=Ok41,
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

    async def post_base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds a tracking comment for the given person id and lab order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to.

        order_id : str
            (Required) (Required) The id of the lab order which the tracking comment will be added for.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/orders/{encode_path_param(order_id)}/tracking-comments",
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

    async def base_url_persons_person_id_chart_lab_panels(
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
    ) -> AsyncHttpResponse[Ok63]:
        """
        Gets a list of observation panels for the specified person id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom the observation panels are being retrieved.

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
        AsyncHttpResponse[Ok63]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels",
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
                    Ok63,
                    parse_obj_as(
                        type_=Ok63,
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

    async def post_base_url_persons_person_id_chart_lab_panels(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds an observation panel the specified person.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person to add the observation panel for.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels",
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

    async def base_url_persons_person_id_chart_lab_panels_panel_id1(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Ok64]:
        """
        Gets an observation panel for the specified person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is being retrieved.

        panel_id : str
            (Required) (Required) The id of the observation panel being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok64]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok64,
                    parse_obj_as(
                        type_=Ok64,
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

    async def put_base_url_persons_person_id_chart_lab_panels_panel_id(
        self,
        person_id: str,
        panel_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Update the specified observation panel for the specified personId.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is to be updated.

        panel_id : str
            (Required) (Required) The id of the panel to be updated.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}",
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

    async def base_url_persons_person_id_chart_lab_panels_panel_id(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete the specified observation panel for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is to be deleted.

        panel_id : str
            (Required) (Required) The id of the observation panel to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}",
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

    async def base_url_persons_person_id_chart_lab_panels_panel_id_results(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Ok65]:
        """
        Gets a list of observation results for the specified person id and observation panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation results are being retrieved.

        panel_id : str
            (Required) (Required) The id of the observation panel for whose observation results are being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ok65]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}/results",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ok65,
                    parse_obj_as(
                        type_=Ok65,
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

    async def post_base_url_persons_person_id_chart_lab_panels_panel_id_results(
        self,
        person_id: str,
        panel_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Adds observation results for the specified person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person to add observation results for.

        panel_id : str
            (Required) (Required) The id of the observation panel to add results to.

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}/results",
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

    async def put_base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
        self,
        person_id: str,
        panel_id: str,
        sequence_number: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Update the specified observation result for the specifed person id, panel id and sequenceNumber.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of person whose observation result is to be updated.

        panel_id : str
            (Required) (Required) The id of the panel whose observation result is to be updated.

        sequence_number : str
            (Required) (Required) The observation result sequence number that is to be updated.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}/results/{encode_path_param(sequence_number)}",
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

    async def base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
        self,
        person_id: str,
        panel_id: str,
        sequence_number: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete the specified observation result for the specifed person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of person whose observation result is to be deleted.

        panel_id : str
            (Required) (Required) The id of the panel whose observation result is to be deleted.

        sequence_number : str
            (Required) (Required) The observation result sequence number that is to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/panels/{encode_path_param(panel_id)}/results/{encode_path_param(sequence_number)}",
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

    async def base_url_persons_person_id_chart_lab_results(
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
    ) -> AsyncHttpResponse[Ok66]:
        """
        Gets a list of observation results for the specified person id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation results are being retrieved.

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
        AsyncHttpResponse[Ok66]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"persons/{encode_path_param(person_id)}/chart/lab/results",
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
                    Ok66,
                    parse_obj_as(
                        type_=Ok66,
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
