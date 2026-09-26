

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.action_help_response import ActionHelpResponse
from ..types.describe_action_response import DescribeActionResponse
from ..types.describe_service_response import DescribeServiceResponse
from ..types.error_model import ErrorModel
from ..types.list_actions_response import ListActionsResponse
from ..types.list_services_response import ListServicesResponse
from ..types.login_response import LoginResponse
from ..types.logout_response import LogoutResponse
from .types.exec_body_osdb_output_type import ExecBodyOsdbOutputType
from .types.load_service_response import LoadServiceResponse
from .types.unload_service_response import UnloadServiceResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOsdbClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_actions(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListActionsResponse]:
        """
        Returns an array of action descriptions for the actions supported by the given service

        Parameters
        ----------
        service_id : str
            Service ID of the service for which actions are to be listed

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListActionsResponse]
            An array of action descriptions for the actions supported by the given service.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/actions/{encode_path_param(service_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListActionsResponse,
                    parse_obj_as(
                        type_=ListActionsResponse,
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

    def describe_action(
        self, service_id: str, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DescribeActionResponse]:
        """
        Returns a description of a given service action.

        Parameters
        ----------
        service_id : str
            Service ID of the service supporting the action.

        action_id : str
            Action ID of the action to describe.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DescribeActionResponse]
            A single action description
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/actions/{encode_path_param(service_id)}/{encode_path_param(action_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DescribeActionResponse,
                    parse_obj_as(
                        type_=DescribeActionResponse,
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

    def execute_action(
        self,
        service_id: str,
        action_id: str,
        *,
        action_specific_property1: typing.Optional[str] = OMIT,
        action_specific_property2: typing.Optional[str] = OMIT,
        osdb_body_data_encoding: typing.Optional[str] = OMIT,
        osdb_body_data_raw: typing.Optional[str] = OMIT,
        osdb_body_data_src_url: typing.Optional[str] = OMIT,
        osdb_output_type: typing.Optional[ExecBodyOsdbOutputType] = OMIT,
        osdb_response_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ErrorModel]:
        """
        Executes a registered service action and returns any output from the action.
        The data returned in the POST response body may be:
        * the raw action output,
        * a URL encapsulating the action request which executes the action when dereferenced  (only for actions using GET),
        * RDF generated from the action output,
        * a URL to an RDF viewer's display of the generated RDF.

        Any parameters required by the action are supplied as a JSON object in the POST body. The parameter types supported are: "query", "header", "uri", "path" and "body".  The parameter type determines where a supplied parameter value is inserted into the HTTP request constructed by OSDB to invoke the target service action. In addition to native parameters required by the service action, 'Execute action' accepts some OSDB-specific parameters.<br/><br/>

        **Examples**
        * ```curl -ik -X POST -d '{ "latitude":"37.7759792", "longitude":"-122.41823" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec```
        * ```curl -ikL -X POST -d '{ "latitude":"37.7759792", "longitude":"-122.41823", "osdb:output_type":"generate_rdf", "osdb:response_format":"application/rdf+xml" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec```
        * ```curl -ikL -X POST -d '{ "latitude":"37.7759792", "longitude":"-122.41823", "osdb:output_type":"display_rdf" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec```
        * ```curl -ik -X POST -d '{ "q":"skiing", "osdb:response_format": "application/rdf+xml" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/facet/search/exec```
        * ```curl -ik -X POST -d '{ "q":"skiing", "osdb:output_type": "url_only" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/facet/search/exec```
        * ```curl -ik -X POST -d '{ "Content-Location": "http://demo.openlinksw.co.uk/pubs", "osdb:body_data_src_url": "http://ods-qa.openlinksw.com/DAV/home/osdb/pubs.csv", "extractor": "csv", "osdb:response_format": "application/rdf+xml", "osdb:body_data_encoding": "text/csv" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/csv_transformer/transform/exec```

        Parameters
        ----------
        service_id : str
            Service ID of the service supporting the action.

        action_id : str
            Action ID of the action to execute.

        action_specific_property1 : typing.Optional[str]
            An example action specific property. There may be 0, 1 or more action specific properties, each holding an action specific parameter value.

        action_specific_property2 : typing.Optional[str]
            An example action specific property. There may be 0, 1 or more action specific properties, each holding an action specific parameter value.

        osdb_body_data_encoding : typing.Optional[str]
            The media type of the data associated with osdb:body_data_raw or osdb:body_data_src_url. In the case of osdb:body_data_raw, this is the media type before base64 encoding.

        osdb_body_data_raw : typing.Optional[str]
            Input data for the action (e.g. CSV data). The data must be base64 encoded by the client. Alternatively, clients can use osdb:body_data_src_url to supply the input data via a web-accessible document.

        osdb_body_data_src_url : typing.Optional[str]
            URL of a resource containing input data for the action (e.g. CSV data). Clients can instead use osdb:body_data_raw to supply the input data directly.

        osdb_output_type : typing.Optional[ExecBodyOsdbOutputType]
            An OSDB-specific parameter controlling the action output type. If omitted, the native action output is returned.

        osdb_response_format : typing.Optional[str]
            Preferred response MIME type. This must be an output MIME type supported natively by the action or, if 'osdb:output_type' is set to 'generate_rdf', a Virtuoso Sponger output format. i.e. 'application/ld+json', 'text/turtle' or 'application/rdf+xml'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ErrorModel]
            Error response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/actions/{encode_path_param(service_id)}/{encode_path_param(action_id)}/exec",
            method="POST",
            json={
                "action_specific_property1": action_specific_property1,
                "action_specific_property2": action_specific_property2,
                "osdb:body_data_encoding": osdb_body_data_encoding,
                "osdb:body_data_raw": osdb_body_data_raw,
                "osdb:body_data_src_url": osdb_body_data_src_url,
                "osdb:output_type": osdb_output_type,
                "osdb:response_format": osdb_response_format,
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
                    ErrorModel,
                    parse_obj_as(
                        type_=ErrorModel,
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

    def action_help(
        self, service_id: str, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ActionHelpResponse]:
        """
        Returns the help text for a given service action

        Parameters
        ----------
        service_id : str
            Service ID of the service supporting the action.

        action_id : str
            Action ID of the action for which help text is being requested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ActionHelpResponse]
            Action help text
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/actions/{encode_path_param(service_id)}/{encode_path_param(action_id)}/help",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActionHelpResponse,
                    parse_obj_as(
                        type_=ActionHelpResponse,
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

    def login(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[LoginResponse]:
        """
        Logs a user into the OSDB server, authenticating them by their WebID and returning an OSDB session ID in cookie osdb.sid

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LoginResponse]
            Confirmation of a successful OSDB login.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/login",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LoginResponse,
                    parse_obj_as(
                        type_=LoginResponse,
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

    def logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[LogoutResponse]:
        """
        Logs a user out of the OSDB server, ending their OSDB session

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LogoutResponse]
            Confirmation of a successful OSDB logout.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/logout",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogoutResponse,
                    parse_obj_as(
                        type_=LogoutResponse,
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

    def list_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListServicesResponse]:
        """
        Returns descriptions of all services registered with the OSDB server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListServicesResponse]
            An array of service descriptions for all services registered with the OSDB server
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListServicesResponse,
                    parse_obj_as(
                        type_=ListServicesResponse,
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

    def load_service(
        self,
        *,
        service_description_url: str,
        service_moniker: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LoadServiceResponse]:
        """
        Loads a service description into the OSDB Service Registry

        Parameters
        ----------
        service_description_url : str
            The URL of the resource containing the service description to load.

        service_moniker : typing.Optional[str]
            Service ID to be used to uniquely identify the service. (Optional: Required for anonymous services or to override the service name in the service description.)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LoadServiceResponse]
            loadService response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/services",
            method="POST",
            json={
                "service_description_url": service_description_url,
                "service_moniker": service_moniker,
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
                    LoadServiceResponse,
                    parse_obj_as(
                        type_=LoadServiceResponse,
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

    def describe_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DescribeServiceResponse]:
        """
        Returns a description of a given service

        Parameters
        ----------
        service_id : str
            Service ID of the service to describe.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DescribeServiceResponse]
            A single service description
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/services/{encode_path_param(service_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DescribeServiceResponse,
                    parse_obj_as(
                        type_=DescribeServiceResponse,
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

    def unload_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UnloadServiceResponse]:
        """
        Removes a service description from the OSDB Service Registry

        Parameters
        ----------
        service_id : str
            Service ID of the service to be unloaded

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UnloadServiceResponse]
            unloadService response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/services/{encode_path_param(service_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnloadServiceResponse,
                    parse_obj_as(
                        type_=UnloadServiceResponse,
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


class AsyncRawOsdbClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_actions(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListActionsResponse]:
        """
        Returns an array of action descriptions for the actions supported by the given service

        Parameters
        ----------
        service_id : str
            Service ID of the service for which actions are to be listed

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListActionsResponse]
            An array of action descriptions for the actions supported by the given service.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/actions/{encode_path_param(service_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListActionsResponse,
                    parse_obj_as(
                        type_=ListActionsResponse,
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

    async def describe_action(
        self, service_id: str, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DescribeActionResponse]:
        """
        Returns a description of a given service action.

        Parameters
        ----------
        service_id : str
            Service ID of the service supporting the action.

        action_id : str
            Action ID of the action to describe.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DescribeActionResponse]
            A single action description
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/actions/{encode_path_param(service_id)}/{encode_path_param(action_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DescribeActionResponse,
                    parse_obj_as(
                        type_=DescribeActionResponse,
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

    async def execute_action(
        self,
        service_id: str,
        action_id: str,
        *,
        action_specific_property1: typing.Optional[str] = OMIT,
        action_specific_property2: typing.Optional[str] = OMIT,
        osdb_body_data_encoding: typing.Optional[str] = OMIT,
        osdb_body_data_raw: typing.Optional[str] = OMIT,
        osdb_body_data_src_url: typing.Optional[str] = OMIT,
        osdb_output_type: typing.Optional[ExecBodyOsdbOutputType] = OMIT,
        osdb_response_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ErrorModel]:
        """
        Executes a registered service action and returns any output from the action.
        The data returned in the POST response body may be:
        * the raw action output,
        * a URL encapsulating the action request which executes the action when dereferenced  (only for actions using GET),
        * RDF generated from the action output,
        * a URL to an RDF viewer's display of the generated RDF.

        Any parameters required by the action are supplied as a JSON object in the POST body. The parameter types supported are: "query", "header", "uri", "path" and "body".  The parameter type determines where a supplied parameter value is inserted into the HTTP request constructed by OSDB to invoke the target service action. In addition to native parameters required by the service action, 'Execute action' accepts some OSDB-specific parameters.<br/><br/>

        **Examples**
        * ```curl -ik -X POST -d '{ "latitude":"37.7759792", "longitude":"-122.41823" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec```
        * ```curl -ikL -X POST -d '{ "latitude":"37.7759792", "longitude":"-122.41823", "osdb:output_type":"generate_rdf", "osdb:response_format":"application/rdf+xml" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec```
        * ```curl -ikL -X POST -d '{ "latitude":"37.7759792", "longitude":"-122.41823", "osdb:output_type":"display_rdf" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec```
        * ```curl -ik -X POST -d '{ "q":"skiing", "osdb:response_format": "application/rdf+xml" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/facet/search/exec```
        * ```curl -ik -X POST -d '{ "q":"skiing", "osdb:output_type": "url_only" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/facet/search/exec```
        * ```curl -ik -X POST -d '{ "Content-Location": "http://demo.openlinksw.co.uk/pubs", "osdb:body_data_src_url": "http://ods-qa.openlinksw.com/DAV/home/osdb/pubs.csv", "extractor": "csv", "osdb:response_format": "application/rdf+xml", "osdb:body_data_encoding": "text/csv" }' -H 'Content-Type: application/json' https://osdb.openlinksw.com/osdb/api/v1/actions/csv_transformer/transform/exec```

        Parameters
        ----------
        service_id : str
            Service ID of the service supporting the action.

        action_id : str
            Action ID of the action to execute.

        action_specific_property1 : typing.Optional[str]
            An example action specific property. There may be 0, 1 or more action specific properties, each holding an action specific parameter value.

        action_specific_property2 : typing.Optional[str]
            An example action specific property. There may be 0, 1 or more action specific properties, each holding an action specific parameter value.

        osdb_body_data_encoding : typing.Optional[str]
            The media type of the data associated with osdb:body_data_raw or osdb:body_data_src_url. In the case of osdb:body_data_raw, this is the media type before base64 encoding.

        osdb_body_data_raw : typing.Optional[str]
            Input data for the action (e.g. CSV data). The data must be base64 encoded by the client. Alternatively, clients can use osdb:body_data_src_url to supply the input data via a web-accessible document.

        osdb_body_data_src_url : typing.Optional[str]
            URL of a resource containing input data for the action (e.g. CSV data). Clients can instead use osdb:body_data_raw to supply the input data directly.

        osdb_output_type : typing.Optional[ExecBodyOsdbOutputType]
            An OSDB-specific parameter controlling the action output type. If omitted, the native action output is returned.

        osdb_response_format : typing.Optional[str]
            Preferred response MIME type. This must be an output MIME type supported natively by the action or, if 'osdb:output_type' is set to 'generate_rdf', a Virtuoso Sponger output format. i.e. 'application/ld+json', 'text/turtle' or 'application/rdf+xml'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ErrorModel]
            Error response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/actions/{encode_path_param(service_id)}/{encode_path_param(action_id)}/exec",
            method="POST",
            json={
                "action_specific_property1": action_specific_property1,
                "action_specific_property2": action_specific_property2,
                "osdb:body_data_encoding": osdb_body_data_encoding,
                "osdb:body_data_raw": osdb_body_data_raw,
                "osdb:body_data_src_url": osdb_body_data_src_url,
                "osdb:output_type": osdb_output_type,
                "osdb:response_format": osdb_response_format,
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
                    ErrorModel,
                    parse_obj_as(
                        type_=ErrorModel,
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

    async def action_help(
        self, service_id: str, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ActionHelpResponse]:
        """
        Returns the help text for a given service action

        Parameters
        ----------
        service_id : str
            Service ID of the service supporting the action.

        action_id : str
            Action ID of the action for which help text is being requested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ActionHelpResponse]
            Action help text
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/actions/{encode_path_param(service_id)}/{encode_path_param(action_id)}/help",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActionHelpResponse,
                    parse_obj_as(
                        type_=ActionHelpResponse,
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

    async def login(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LoginResponse]:
        """
        Logs a user into the OSDB server, authenticating them by their WebID and returning an OSDB session ID in cookie osdb.sid

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LoginResponse]
            Confirmation of a successful OSDB login.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/login",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LoginResponse,
                    parse_obj_as(
                        type_=LoginResponse,
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

    async def logout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LogoutResponse]:
        """
        Logs a user out of the OSDB server, ending their OSDB session

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LogoutResponse]
            Confirmation of a successful OSDB logout.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/logout",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogoutResponse,
                    parse_obj_as(
                        type_=LogoutResponse,
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

    async def list_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListServicesResponse]:
        """
        Returns descriptions of all services registered with the OSDB server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListServicesResponse]
            An array of service descriptions for all services registered with the OSDB server
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListServicesResponse,
                    parse_obj_as(
                        type_=ListServicesResponse,
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

    async def load_service(
        self,
        *,
        service_description_url: str,
        service_moniker: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LoadServiceResponse]:
        """
        Loads a service description into the OSDB Service Registry

        Parameters
        ----------
        service_description_url : str
            The URL of the resource containing the service description to load.

        service_moniker : typing.Optional[str]
            Service ID to be used to uniquely identify the service. (Optional: Required for anonymous services or to override the service name in the service description.)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LoadServiceResponse]
            loadService response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/services",
            method="POST",
            json={
                "service_description_url": service_description_url,
                "service_moniker": service_moniker,
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
                    LoadServiceResponse,
                    parse_obj_as(
                        type_=LoadServiceResponse,
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

    async def describe_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DescribeServiceResponse]:
        """
        Returns a description of a given service

        Parameters
        ----------
        service_id : str
            Service ID of the service to describe.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DescribeServiceResponse]
            A single service description
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/services/{encode_path_param(service_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DescribeServiceResponse,
                    parse_obj_as(
                        type_=DescribeServiceResponse,
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

    async def unload_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UnloadServiceResponse]:
        """
        Removes a service description from the OSDB Service Registry

        Parameters
        ----------
        service_id : str
            Service ID of the service to be unloaded

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UnloadServiceResponse]
            unloadService response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/services/{encode_path_param(service_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnloadServiceResponse,
                    parse_obj_as(
                        type_=UnloadServiceResponse,
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
