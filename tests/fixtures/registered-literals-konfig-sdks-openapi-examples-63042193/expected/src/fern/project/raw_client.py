

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.context_get_restrictions429response import ContextGetRestrictions429Response
from ..types.project_create_checkout_key_response import ProjectCreateCheckoutKeyResponse
from ..types.project_create_env_var_response import ProjectCreateEnvVarResponse
from ..types.project_create_project_default_settings405response import ProjectCreateProjectDefaultSettings405Response
from ..types.project_delete_checkout_key_by_fingerprint_response import ProjectDeleteCheckoutKeyByFingerprintResponse
from ..types.project_delete_environment_variable_response import ProjectDeleteEnvironmentVariableResponse
from ..types.project_get_by_slug_response import ProjectGetBySlugResponse
from ..types.project_get_checkout_key_by_fingerprint_response import ProjectGetCheckoutKeyByFingerprintResponse
from ..types.project_get_masked_env_var_response import ProjectGetMaskedEnvVarResponse
from ..types.project_list_checkout_keys_response import ProjectListCheckoutKeysResponse
from ..types.project_list_env_var_values_response import ProjectListEnvVarValuesResponse
from ..types.project_settings import ProjectSettings
from ..types.project_settings_advanced import ProjectSettingsAdvanced
from .types.project_create_checkout_key_request_type import ProjectCreateCheckoutKeyRequestType
from .types.project_list_checkout_keys_request_digest import ProjectListCheckoutKeysRequestDigest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getbyslug(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectGetBySlugResponse]:
        """
        Retrieves a project by project slug.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectGetBySlugResponse]
            A project object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectGetBySlugResponse,
                    parse_obj_as(
                        type_=ProjectGetBySlugResponse,
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

    def listcheckoutkeys(
        self,
        project_slug: str,
        *,
        digest: typing.Optional[ProjectListCheckoutKeysRequestDigest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectListCheckoutKeysResponse]:
        """
        Returns a sequence of checkout keys for `:project`.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        digest : typing.Optional[ProjectListCheckoutKeysRequestDigest]
            The fingerprint digest type to return. This may be either `md5` or `sha256`. If not passed, defaults to `md5`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectListCheckoutKeysResponse]
            A sequence of checkout keys.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/checkout-key",
            method="GET",
            params={
                "digest": digest,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectListCheckoutKeysResponse,
                    parse_obj_as(
                        type_=ProjectListCheckoutKeysResponse,
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

    def createcheckoutkey(
        self,
        project_slug: str,
        *,
        type: ProjectCreateCheckoutKeyRequestType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectCreateCheckoutKeyResponse]:
        """
        Not available to projects that use GitLab or GitHub App. Creates a new checkout key. This API request is only usable with a user API token.
                                   Please ensure that you have authorized your account with GitHub before creating user keys.
                                   This is necessary to give CircleCI the permission to create a user key associated with
                                   your GitHub user account. You can find this page by visiting Project Settings > Checkout SSH Keys

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        type : ProjectCreateCheckoutKeyRequestType
            The type of checkout key to create. This may be either `deploy-key` or `user-key`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectCreateCheckoutKeyResponse]
            The checkout key.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/checkout-key",
            method="POST",
            json={
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
                    ProjectCreateCheckoutKeyResponse,
                    parse_obj_as(
                        type_=ProjectCreateCheckoutKeyResponse,
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

    def getcheckoutkeybyfingerprint(
        self, project_slug: str, fingerprint: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectGetCheckoutKeyByFingerprintResponse]:
        """
        Returns an individual checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        fingerprint : str
            An SSH key fingerprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectGetCheckoutKeyByFingerprintResponse]
            The checkout key.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/checkout-key/{encode_path_param(fingerprint)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectGetCheckoutKeyByFingerprintResponse,
                    parse_obj_as(
                        type_=ProjectGetCheckoutKeyByFingerprintResponse,
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

    def deletecheckoutkeybyfingerprint(
        self, project_slug: str, fingerprint: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectDeleteCheckoutKeyByFingerprintResponse]:
        """
        Deletes the checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        fingerprint : str
            An SSH key fingerprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDeleteCheckoutKeyByFingerprintResponse]
            A confirmation message.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/checkout-key/{encode_path_param(fingerprint)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDeleteCheckoutKeyByFingerprintResponse,
                    parse_obj_as(
                        type_=ProjectDeleteCheckoutKeyByFingerprintResponse,
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

    def listenvvarvalues(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectListEnvVarValuesResponse]:
        """
        Returns four 'x' characters, in addition to the last four ASCII characters of the value, consistent with the display of environment variable values on the CircleCI website.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectListEnvVarValuesResponse]
            A sequence of environment variables.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/envvar",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectListEnvVarValuesResponse,
                    parse_obj_as(
                        type_=ProjectListEnvVarValuesResponse,
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

    def createenvvar(
        self, project_slug: str, *, name: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectCreateEnvVarResponse]:
        """
        Creates a new environment variable.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        value : str
            The value of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectCreateEnvVarResponse]
            The environment variable.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/envvar",
            method="POST",
            json={
                "name": name,
                "value": value,
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
                    ProjectCreateEnvVarResponse,
                    parse_obj_as(
                        type_=ProjectCreateEnvVarResponse,
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

    def getmaskedenvvar(
        self, project_slug: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectGetMaskedEnvVarResponse]:
        """
        Returns the masked value of environment variable :name.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectGetMaskedEnvVarResponse]
            The environment variable.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/envvar/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectGetMaskedEnvVarResponse,
                    parse_obj_as(
                        type_=ProjectGetMaskedEnvVarResponse,
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

    def deleteenvironmentvariable(
        self, project_slug: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectDeleteEnvironmentVariableResponse]:
        """
        Deletes the environment variable named :name.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDeleteEnvironmentVariableResponse]
            A confirmation message.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/envvar/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDeleteEnvironmentVariableResponse,
                    parse_obj_as(
                        type_=ProjectDeleteEnvironmentVariableResponse,
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

    def createprojectdefaultsettings(
        self, provider: str, organization: str, project: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectSettings]:
        """
        [__EXPERIMENTAL__]  Creates a new CircleCI project, and returns a list of the default advanced settings. Can only be called on a repo with a main branch and an existing config.yml file. Not yet available to projects that use GitLab or GitHub App.

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectSettings]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(provider)}/{encode_path_param(organization)}/{encode_path_param(project)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectSettings,
                    parse_obj_as(
                        type_=ProjectSettings,
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
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProjectCreateProjectDefaultSettings405Response,
                        parse_obj_as(
                            type_=ProjectCreateProjectDefaultSettings405Response,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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

    def getsettings(
        self, provider: str, organization: str, project: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectSettings]:
        """
        [__EXPERIMENTAL__] Returns a list of the advanced settings for a CircleCI project, whether enabled (true) or not (false).

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectSettings]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(provider)}/{encode_path_param(organization)}/{encode_path_param(project)}/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectSettings,
                    parse_obj_as(
                        type_=ProjectSettings,
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
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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

    def updatesettings(
        self,
        provider: str,
        organization: str,
        project: str,
        *,
        advanced: typing.Optional[ProjectSettingsAdvanced] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectSettings]:
        """
        [__EXPERIMENTAL__] Updates one or more of the advanced settings for a CircleCI project.

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        advanced : typing.Optional[ProjectSettingsAdvanced]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectSettings]
            Successful response. Always includes the full advanced settings object. Returned even when the provided updates match the existing settings, but can also be returned when `oss: true` fails to set.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(provider)}/{encode_path_param(organization)}/{encode_path_param(project)}/settings",
            method="PATCH",
            json={
                "advanced": convert_and_respect_annotation_metadata(
                    object_=advanced, annotation=ProjectSettingsAdvanced, direction="write"
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
                    ProjectSettings,
                    parse_obj_as(
                        type_=ProjectSettings,
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
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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


class AsyncRawProjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getbyslug(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectGetBySlugResponse]:
        """
        Retrieves a project by project slug.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectGetBySlugResponse]
            A project object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectGetBySlugResponse,
                    parse_obj_as(
                        type_=ProjectGetBySlugResponse,
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

    async def listcheckoutkeys(
        self,
        project_slug: str,
        *,
        digest: typing.Optional[ProjectListCheckoutKeysRequestDigest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectListCheckoutKeysResponse]:
        """
        Returns a sequence of checkout keys for `:project`.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        digest : typing.Optional[ProjectListCheckoutKeysRequestDigest]
            The fingerprint digest type to return. This may be either `md5` or `sha256`. If not passed, defaults to `md5`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectListCheckoutKeysResponse]
            A sequence of checkout keys.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/checkout-key",
            method="GET",
            params={
                "digest": digest,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectListCheckoutKeysResponse,
                    parse_obj_as(
                        type_=ProjectListCheckoutKeysResponse,
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

    async def createcheckoutkey(
        self,
        project_slug: str,
        *,
        type: ProjectCreateCheckoutKeyRequestType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectCreateCheckoutKeyResponse]:
        """
        Not available to projects that use GitLab or GitHub App. Creates a new checkout key. This API request is only usable with a user API token.
                                   Please ensure that you have authorized your account with GitHub before creating user keys.
                                   This is necessary to give CircleCI the permission to create a user key associated with
                                   your GitHub user account. You can find this page by visiting Project Settings > Checkout SSH Keys

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        type : ProjectCreateCheckoutKeyRequestType
            The type of checkout key to create. This may be either `deploy-key` or `user-key`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectCreateCheckoutKeyResponse]
            The checkout key.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/checkout-key",
            method="POST",
            json={
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
                    ProjectCreateCheckoutKeyResponse,
                    parse_obj_as(
                        type_=ProjectCreateCheckoutKeyResponse,
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

    async def getcheckoutkeybyfingerprint(
        self, project_slug: str, fingerprint: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectGetCheckoutKeyByFingerprintResponse]:
        """
        Returns an individual checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        fingerprint : str
            An SSH key fingerprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectGetCheckoutKeyByFingerprintResponse]
            The checkout key.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/checkout-key/{encode_path_param(fingerprint)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectGetCheckoutKeyByFingerprintResponse,
                    parse_obj_as(
                        type_=ProjectGetCheckoutKeyByFingerprintResponse,
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

    async def deletecheckoutkeybyfingerprint(
        self, project_slug: str, fingerprint: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectDeleteCheckoutKeyByFingerprintResponse]:
        """
        Deletes the checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        fingerprint : str
            An SSH key fingerprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDeleteCheckoutKeyByFingerprintResponse]
            A confirmation message.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/checkout-key/{encode_path_param(fingerprint)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDeleteCheckoutKeyByFingerprintResponse,
                    parse_obj_as(
                        type_=ProjectDeleteCheckoutKeyByFingerprintResponse,
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

    async def listenvvarvalues(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectListEnvVarValuesResponse]:
        """
        Returns four 'x' characters, in addition to the last four ASCII characters of the value, consistent with the display of environment variable values on the CircleCI website.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectListEnvVarValuesResponse]
            A sequence of environment variables.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/envvar",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectListEnvVarValuesResponse,
                    parse_obj_as(
                        type_=ProjectListEnvVarValuesResponse,
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

    async def createenvvar(
        self, project_slug: str, *, name: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectCreateEnvVarResponse]:
        """
        Creates a new environment variable.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        value : str
            The value of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectCreateEnvVarResponse]
            The environment variable.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/envvar",
            method="POST",
            json={
                "name": name,
                "value": value,
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
                    ProjectCreateEnvVarResponse,
                    parse_obj_as(
                        type_=ProjectCreateEnvVarResponse,
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

    async def getmaskedenvvar(
        self, project_slug: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectGetMaskedEnvVarResponse]:
        """
        Returns the masked value of environment variable :name.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectGetMaskedEnvVarResponse]
            The environment variable.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/envvar/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectGetMaskedEnvVarResponse,
                    parse_obj_as(
                        type_=ProjectGetMaskedEnvVarResponse,
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

    async def deleteenvironmentvariable(
        self, project_slug: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectDeleteEnvironmentVariableResponse]:
        """
        Deletes the environment variable named :name.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDeleteEnvironmentVariableResponse]
            A confirmation message.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/envvar/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDeleteEnvironmentVariableResponse,
                    parse_obj_as(
                        type_=ProjectDeleteEnvironmentVariableResponse,
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

    async def createprojectdefaultsettings(
        self, provider: str, organization: str, project: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectSettings]:
        """
        [__EXPERIMENTAL__]  Creates a new CircleCI project, and returns a list of the default advanced settings. Can only be called on a repo with a main branch and an existing config.yml file. Not yet available to projects that use GitLab or GitHub App.

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectSettings]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(provider)}/{encode_path_param(organization)}/{encode_path_param(project)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectSettings,
                    parse_obj_as(
                        type_=ProjectSettings,
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
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProjectCreateProjectDefaultSettings405Response,
                        parse_obj_as(
                            type_=ProjectCreateProjectDefaultSettings405Response,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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

    async def getsettings(
        self, provider: str, organization: str, project: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectSettings]:
        """
        [__EXPERIMENTAL__] Returns a list of the advanced settings for a CircleCI project, whether enabled (true) or not (false).

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectSettings]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(provider)}/{encode_path_param(organization)}/{encode_path_param(project)}/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectSettings,
                    parse_obj_as(
                        type_=ProjectSettings,
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
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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

    async def updatesettings(
        self,
        provider: str,
        organization: str,
        project: str,
        *,
        advanced: typing.Optional[ProjectSettingsAdvanced] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectSettings]:
        """
        [__EXPERIMENTAL__] Updates one or more of the advanced settings for a CircleCI project.

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        advanced : typing.Optional[ProjectSettingsAdvanced]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectSettings]
            Successful response. Always includes the full advanced settings object. Returned even when the provided updates match the existing settings, but can also be returned when `oss: true` fails to set.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(provider)}/{encode_path_param(organization)}/{encode_path_param(project)}/settings",
            method="PATCH",
            json={
                "advanced": convert_and_respect_annotation_metadata(
                    object_=advanced, annotation=ProjectSettingsAdvanced, direction="write"
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
                    ProjectSettings,
                    parse_obj_as(
                        type_=ProjectSettings,
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
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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
