

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
from ..types.api_paged_response_content_submission_shared_business_entities_content_definition import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition,
)
from ..types.api_paged_response_content_submission_shared_business_entities_content_definition_attribute import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
)
from ..types.content_submission_shared_business_entities_content_definition import (
    ContentSubmissionSharedBusinessEntitiesContentDefinition,
)
from ..types.content_submission_shared_business_entities_content_definition_attribute import (
    ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContentdefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def putcontentdefinitionattributes(
        self,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/ContentDefinitionAttributes/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
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

    def putcontentdefinitionattributeasync(
        self,
        content_definition_attribute_id: int,
        *,
        name: str,
        content_definition_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_attribute_id : int
            The ID of the Attribute to update.

        name : str
            The name of this Attribute.

        content_definition_id : typing.Optional[int]
            The ID of the content definition to which this attribute belongs.

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
            f"api/v2/ContentDefinitionAttributes/{encode_path_param(content_definition_attribute_id)}",
            method="PUT",
            json={
                "ContentDefinitionID": content_definition_id,
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

    def deletecontentdefinitionattribute(
        self, content_definition_attribute_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_attribute_id : int
            The ID of the Attribute to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitionAttributes/{encode_path_param(content_definition_attribute_id)}",
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

    def getcontentdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        type_id: typing.Optional[int] = None,
        package_type_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition]:
        """
        Gets a collection of ContentDefinitions. When successful, the response is a PagedResponse of ContentDefinitions.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        name : typing.Optional[str]
            Optional. Filter by Name. Supports beginning and ending wildcard (*).

        type_id : typing.Optional[int]
            Optional. Filter by TypeID.

        package_type_id : typing.Optional[str]
            Optional. Filter by PackageTypeID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/ContentDefinitions",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "userID": user_id,
                "includeAttributes": include_attributes,
                "name": name,
                "typeID": type_id,
                "packageTypeID": package_type_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition,
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

    def postcontentdefinition(
        self,
        *,
        description: str,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]
        ] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        type_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Creates a ContentDefinition.  The body of the POST is the ContentDefinition to create.
                    The ContentDefinitionID will be assigned on creation of the Job.  When successful, the response
                    is the JobID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        description : str
            The description used on the package type in the AGCO Update System

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]]
            Attributes of this ContentDefinition

        content_definition_id : typing.Optional[int]
            The ID of this content definition.

        name : typing.Optional[str]
            The name of this content. Name must be valid for Attribute on PackageType.

        package_type_id : typing.Optional[str]
            Read Only. The ID of the package type used for this content.

        type_id : typing.Optional[int]
            The type of content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/ContentDefinitions",
            method="POST",
            json={
                "Attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
                    direction="write",
                ),
                "ContentDefinitionID": content_definition_id,
                "Description": description,
                "Name": name,
                "PackageTypeID": package_type_id,
                "TypeID": type_id,
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

    def getcontentdefinition(
        self,
        content_definition_id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentSubmissionSharedBusinessEntitiesContentDefinition]:
        """
        Gets a ContentDefinition by ID. When successful, the response is the requested ContentDefinition.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition to get.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentSubmissionSharedBusinessEntitiesContentDefinition]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id)}",
            method="GET",
            params={
                "includeAttributes": include_attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesContentDefinition,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesContentDefinition,
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

    def putcontentdefinition(
        self,
        content_definition_id_: int,
        *,
        description: str,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]
        ] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        type_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates a ContentDefinition.  The body of the PUT is the updated ContentDefinition.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id_ : int
            The ID of the ContentDefinition to update

        description : str
            The description used on the package type in the AGCO Update System

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]]
            Attributes of this ContentDefinition

        content_definition_id : typing.Optional[int]
            The ID of this content definition.

        name : typing.Optional[str]
            The name of this content. Name must be valid for Attribute on PackageType.

        package_type_id : typing.Optional[str]
            Read Only. The ID of the package type used for this content.

        type_id : typing.Optional[int]
            The type of content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id_)}",
            method="PUT",
            json={
                "Attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
                    direction="write",
                ),
                "ContentDefinitionID": content_definition_id,
                "Description": description,
                "Name": name,
                "PackageTypeID": package_type_id,
                "TypeID": type_id,
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

    def deletecontentdefinition(
        self, content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes an ContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id)}",
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

    def getcontentdefinitionattributes(
        self,
        content_definition_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition.

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
        HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id)}/Attributes",
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
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
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

    def postcontentdefinitionattribute(
        self,
        content_definition_id_: int,
        *,
        name: str,
        content_definition_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id_ : int
            The ID of the ContentDefinition

        name : str
            The name of this Attribute.

        content_definition_id : typing.Optional[int]
            The ID of the content definition to which this attribute belongs.

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
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id_)}/Attributes",
            method="POST",
            json={
                "ContentDefinitionID": content_definition_id,
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

    def postcontentdefinitionattributes(
        self,
        content_definition_id: int,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id : int

        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id)}/Attributes/Batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
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


class AsyncRawContentdefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def putcontentdefinitionattributes(
        self,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/ContentDefinitionAttributes/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
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

    async def putcontentdefinitionattributeasync(
        self,
        content_definition_attribute_id: int,
        *,
        name: str,
        content_definition_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_attribute_id : int
            The ID of the Attribute to update.

        name : str
            The name of this Attribute.

        content_definition_id : typing.Optional[int]
            The ID of the content definition to which this attribute belongs.

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
            f"api/v2/ContentDefinitionAttributes/{encode_path_param(content_definition_attribute_id)}",
            method="PUT",
            json={
                "ContentDefinitionID": content_definition_id,
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

    async def deletecontentdefinitionattribute(
        self, content_definition_attribute_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_attribute_id : int
            The ID of the Attribute to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitionAttributes/{encode_path_param(content_definition_attribute_id)}",
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

    async def getcontentdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        type_id: typing.Optional[int] = None,
        package_type_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition]:
        """
        Gets a collection of ContentDefinitions. When successful, the response is a PagedResponse of ContentDefinitions.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        name : typing.Optional[str]
            Optional. Filter by Name. Supports beginning and ending wildcard (*).

        type_id : typing.Optional[int]
            Optional. Filter by TypeID.

        package_type_id : typing.Optional[str]
            Optional. Filter by PackageTypeID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/ContentDefinitions",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "userID": user_id,
                "includeAttributes": include_attributes,
                "name": name,
                "typeID": type_id,
                "packageTypeID": package_type_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition,
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

    async def postcontentdefinition(
        self,
        *,
        description: str,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]
        ] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        type_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Creates a ContentDefinition.  The body of the POST is the ContentDefinition to create.
                    The ContentDefinitionID will be assigned on creation of the Job.  When successful, the response
                    is the JobID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        description : str
            The description used on the package type in the AGCO Update System

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]]
            Attributes of this ContentDefinition

        content_definition_id : typing.Optional[int]
            The ID of this content definition.

        name : typing.Optional[str]
            The name of this content. Name must be valid for Attribute on PackageType.

        package_type_id : typing.Optional[str]
            Read Only. The ID of the package type used for this content.

        type_id : typing.Optional[int]
            The type of content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/ContentDefinitions",
            method="POST",
            json={
                "Attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
                    direction="write",
                ),
                "ContentDefinitionID": content_definition_id,
                "Description": description,
                "Name": name,
                "PackageTypeID": package_type_id,
                "TypeID": type_id,
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

    async def getcontentdefinition(
        self,
        content_definition_id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesContentDefinition]:
        """
        Gets a ContentDefinition by ID. When successful, the response is the requested ContentDefinition.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition to get.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesContentDefinition]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id)}",
            method="GET",
            params={
                "includeAttributes": include_attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesContentDefinition,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesContentDefinition,
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

    async def putcontentdefinition(
        self,
        content_definition_id_: int,
        *,
        description: str,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]
        ] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        type_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates a ContentDefinition.  The body of the PUT is the updated ContentDefinition.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id_ : int
            The ID of the ContentDefinition to update

        description : str
            The description used on the package type in the AGCO Update System

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]]
            Attributes of this ContentDefinition

        content_definition_id : typing.Optional[int]
            The ID of this content definition.

        name : typing.Optional[str]
            The name of this content. Name must be valid for Attribute on PackageType.

        package_type_id : typing.Optional[str]
            Read Only. The ID of the package type used for this content.

        type_id : typing.Optional[int]
            The type of content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id_)}",
            method="PUT",
            json={
                "Attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
                    direction="write",
                ),
                "ContentDefinitionID": content_definition_id,
                "Description": description,
                "Name": name,
                "PackageTypeID": package_type_id,
                "TypeID": type_id,
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

    async def deletecontentdefinition(
        self, content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes an ContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id)}",
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

    async def getcontentdefinitionattributes(
        self,
        content_definition_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition.

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
        AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id)}/Attributes",
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
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
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

    async def postcontentdefinitionattribute(
        self,
        content_definition_id_: int,
        *,
        name: str,
        content_definition_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id_ : int
            The ID of the ContentDefinition

        name : str
            The name of this Attribute.

        content_definition_id : typing.Optional[int]
            The ID of the content definition to which this attribute belongs.

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
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id_)}/Attributes",
            method="POST",
            json={
                "ContentDefinitionID": content_definition_id,
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

    async def postcontentdefinitionattributes(
        self,
        content_definition_id: int,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id : int

        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentDefinitions/{encode_path_param(content_definition_id)}/Attributes/Batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
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
