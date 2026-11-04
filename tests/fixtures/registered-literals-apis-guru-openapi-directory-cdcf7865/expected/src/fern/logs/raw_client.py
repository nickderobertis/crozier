

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.logs_read_response import LogsReadResponse
from pydantic import ValidationError


class RawLogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def actions(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """

        A log can have one of many actions. The complete list of loggable actions (in the format {identifier}: {description}) is as follows:
        * `project_created`: A Node is created
        * `project_registered`: A Node is registered
        * `project_deleted`: A Node is deleted
        * `created_from`: A Node is created using an existing Node as a template
        * `pointer_created`: A Pointer is created
        * `pointer_forked`: A Pointer is forked
        * `pointer_removed`: A Pointer is removed
        * `node_removed`: A component is deleted
        * `node_forked`: A Node is forked
        ---
        * `made_public`: A Node is made public
        * `made_private`: A Node is made private
        * `tag_added`: A tag is added to a Node
        * `tag_removed`: A tag is removed from a Node
        * `edit_title`: A Node's title is changed
        * `edit_description`: A Node's description is changed
        * `updated_fields`: One or more of a Node's fields are changed
        * `external_ids_added`: An external identifier is added to a Node (e.g. DOI, ARK)
        * `view_only_link_added`: A view-only link was added to a Node
        * `view_only_link_removed`:  A view-only link was removed from a Node
        ---
        * `contributor_added`: A Contributor is added to a Node
        * `contributor_removed`: A Contributor is removed from a Node
        * `contributors_reordered`: A Contributor's position in a Node's bibliography is changed
        * `permissions_updated`: A Contributor`s permissions on a Node are changed
        * `made_contributor_visible`: A Contributor is made bibliographically visible on a Node
        * `made_contributor_invisible`: A Contributor is made bibliographically invisible on a Node
        ---
        * `wiki_updated`: A Node's wiki is updated
        * `wiki_deleted`: A Node's wiki is deleted
        * `wiki_renamed`: A Node's wiki is renamed
        * `made_wiki_public`: A Node's wiki is made public
        * `made_wiki_private`: A Node's wiki is made private
        ---
        * `addon_added`: An add-on is linked to a Node
        * `addon_removed`: An add-on is unlinked from a Node
        * `addon_file_moved`: A File in a Node's linked add-on is moved
        * `addon_file_copied`: A File in a Node's linked add-on is copied
        * `addon_file_renamed`: A File in a Node's linked add-on is renamed
        * `node_authorized`: An addon is authorized for a project
        * `node_deauthorized`: An addon is deauthorized for a project
        * `folder_created`: A Folder is created in a Node's linked add-on
        * `file_added`: A File is added to a Node's linked add-on
        * `file_updated`: A File is updated on a Node's linked add-on
        * `file_removed`: A File is removed from a Node's linked add-on
        * `file_restored`: A File is restored in a Node's linked add-on
        ---
        * `comment_added`: A Comment is added to some item
        * `comment_removed`: A Comment is removed from some item
        * `comment_updated`: A Comment is updated on some item
        ---
        * `embargo_initiated`: An embargoed Registration is proposed on a Node
        * `embargo_approved`: A proposed Embargo of a Node is approved
        * `embargo_cancelled`: A proposed Embargo of a Node is cancelled
        * `embargo_completed`: A proposed Embargo of a Node is completed
        * `retraction_initiated`: A Withdrawal of a Registration is proposed
        * `retraction_approved`: A Withdrawal of a Registration is approved
        * `retraction_cancelled`: A Withdrawal of a Registration is cancelled
        * `registration_initiated`: A Registration of a Node is proposed
        * `registration_approved`: A proposed Registration is approved
        * `registration_cancelled`: A proposed Registration is cancelled

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "actions/",
            method="GET",
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

    def read(
        self, log_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LogsReadResponse]:
        """
        Retrieves the details of a log.
        A log is permanent immutable record of a node's history. A log is created when a user performs one of many actions. See the [actions](#Logs_logs_actions) section for more details.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested log, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        log_id : str
            The unique identifier of the log you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LogsReadResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"logs/{encode_path_param(log_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogsReadResponse,
                    parse_obj_as(
                        type_=LogsReadResponse,
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


class AsyncRawLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def actions(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """

        A log can have one of many actions. The complete list of loggable actions (in the format {identifier}: {description}) is as follows:
        * `project_created`: A Node is created
        * `project_registered`: A Node is registered
        * `project_deleted`: A Node is deleted
        * `created_from`: A Node is created using an existing Node as a template
        * `pointer_created`: A Pointer is created
        * `pointer_forked`: A Pointer is forked
        * `pointer_removed`: A Pointer is removed
        * `node_removed`: A component is deleted
        * `node_forked`: A Node is forked
        ---
        * `made_public`: A Node is made public
        * `made_private`: A Node is made private
        * `tag_added`: A tag is added to a Node
        * `tag_removed`: A tag is removed from a Node
        * `edit_title`: A Node's title is changed
        * `edit_description`: A Node's description is changed
        * `updated_fields`: One or more of a Node's fields are changed
        * `external_ids_added`: An external identifier is added to a Node (e.g. DOI, ARK)
        * `view_only_link_added`: A view-only link was added to a Node
        * `view_only_link_removed`:  A view-only link was removed from a Node
        ---
        * `contributor_added`: A Contributor is added to a Node
        * `contributor_removed`: A Contributor is removed from a Node
        * `contributors_reordered`: A Contributor's position in a Node's bibliography is changed
        * `permissions_updated`: A Contributor`s permissions on a Node are changed
        * `made_contributor_visible`: A Contributor is made bibliographically visible on a Node
        * `made_contributor_invisible`: A Contributor is made bibliographically invisible on a Node
        ---
        * `wiki_updated`: A Node's wiki is updated
        * `wiki_deleted`: A Node's wiki is deleted
        * `wiki_renamed`: A Node's wiki is renamed
        * `made_wiki_public`: A Node's wiki is made public
        * `made_wiki_private`: A Node's wiki is made private
        ---
        * `addon_added`: An add-on is linked to a Node
        * `addon_removed`: An add-on is unlinked from a Node
        * `addon_file_moved`: A File in a Node's linked add-on is moved
        * `addon_file_copied`: A File in a Node's linked add-on is copied
        * `addon_file_renamed`: A File in a Node's linked add-on is renamed
        * `node_authorized`: An addon is authorized for a project
        * `node_deauthorized`: An addon is deauthorized for a project
        * `folder_created`: A Folder is created in a Node's linked add-on
        * `file_added`: A File is added to a Node's linked add-on
        * `file_updated`: A File is updated on a Node's linked add-on
        * `file_removed`: A File is removed from a Node's linked add-on
        * `file_restored`: A File is restored in a Node's linked add-on
        ---
        * `comment_added`: A Comment is added to some item
        * `comment_removed`: A Comment is removed from some item
        * `comment_updated`: A Comment is updated on some item
        ---
        * `embargo_initiated`: An embargoed Registration is proposed on a Node
        * `embargo_approved`: A proposed Embargo of a Node is approved
        * `embargo_cancelled`: A proposed Embargo of a Node is cancelled
        * `embargo_completed`: A proposed Embargo of a Node is completed
        * `retraction_initiated`: A Withdrawal of a Registration is proposed
        * `retraction_approved`: A Withdrawal of a Registration is approved
        * `retraction_cancelled`: A Withdrawal of a Registration is cancelled
        * `registration_initiated`: A Registration of a Node is proposed
        * `registration_approved`: A proposed Registration is approved
        * `registration_cancelled`: A proposed Registration is cancelled

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "actions/",
            method="GET",
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

    async def read(
        self, log_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LogsReadResponse]:
        """
        Retrieves the details of a log.
        A log is permanent immutable record of a node's history. A log is created when a user performs one of many actions. See the [actions](#Logs_logs_actions) section for more details.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested log, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        log_id : str
            The unique identifier of the log you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LogsReadResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"logs/{encode_path_param(log_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogsReadResponse,
                    parse_obj_as(
                        type_=LogsReadResponse,
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
