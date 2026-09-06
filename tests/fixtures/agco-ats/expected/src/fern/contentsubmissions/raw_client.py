

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
from ..types.api_paged_response_content_submission_shared_business_entities_content_submission import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission,
)
from ..types.api_paged_response_content_submission_shared_business_entities_content_submission_attribute import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
)
from ..types.build_system_shared_interfaces_i_job_run import BuildSystemSharedInterfacesIJobRun
from ..types.content_submission_shared_business_entities_content_definition import (
    ContentSubmissionSharedBusinessEntitiesContentDefinition,
)
from ..types.content_submission_shared_business_entities_content_submission import (
    ContentSubmissionSharedBusinessEntitiesContentSubmission,
)
from ..types.content_submission_shared_business_entities_content_submission_attribute import (
    ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContentsubmissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def putcontentsubmissionattributes(
        self,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/ContentSubmissionAttributes/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
                direction="write",
            ),
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

    def putcontentsubmissionattributeasync(
        self,
        content_submission_attribute_id: int,
        *,
        name: str,
        content_submission_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_attribute_id : int
            The ID of the Attribute to update.

        name : str
            The name of this Attribute.

        content_submission_id : typing.Optional[int]
            The ID of the content submission to which this attribute belongs.

        id : typing.Optional[int]
            The ID of this attribute.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissionAttributes/{encode_path_param(content_submission_attribute_id)}",
            method="PUT",
            json={
                "ContentSubmissionID": content_submission_id,
                "ID": id,
                "Name": name,
                "Value": value,
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

    def deletecontentsubmissionattribute(
        self, content_submission_attribute_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_attribute_id : int
            The ID of the Attribute to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissionAttributes/{encode_path_param(content_submission_attribute_id)}",
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

    def getcontentsubmissions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        content_definition_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        release_id: typing.Optional[int] = None,
        type_id: typing.Optional[int] = None,
        version: typing.Optional[int] = None,
        include_definition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission]:
        """
        Gets a collection of ContentSubmissions. When successful, the response is a PagedResponse of ContentSubmissions. Additional searches: attributes[Name]=Value. This can be used to search for submissions that have the specified values for attributes. Beginning and ending wildcard (*) supported for value.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        content_definition_id : typing.Optional[int]
            Optional. Filter by ContentDefinitionID

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        release_id : typing.Optional[int]
            Optional. Filter the submissions by whether they are part of the Release with the specified Release ID.

        type_id : typing.Optional[int]
            Optional. Filter submissions by their ContentDefinition's Type ID.

        version : typing.Optional[int]
            Optional. Filter submissions by their Version.

        include_definition : typing.Optional[bool]
            Optional. If true, includes the ContentDefinition for each submission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/ContentSubmissions",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "userID": user_id,
                "contentDefinitionID": content_definition_id,
                "includeAttributes": include_attributes,
                "releaseID": release_id,
                "typeID": type_id,
                "version": version,
                "includeDefinition": include_definition,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission,
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

    def postcontentsubmission(
        self,
        *,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]
        ] = OMIT,
        build_id: typing.Optional[int] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        content_submission_id: typing.Optional[int] = OMIT,
        definition: typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        release_notes: typing.Optional[str] = OMIT,
        repository: typing.Optional[str] = OMIT,
        revision: typing.Optional[int] = OMIT,
        submission_date: typing.Optional[dt.datetime] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Creates a ContentSubmission.  The body of the POST is the ContentSubmission to create.
                    The ContentSubmissionID will be assigned on creation of the Job.  When successful, the response
                    is the ContentSubmissionID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]]
            Attributes of this ContentSubmission

        build_id : typing.Optional[int]
            ReadOnly. The ID of the Azure DevOps Build which will build the content package.

        content_definition_id : typing.Optional[int]
            The ID of the Content Definition.

        content_submission_id : typing.Optional[int]
            The ID of this Content Submission.

        definition : typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition]
            The ContentDefinition for this ContentSubmission

        job_run_id : typing.Optional[int]
            ReadOnly. The ID of the JobRun which will build the content package.

        package_id : typing.Optional[str]
            The ID of package generated by this content submission.

        release_notes : typing.Optional[str]
            Release Notes for this ContentSubmission

        repository : typing.Optional[str]
            The SVN repository used as the source of this content submission

        revision : typing.Optional[int]
            The SVN revision used as the source of this content submission.

        submission_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time the content submission was made.

        user_id : typing.Optional[int]
            Read Only. The ID of the user who submitted the content

        version : typing.Optional[int]
            Optional.  The version number assigned to this Content Submission and the resulting Package.
                        If not provided, version shall be 1 if it is the first content submission for the
                        ContentDefinitionID otherwise it shall be the highest content submission version for the
                        specified ContentDefinitionID incremented by 1.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/ContentSubmissions",
            method="POST",
            json={
                "Attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
                    direction="write",
                ),
                "BuildID": build_id,
                "ContentDefinitionID": content_definition_id,
                "ContentSubmissionID": content_submission_id,
                "Definition": convert_and_respect_annotation_metadata(
                    object_=definition,
                    annotation=ContentSubmissionSharedBusinessEntitiesContentDefinition,
                    direction="write",
                ),
                "JobRunID": job_run_id,
                "PackageID": package_id,
                "ReleaseNotes": release_notes,
                "Repository": repository,
                "Revision": revision,
                "SubmissionDate": submission_date,
                "UserID": user_id,
                "Version": version,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    def getcontentsubmission(
        self,
        content_submission_id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentSubmissionSharedBusinessEntitiesContentSubmission]:
        """
        Gets a ContentSubmission by ID. When successful, the response is the requested ContentSubmission.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to get.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentSubmissionSharedBusinessEntitiesContentSubmission]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id)}",
            method="GET",
            params={
                "includeAttributes": include_attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesContentSubmission,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesContentSubmission,
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

    def putcontentsubmission(
        self,
        content_submission_id_: int,
        *,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]
        ] = OMIT,
        build_id: typing.Optional[int] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        content_submission_id: typing.Optional[int] = OMIT,
        definition: typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        release_notes: typing.Optional[str] = OMIT,
        repository: typing.Optional[str] = OMIT,
        revision: typing.Optional[int] = OMIT,
        submission_date: typing.Optional[dt.datetime] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates a ContentSubmission.  The body of the PUT is the updated ContentSubmission.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_submission_id_ : int
            The ID of the ContentSubmission to update

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]]
            Attributes of this ContentSubmission

        build_id : typing.Optional[int]
            ReadOnly. The ID of the Azure DevOps Build which will build the content package.

        content_definition_id : typing.Optional[int]
            The ID of the Content Definition.

        content_submission_id : typing.Optional[int]
            The ID of this Content Submission.

        definition : typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition]
            The ContentDefinition for this ContentSubmission

        job_run_id : typing.Optional[int]
            ReadOnly. The ID of the JobRun which will build the content package.

        package_id : typing.Optional[str]
            The ID of package generated by this content submission.

        release_notes : typing.Optional[str]
            Release Notes for this ContentSubmission

        repository : typing.Optional[str]
            The SVN repository used as the source of this content submission

        revision : typing.Optional[int]
            The SVN revision used as the source of this content submission.

        submission_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time the content submission was made.

        user_id : typing.Optional[int]
            Read Only. The ID of the user who submitted the content

        version : typing.Optional[int]
            Optional.  The version number assigned to this Content Submission and the resulting Package.
                        If not provided, version shall be 1 if it is the first content submission for the
                        ContentDefinitionID otherwise it shall be the highest content submission version for the
                        specified ContentDefinitionID incremented by 1.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id_)}",
            method="PUT",
            json={
                "Attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
                    direction="write",
                ),
                "BuildID": build_id,
                "ContentDefinitionID": content_definition_id,
                "ContentSubmissionID": content_submission_id,
                "Definition": convert_and_respect_annotation_metadata(
                    object_=definition,
                    annotation=ContentSubmissionSharedBusinessEntitiesContentDefinition,
                    direction="write",
                ),
                "JobRunID": job_run_id,
                "PackageID": package_id,
                "ReleaseNotes": release_notes,
                "Repository": repository,
                "Revision": revision,
                "SubmissionDate": submission_date,
                "UserID": user_id,
                "Version": version,
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

    def deletecontentsubmission(
        self, content_submission_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes an ContentSubmission. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id)}",
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

    def getcontentsubmissionattributes(
        self,
        content_submission_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission.

        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        name : typing.Optional[str]
            Optional. Filter the attributes by Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id)}/Attributes",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
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

    def postcontentsubmissionattribute(
        self,
        content_submission_id_: int,
        *,
        name: str,
        content_submission_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id_ : int
            The ID of the ContentSubmission

        name : str
            The name of this Attribute.

        content_submission_id : typing.Optional[int]
            The ID of the content submission to which this attribute belongs.

        id : typing.Optional[int]
            The ID of this attribute.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id_)}/Attributes",
            method="POST",
            json={
                "ContentSubmissionID": content_submission_id,
                "ID": id,
                "Name": name,
                "Value": value,
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
                    int,
                    parse_obj_as(
                        type_=int,
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

    def postcontentsubmissionattributes(
        self,
        content_submission_id: int,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int

        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id)}/Attributes/Batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
                direction="write",
            ),
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

    def getcontentsubmissionstatus(
        self,
        content_submission_id: int,
        *,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BuildSystemSharedInterfacesIJobRun]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to get.

        include_activity_run_details : typing.Optional[bool]
            True to include all status details if JobRun. Defaults to false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BuildSystemSharedInterfacesIJobRun]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id)}/Status",
            method="GET",
            params={
                "includeActivityRunDetails": include_activity_run_details,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedInterfacesIJobRun,
                    parse_obj_as(
                        type_=BuildSystemSharedInterfacesIJobRun,
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


class AsyncRawContentsubmissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def putcontentsubmissionattributes(
        self,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/ContentSubmissionAttributes/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
                direction="write",
            ),
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

    async def putcontentsubmissionattributeasync(
        self,
        content_submission_attribute_id: int,
        *,
        name: str,
        content_submission_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_attribute_id : int
            The ID of the Attribute to update.

        name : str
            The name of this Attribute.

        content_submission_id : typing.Optional[int]
            The ID of the content submission to which this attribute belongs.

        id : typing.Optional[int]
            The ID of this attribute.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissionAttributes/{encode_path_param(content_submission_attribute_id)}",
            method="PUT",
            json={
                "ContentSubmissionID": content_submission_id,
                "ID": id,
                "Name": name,
                "Value": value,
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

    async def deletecontentsubmissionattribute(
        self, content_submission_attribute_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_attribute_id : int
            The ID of the Attribute to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissionAttributes/{encode_path_param(content_submission_attribute_id)}",
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

    async def getcontentsubmissions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        content_definition_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        release_id: typing.Optional[int] = None,
        type_id: typing.Optional[int] = None,
        version: typing.Optional[int] = None,
        include_definition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission]:
        """
        Gets a collection of ContentSubmissions. When successful, the response is a PagedResponse of ContentSubmissions. Additional searches: attributes[Name]=Value. This can be used to search for submissions that have the specified values for attributes. Beginning and ending wildcard (*) supported for value.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        content_definition_id : typing.Optional[int]
            Optional. Filter by ContentDefinitionID

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        release_id : typing.Optional[int]
            Optional. Filter the submissions by whether they are part of the Release with the specified Release ID.

        type_id : typing.Optional[int]
            Optional. Filter submissions by their ContentDefinition's Type ID.

        version : typing.Optional[int]
            Optional. Filter submissions by their Version.

        include_definition : typing.Optional[bool]
            Optional. If true, includes the ContentDefinition for each submission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/ContentSubmissions",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "userID": user_id,
                "contentDefinitionID": content_definition_id,
                "includeAttributes": include_attributes,
                "releaseID": release_id,
                "typeID": type_id,
                "version": version,
                "includeDefinition": include_definition,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission,
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

    async def postcontentsubmission(
        self,
        *,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]
        ] = OMIT,
        build_id: typing.Optional[int] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        content_submission_id: typing.Optional[int] = OMIT,
        definition: typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        release_notes: typing.Optional[str] = OMIT,
        repository: typing.Optional[str] = OMIT,
        revision: typing.Optional[int] = OMIT,
        submission_date: typing.Optional[dt.datetime] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Creates a ContentSubmission.  The body of the POST is the ContentSubmission to create.
                    The ContentSubmissionID will be assigned on creation of the Job.  When successful, the response
                    is the ContentSubmissionID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]]
            Attributes of this ContentSubmission

        build_id : typing.Optional[int]
            ReadOnly. The ID of the Azure DevOps Build which will build the content package.

        content_definition_id : typing.Optional[int]
            The ID of the Content Definition.

        content_submission_id : typing.Optional[int]
            The ID of this Content Submission.

        definition : typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition]
            The ContentDefinition for this ContentSubmission

        job_run_id : typing.Optional[int]
            ReadOnly. The ID of the JobRun which will build the content package.

        package_id : typing.Optional[str]
            The ID of package generated by this content submission.

        release_notes : typing.Optional[str]
            Release Notes for this ContentSubmission

        repository : typing.Optional[str]
            The SVN repository used as the source of this content submission

        revision : typing.Optional[int]
            The SVN revision used as the source of this content submission.

        submission_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time the content submission was made.

        user_id : typing.Optional[int]
            Read Only. The ID of the user who submitted the content

        version : typing.Optional[int]
            Optional.  The version number assigned to this Content Submission and the resulting Package.
                        If not provided, version shall be 1 if it is the first content submission for the
                        ContentDefinitionID otherwise it shall be the highest content submission version for the
                        specified ContentDefinitionID incremented by 1.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/ContentSubmissions",
            method="POST",
            json={
                "Attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
                    direction="write",
                ),
                "BuildID": build_id,
                "ContentDefinitionID": content_definition_id,
                "ContentSubmissionID": content_submission_id,
                "Definition": convert_and_respect_annotation_metadata(
                    object_=definition,
                    annotation=ContentSubmissionSharedBusinessEntitiesContentDefinition,
                    direction="write",
                ),
                "JobRunID": job_run_id,
                "PackageID": package_id,
                "ReleaseNotes": release_notes,
                "Repository": repository,
                "Revision": revision,
                "SubmissionDate": submission_date,
                "UserID": user_id,
                "Version": version,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    async def getcontentsubmission(
        self,
        content_submission_id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesContentSubmission]:
        """
        Gets a ContentSubmission by ID. When successful, the response is the requested ContentSubmission.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to get.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesContentSubmission]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id)}",
            method="GET",
            params={
                "includeAttributes": include_attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesContentSubmission,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesContentSubmission,
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

    async def putcontentsubmission(
        self,
        content_submission_id_: int,
        *,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]
        ] = OMIT,
        build_id: typing.Optional[int] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        content_submission_id: typing.Optional[int] = OMIT,
        definition: typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        release_notes: typing.Optional[str] = OMIT,
        repository: typing.Optional[str] = OMIT,
        revision: typing.Optional[int] = OMIT,
        submission_date: typing.Optional[dt.datetime] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates a ContentSubmission.  The body of the PUT is the updated ContentSubmission.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_submission_id_ : int
            The ID of the ContentSubmission to update

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]]
            Attributes of this ContentSubmission

        build_id : typing.Optional[int]
            ReadOnly. The ID of the Azure DevOps Build which will build the content package.

        content_definition_id : typing.Optional[int]
            The ID of the Content Definition.

        content_submission_id : typing.Optional[int]
            The ID of this Content Submission.

        definition : typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition]
            The ContentDefinition for this ContentSubmission

        job_run_id : typing.Optional[int]
            ReadOnly. The ID of the JobRun which will build the content package.

        package_id : typing.Optional[str]
            The ID of package generated by this content submission.

        release_notes : typing.Optional[str]
            Release Notes for this ContentSubmission

        repository : typing.Optional[str]
            The SVN repository used as the source of this content submission

        revision : typing.Optional[int]
            The SVN revision used as the source of this content submission.

        submission_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time the content submission was made.

        user_id : typing.Optional[int]
            Read Only. The ID of the user who submitted the content

        version : typing.Optional[int]
            Optional.  The version number assigned to this Content Submission and the resulting Package.
                        If not provided, version shall be 1 if it is the first content submission for the
                        ContentDefinitionID otherwise it shall be the highest content submission version for the
                        specified ContentDefinitionID incremented by 1.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id_)}",
            method="PUT",
            json={
                "Attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
                    direction="write",
                ),
                "BuildID": build_id,
                "ContentDefinitionID": content_definition_id,
                "ContentSubmissionID": content_submission_id,
                "Definition": convert_and_respect_annotation_metadata(
                    object_=definition,
                    annotation=ContentSubmissionSharedBusinessEntitiesContentDefinition,
                    direction="write",
                ),
                "JobRunID": job_run_id,
                "PackageID": package_id,
                "ReleaseNotes": release_notes,
                "Repository": repository,
                "Revision": revision,
                "SubmissionDate": submission_date,
                "UserID": user_id,
                "Version": version,
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

    async def deletecontentsubmission(
        self, content_submission_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes an ContentSubmission. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id)}",
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

    async def getcontentsubmissionattributes(
        self,
        content_submission_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission.

        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        name : typing.Optional[str]
            Optional. Filter the attributes by Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id)}/Attributes",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
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

    async def postcontentsubmissionattribute(
        self,
        content_submission_id_: int,
        *,
        name: str,
        content_submission_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id_ : int
            The ID of the ContentSubmission

        name : str
            The name of this Attribute.

        content_submission_id : typing.Optional[int]
            The ID of the content submission to which this attribute belongs.

        id : typing.Optional[int]
            The ID of this attribute.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id_)}/Attributes",
            method="POST",
            json={
                "ContentSubmissionID": content_submission_id,
                "ID": id,
                "Name": name,
                "Value": value,
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
                    int,
                    parse_obj_as(
                        type_=int,
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

    async def postcontentsubmissionattributes(
        self,
        content_submission_id: int,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int

        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id)}/Attributes/Batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
                direction="write",
            ),
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

    async def getcontentsubmissionstatus(
        self,
        content_submission_id: int,
        *,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BuildSystemSharedInterfacesIJobRun]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to get.

        include_activity_run_details : typing.Optional[bool]
            True to include all status details if JobRun. Defaults to false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BuildSystemSharedInterfacesIJobRun]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissions/{encode_path_param(content_submission_id)}/Status",
            method="GET",
            params={
                "includeActivityRunDetails": include_activity_run_details,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedInterfacesIJobRun,
                    parse_obj_as(
                        type_=BuildSystemSharedInterfacesIJobRun,
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
