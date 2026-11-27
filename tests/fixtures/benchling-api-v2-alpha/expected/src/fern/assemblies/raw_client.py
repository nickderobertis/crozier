

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
from ..types.assembly import Assembly
from ..types.assembly_spec_finalized_output_location import AssemblySpecFinalizedOutputLocation
from ..types.assembly_spec_shared_assembly_parameters import AssemblySpecSharedAssemblyParameters
from ..types.assembly_spec_shared_bins_item import AssemblySpecSharedBinsItem
from ..types.assembly_spec_shared_constructs_item import AssemblySpecSharedConstructsItem
from ..types.assembly_spec_shared_fragments_item import AssemblySpecSharedFragmentsItem
from ..types.assembly_spec_shared_topology import AssemblySpecSharedTopology
from ..types.async_task_link import AsyncTaskLink
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAssembliesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_assembly(
        self, bulk_assembly_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Assembly]:
        """
        Get a bulk assembly by its API identifier.

        Parameters
        ----------
        bulk_assembly_id : str
            API identifier of bulk assembly

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Assembly]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assemblies/{encode_path_param(bulk_assembly_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Assembly,
                    parse_obj_as(
                        type_=Assembly,
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

    def create_and_finalize_assembly(
        self,
        *,
        assembly_parameters: AssemblySpecSharedAssemblyParameters,
        bins: typing.Sequence[AssemblySpecSharedBinsItem],
        constructs: typing.Sequence[AssemblySpecSharedConstructsItem],
        fragments: typing.Sequence[AssemblySpecSharedFragmentsItem],
        topology: AssemblySpecSharedTopology,
        folder_id: str,
        name: str,
        output_location: AssemblySpecFinalizedOutputLocation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncTaskLink]:
        """
        Create and finalize a new bulk assembly in a single step.

        Parameters
        ----------
        assembly_parameters : AssemblySpecSharedAssemblyParameters
            Assembly-wide parameters to describe requirements and procedures for the assembly.

        bins : typing.Sequence[AssemblySpecSharedBinsItem]
            Bins are used to group fragments according to their position in the output construct or add a spacer (i.e. constant) region.

        constructs : typing.Sequence[AssemblySpecSharedConstructsItem]
            Output constructs that should be created.

        fragments : typing.Sequence[AssemblySpecSharedFragmentsItem]
            Fragments to be used in the assembly.

        topology : AssemblySpecSharedTopology
            Whether the created constructs should be circular or linear.

        folder_id : str
            API identifier of the folder in which the assembly should be created.

        name : str
            Name of the bulk assembly.

        output_location : AssemblySpecFinalizedOutputLocation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AsyncTaskLink]
            This endpoint launches a [long-running task](#/Tasks/getTask) and returns the Task ID of the launched task.
            The task response contains a [finalized bulk assembly](#components/schemas/Assembly).
        """
        _response = self._client_wrapper.httpx_client.request(
            "assemblies:create-and-finalize",
            method="POST",
            json={
                "assemblyParameters": convert_and_respect_annotation_metadata(
                    object_=assembly_parameters, annotation=AssemblySpecSharedAssemblyParameters, direction="write"
                ),
                "bins": convert_and_respect_annotation_metadata(
                    object_=bins, annotation=typing.Sequence[AssemblySpecSharedBinsItem], direction="write"
                ),
                "constructs": convert_and_respect_annotation_metadata(
                    object_=constructs, annotation=typing.Sequence[AssemblySpecSharedConstructsItem], direction="write"
                ),
                "fragments": convert_and_respect_annotation_metadata(
                    object_=fragments, annotation=typing.Sequence[AssemblySpecSharedFragmentsItem], direction="write"
                ),
                "topology": topology,
                "folderId": folder_id,
                "name": name,
                "outputLocation": convert_and_respect_annotation_metadata(
                    object_=output_location, annotation=AssemblySpecFinalizedOutputLocation, direction="write"
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
                    AsyncTaskLink,
                    parse_obj_as(
                        type_=AsyncTaskLink,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def validate_assembly(
        self,
        *,
        assembly_parameters: AssemblySpecSharedAssemblyParameters,
        bins: typing.Sequence[AssemblySpecSharedBinsItem],
        constructs: typing.Sequence[AssemblySpecSharedConstructsItem],
        fragments: typing.Sequence[AssemblySpecSharedFragmentsItem],
        topology: AssemblySpecSharedTopology,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncTaskLink]:
        """
        Validate an assembly prior to finalization to see if it will succeed.

        Parameters
        ----------
        assembly_parameters : AssemblySpecSharedAssemblyParameters
            Assembly-wide parameters to describe requirements and procedures for the assembly.

        bins : typing.Sequence[AssemblySpecSharedBinsItem]
            Bins are used to group fragments according to their position in the output construct or add a spacer (i.e. constant) region.

        constructs : typing.Sequence[AssemblySpecSharedConstructsItem]
            Output constructs that should be created.

        fragments : typing.Sequence[AssemblySpecSharedFragmentsItem]
            Fragments to be used in the assembly.

        topology : AssemblySpecSharedTopology
            Whether the created constructs should be circular or linear.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AsyncTaskLink]
            This endpoint launched a [long-running task](#/Tasks/getTask) and returns the Task ID of the launched task.
            The task response contains a set of [validation results](#components/schemas/AssemblyValidationResult).
        """
        _response = self._client_wrapper.httpx_client.request(
            "assemblies:validate",
            method="POST",
            json={
                "assemblyParameters": convert_and_respect_annotation_metadata(
                    object_=assembly_parameters, annotation=AssemblySpecSharedAssemblyParameters, direction="write"
                ),
                "bins": convert_and_respect_annotation_metadata(
                    object_=bins, annotation=typing.Sequence[AssemblySpecSharedBinsItem], direction="write"
                ),
                "constructs": convert_and_respect_annotation_metadata(
                    object_=constructs, annotation=typing.Sequence[AssemblySpecSharedConstructsItem], direction="write"
                ),
                "fragments": convert_and_respect_annotation_metadata(
                    object_=fragments, annotation=typing.Sequence[AssemblySpecSharedFragmentsItem], direction="write"
                ),
                "topology": topology,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsyncTaskLink,
                    parse_obj_as(
                        type_=AsyncTaskLink,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAssembliesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_assembly(
        self, bulk_assembly_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Assembly]:
        """
        Get a bulk assembly by its API identifier.

        Parameters
        ----------
        bulk_assembly_id : str
            API identifier of bulk assembly

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Assembly]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assemblies/{encode_path_param(bulk_assembly_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Assembly,
                    parse_obj_as(
                        type_=Assembly,
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

    async def create_and_finalize_assembly(
        self,
        *,
        assembly_parameters: AssemblySpecSharedAssemblyParameters,
        bins: typing.Sequence[AssemblySpecSharedBinsItem],
        constructs: typing.Sequence[AssemblySpecSharedConstructsItem],
        fragments: typing.Sequence[AssemblySpecSharedFragmentsItem],
        topology: AssemblySpecSharedTopology,
        folder_id: str,
        name: str,
        output_location: AssemblySpecFinalizedOutputLocation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AsyncTaskLink]:
        """
        Create and finalize a new bulk assembly in a single step.

        Parameters
        ----------
        assembly_parameters : AssemblySpecSharedAssemblyParameters
            Assembly-wide parameters to describe requirements and procedures for the assembly.

        bins : typing.Sequence[AssemblySpecSharedBinsItem]
            Bins are used to group fragments according to their position in the output construct or add a spacer (i.e. constant) region.

        constructs : typing.Sequence[AssemblySpecSharedConstructsItem]
            Output constructs that should be created.

        fragments : typing.Sequence[AssemblySpecSharedFragmentsItem]
            Fragments to be used in the assembly.

        topology : AssemblySpecSharedTopology
            Whether the created constructs should be circular or linear.

        folder_id : str
            API identifier of the folder in which the assembly should be created.

        name : str
            Name of the bulk assembly.

        output_location : AssemblySpecFinalizedOutputLocation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AsyncTaskLink]
            This endpoint launches a [long-running task](#/Tasks/getTask) and returns the Task ID of the launched task.
            The task response contains a [finalized bulk assembly](#components/schemas/Assembly).
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assemblies:create-and-finalize",
            method="POST",
            json={
                "assemblyParameters": convert_and_respect_annotation_metadata(
                    object_=assembly_parameters, annotation=AssemblySpecSharedAssemblyParameters, direction="write"
                ),
                "bins": convert_and_respect_annotation_metadata(
                    object_=bins, annotation=typing.Sequence[AssemblySpecSharedBinsItem], direction="write"
                ),
                "constructs": convert_and_respect_annotation_metadata(
                    object_=constructs, annotation=typing.Sequence[AssemblySpecSharedConstructsItem], direction="write"
                ),
                "fragments": convert_and_respect_annotation_metadata(
                    object_=fragments, annotation=typing.Sequence[AssemblySpecSharedFragmentsItem], direction="write"
                ),
                "topology": topology,
                "folderId": folder_id,
                "name": name,
                "outputLocation": convert_and_respect_annotation_metadata(
                    object_=output_location, annotation=AssemblySpecFinalizedOutputLocation, direction="write"
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
                    AsyncTaskLink,
                    parse_obj_as(
                        type_=AsyncTaskLink,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def validate_assembly(
        self,
        *,
        assembly_parameters: AssemblySpecSharedAssemblyParameters,
        bins: typing.Sequence[AssemblySpecSharedBinsItem],
        constructs: typing.Sequence[AssemblySpecSharedConstructsItem],
        fragments: typing.Sequence[AssemblySpecSharedFragmentsItem],
        topology: AssemblySpecSharedTopology,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AsyncTaskLink]:
        """
        Validate an assembly prior to finalization to see if it will succeed.

        Parameters
        ----------
        assembly_parameters : AssemblySpecSharedAssemblyParameters
            Assembly-wide parameters to describe requirements and procedures for the assembly.

        bins : typing.Sequence[AssemblySpecSharedBinsItem]
            Bins are used to group fragments according to their position in the output construct or add a spacer (i.e. constant) region.

        constructs : typing.Sequence[AssemblySpecSharedConstructsItem]
            Output constructs that should be created.

        fragments : typing.Sequence[AssemblySpecSharedFragmentsItem]
            Fragments to be used in the assembly.

        topology : AssemblySpecSharedTopology
            Whether the created constructs should be circular or linear.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AsyncTaskLink]
            This endpoint launched a [long-running task](#/Tasks/getTask) and returns the Task ID of the launched task.
            The task response contains a set of [validation results](#components/schemas/AssemblyValidationResult).
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assemblies:validate",
            method="POST",
            json={
                "assemblyParameters": convert_and_respect_annotation_metadata(
                    object_=assembly_parameters, annotation=AssemblySpecSharedAssemblyParameters, direction="write"
                ),
                "bins": convert_and_respect_annotation_metadata(
                    object_=bins, annotation=typing.Sequence[AssemblySpecSharedBinsItem], direction="write"
                ),
                "constructs": convert_and_respect_annotation_metadata(
                    object_=constructs, annotation=typing.Sequence[AssemblySpecSharedConstructsItem], direction="write"
                ),
                "fragments": convert_and_respect_annotation_metadata(
                    object_=fragments, annotation=typing.Sequence[AssemblySpecSharedFragmentsItem], direction="write"
                ),
                "topology": topology,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsyncTaskLink,
                    parse_obj_as(
                        type_=AsyncTaskLink,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
