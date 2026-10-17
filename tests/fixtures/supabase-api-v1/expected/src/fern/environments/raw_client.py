

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.action_run_response_output import ActionRunResponseOutput
from ..types.branch_delete_response_output import BranchDeleteResponseOutput
from ..types.branch_detail_response_output import BranchDetailResponseOutput
from ..types.branch_response_output import BranchResponseOutput
from ..types.branch_restore_response_output import BranchRestoreResponseOutput
from ..types.branch_update_response_output import BranchUpdateResponseOutput
from ..types.list_action_run_response_output import ListActionRunResponseOutput
from ..types.update_run_status_response_output import UpdateRunStatusResponseOutput
from .types.create_branch_body_desired_instance_size import CreateBranchBodyDesiredInstanceSize
from .types.create_branch_body_postgres_engine import CreateBranchBodyPostgresEngine
from .types.create_branch_body_release_channel import CreateBranchBodyReleaseChannel
from .types.update_branch_body_status import UpdateBranchBodyStatus
from .types.update_run_status_body_clone import UpdateRunStatusBodyClone
from .types.update_run_status_body_configure import UpdateRunStatusBodyConfigure
from .types.update_run_status_body_deploy import UpdateRunStatusBodyDeploy
from .types.update_run_status_body_health import UpdateRunStatusBodyHealth
from .types.update_run_status_body_migrate import UpdateRunStatusBodyMigrate
from .types.update_run_status_body_pull import UpdateRunStatusBodyPull
from .types.update_run_status_body_seed import UpdateRunStatusBodySeed
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEnvironmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v1get_a_branch_config(
        self, branch_id_or_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BranchDetailResponseOutput]:
        """
        Fetches configurations of the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BranchDetailResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BranchDetailResponseOutput,
                    parse_obj_as(
                        type_=BranchDetailResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1delete_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        force: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BranchDeleteResponseOutput]:
        """
        Deletes the specified database branch. By default, deletes immediately. Use force=false to schedule deletion with 1-hour grace period (only when soft deletion is enabled).

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        force : typing.Optional[str]
            If set to false, schedule deletion with 1-hour grace period (only when soft deletion is enabled).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BranchDeleteResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}",
            method="DELETE",
            params={
                "force": force,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BranchDeleteResponseOutput,
                    parse_obj_as(
                        type_=BranchDeleteResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1update_a_branch_config(
        self,
        branch_id_or_ref: str,
        *,
        branch_name: typing.Optional[str] = OMIT,
        git_branch: typing.Optional[str] = OMIT,
        reset_on_push: typing.Optional[bool] = OMIT,
        persistent: typing.Optional[bool] = OMIT,
        status: typing.Optional[UpdateBranchBodyStatus] = OMIT,
        request_review: typing.Optional[bool] = OMIT,
        notify_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BranchResponseOutput]:
        """
        Updates the configuration of the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        branch_name : typing.Optional[str]

        git_branch : typing.Optional[str]

        reset_on_push : typing.Optional[bool]
            This field is deprecated and will be ignored. Use v1-reset-a-branch endpoint directly instead.

        persistent : typing.Optional[bool]

        status : typing.Optional[UpdateBranchBodyStatus]

        request_review : typing.Optional[bool]

        notify_url : typing.Optional[str]
            HTTP endpoint to receive branch status updates.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BranchResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}",
            method="PATCH",
            json={
                "branch_name": branch_name,
                "git_branch": git_branch,
                "reset_on_push": reset_on_push,
                "persistent": persistent,
                "status": status,
                "request_review": request_review,
                "notify_url": notify_url,
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
                    BranchResponseOutput,
                    parse_obj_as(
                        type_=BranchResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1push_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BranchUpdateResponseOutput]:
        """
        Pushes the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BranchUpdateResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}/push",
            method="POST",
            json={
                "migration_version": migration_version,
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
                    BranchUpdateResponseOutput,
                    parse_obj_as(
                        type_=BranchUpdateResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1merge_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BranchUpdateResponseOutput]:
        """
        Merges the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BranchUpdateResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}/merge",
            method="POST",
            json={
                "migration_version": migration_version,
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
                    BranchUpdateResponseOutput,
                    parse_obj_as(
                        type_=BranchUpdateResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1reset_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BranchUpdateResponseOutput]:
        """
        Resets the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BranchUpdateResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}/reset",
            method="POST",
            json={
                "migration_version": migration_version,
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
                    BranchUpdateResponseOutput,
                    parse_obj_as(
                        type_=BranchUpdateResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1restore_a_branch(
        self, branch_id_or_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BranchRestoreResponseOutput]:
        """
        Cancels scheduled deletion and restores the branch to active state

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BranchRestoreResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}/restore",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BranchRestoreResponseOutput,
                    parse_obj_as(
                        type_=BranchRestoreResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1diff_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        included_schemas: typing.Optional[str] = None,
        pgdelta: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Diffs the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        included_schemas : typing.Optional[str]

        pgdelta : typing.Optional[str]
            Use pg-delta instead of Migra for diffing when true.
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}/diff",
            method="GET",
            params={
                "included_schemas": included_schemas,
                "pgdelta": pgdelta,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
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

    def v1list_action_runs(
        self,
        ref: str,
        *,
        offset: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListActionRunResponseOutput]:
        """
        Returns a paginated list of action runs of the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        offset : typing.Optional[float]

        limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListActionRunResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/actions",
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
                    ListActionRunResponseOutput,
                    parse_obj_as(
                        type_=ListActionRunResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1count_action_runs(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Returns the total number of action runs of the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/actions",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def v1get_action_run(
        self, ref: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ActionRunResponseOutput]:
        """
        Returns the current status of the specified action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ActionRunResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/actions/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActionRunResponseOutput,
                    parse_obj_as(
                        type_=ActionRunResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1update_action_run_status(
        self,
        ref: str,
        run_id: str,
        *,
        clone: typing.Optional[UpdateRunStatusBodyClone] = OMIT,
        pull: typing.Optional[UpdateRunStatusBodyPull] = OMIT,
        health: typing.Optional[UpdateRunStatusBodyHealth] = OMIT,
        configure: typing.Optional[UpdateRunStatusBodyConfigure] = OMIT,
        migrate: typing.Optional[UpdateRunStatusBodyMigrate] = OMIT,
        seed: typing.Optional[UpdateRunStatusBodySeed] = OMIT,
        deploy: typing.Optional[UpdateRunStatusBodyDeploy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateRunStatusResponseOutput]:
        """
        Updates the status of an ongoing action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        clone : typing.Optional[UpdateRunStatusBodyClone]

        pull : typing.Optional[UpdateRunStatusBodyPull]

        health : typing.Optional[UpdateRunStatusBodyHealth]

        configure : typing.Optional[UpdateRunStatusBodyConfigure]

        migrate : typing.Optional[UpdateRunStatusBodyMigrate]

        seed : typing.Optional[UpdateRunStatusBodySeed]

        deploy : typing.Optional[UpdateRunStatusBodyDeploy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateRunStatusResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/actions/{encode_path_param(run_id)}/status",
            method="PATCH",
            json={
                "clone": clone,
                "pull": pull,
                "health": health,
                "configure": configure,
                "migrate": migrate,
                "seed": seed,
                "deploy": deploy,
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
                    UpdateRunStatusResponseOutput,
                    parse_obj_as(
                        type_=UpdateRunStatusResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1get_action_run_logs(
        self, ref: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Returns the logs from the specified action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/actions/{encode_path_param(run_id)}/logs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
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

    def v1list_all_branches(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[BranchResponseOutput]]:
        """
        Returns all database branches of the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[BranchResponseOutput]]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/branches",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BranchResponseOutput],
                    parse_obj_as(
                        type_=typing.List[BranchResponseOutput],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1create_a_branch(
        self,
        ref: str,
        *,
        branch_name: str,
        git_branch: typing.Optional[str] = OMIT,
        is_default: typing.Optional[bool] = OMIT,
        persistent: typing.Optional[bool] = OMIT,
        region: typing.Optional[str] = OMIT,
        desired_instance_size: typing.Optional[CreateBranchBodyDesiredInstanceSize] = OMIT,
        release_channel: typing.Optional[CreateBranchBodyReleaseChannel] = OMIT,
        postgres_engine: typing.Optional[CreateBranchBodyPostgresEngine] = OMIT,
        secrets: typing.Optional[typing.Dict[str, str]] = OMIT,
        with_data: typing.Optional[bool] = OMIT,
        notify_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BranchResponseOutput]:
        """
        Creates a database branch from the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        branch_name : str

        git_branch : typing.Optional[str]

        is_default : typing.Optional[bool]

        persistent : typing.Optional[bool]

        region : typing.Optional[str]

        desired_instance_size : typing.Optional[CreateBranchBodyDesiredInstanceSize]

        release_channel : typing.Optional[CreateBranchBodyReleaseChannel]
            Release channel. If not provided, GA will be used.

        postgres_engine : typing.Optional[CreateBranchBodyPostgresEngine]
            Postgres engine version. If not provided, the latest version will be used.

        secrets : typing.Optional[typing.Dict[str, str]]

        with_data : typing.Optional[bool]

        notify_url : typing.Optional[str]
            HTTP endpoint to receive branch status updates.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BranchResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/branches",
            method="POST",
            json={
                "branch_name": branch_name,
                "git_branch": git_branch,
                "is_default": is_default,
                "persistent": persistent,
                "region": region,
                "desired_instance_size": desired_instance_size,
                "release_channel": release_channel,
                "postgres_engine": postgres_engine,
                "secrets": secrets,
                "with_data": with_data,
                "notify_url": notify_url,
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
                    BranchResponseOutput,
                    parse_obj_as(
                        type_=BranchResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def v1disable_preview_branching(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Disables preview branching for the specified project

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/branches",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def v1get_a_branch(
        self, ref: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BranchResponseOutput]:
        """
        Fetches the specified database branch by its name.

        Parameters
        ----------
        ref : str
            Project ref

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BranchResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/branches/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BranchResponseOutput,
                    parse_obj_as(
                        type_=BranchResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawEnvironmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v1get_a_branch_config(
        self, branch_id_or_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BranchDetailResponseOutput]:
        """
        Fetches configurations of the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BranchDetailResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BranchDetailResponseOutput,
                    parse_obj_as(
                        type_=BranchDetailResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1delete_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        force: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BranchDeleteResponseOutput]:
        """
        Deletes the specified database branch. By default, deletes immediately. Use force=false to schedule deletion with 1-hour grace period (only when soft deletion is enabled).

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        force : typing.Optional[str]
            If set to false, schedule deletion with 1-hour grace period (only when soft deletion is enabled).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BranchDeleteResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}",
            method="DELETE",
            params={
                "force": force,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BranchDeleteResponseOutput,
                    parse_obj_as(
                        type_=BranchDeleteResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1update_a_branch_config(
        self,
        branch_id_or_ref: str,
        *,
        branch_name: typing.Optional[str] = OMIT,
        git_branch: typing.Optional[str] = OMIT,
        reset_on_push: typing.Optional[bool] = OMIT,
        persistent: typing.Optional[bool] = OMIT,
        status: typing.Optional[UpdateBranchBodyStatus] = OMIT,
        request_review: typing.Optional[bool] = OMIT,
        notify_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BranchResponseOutput]:
        """
        Updates the configuration of the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        branch_name : typing.Optional[str]

        git_branch : typing.Optional[str]

        reset_on_push : typing.Optional[bool]
            This field is deprecated and will be ignored. Use v1-reset-a-branch endpoint directly instead.

        persistent : typing.Optional[bool]

        status : typing.Optional[UpdateBranchBodyStatus]

        request_review : typing.Optional[bool]

        notify_url : typing.Optional[str]
            HTTP endpoint to receive branch status updates.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BranchResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}",
            method="PATCH",
            json={
                "branch_name": branch_name,
                "git_branch": git_branch,
                "reset_on_push": reset_on_push,
                "persistent": persistent,
                "status": status,
                "request_review": request_review,
                "notify_url": notify_url,
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
                    BranchResponseOutput,
                    parse_obj_as(
                        type_=BranchResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1push_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BranchUpdateResponseOutput]:
        """
        Pushes the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BranchUpdateResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}/push",
            method="POST",
            json={
                "migration_version": migration_version,
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
                    BranchUpdateResponseOutput,
                    parse_obj_as(
                        type_=BranchUpdateResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1merge_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BranchUpdateResponseOutput]:
        """
        Merges the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BranchUpdateResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}/merge",
            method="POST",
            json={
                "migration_version": migration_version,
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
                    BranchUpdateResponseOutput,
                    parse_obj_as(
                        type_=BranchUpdateResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1reset_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BranchUpdateResponseOutput]:
        """
        Resets the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BranchUpdateResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}/reset",
            method="POST",
            json={
                "migration_version": migration_version,
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
                    BranchUpdateResponseOutput,
                    parse_obj_as(
                        type_=BranchUpdateResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1restore_a_branch(
        self, branch_id_or_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BranchRestoreResponseOutput]:
        """
        Cancels scheduled deletion and restores the branch to active state

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BranchRestoreResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}/restore",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BranchRestoreResponseOutput,
                    parse_obj_as(
                        type_=BranchRestoreResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1diff_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        included_schemas: typing.Optional[str] = None,
        pgdelta: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Diffs the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        included_schemas : typing.Optional[str]

        pgdelta : typing.Optional[str]
            Use pg-delta instead of Migra for diffing when true.
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/branches/{encode_path_param(branch_id_or_ref)}/diff",
            method="GET",
            params={
                "included_schemas": included_schemas,
                "pgdelta": pgdelta,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
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

    async def v1list_action_runs(
        self,
        ref: str,
        *,
        offset: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListActionRunResponseOutput]:
        """
        Returns a paginated list of action runs of the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        offset : typing.Optional[float]

        limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListActionRunResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/actions",
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
                    ListActionRunResponseOutput,
                    parse_obj_as(
                        type_=ListActionRunResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1count_action_runs(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Returns the total number of action runs of the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/actions",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def v1get_action_run(
        self, ref: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ActionRunResponseOutput]:
        """
        Returns the current status of the specified action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ActionRunResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/actions/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActionRunResponseOutput,
                    parse_obj_as(
                        type_=ActionRunResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1update_action_run_status(
        self,
        ref: str,
        run_id: str,
        *,
        clone: typing.Optional[UpdateRunStatusBodyClone] = OMIT,
        pull: typing.Optional[UpdateRunStatusBodyPull] = OMIT,
        health: typing.Optional[UpdateRunStatusBodyHealth] = OMIT,
        configure: typing.Optional[UpdateRunStatusBodyConfigure] = OMIT,
        migrate: typing.Optional[UpdateRunStatusBodyMigrate] = OMIT,
        seed: typing.Optional[UpdateRunStatusBodySeed] = OMIT,
        deploy: typing.Optional[UpdateRunStatusBodyDeploy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateRunStatusResponseOutput]:
        """
        Updates the status of an ongoing action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        clone : typing.Optional[UpdateRunStatusBodyClone]

        pull : typing.Optional[UpdateRunStatusBodyPull]

        health : typing.Optional[UpdateRunStatusBodyHealth]

        configure : typing.Optional[UpdateRunStatusBodyConfigure]

        migrate : typing.Optional[UpdateRunStatusBodyMigrate]

        seed : typing.Optional[UpdateRunStatusBodySeed]

        deploy : typing.Optional[UpdateRunStatusBodyDeploy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateRunStatusResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/actions/{encode_path_param(run_id)}/status",
            method="PATCH",
            json={
                "clone": clone,
                "pull": pull,
                "health": health,
                "configure": configure,
                "migrate": migrate,
                "seed": seed,
                "deploy": deploy,
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
                    UpdateRunStatusResponseOutput,
                    parse_obj_as(
                        type_=UpdateRunStatusResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1get_action_run_logs(
        self, ref: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Returns the logs from the specified action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/actions/{encode_path_param(run_id)}/logs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
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

    async def v1list_all_branches(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[BranchResponseOutput]]:
        """
        Returns all database branches of the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[BranchResponseOutput]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/branches",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BranchResponseOutput],
                    parse_obj_as(
                        type_=typing.List[BranchResponseOutput],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1create_a_branch(
        self,
        ref: str,
        *,
        branch_name: str,
        git_branch: typing.Optional[str] = OMIT,
        is_default: typing.Optional[bool] = OMIT,
        persistent: typing.Optional[bool] = OMIT,
        region: typing.Optional[str] = OMIT,
        desired_instance_size: typing.Optional[CreateBranchBodyDesiredInstanceSize] = OMIT,
        release_channel: typing.Optional[CreateBranchBodyReleaseChannel] = OMIT,
        postgres_engine: typing.Optional[CreateBranchBodyPostgresEngine] = OMIT,
        secrets: typing.Optional[typing.Dict[str, str]] = OMIT,
        with_data: typing.Optional[bool] = OMIT,
        notify_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BranchResponseOutput]:
        """
        Creates a database branch from the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        branch_name : str

        git_branch : typing.Optional[str]

        is_default : typing.Optional[bool]

        persistent : typing.Optional[bool]

        region : typing.Optional[str]

        desired_instance_size : typing.Optional[CreateBranchBodyDesiredInstanceSize]

        release_channel : typing.Optional[CreateBranchBodyReleaseChannel]
            Release channel. If not provided, GA will be used.

        postgres_engine : typing.Optional[CreateBranchBodyPostgresEngine]
            Postgres engine version. If not provided, the latest version will be used.

        secrets : typing.Optional[typing.Dict[str, str]]

        with_data : typing.Optional[bool]

        notify_url : typing.Optional[str]
            HTTP endpoint to receive branch status updates.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BranchResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/branches",
            method="POST",
            json={
                "branch_name": branch_name,
                "git_branch": git_branch,
                "is_default": is_default,
                "persistent": persistent,
                "region": region,
                "desired_instance_size": desired_instance_size,
                "release_channel": release_channel,
                "postgres_engine": postgres_engine,
                "secrets": secrets,
                "with_data": with_data,
                "notify_url": notify_url,
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
                    BranchResponseOutput,
                    parse_obj_as(
                        type_=BranchResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def v1disable_preview_branching(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Disables preview branching for the specified project

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/branches",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def v1get_a_branch(
        self, ref: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BranchResponseOutput]:
        """
        Fetches the specified database branch by its name.

        Parameters
        ----------
        ref : str
            Project ref

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BranchResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/branches/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BranchResponseOutput,
                    parse_obj_as(
                        type_=BranchResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
