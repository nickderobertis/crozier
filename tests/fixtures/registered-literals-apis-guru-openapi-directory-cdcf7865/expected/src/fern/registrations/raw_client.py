

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.registrations_children_list_response_item import RegistrationsChildrenListResponseItem
from .types.registrations_citation_read_response import RegistrationsCitationReadResponse
from .types.registrations_citations_list_response_item import RegistrationsCitationsListResponseItem
from .types.registrations_comments_list_response_item import RegistrationsCommentsListResponseItem
from .types.registrations_contributors_list_response_item import RegistrationsContributorsListResponseItem
from .types.registrations_contributors_read_response_item import RegistrationsContributorsReadResponseItem
from .types.registrations_files_list_response_item import RegistrationsFilesListResponseItem
from .types.registrations_files_read_response import RegistrationsFilesReadResponse
from .types.registrations_forks_list_response_item import RegistrationsForksListResponseItem
from .types.registrations_identifiers_list_response_item import RegistrationsIdentifiersListResponseItem
from .types.registrations_institutions_list_response_item import RegistrationsInstitutionsListResponseItem
from .types.registrations_linked_nodes_list_response_item import RegistrationsLinkedNodesListResponseItem
from .types.registrations_list_response_item import RegistrationsListResponseItem
from .types.registrations_logs_list_response_item import RegistrationsLogsListResponseItem
from .types.registrations_providers_list_response_item import RegistrationsProvidersListResponseItem
from .types.registrations_read_response import RegistrationsReadResponse
from .types.registrations_view_only_links_list_response_item import RegistrationsViewOnlyLinksListResponseItem
from .types.registrations_view_only_links_read_response import RegistrationsViewOnlyLinksReadResponse
from .types.registrations_wikis_list_response_item import RegistrationsWikisListResponseItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRegistrationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsListResponseItem]]:
        """
        A paginated list of registrations on the OSF to which the user has access.

        The returned registrations are those which are public or which the user has access to view.

        Non-registered nodes cannot be accessed through this endpoint (use the [nodes](#Nodes_nodes_list) endpoints instead).

        #### Registrations
        A registration on the OSF creates a frozen, time-stamped version of a project that cannot be edited or deleted. The *original project* can still be edited, while the registered version cannot.

        Registrations can be made public immediately or embargoed for up to 4 years.

        #### Withdrawals
        Registrations cannot be deleted, but they can be withdrawn. Withdrawing a registration removes the content of the registration but leaves behind basic metadata. A withdrawn registration will display a limited subset of information, namely, title, description, date_created, date_registered, date_withdrawn, registration, withdrawn, withdrawal_justification, and registration supplement. All other fields will be displayed as null. Additionally, the only relationship that remains accesible for a withdrawn registration is the contributors. All other relationships will return a **403 Forbidden** response.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 registrations. Each resource in the array is a separate registration object and contains the full representation of the registration, meaning additional requests to a registration's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/?filter[title]=open.

        Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "registrations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsListResponseItem],
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

    def read(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegistrationsReadResponse]:
        """
        Retrieve the details of a given registration.
        #### Permissions
        Only project contributors may retrieve the details of a registration that is embargoed, or has not yet been made public. Attempting to retrieve a private registration for which you are not a contributor will result in a **403 Forbidden** response.

        Authentication is not required to view the details of a public registration, as public registrations give read-only access to everyone.
        #### Registrations
        A registration on the OSF creates a frozen, time-stamped version of a project that cannot be edited or deleted. The *original project* can still be edited, while the registered version cannot.

        Registrations can be made public immediately or embargoed for up to 4 years.

        #### Withdrawals
        Registrations cannot be deleted, but they can be withdrawn. Withdrawing a registration removes the content of the registration but leaves behind basic metadata. A withdrawn registration will display a limited subset of information, namely, title, description, date_created, date_registered, date_withdrawn, registration, withdrawn, withdrawal_justification, and registration supplement. All other fields will be displayed as null. Additionally, the only relationship that remains accesible for a withdrawn registration is the contributors. All other relationships will return a **403 Forbidden** response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegistrationsReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationsReadResponse,
                    parse_obj_as(
                        type_=RegistrationsReadResponse,
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

    def partial_update(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Updates a registration's privacy from **private** to **public**.

        Registrations can be updated with either a **PUT** or **PATCH** request. The `public` field is the only field that can be modified on a registration

        Registrations can only be turned from private to public, not vice versa.
        #### Permissions
        Only project administrators may update a registration.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/",
            method="PATCH",
            json={},
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

    def children_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsChildrenListResponseItem]]:
        """

        A paginated list of children of a registration.

        The list consists of the next level child registrations for the given registration. The returned registrations are sorted by their `date_modified`, with the most recently updated child registrations appearing first.

        The list will include child registrations that are public, as well as child registrations that are private, if the authenticated user has permission to view them.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 child registrations. If the given registration has zero child registrations, the `data` key will contain an empty array. Each resource in the array is a separate registration object and contains the full representation of the child registration.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        #### Filtering
        You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/children/?filter[title]=reproducibility.

        Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.

        Most fields are string fields and will be filtered using simple substring matching. Public is a boolean field, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsChildrenListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/children/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsChildrenListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsChildrenListResponseItem],
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

    def citations_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsCitationsListResponseItem]]:
        """

        A paginated list of the registration's alternative citation styles

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 citation styles. Each resource in the array is a separate citation styles object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include citation styles that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/citations/?filter[title]=open.

        Citation styles may be filtered by their `id`, `title`, `short-title`, and `summary`.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsCitationsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/citations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsCitationsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsCitationsListResponseItem],
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

    def citation_read(
        self, registration_id: str, citation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegistrationsCitationReadResponse]:
        """
        Retrieves the citation style details for a registration, in CSL format.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the details necessary for the citation style.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        citation_id : str
            The unique identifier of the citation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegistrationsCitationReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/citations/{encode_path_param(citation_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationsCitationReadResponse,
                    parse_obj_as(
                        type_=RegistrationsCitationReadResponse,
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

    def comments_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsCommentsListResponseItem]]:
        """

        A paginated list of the registration's comments.

        The returned comments are sorted by their creation date, with the most recent comments appearing first.
        #### Permissions
        Comments of public registrations are given read-only access to everyone.

        If the comment-level is `private`, only registration contributors have permission to comment.

        If the comment-level is `public`, any logged-in OSF user can comment.

        Comments of private registrations are only visible to contributors and administrators on the registration.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include comments that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wuerf/comments/?filter[target]=wuerf

        Comments may be filtered by their `deleted`, `target`, `date_created`, `date_modified`.

        Most fields are string fields and will be filtered using simple substring matching. Deleted is a boolean field, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting `true` or `false` in the query will cause the match to fail.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsCommentsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/comments/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsCommentsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsCommentsListResponseItem],
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

    def contributors_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsContributorsListResponseItem]]:
        """
        A paginated list of all contributors on this registration.
        The returned contributors are sorted by their index.

        Contributors are users who can make changes to the registration or, in the case of private registration, have read access to the registration.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed in the contributors list on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 contributors. Each resource in the array contains the full representation of the contributor. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wu3a4/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsContributorsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/contributors/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsContributorsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsContributorsListResponseItem],
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

    def contributors_read(
        self, registration_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsContributorsReadResponseItem]]:
        """
        Retrieves the details of a contributor on this registration.

        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsContributorsReadResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/contributors/{encode_path_param(user_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsContributorsReadResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsContributorsReadResponseItem],
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

    def providers_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsProvidersListResponseItem]]:
        """
        A paginated list of storage providers enabled on the registration

        Users of the OSF may access their data on a [number of cloud-storage services](https://api.osf.io/v2/#storage-providers) that have integrations with the OSF. We call these **providers**. By default, every node has access to the OSF-provided storage but may use as many of the supported providers as desired.


        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 files. Each resource in the array is a separate file object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Note: In the OSF filesystem model, providers are treated as folders, but with special properties that distinguish them from regular folders. Every provider folder is considered a root folder, and may not be deleted through the regular file API.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsProvidersListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/files/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsProvidersListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsProvidersListResponseItem],
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

    def files_list(
        self, registration_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsFilesListResponseItem]]:
        """
        List of all the registration's files/folders for a given storage provider.

        #### Returns

        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of files. Each resource in the array is a separate file object and contains the full representation of the file.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        #### Filtering

        You can optionally request that the response only include files that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/files/osfstorage/?filter[kind]=file

        Files may be filtered by `id`, `name`, `node`, `kind`, `path`, `provider`, `size`, and `last_touched`.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        provider : str
            The unique identifier of the storage provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsFilesListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/files/{encode_path_param(provider)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsFilesListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsFilesListResponseItem],
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

    def files_read(
        self, registration_id: str, provider: str, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegistrationsFilesReadResponse]:
        """
        Retrieves the details of a registration file for the given storage provider.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested registration file object, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        provider : str
            The unique identifier of the storage provider.

        path : str
            The unique identifier of the file path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegistrationsFilesReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/files/{encode_path_param(provider)}/{encode_path_param(path)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationsFilesReadResponse,
                    parse_obj_as(
                        type_=RegistrationsFilesReadResponse,
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

    def forks_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsForksListResponseItem]]:
        """

        A paginated list of the registration’s forks

        The returned forks are sorted by their `forked_date`, with the most recent forks appearing first.

        Forking a registration creates a copy of an existing registration and all of its contents.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 forks. If the current registration has no fork, the `data` key will contain an empty array. Each resource in the array is a separate registration object and contains the full representation of the registration's fork.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsForksListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/forks/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsForksListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsForksListResponseItem],
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

    def forks_create(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Creates a fork of the given registration.

        Forking a project creates a copy of an existing registration and all of its contents. The fork always points back to the original registration, forming a network of registrations.

        You might use a fork to copy another's work to build on and extend. For example, a professor may create an OSF project of materials for individual student use. Each student forks the project to have his or her own copy of the materials to start his/her own work.

        When creating a fork, your fork will only contain public components of the current registration and components for which you are a contributor. Private components that you do not have access to will not be forked.
        #### Required
        There are no required attributes when creating a fork, as all of the forked registration's attributes will be copied from the current registration.

        The `title` field is optional, with the default title being "Fork of " prepended to the current registration's title.
        #### Returns
        Returns a JSON object with a `data` key containing the complete representation of the forked registration, if the request is successful.
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/forks/",
            method="POST",
            json={},
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

    def identifiers_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsIdentifiersListResponseItem]]:
        """
        A paginated list of the registration's identifiers.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of identifiers. Each resource in the array is a separate identifier object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering

        You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/identifiers/?filter[category]=ark

        Identifiers may be filtered by their `category` e.g `ark` or `doi`.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsIdentifiersListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/identifiers/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsIdentifiersListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsIdentifiersListResponseItem],
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

    def institutions_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsInstitutionsListResponseItem]]:
        """
        A paginated list of institutions affiliated with the registration.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 affiliated institutions. Each resource in the array is a separate institution object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsInstitutionsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/institutions/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsInstitutionsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsInstitutionsListResponseItem],
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

    def linked_nodes_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsLinkedNodesListResponseItem]]:
        """
        List of all nodes linked to the registration.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/linked_nodes/?filter[title]=reproducibility/?filter[title]=reproducibility.

        Nodes may be filtered by their `title`, `category`, `description`, `public`, `registration`, or `tags`. `title`, `description`, and `category` are string fields and will be filteres using simple substring matching. `public`, `registration` are boolean and can be filtered using truthy values, such as `true`, `false`, `0`, `1`. `tags` is an array of simple strings.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsLinkedNodesListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/linked_nodes/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsLinkedNodesListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsLinkedNodesListResponseItem],
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

    def logs_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsLogsListResponseItem]]:
        """
        A paginated list of the registration's logs.

        The returned logs are sorted by their `date`, with the most recents logs appearing first.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 logs. Each resource in the array is a separate logs object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include logs that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/logs/?filter[action]=made_private.

        Logs may be filtered by their `action`, and `date`.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsLogsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/logs/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsLogsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsLogsListResponseItem],
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

    def view_only_links_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsViewOnlyLinksListResponseItem]]:
        """
        A paginated list of view only links created for this registration.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 view only links. Each resource in the array is a view only link object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        #### Permissions

        View only links on a registration, public or private, are readable and writeable only by users that are administrators on the registration.

        #### Filtering

        You can optionally request that the response only include view only links that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wu3a4/view_only_links/?filter[anonymous]=true.

        View Only Links may be filtered based on their `name`, `anonymous` and `date_created` fields. Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsViewOnlyLinksListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/view_only_links/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsViewOnlyLinksListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsViewOnlyLinksListResponseItem],
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

    def view_only_links_read(
        self, registration_id: str, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegistrationsViewOnlyLinksReadResponse]:
        """
        Retrieves the details of a view only link created from this registration.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Permissions

        View only links on a registration, public or private, are readable and writeable only by users that are administrators on the registration.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        link_id : str
            The unique identifier of the view only link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegistrationsViewOnlyLinksReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/view_only_links/{encode_path_param(link_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationsViewOnlyLinksReadResponse,
                    parse_obj_as(
                        type_=RegistrationsViewOnlyLinksReadResponse,
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

    def wikis_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RegistrationsWikisListResponseItem]]:
        """
        A paginated list of the registration's wiki pages
        #### Returns
        A list of all registration's current wiki page versions ordered by their date_modified. Each resource contains the full representation of the wiki, meaning additional requests to an individual wiki's detail view are not necessary.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Filtering
        Wiki pages can be filtered based on their `name` and `date_modified` fields.
        + `filter[name]=<Str>` -- filter wiki pages by name
        + `filter[date_modified][comparison_operator]=YYYY-MM-DDTH:M:S` -- filter wiki pages based on date modified.

        Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RegistrationsWikisListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/wikis/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsWikisListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsWikisListResponseItem],
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


class AsyncRawRegistrationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsListResponseItem]]:
        """
        A paginated list of registrations on the OSF to which the user has access.

        The returned registrations are those which are public or which the user has access to view.

        Non-registered nodes cannot be accessed through this endpoint (use the [nodes](#Nodes_nodes_list) endpoints instead).

        #### Registrations
        A registration on the OSF creates a frozen, time-stamped version of a project that cannot be edited or deleted. The *original project* can still be edited, while the registered version cannot.

        Registrations can be made public immediately or embargoed for up to 4 years.

        #### Withdrawals
        Registrations cannot be deleted, but they can be withdrawn. Withdrawing a registration removes the content of the registration but leaves behind basic metadata. A withdrawn registration will display a limited subset of information, namely, title, description, date_created, date_registered, date_withdrawn, registration, withdrawn, withdrawal_justification, and registration supplement. All other fields will be displayed as null. Additionally, the only relationship that remains accesible for a withdrawn registration is the contributors. All other relationships will return a **403 Forbidden** response.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 registrations. Each resource in the array is a separate registration object and contains the full representation of the registration, meaning additional requests to a registration's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/?filter[title]=open.

        Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "registrations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsListResponseItem],
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

    async def read(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegistrationsReadResponse]:
        """
        Retrieve the details of a given registration.
        #### Permissions
        Only project contributors may retrieve the details of a registration that is embargoed, or has not yet been made public. Attempting to retrieve a private registration for which you are not a contributor will result in a **403 Forbidden** response.

        Authentication is not required to view the details of a public registration, as public registrations give read-only access to everyone.
        #### Registrations
        A registration on the OSF creates a frozen, time-stamped version of a project that cannot be edited or deleted. The *original project* can still be edited, while the registered version cannot.

        Registrations can be made public immediately or embargoed for up to 4 years.

        #### Withdrawals
        Registrations cannot be deleted, but they can be withdrawn. Withdrawing a registration removes the content of the registration but leaves behind basic metadata. A withdrawn registration will display a limited subset of information, namely, title, description, date_created, date_registered, date_withdrawn, registration, withdrawn, withdrawal_justification, and registration supplement. All other fields will be displayed as null. Additionally, the only relationship that remains accesible for a withdrawn registration is the contributors. All other relationships will return a **403 Forbidden** response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegistrationsReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationsReadResponse,
                    parse_obj_as(
                        type_=RegistrationsReadResponse,
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

    async def partial_update(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Updates a registration's privacy from **private** to **public**.

        Registrations can be updated with either a **PUT** or **PATCH** request. The `public` field is the only field that can be modified on a registration

        Registrations can only be turned from private to public, not vice versa.
        #### Permissions
        Only project administrators may update a registration.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/",
            method="PATCH",
            json={},
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

    async def children_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsChildrenListResponseItem]]:
        """

        A paginated list of children of a registration.

        The list consists of the next level child registrations for the given registration. The returned registrations are sorted by their `date_modified`, with the most recently updated child registrations appearing first.

        The list will include child registrations that are public, as well as child registrations that are private, if the authenticated user has permission to view them.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 child registrations. If the given registration has zero child registrations, the `data` key will contain an empty array. Each resource in the array is a separate registration object and contains the full representation of the child registration.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        #### Filtering
        You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/children/?filter[title]=reproducibility.

        Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.

        Most fields are string fields and will be filtered using simple substring matching. Public is a boolean field, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsChildrenListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/children/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsChildrenListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsChildrenListResponseItem],
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

    async def citations_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsCitationsListResponseItem]]:
        """

        A paginated list of the registration's alternative citation styles

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 citation styles. Each resource in the array is a separate citation styles object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include citation styles that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/citations/?filter[title]=open.

        Citation styles may be filtered by their `id`, `title`, `short-title`, and `summary`.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsCitationsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/citations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsCitationsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsCitationsListResponseItem],
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

    async def citation_read(
        self, registration_id: str, citation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegistrationsCitationReadResponse]:
        """
        Retrieves the citation style details for a registration, in CSL format.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the details necessary for the citation style.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        citation_id : str
            The unique identifier of the citation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegistrationsCitationReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/citations/{encode_path_param(citation_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationsCitationReadResponse,
                    parse_obj_as(
                        type_=RegistrationsCitationReadResponse,
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

    async def comments_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsCommentsListResponseItem]]:
        """

        A paginated list of the registration's comments.

        The returned comments are sorted by their creation date, with the most recent comments appearing first.
        #### Permissions
        Comments of public registrations are given read-only access to everyone.

        If the comment-level is `private`, only registration contributors have permission to comment.

        If the comment-level is `public`, any logged-in OSF user can comment.

        Comments of private registrations are only visible to contributors and administrators on the registration.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include comments that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wuerf/comments/?filter[target]=wuerf

        Comments may be filtered by their `deleted`, `target`, `date_created`, `date_modified`.

        Most fields are string fields and will be filtered using simple substring matching. Deleted is a boolean field, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting `true` or `false` in the query will cause the match to fail.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsCommentsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/comments/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsCommentsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsCommentsListResponseItem],
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

    async def contributors_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsContributorsListResponseItem]]:
        """
        A paginated list of all contributors on this registration.
        The returned contributors are sorted by their index.

        Contributors are users who can make changes to the registration or, in the case of private registration, have read access to the registration.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed in the contributors list on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 contributors. Each resource in the array contains the full representation of the contributor. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wu3a4/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsContributorsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/contributors/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsContributorsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsContributorsListResponseItem],
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

    async def contributors_read(
        self, registration_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsContributorsReadResponseItem]]:
        """
        Retrieves the details of a contributor on this registration.

        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsContributorsReadResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/contributors/{encode_path_param(user_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsContributorsReadResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsContributorsReadResponseItem],
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

    async def providers_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsProvidersListResponseItem]]:
        """
        A paginated list of storage providers enabled on the registration

        Users of the OSF may access their data on a [number of cloud-storage services](https://api.osf.io/v2/#storage-providers) that have integrations with the OSF. We call these **providers**. By default, every node has access to the OSF-provided storage but may use as many of the supported providers as desired.


        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 files. Each resource in the array is a separate file object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Note: In the OSF filesystem model, providers are treated as folders, but with special properties that distinguish them from regular folders. Every provider folder is considered a root folder, and may not be deleted through the regular file API.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsProvidersListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/files/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsProvidersListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsProvidersListResponseItem],
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

    async def files_list(
        self, registration_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsFilesListResponseItem]]:
        """
        List of all the registration's files/folders for a given storage provider.

        #### Returns

        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of files. Each resource in the array is a separate file object and contains the full representation of the file.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        #### Filtering

        You can optionally request that the response only include files that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/files/osfstorage/?filter[kind]=file

        Files may be filtered by `id`, `name`, `node`, `kind`, `path`, `provider`, `size`, and `last_touched`.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        provider : str
            The unique identifier of the storage provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsFilesListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/files/{encode_path_param(provider)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsFilesListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsFilesListResponseItem],
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

    async def files_read(
        self, registration_id: str, provider: str, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegistrationsFilesReadResponse]:
        """
        Retrieves the details of a registration file for the given storage provider.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested registration file object, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        provider : str
            The unique identifier of the storage provider.

        path : str
            The unique identifier of the file path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegistrationsFilesReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/files/{encode_path_param(provider)}/{encode_path_param(path)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationsFilesReadResponse,
                    parse_obj_as(
                        type_=RegistrationsFilesReadResponse,
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

    async def forks_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsForksListResponseItem]]:
        """

        A paginated list of the registration’s forks

        The returned forks are sorted by their `forked_date`, with the most recent forks appearing first.

        Forking a registration creates a copy of an existing registration and all of its contents.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 forks. If the current registration has no fork, the `data` key will contain an empty array. Each resource in the array is a separate registration object and contains the full representation of the registration's fork.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsForksListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/forks/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsForksListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsForksListResponseItem],
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

    async def forks_create(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Creates a fork of the given registration.

        Forking a project creates a copy of an existing registration and all of its contents. The fork always points back to the original registration, forming a network of registrations.

        You might use a fork to copy another's work to build on and extend. For example, a professor may create an OSF project of materials for individual student use. Each student forks the project to have his or her own copy of the materials to start his/her own work.

        When creating a fork, your fork will only contain public components of the current registration and components for which you are a contributor. Private components that you do not have access to will not be forked.
        #### Required
        There are no required attributes when creating a fork, as all of the forked registration's attributes will be copied from the current registration.

        The `title` field is optional, with the default title being "Fork of " prepended to the current registration's title.
        #### Returns
        Returns a JSON object with a `data` key containing the complete representation of the forked registration, if the request is successful.
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/forks/",
            method="POST",
            json={},
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

    async def identifiers_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsIdentifiersListResponseItem]]:
        """
        A paginated list of the registration's identifiers.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of identifiers. Each resource in the array is a separate identifier object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering

        You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/identifiers/?filter[category]=ark

        Identifiers may be filtered by their `category` e.g `ark` or `doi`.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsIdentifiersListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/identifiers/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsIdentifiersListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsIdentifiersListResponseItem],
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

    async def institutions_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsInstitutionsListResponseItem]]:
        """
        A paginated list of institutions affiliated with the registration.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 affiliated institutions. Each resource in the array is a separate institution object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsInstitutionsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/institutions/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsInstitutionsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsInstitutionsListResponseItem],
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

    async def linked_nodes_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsLinkedNodesListResponseItem]]:
        """
        List of all nodes linked to the registration.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/linked_nodes/?filter[title]=reproducibility/?filter[title]=reproducibility.

        Nodes may be filtered by their `title`, `category`, `description`, `public`, `registration`, or `tags`. `title`, `description`, and `category` are string fields and will be filteres using simple substring matching. `public`, `registration` are boolean and can be filtered using truthy values, such as `true`, `false`, `0`, `1`. `tags` is an array of simple strings.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsLinkedNodesListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/linked_nodes/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsLinkedNodesListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsLinkedNodesListResponseItem],
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

    async def logs_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsLogsListResponseItem]]:
        """
        A paginated list of the registration's logs.

        The returned logs are sorted by their `date`, with the most recents logs appearing first.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 logs. Each resource in the array is a separate logs object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include logs that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/logs/?filter[action]=made_private.

        Logs may be filtered by their `action`, and `date`.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsLogsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/logs/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsLogsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsLogsListResponseItem],
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

    async def view_only_links_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsViewOnlyLinksListResponseItem]]:
        """
        A paginated list of view only links created for this registration.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 view only links. Each resource in the array is a view only link object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        #### Permissions

        View only links on a registration, public or private, are readable and writeable only by users that are administrators on the registration.

        #### Filtering

        You can optionally request that the response only include view only links that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wu3a4/view_only_links/?filter[anonymous]=true.

        View Only Links may be filtered based on their `name`, `anonymous` and `date_created` fields. Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsViewOnlyLinksListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/view_only_links/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsViewOnlyLinksListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsViewOnlyLinksListResponseItem],
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

    async def view_only_links_read(
        self, registration_id: str, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegistrationsViewOnlyLinksReadResponse]:
        """
        Retrieves the details of a view only link created from this registration.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Permissions

        View only links on a registration, public or private, are readable and writeable only by users that are administrators on the registration.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        link_id : str
            The unique identifier of the view only link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegistrationsViewOnlyLinksReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/view_only_links/{encode_path_param(link_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationsViewOnlyLinksReadResponse,
                    parse_obj_as(
                        type_=RegistrationsViewOnlyLinksReadResponse,
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

    async def wikis_list(
        self, registration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RegistrationsWikisListResponseItem]]:
        """
        A paginated list of the registration's wiki pages
        #### Returns
        A list of all registration's current wiki page versions ordered by their date_modified. Each resource contains the full representation of the wiki, meaning additional requests to an individual wiki's detail view are not necessary.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Filtering
        Wiki pages can be filtered based on their `name` and `date_modified` fields.
        + `filter[name]=<Str>` -- filter wiki pages by name
        + `filter[date_modified][comparison_operator]=YYYY-MM-DDTH:M:S` -- filter wiki pages based on date modified.

        Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.

        Parameters
        ----------
        registration_id : str
            The unique identifier of the registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RegistrationsWikisListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registrations/{encode_path_param(registration_id)}/wikis/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RegistrationsWikisListResponseItem],
                    parse_obj_as(
                        type_=typing.List[RegistrationsWikisListResponseItem],
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
