

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.content_submission_shared_business_entities_content_submission_type import (
    ContentSubmissionSharedBusinessEntitiesContentSubmissionType,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContentsubmissiontypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getcontentsubmissiontypes(
        self, *, enabled: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]]:
        """
        No Documentation Found.

        Parameters
        ----------
        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/ContentSubmissionTypes",
            method="GET",
            params={
                "enabled": enabled,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType],
                    parse_obj_as(
                        type_=typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType],
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

    def postcontentsubmissiontype(
        self,
        *,
        description: str,
        name: str,
        attribute_template: typing.Optional[str] = OMIT,
        build_definition_id: typing.Optional[int] = OMIT,
        category_template: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        inventory_package_id: typing.Optional[str] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        release_notes_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            A description for the Content Submission Type

        name : str
            The Name of the Content Submission Type

        attribute_template : typing.Optional[str]
            A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        build_definition_id : typing.Optional[int]
            The ID of the Azure DevOps Build Definition for which to create a Build. Either 'BuildDefinitionID' or 'JobID' is required.

        category_template : typing.Optional[str]
            A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        enabled : typing.Optional[bool]
            Indicates whether this submission type is available to be used

        id : typing.Optional[int]
            The ID of the Content Submission Type

        inventory_package_id : typing.Optional[str]
            The ID of the Inventory Package from which to read the version of the package installed.

        job_id : typing.Optional[int]
            The ID of the JobDefinition for which to initiate a Job. A value of '0' will cause a submission to fail. Either 'BuildDefinitionID' or 'JobID' is required.

        release_notes_description : typing.Optional[str]
            A description of how release notes for this Content Submission Type are used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/ContentSubmissionTypes",
            method="POST",
            json={
                "AttributeTemplate": attribute_template,
                "BuildDefinitionID": build_definition_id,
                "CategoryTemplate": category_template,
                "Description": description,
                "Enabled": enabled,
                "ID": id,
                "InventoryPackageID": inventory_package_id,
                "JobID": job_id,
                "Name": name,
                "ReleaseNotesDescription": release_notes_description,
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

    def getcontentsubmissiontype(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The ID of the Content Submission Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissionTypes/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesContentSubmissionType,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesContentSubmissionType,
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

    def putcontentsubmissiontype(
        self,
        id_: int,
        *,
        description: str,
        name: str,
        attribute_template: typing.Optional[str] = OMIT,
        build_definition_id: typing.Optional[int] = OMIT,
        category_template: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        inventory_package_id: typing.Optional[str] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        release_notes_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            The ID of the Content Submission Type

        description : str
            A description for the Content Submission Type

        name : str
            The Name of the Content Submission Type

        attribute_template : typing.Optional[str]
            A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        build_definition_id : typing.Optional[int]
            The ID of the Azure DevOps Build Definition for which to create a Build. Either 'BuildDefinitionID' or 'JobID' is required.

        category_template : typing.Optional[str]
            A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        enabled : typing.Optional[bool]
            Indicates whether this submission type is available to be used

        id : typing.Optional[int]
            The ID of the Content Submission Type

        inventory_package_id : typing.Optional[str]
            The ID of the Inventory Package from which to read the version of the package installed.

        job_id : typing.Optional[int]
            The ID of the JobDefinition for which to initiate a Job. A value of '0' will cause a submission to fail. Either 'BuildDefinitionID' or 'JobID' is required.

        release_notes_description : typing.Optional[str]
            A description of how release notes for this Content Submission Type are used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissionTypes/{encode_path_param(id_)}",
            method="PUT",
            json={
                "AttributeTemplate": attribute_template,
                "BuildDefinitionID": build_definition_id,
                "CategoryTemplate": category_template,
                "Description": description,
                "Enabled": enabled,
                "ID": id,
                "InventoryPackageID": inventory_package_id,
                "JobID": job_id,
                "Name": name,
                "ReleaseNotesDescription": release_notes_description,
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

    def deletecontentsubmissiontype(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The ID of the Content Submission Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissionTypes/{encode_path_param(id)}",
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


class AsyncRawContentsubmissiontypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getcontentsubmissiontypes(
        self, *, enabled: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]]:
        """
        No Documentation Found.

        Parameters
        ----------
        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/ContentSubmissionTypes",
            method="GET",
            params={
                "enabled": enabled,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType],
                    parse_obj_as(
                        type_=typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType],
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

    async def postcontentsubmissiontype(
        self,
        *,
        description: str,
        name: str,
        attribute_template: typing.Optional[str] = OMIT,
        build_definition_id: typing.Optional[int] = OMIT,
        category_template: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        inventory_package_id: typing.Optional[str] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        release_notes_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            A description for the Content Submission Type

        name : str
            The Name of the Content Submission Type

        attribute_template : typing.Optional[str]
            A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        build_definition_id : typing.Optional[int]
            The ID of the Azure DevOps Build Definition for which to create a Build. Either 'BuildDefinitionID' or 'JobID' is required.

        category_template : typing.Optional[str]
            A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        enabled : typing.Optional[bool]
            Indicates whether this submission type is available to be used

        id : typing.Optional[int]
            The ID of the Content Submission Type

        inventory_package_id : typing.Optional[str]
            The ID of the Inventory Package from which to read the version of the package installed.

        job_id : typing.Optional[int]
            The ID of the JobDefinition for which to initiate a Job. A value of '0' will cause a submission to fail. Either 'BuildDefinitionID' or 'JobID' is required.

        release_notes_description : typing.Optional[str]
            A description of how release notes for this Content Submission Type are used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/ContentSubmissionTypes",
            method="POST",
            json={
                "AttributeTemplate": attribute_template,
                "BuildDefinitionID": build_definition_id,
                "CategoryTemplate": category_template,
                "Description": description,
                "Enabled": enabled,
                "ID": id,
                "InventoryPackageID": inventory_package_id,
                "JobID": job_id,
                "Name": name,
                "ReleaseNotesDescription": release_notes_description,
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

    async def getcontentsubmissiontype(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The ID of the Content Submission Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissionTypes/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesContentSubmissionType,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesContentSubmissionType,
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

    async def putcontentsubmissiontype(
        self,
        id_: int,
        *,
        description: str,
        name: str,
        attribute_template: typing.Optional[str] = OMIT,
        build_definition_id: typing.Optional[int] = OMIT,
        category_template: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        inventory_package_id: typing.Optional[str] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        release_notes_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            The ID of the Content Submission Type

        description : str
            A description for the Content Submission Type

        name : str
            The Name of the Content Submission Type

        attribute_template : typing.Optional[str]
            A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        build_definition_id : typing.Optional[int]
            The ID of the Azure DevOps Build Definition for which to create a Build. Either 'BuildDefinitionID' or 'JobID' is required.

        category_template : typing.Optional[str]
            A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        enabled : typing.Optional[bool]
            Indicates whether this submission type is available to be used

        id : typing.Optional[int]
            The ID of the Content Submission Type

        inventory_package_id : typing.Optional[str]
            The ID of the Inventory Package from which to read the version of the package installed.

        job_id : typing.Optional[int]
            The ID of the JobDefinition for which to initiate a Job. A value of '0' will cause a submission to fail. Either 'BuildDefinitionID' or 'JobID' is required.

        release_notes_description : typing.Optional[str]
            A description of how release notes for this Content Submission Type are used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissionTypes/{encode_path_param(id_)}",
            method="PUT",
            json={
                "AttributeTemplate": attribute_template,
                "BuildDefinitionID": build_definition_id,
                "CategoryTemplate": category_template,
                "Description": description,
                "Enabled": enabled,
                "ID": id,
                "InventoryPackageID": inventory_package_id,
                "JobID": job_id,
                "Name": name,
                "ReleaseNotesDescription": release_notes_description,
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

    async def deletecontentsubmissiontype(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The ID of the Content Submission Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentSubmissionTypes/{encode_path_param(id)}",
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
