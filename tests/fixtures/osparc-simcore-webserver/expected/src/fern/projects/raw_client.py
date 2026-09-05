

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
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.boot_options import BootOptions
from ..types.conversation_message_type import ConversationMessageType
from ..types.conversation_type import ConversationType
from ..types.envelope_conversation_message_rest_get import EnvelopeConversationMessageRestGet
from ..types.envelope_conversation_rest_get import EnvelopeConversationRestGet
from ..types.envelope_dict_annotated_str_string_constraints_image_resources import (
    EnvelopeDictAnnotatedStrStringConstraintsImageResources,
)
from ..types.envelope_dict_uuid_project_input_get import EnvelopeDictUuidProjectInputGet
from ..types.envelope_dict_uuid_project_output_get import EnvelopeDictUuidProjectOutputGet
from ..types.envelope_get_project_inactivity_response import EnvelopeGetProjectInactivityResponse
from ..types.envelope_list_project_group_get import EnvelopeListProjectGroupGet
from ..types.envelope_list_project_metadata_port_get import EnvelopeListProjectMetadataPortGet
from ..types.envelope_list_project_node_preview import EnvelopeListProjectNodePreview
from ..types.envelope_node_created import EnvelopeNodeCreated
from ..types.envelope_node_retrieved import EnvelopeNodeRetrieved
from ..types.envelope_project_get import EnvelopeProjectGet
from ..types.envelope_project_group_access import EnvelopeProjectGroupAccess
from ..types.envelope_project_group_get import EnvelopeProjectGroupGet
from ..types.envelope_project_metadata_get import EnvelopeProjectMetadataGet
from ..types.envelope_project_node_preview import EnvelopeProjectNodePreview
from ..types.envelope_project_node_services_get import EnvelopeProjectNodeServicesGet
from ..types.envelope_project_share_accepted import EnvelopeProjectShareAccepted
from ..types.envelope_project_state_output_schema import EnvelopeProjectStateOutputSchema
from ..types.envelope_task_get import EnvelopeTaskGet
from ..types.envelope_union_node_get_idle_node_get_unknown_running_dynamic_service_details_node_get import (
    EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet,
)
from ..types.envelope_union_pricing_unit_get_none_type import EnvelopeUnionPricingUnitGetNoneType
from ..types.envelope_union_wallet_get_none_type import EnvelopeUnionWalletGetNoneType
from ..types.envelope_wallet_get import EnvelopeWalletGet
from ..types.group_id_int import GroupIdInt
from ..types.input_id import InputId
from ..types.inputs_dict_input import InputsDictInput
from ..types.long_truncated_str import LongTruncatedStr
from ..types.node_ui_patch import NodeUiPatch
from ..types.page_conversation_message_rest_get import PageConversationMessageRestGet
from ..types.page_conversation_rest_get import PageConversationRestGet
from ..types.page_project_list_item import PageProjectListItem
from ..types.project_input_update import ProjectInputUpdate
from ..types.project_template_type import ProjectTemplateType
from ..types.project_type_api import ProjectTypeApi
from ..types.short_truncated_str import ShortTruncatedStr
from ..types.study_ui_input import StudyUiInput
from ..types.unit_str import UnitStr
from ..types.wallet_id_int import WalletIdInt
from .types.create_project_request_body import CreateProjectRequestBody
from .types.pay_project_debt_request_amount import PayProjectDebtRequestAmount
from .types.project_metadata_update_custom_value import ProjectMetadataUpdateCustomValue
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def export_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        creates an archive of the project and downloads it

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}:xport",
            method="POST",
            request_options=request_options,
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

    def list_projects(
        self,
        *,
        type: typing.Optional[ProjectTypeApi] = None,
        template_type: typing.Optional[ProjectTemplateType] = None,
        show_hidden: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        folder_id: typing.Optional[int] = None,
        workspace_id: typing.Optional[int] = None,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageProjectListItem]:
        """
        Parameters
        ----------
        type : typing.Optional[ProjectTypeApi]

        template_type : typing.Optional[ProjectTemplateType]

        show_hidden : typing.Optional[bool]

        search : typing.Optional[str]

        folder_id : typing.Optional[int]

        workspace_id : typing.Optional[int]

        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageProjectListItem]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/projects",
            method="GET",
            params={
                "type": type,
                "template_type": template_type,
                "show_hidden": show_hidden,
                "search": search,
                "folder_id": folder_id,
                "workspace_id": workspace_id,
                "filters": filters,
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageProjectListItem,
                    parse_obj_as(
                        type_=PageProjectListItem,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def create_project(
        self,
        *,
        request: CreateProjectRequestBody,
        x_simcore_user_agent: typing.Optional[str] = None,
        x_simcore_parent_project_uuid: typing.Optional[str] = None,
        x_simcore_parent_node_id: typing.Optional[str] = None,
        from_study: typing.Optional[str] = None,
        as_template: typing.Optional[bool] = None,
        copy_data: typing.Optional[bool] = None,
        hidden: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeTaskGet]:
        """
        Creates a new project or copies an existing one. NOTE: implemented as a long running task, i.e. requires polling `status_href` (HTTP_200_OK) to get status and `result_href` (HTTP_201_CREATED) to get created project

        Parameters
        ----------
        request : CreateProjectRequestBody

        x_simcore_user_agent : typing.Optional[str]

        x_simcore_parent_project_uuid : typing.Optional[str]

        x_simcore_parent_node_id : typing.Optional[str]

        from_study : typing.Optional[str]

        as_template : typing.Optional[bool]

        copy_data : typing.Optional[bool]

        hidden : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/projects",
            method="POST",
            params={
                "x_simcore_user_agent": x_simcore_user_agent,
                "x_simcore_parent_project_uuid": x_simcore_parent_project_uuid,
                "x_simcore_parent_node_id": x_simcore_parent_node_id,
                "from_study": from_study,
                "as_template": as_template,
                "copy_data": copy_data,
                "hidden": hidden,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateProjectRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_active_project(
        self, *, client_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProjectGet]:
        """
        Parameters
        ----------
        client_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/projects/active",
            method="GET",
            params={
                "client_session_id": client_session_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProjectGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def delete_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}",
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def patch_project(
        self,
        project_id: str,
        *,
        name: typing.Optional[ShortTruncatedStr] = OMIT,
        description: typing.Optional[LongTruncatedStr] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        classifiers: typing.Optional[typing.Sequence[str]] = OMIT,
        dev: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ui: typing.Optional[StudyUiInput] = OMIT,
        quality: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        template_type: typing.Optional[ProjectTemplateType] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        name : typing.Optional[ShortTruncatedStr]

        description : typing.Optional[LongTruncatedStr]

        thumbnail : typing.Optional[str]

        classifiers : typing.Optional[typing.Sequence[str]]

        dev : typing.Optional[typing.Dict[str, typing.Any]]

        ui : typing.Optional[StudyUiInput]

        quality : typing.Optional[typing.Dict[str, typing.Any]]

        template_type : typing.Optional[ProjectTemplateType]

        hidden : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "thumbnail": thumbnail,
                "classifiers": classifiers,
                "dev": dev,
                "ui": convert_and_respect_annotation_metadata(
                    object_=ui, annotation=typing.Optional[StudyUiInput], direction="write"
                ),
                "quality": quality,
                "templateType": template_type,
                "hidden": hidden,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def clone_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeTaskGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}:clone",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def list_projects_full_search(
        self,
        *,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[ProjectTypeApi] = None,
        template_type: typing.Optional[ProjectTemplateType] = None,
        text: typing.Optional[str] = None,
        tag_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageProjectListItem]:
        """
        Parameters
        ----------
        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        type : typing.Optional[ProjectTypeApi]

        template_type : typing.Optional[ProjectTemplateType]

        text : typing.Optional[str]

        tag_ids : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageProjectListItem]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/projects:search",
            method="GET",
            params={
                "filters": filters,
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
                "type": type,
                "template_type": template_type,
                "text": text,
                "tag_ids": tag_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageProjectListItem,
                    parse_obj_as(
                        type_=PageProjectListItem,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_project_inactivity(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeGetProjectInactivityResponse]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeGetProjectInactivityResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/inactivity",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGetProjectInactivityResponse,
                    parse_obj_as(
                        type_=EnvelopeGetProjectInactivityResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def share_project(
        self,
        project_id: str,
        *,
        sharee_email: str,
        read: bool,
        write: bool,
        delete: bool,
        sharer_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeProjectShareAccepted]:
        """
        Parameters
        ----------
        project_id : str

        sharee_email : str

        read : bool

        write : bool

        delete : bool

        sharer_message : typing.Optional[str]
            An optional message from sharer to sharee

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectShareAccepted]
            The request to share the project has been accepted, but the actual sharing process has to be confirmed.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}:share",
            method="POST",
            json={
                "shareeEmail": sharee_email,
                "sharerMessage": sharer_message,
                "read": read,
                "write": write,
                "delete": delete,
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
                    EnvelopeProjectShareAccepted,
                    parse_obj_as(
                        type_=EnvelopeProjectShareAccepted,
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

    def create_project_group(
        self,
        project_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeProjectGroupGet]:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectGroupGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/groups/{encode_path_param(group_id)}",
            method="POST",
            json={
                "read": read,
                "write": write,
                "delete": delete,
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
                    EnvelopeProjectGroupGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGroupGet,
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

    def replace_project_group(
        self,
        project_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeProjectGroupGet]:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectGroupGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/groups/{encode_path_param(group_id)}",
            method="PUT",
            json={
                "read": read,
                "write": write,
                "delete": delete,
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
                    EnvelopeProjectGroupGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGroupGet,
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

    def delete_project_group(
        self, project_id: str, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
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

    def list_project_groups(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListProjectGroupGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListProjectGroupGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/groups",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListProjectGroupGet,
                    parse_obj_as(
                        type_=EnvelopeListProjectGroupGet,
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

    def list_project_conversations(
        self,
        project_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageConversationRestGet]:
        """
        Parameters
        ----------
        project_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageConversationRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations",
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
                    PageConversationRestGet,
                    parse_obj_as(
                        type_=PageConversationRestGet,
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

    def create_project_conversation(
        self,
        project_id: str,
        *,
        name: str,
        type: ConversationType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        project_id : str

        name : str

        type : ConversationType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations",
            method="POST",
            json={
                "name": name,
                "type": type,
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
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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

    def get_project_conversation(
        self, project_id: str, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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

    def update_project_conversation(
        self,
        project_id: str,
        conversation_id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}",
            method="PUT",
            json={
                "name": name,
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
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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

    def delete_project_conversation(
        self, project_id: str, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}",
            method="DELETE",
            request_options=request_options,
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

    def list_project_conversation_messages(
        self,
        project_id: str,
        conversation_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageConversationMessageRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageConversationMessageRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}/messages",
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
                    PageConversationMessageRestGet,
                    parse_obj_as(
                        type_=PageConversationMessageRestGet,
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

    def create_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        *,
        content: str,
        type: ConversationMessageType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        content : str

        type : ConversationMessageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}/messages",
            method="POST",
            json={
                "content": content,
                "type": type,
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
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    def get_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    def update_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="PUT",
            json={
                "content": content,
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
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    def delete_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
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

    def replace_project_folder(
        self,
        project_id: str,
        folder_id: typing.Optional[int],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Move project to the folder

        Parameters
        ----------
        project_id : str

        folder_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/folders/{encode_path_param(folder_id)}",
            method="PUT",
            request_options=request_options,
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

    def get_project_metadata(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProjectMetadataGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectMetadataGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectMetadataGet,
                    parse_obj_as(
                        type_=EnvelopeProjectMetadataGet,
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

    def update_project_metadata(
        self,
        project_id: str,
        *,
        custom: typing.Dict[str, ProjectMetadataUpdateCustomValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeProjectMetadataGet]:
        """
        Parameters
        ----------
        project_id : str

        custom : typing.Dict[str, ProjectMetadataUpdateCustomValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectMetadataGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/metadata",
            method="PATCH",
            json={
                "custom": convert_and_respect_annotation_metadata(
                    object_=custom, annotation=typing.Dict[str, ProjectMetadataUpdateCustomValue], direction="write"
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
                    EnvelopeProjectMetadataGet,
                    parse_obj_as(
                        type_=EnvelopeProjectMetadataGet,
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

    def create_node(
        self,
        project_id: str,
        *,
        service_key: str,
        service_version: str,
        service_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeNodeCreated]:
        """
        Parameters
        ----------
        project_id : str

        service_key : str

        service_version : str

        service_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeNodeCreated]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes",
            method="POST",
            json={
                "service_key": service_key,
                "service_version": service_version,
                "service_id": service_id,
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
                    EnvelopeNodeCreated,
                    parse_obj_as(
                        type_=EnvelopeNodeCreated,
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

    def get_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet,
                    parse_obj_as(
                        type_=EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet,
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

    def delete_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}",
            method="DELETE",
            request_options=request_options,
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

    def patch_project_node(
        self,
        project_id: str,
        node_id: str,
        *,
        key: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        inputs: typing.Optional[InputsDictInput] = OMIT,
        inputs_required: typing.Optional[typing.Sequence[InputId]] = OMIT,
        inputs_units: typing.Optional[typing.Dict[str, typing.Optional[UnitStr]]] = OMIT,
        input_nodes: typing.Optional[typing.Sequence[str]] = OMIT,
        progress: typing.Optional[float] = OMIT,
        boot_options: typing.Optional[BootOptions] = OMIT,
        outputs: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ui: typing.Optional[NodeUiPatch] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        key : typing.Optional[str]

        version : typing.Optional[str]

        label : typing.Optional[str]

        inputs : typing.Optional[InputsDictInput]

        inputs_required : typing.Optional[typing.Sequence[InputId]]

        inputs_units : typing.Optional[typing.Dict[str, typing.Optional[UnitStr]]]

        input_nodes : typing.Optional[typing.Sequence[str]]

        progress : typing.Optional[float]

        boot_options : typing.Optional[BootOptions]

        outputs : typing.Optional[typing.Dict[str, typing.Any]]

        ui : typing.Optional[NodeUiPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}",
            method="PATCH",
            json={
                "key": key,
                "version": version,
                "label": label,
                "inputs": convert_and_respect_annotation_metadata(
                    object_=inputs, annotation=InputsDictInput, direction="write"
                ),
                "inputsRequired": inputs_required,
                "inputsUnits": inputs_units,
                "inputNodes": input_nodes,
                "progress": progress,
                "bootOptions": boot_options,
                "outputs": outputs,
                "ui": convert_and_respect_annotation_metadata(object_=ui, annotation=NodeUiPatch, direction="write"),
            },
            headers={
                "content-type": "application/json",
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

    def retrieve_node(
        self,
        project_id: str,
        node_id: str,
        *,
        port_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeNodeRetrieved]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        port_keys : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeNodeRetrieved]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}:retrieve",
            method="POST",
            json={
                "port_keys": port_keys,
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
                    EnvelopeNodeRetrieved,
                    parse_obj_as(
                        type_=EnvelopeNodeRetrieved,
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

    def start_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}:start",
            method="POST",
            request_options=request_options,
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

    def stop_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeTaskGet]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}:stop",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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

    def restart_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Note that it has only effect on nodes associated to dynamic services

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}:restart",
            method="POST",
            request_options=request_options,
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

    def update_node_outputs(
        self,
        project_id: str,
        node_id: str,
        *,
        outputs: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        outputs : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/outputs",
            method="PATCH",
            json={
                "outputs": outputs,
            },
            headers={
                "content-type": "application/json",
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

    def get_node_resources(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/resources",
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

    def replace_node_resources(
        self,
        project_id: str,
        node_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/resources",
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

    def get_project_services(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProjectNodeServicesGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectNodeServicesGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/-/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectNodeServicesGet,
                    parse_obj_as(
                        type_=EnvelopeProjectNodeServicesGet,
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

    def get_project_services_access_for_gid(
        self, project_id: str, *, for_gid: GroupIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProjectGroupAccess]:
        """
        Check whether provided group has access to the project services

        Parameters
        ----------
        project_id : str

        for_gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectGroupAccess]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/-/services:access",
            method="GET",
            params={
                "for_gid": for_gid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectGroupAccess,
                    parse_obj_as(
                        type_=EnvelopeProjectGroupAccess,
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

    def list_project_nodes_previews(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListProjectNodePreview]:
        """
        Lists all previews in the node's project

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListProjectNodePreview]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/-/preview",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListProjectNodePreview,
                    parse_obj_as(
                        type_=EnvelopeListProjectNodePreview,
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

    def get_project_node_preview(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProjectNodePreview]:
        """
        Gets a give node's preview

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectNodePreview]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/preview",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectNodePreview,
                    parse_obj_as(
                        type_=EnvelopeProjectNodePreview,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def get_project_node_pricing_unit(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeUnionPricingUnitGetNoneType]:
        """
        Get currently connected pricing unit to the project node.

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeUnionPricingUnitGetNoneType]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/pricing-unit",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeUnionPricingUnitGetNoneType,
                    parse_obj_as(
                        type_=EnvelopeUnionPricingUnitGetNoneType,
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

    def connect_pricing_unit_to_project_node(
        self,
        project_id: str,
        node_id: str,
        pricing_plan_id: int,
        pricing_unit_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Connect pricing unit to the project node (Project node can have only one pricing unit)

        Parameters
        ----------
        project_id : str

        node_id : str

        pricing_plan_id : int

        pricing_unit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/pricing-plan/{encode_path_param(pricing_plan_id)}/pricing-unit/{encode_path_param(pricing_unit_id)}",
            method="PUT",
            request_options=request_options,
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

    def get_project_inputs(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeDictUuidProjectInputGet]:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeDictUuidProjectInputGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/inputs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictUuidProjectInputGet,
                    parse_obj_as(
                        type_=EnvelopeDictUuidProjectInputGet,
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

    def update_project_inputs(
        self,
        project_id: str,
        *,
        request: typing.Sequence[ProjectInputUpdate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeDictUuidProjectInputGet]:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request : typing.Sequence[ProjectInputUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeDictUuidProjectInputGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/inputs",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[ProjectInputUpdate], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictUuidProjectInputGet,
                    parse_obj_as(
                        type_=EnvelopeDictUuidProjectInputGet,
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

    def get_project_outputs(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeDictUuidProjectOutputGet]:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeDictUuidProjectOutputGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/outputs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictUuidProjectOutputGet,
                    parse_obj_as(
                        type_=EnvelopeDictUuidProjectOutputGet,
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

    def list_project_metadata_ports(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListProjectMetadataPortGet]:
        """
        New in version *0.12*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListProjectMetadataPortGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/metadata/ports",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListProjectMetadataPortGet,
                    parse_obj_as(
                        type_=EnvelopeListProjectMetadataPortGet,
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

    def open_project(
        self,
        project_id: str,
        *,
        request: str,
        disable_service_auto_start: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeProjectGet]:
        """
        Parameters
        ----------
        project_id : str

        request : str

        disable_service_auto_start : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}:open",
            method="POST",
            params={
                "disable_service_auto_start": disable_service_auto_start,
            },
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
                    EnvelopeProjectGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def close_project(
        self, project_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}:close",
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_project_state(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProjectStateOutputSchema]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectStateOutputSchema]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/state",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectStateOutputSchema,
                    parse_obj_as(
                        type_=EnvelopeProjectStateOutputSchema,
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

    def add_project_tag(
        self, project_uuid: str, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProjectGet]:
        """
        Links an existing label with an existing study

        NOTE: that the tag is not created here

        Parameters
        ----------
        project_uuid : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_uuid)}/tags/{encode_path_param(tag_id)}:add",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGet,
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

    def remove_project_tag(
        self, project_uuid: str, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProjectGet]:
        """
        Removes an existing link between a label and a study

        NOTE: that the tag is not deleted here

        Parameters
        ----------
        project_uuid : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProjectGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_uuid)}/tags/{encode_path_param(tag_id)}:remove",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGet,
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

    def get_project_wallet(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeUnionWalletGetNoneType]:
        """
        Get current connected wallet to the project.

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeUnionWalletGetNoneType]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/wallet",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeUnionWalletGetNoneType,
                    parse_obj_as(
                        type_=EnvelopeUnionWalletGetNoneType,
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

    def connect_wallet_to_project(
        self, project_id: str, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeWalletGet]:
        """
        Connect wallet to the project (Project can have only one wallet)

        Parameters
        ----------
        project_id : str

        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeWalletGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/wallet/{encode_path_param(wallet_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeWalletGet,
                    parse_obj_as(
                        type_=EnvelopeWalletGet,
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

    def pay_project_debt(
        self,
        project_id: str,
        wallet_id: WalletIdInt,
        *,
        amount: PayProjectDebtRequestAmount,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        wallet_id : WalletIdInt

        amount : PayProjectDebtRequestAmount

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/wallet/{encode_path_param(wallet_id)}:pay-debt",
            method="POST",
            params={
                "amount": amount,
            },
            request_options=request_options,
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

    def move_project_to_workspace(
        self,
        project_id: str,
        workspace_id: typing.Optional[int],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Move project to the workspace

        Parameters
        ----------
        project_id : str

        workspace_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/workspaces/{encode_path_param(workspace_id)}:move",
            method="POST",
            request_options=request_options,
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


class AsyncRawProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def export_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        creates an archive of the project and downloads it

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}:xport",
            method="POST",
            request_options=request_options,
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

    async def list_projects(
        self,
        *,
        type: typing.Optional[ProjectTypeApi] = None,
        template_type: typing.Optional[ProjectTemplateType] = None,
        show_hidden: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        folder_id: typing.Optional[int] = None,
        workspace_id: typing.Optional[int] = None,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageProjectListItem]:
        """
        Parameters
        ----------
        type : typing.Optional[ProjectTypeApi]

        template_type : typing.Optional[ProjectTemplateType]

        show_hidden : typing.Optional[bool]

        search : typing.Optional[str]

        folder_id : typing.Optional[int]

        workspace_id : typing.Optional[int]

        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageProjectListItem]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/projects",
            method="GET",
            params={
                "type": type,
                "template_type": template_type,
                "show_hidden": show_hidden,
                "search": search,
                "folder_id": folder_id,
                "workspace_id": workspace_id,
                "filters": filters,
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageProjectListItem,
                    parse_obj_as(
                        type_=PageProjectListItem,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def create_project(
        self,
        *,
        request: CreateProjectRequestBody,
        x_simcore_user_agent: typing.Optional[str] = None,
        x_simcore_parent_project_uuid: typing.Optional[str] = None,
        x_simcore_parent_node_id: typing.Optional[str] = None,
        from_study: typing.Optional[str] = None,
        as_template: typing.Optional[bool] = None,
        copy_data: typing.Optional[bool] = None,
        hidden: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeTaskGet]:
        """
        Creates a new project or copies an existing one. NOTE: implemented as a long running task, i.e. requires polling `status_href` (HTTP_200_OK) to get status and `result_href` (HTTP_201_CREATED) to get created project

        Parameters
        ----------
        request : CreateProjectRequestBody

        x_simcore_user_agent : typing.Optional[str]

        x_simcore_parent_project_uuid : typing.Optional[str]

        x_simcore_parent_node_id : typing.Optional[str]

        from_study : typing.Optional[str]

        as_template : typing.Optional[bool]

        copy_data : typing.Optional[bool]

        hidden : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/projects",
            method="POST",
            params={
                "x_simcore_user_agent": x_simcore_user_agent,
                "x_simcore_parent_project_uuid": x_simcore_parent_project_uuid,
                "x_simcore_parent_node_id": x_simcore_parent_node_id,
                "from_study": from_study,
                "as_template": as_template,
                "copy_data": copy_data,
                "hidden": hidden,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateProjectRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_active_project(
        self, *, client_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProjectGet]:
        """
        Parameters
        ----------
        client_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/projects/active",
            method="GET",
            params={
                "client_session_id": client_session_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProjectGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def delete_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}",
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def patch_project(
        self,
        project_id: str,
        *,
        name: typing.Optional[ShortTruncatedStr] = OMIT,
        description: typing.Optional[LongTruncatedStr] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        classifiers: typing.Optional[typing.Sequence[str]] = OMIT,
        dev: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ui: typing.Optional[StudyUiInput] = OMIT,
        quality: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        template_type: typing.Optional[ProjectTemplateType] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        name : typing.Optional[ShortTruncatedStr]

        description : typing.Optional[LongTruncatedStr]

        thumbnail : typing.Optional[str]

        classifiers : typing.Optional[typing.Sequence[str]]

        dev : typing.Optional[typing.Dict[str, typing.Any]]

        ui : typing.Optional[StudyUiInput]

        quality : typing.Optional[typing.Dict[str, typing.Any]]

        template_type : typing.Optional[ProjectTemplateType]

        hidden : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "thumbnail": thumbnail,
                "classifiers": classifiers,
                "dev": dev,
                "ui": convert_and_respect_annotation_metadata(
                    object_=ui, annotation=typing.Optional[StudyUiInput], direction="write"
                ),
                "quality": quality,
                "templateType": template_type,
                "hidden": hidden,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def clone_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeTaskGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}:clone",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def list_projects_full_search(
        self,
        *,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[ProjectTypeApi] = None,
        template_type: typing.Optional[ProjectTemplateType] = None,
        text: typing.Optional[str] = None,
        tag_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageProjectListItem]:
        """
        Parameters
        ----------
        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        type : typing.Optional[ProjectTypeApi]

        template_type : typing.Optional[ProjectTemplateType]

        text : typing.Optional[str]

        tag_ids : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageProjectListItem]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/projects:search",
            method="GET",
            params={
                "filters": filters,
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
                "type": type,
                "template_type": template_type,
                "text": text,
                "tag_ids": tag_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageProjectListItem,
                    parse_obj_as(
                        type_=PageProjectListItem,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_project_inactivity(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeGetProjectInactivityResponse]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeGetProjectInactivityResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/inactivity",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGetProjectInactivityResponse,
                    parse_obj_as(
                        type_=EnvelopeGetProjectInactivityResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def share_project(
        self,
        project_id: str,
        *,
        sharee_email: str,
        read: bool,
        write: bool,
        delete: bool,
        sharer_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeProjectShareAccepted]:
        """
        Parameters
        ----------
        project_id : str

        sharee_email : str

        read : bool

        write : bool

        delete : bool

        sharer_message : typing.Optional[str]
            An optional message from sharer to sharee

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectShareAccepted]
            The request to share the project has been accepted, but the actual sharing process has to be confirmed.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}:share",
            method="POST",
            json={
                "shareeEmail": sharee_email,
                "sharerMessage": sharer_message,
                "read": read,
                "write": write,
                "delete": delete,
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
                    EnvelopeProjectShareAccepted,
                    parse_obj_as(
                        type_=EnvelopeProjectShareAccepted,
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

    async def create_project_group(
        self,
        project_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeProjectGroupGet]:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectGroupGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/groups/{encode_path_param(group_id)}",
            method="POST",
            json={
                "read": read,
                "write": write,
                "delete": delete,
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
                    EnvelopeProjectGroupGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGroupGet,
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

    async def replace_project_group(
        self,
        project_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeProjectGroupGet]:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectGroupGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/groups/{encode_path_param(group_id)}",
            method="PUT",
            json={
                "read": read,
                "write": write,
                "delete": delete,
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
                    EnvelopeProjectGroupGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGroupGet,
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

    async def delete_project_group(
        self, project_id: str, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
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

    async def list_project_groups(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListProjectGroupGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListProjectGroupGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/groups",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListProjectGroupGet,
                    parse_obj_as(
                        type_=EnvelopeListProjectGroupGet,
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

    async def list_project_conversations(
        self,
        project_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageConversationRestGet]:
        """
        Parameters
        ----------
        project_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageConversationRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations",
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
                    PageConversationRestGet,
                    parse_obj_as(
                        type_=PageConversationRestGet,
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

    async def create_project_conversation(
        self,
        project_id: str,
        *,
        name: str,
        type: ConversationType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        project_id : str

        name : str

        type : ConversationType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations",
            method="POST",
            json={
                "name": name,
                "type": type,
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
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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

    async def get_project_conversation(
        self, project_id: str, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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

    async def update_project_conversation(
        self,
        project_id: str,
        conversation_id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}",
            method="PUT",
            json={
                "name": name,
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
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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

    async def delete_project_conversation(
        self, project_id: str, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}",
            method="DELETE",
            request_options=request_options,
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

    async def list_project_conversation_messages(
        self,
        project_id: str,
        conversation_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageConversationMessageRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageConversationMessageRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}/messages",
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
                    PageConversationMessageRestGet,
                    parse_obj_as(
                        type_=PageConversationMessageRestGet,
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

    async def create_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        *,
        content: str,
        type: ConversationMessageType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        content : str

        type : ConversationMessageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}/messages",
            method="POST",
            json={
                "content": content,
                "type": type,
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
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    async def get_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    async def update_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        content: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        content : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="PUT",
            json={
                "content": content,
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
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    async def delete_project_conversation_message(
        self,
        project_id: str,
        conversation_id: str,
        message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
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

    async def replace_project_folder(
        self,
        project_id: str,
        folder_id: typing.Optional[int],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Move project to the folder

        Parameters
        ----------
        project_id : str

        folder_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/folders/{encode_path_param(folder_id)}",
            method="PUT",
            request_options=request_options,
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

    async def get_project_metadata(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProjectMetadataGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectMetadataGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectMetadataGet,
                    parse_obj_as(
                        type_=EnvelopeProjectMetadataGet,
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

    async def update_project_metadata(
        self,
        project_id: str,
        *,
        custom: typing.Dict[str, ProjectMetadataUpdateCustomValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeProjectMetadataGet]:
        """
        Parameters
        ----------
        project_id : str

        custom : typing.Dict[str, ProjectMetadataUpdateCustomValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectMetadataGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/metadata",
            method="PATCH",
            json={
                "custom": convert_and_respect_annotation_metadata(
                    object_=custom, annotation=typing.Dict[str, ProjectMetadataUpdateCustomValue], direction="write"
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
                    EnvelopeProjectMetadataGet,
                    parse_obj_as(
                        type_=EnvelopeProjectMetadataGet,
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

    async def create_node(
        self,
        project_id: str,
        *,
        service_key: str,
        service_version: str,
        service_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeNodeCreated]:
        """
        Parameters
        ----------
        project_id : str

        service_key : str

        service_version : str

        service_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeNodeCreated]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes",
            method="POST",
            json={
                "service_key": service_key,
                "service_version": service_version,
                "service_id": service_id,
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
                    EnvelopeNodeCreated,
                    parse_obj_as(
                        type_=EnvelopeNodeCreated,
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

    async def get_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet,
                    parse_obj_as(
                        type_=EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGet,
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

    async def delete_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}",
            method="DELETE",
            request_options=request_options,
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

    async def patch_project_node(
        self,
        project_id: str,
        node_id: str,
        *,
        key: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        inputs: typing.Optional[InputsDictInput] = OMIT,
        inputs_required: typing.Optional[typing.Sequence[InputId]] = OMIT,
        inputs_units: typing.Optional[typing.Dict[str, typing.Optional[UnitStr]]] = OMIT,
        input_nodes: typing.Optional[typing.Sequence[str]] = OMIT,
        progress: typing.Optional[float] = OMIT,
        boot_options: typing.Optional[BootOptions] = OMIT,
        outputs: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ui: typing.Optional[NodeUiPatch] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        key : typing.Optional[str]

        version : typing.Optional[str]

        label : typing.Optional[str]

        inputs : typing.Optional[InputsDictInput]

        inputs_required : typing.Optional[typing.Sequence[InputId]]

        inputs_units : typing.Optional[typing.Dict[str, typing.Optional[UnitStr]]]

        input_nodes : typing.Optional[typing.Sequence[str]]

        progress : typing.Optional[float]

        boot_options : typing.Optional[BootOptions]

        outputs : typing.Optional[typing.Dict[str, typing.Any]]

        ui : typing.Optional[NodeUiPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}",
            method="PATCH",
            json={
                "key": key,
                "version": version,
                "label": label,
                "inputs": convert_and_respect_annotation_metadata(
                    object_=inputs, annotation=InputsDictInput, direction="write"
                ),
                "inputsRequired": inputs_required,
                "inputsUnits": inputs_units,
                "inputNodes": input_nodes,
                "progress": progress,
                "bootOptions": boot_options,
                "outputs": outputs,
                "ui": convert_and_respect_annotation_metadata(object_=ui, annotation=NodeUiPatch, direction="write"),
            },
            headers={
                "content-type": "application/json",
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

    async def retrieve_node(
        self,
        project_id: str,
        node_id: str,
        *,
        port_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeNodeRetrieved]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        port_keys : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeNodeRetrieved]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}:retrieve",
            method="POST",
            json={
                "port_keys": port_keys,
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
                    EnvelopeNodeRetrieved,
                    parse_obj_as(
                        type_=EnvelopeNodeRetrieved,
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

    async def start_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}:start",
            method="POST",
            request_options=request_options,
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

    async def stop_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeTaskGet]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}:stop",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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

    async def restart_node(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Note that it has only effect on nodes associated to dynamic services

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}:restart",
            method="POST",
            request_options=request_options,
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

    async def update_node_outputs(
        self,
        project_id: str,
        node_id: str,
        *,
        outputs: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        outputs : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/outputs",
            method="PATCH",
            json={
                "outputs": outputs,
            },
            headers={
                "content-type": "application/json",
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

    async def get_node_resources(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/resources",
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

    async def replace_node_resources(
        self,
        project_id: str,
        node_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]:
        """
        Parameters
        ----------
        project_id : str

        node_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeDictAnnotatedStrStringConstraintsImageResources]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/resources",
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

    async def get_project_services(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProjectNodeServicesGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectNodeServicesGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/-/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectNodeServicesGet,
                    parse_obj_as(
                        type_=EnvelopeProjectNodeServicesGet,
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

    async def get_project_services_access_for_gid(
        self, project_id: str, *, for_gid: GroupIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProjectGroupAccess]:
        """
        Check whether provided group has access to the project services

        Parameters
        ----------
        project_id : str

        for_gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectGroupAccess]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/-/services:access",
            method="GET",
            params={
                "for_gid": for_gid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectGroupAccess,
                    parse_obj_as(
                        type_=EnvelopeProjectGroupAccess,
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

    async def list_project_nodes_previews(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListProjectNodePreview]:
        """
        Lists all previews in the node's project

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListProjectNodePreview]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/-/preview",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListProjectNodePreview,
                    parse_obj_as(
                        type_=EnvelopeListProjectNodePreview,
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

    async def get_project_node_preview(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProjectNodePreview]:
        """
        Gets a give node's preview

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectNodePreview]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/preview",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectNodePreview,
                    parse_obj_as(
                        type_=EnvelopeProjectNodePreview,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def get_project_node_pricing_unit(
        self, project_id: str, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeUnionPricingUnitGetNoneType]:
        """
        Get currently connected pricing unit to the project node.

        Parameters
        ----------
        project_id : str

        node_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeUnionPricingUnitGetNoneType]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/pricing-unit",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeUnionPricingUnitGetNoneType,
                    parse_obj_as(
                        type_=EnvelopeUnionPricingUnitGetNoneType,
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

    async def connect_pricing_unit_to_project_node(
        self,
        project_id: str,
        node_id: str,
        pricing_plan_id: int,
        pricing_unit_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Connect pricing unit to the project node (Project node can have only one pricing unit)

        Parameters
        ----------
        project_id : str

        node_id : str

        pricing_plan_id : int

        pricing_unit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/nodes/{encode_path_param(node_id)}/pricing-plan/{encode_path_param(pricing_plan_id)}/pricing-unit/{encode_path_param(pricing_unit_id)}",
            method="PUT",
            request_options=request_options,
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

    async def get_project_inputs(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeDictUuidProjectInputGet]:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeDictUuidProjectInputGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/inputs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictUuidProjectInputGet,
                    parse_obj_as(
                        type_=EnvelopeDictUuidProjectInputGet,
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

    async def update_project_inputs(
        self,
        project_id: str,
        *,
        request: typing.Sequence[ProjectInputUpdate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeDictUuidProjectInputGet]:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request : typing.Sequence[ProjectInputUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeDictUuidProjectInputGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/inputs",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[ProjectInputUpdate], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictUuidProjectInputGet,
                    parse_obj_as(
                        type_=EnvelopeDictUuidProjectInputGet,
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

    async def get_project_outputs(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeDictUuidProjectOutputGet]:
        """
        New in version *0.10*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeDictUuidProjectOutputGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/outputs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictUuidProjectOutputGet,
                    parse_obj_as(
                        type_=EnvelopeDictUuidProjectOutputGet,
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

    async def list_project_metadata_ports(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListProjectMetadataPortGet]:
        """
        New in version *0.12*

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListProjectMetadataPortGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/metadata/ports",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListProjectMetadataPortGet,
                    parse_obj_as(
                        type_=EnvelopeListProjectMetadataPortGet,
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

    async def open_project(
        self,
        project_id: str,
        *,
        request: str,
        disable_service_auto_start: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeProjectGet]:
        """
        Parameters
        ----------
        project_id : str

        request : str

        disable_service_auto_start : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}:open",
            method="POST",
            params={
                "disable_service_auto_start": disable_service_auto_start,
            },
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
                    EnvelopeProjectGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def close_project(
        self, project_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}:close",
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_project_state(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProjectStateOutputSchema]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectStateOutputSchema]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/state",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectStateOutputSchema,
                    parse_obj_as(
                        type_=EnvelopeProjectStateOutputSchema,
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

    async def add_project_tag(
        self, project_uuid: str, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProjectGet]:
        """
        Links an existing label with an existing study

        NOTE: that the tag is not created here

        Parameters
        ----------
        project_uuid : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_uuid)}/tags/{encode_path_param(tag_id)}:add",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGet,
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

    async def remove_project_tag(
        self, project_uuid: str, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProjectGet]:
        """
        Removes an existing link between a label and a study

        NOTE: that the tag is not deleted here

        Parameters
        ----------
        project_uuid : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProjectGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_uuid)}/tags/{encode_path_param(tag_id)}:remove",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProjectGet,
                    parse_obj_as(
                        type_=EnvelopeProjectGet,
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

    async def get_project_wallet(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeUnionWalletGetNoneType]:
        """
        Get current connected wallet to the project.

        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeUnionWalletGetNoneType]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/wallet",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeUnionWalletGetNoneType,
                    parse_obj_as(
                        type_=EnvelopeUnionWalletGetNoneType,
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

    async def connect_wallet_to_project(
        self, project_id: str, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeWalletGet]:
        """
        Connect wallet to the project (Project can have only one wallet)

        Parameters
        ----------
        project_id : str

        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeWalletGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/wallet/{encode_path_param(wallet_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeWalletGet,
                    parse_obj_as(
                        type_=EnvelopeWalletGet,
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

    async def pay_project_debt(
        self,
        project_id: str,
        wallet_id: WalletIdInt,
        *,
        amount: PayProjectDebtRequestAmount,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        wallet_id : WalletIdInt

        amount : PayProjectDebtRequestAmount

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/wallet/{encode_path_param(wallet_id)}:pay-debt",
            method="POST",
            params={
                "amount": amount,
            },
            request_options=request_options,
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

    async def move_project_to_workspace(
        self,
        project_id: str,
        workspace_id: typing.Optional[int],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Move project to the workspace

        Parameters
        ----------
        project_id : str

        workspace_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/projects/{encode_path_param(project_id)}/workspaces/{encode_path_param(workspace_id)}:move",
            method="POST",
            request_options=request_options,
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
