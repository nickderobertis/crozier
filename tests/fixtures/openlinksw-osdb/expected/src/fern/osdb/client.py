

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.action_help_response import ActionHelpResponse
from ..types.describe_action_response import DescribeActionResponse
from ..types.describe_service_response import DescribeServiceResponse
from ..types.error_model import ErrorModel
from ..types.list_actions_response import ListActionsResponse
from ..types.list_services_response import ListServicesResponse
from ..types.login_response import LoginResponse
from ..types.logout_response import LogoutResponse
from .raw_client import AsyncRawOsdbClient, RawOsdbClient
from .types.exec_body_osdb_output_type import ExecBodyOsdbOutputType
from .types.load_service_response import LoadServiceResponse
from .types.unload_service_response import UnloadServiceResponse


OMIT = typing.cast(typing.Any, ...)


class OsdbClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOsdbClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOsdbClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOsdbClient
        """
        return self._raw_client

    def list_actions(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListActionsResponse:
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
        ListActionsResponse
            An array of action descriptions for the actions supported by the given service.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.osdb.list_actions(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.list_actions(service_id, request_options=request_options)
        return _response.data

    def describe_action(
        self, service_id: str, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DescribeActionResponse:
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
        DescribeActionResponse
            A single action description

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.osdb.describe_action(
            service_id="serviceId",
            action_id="actionId",
        )
        """
        _response = self._raw_client.describe_action(service_id, action_id, request_options=request_options)
        return _response.data

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
    ) -> ErrorModel:
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
        ErrorModel
            Error response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.osdb.execute_action(
            service_id="serviceId",
            action_id="actionId",
        )
        """
        _response = self._raw_client.execute_action(
            service_id,
            action_id,
            action_specific_property1=action_specific_property1,
            action_specific_property2=action_specific_property2,
            osdb_body_data_encoding=osdb_body_data_encoding,
            osdb_body_data_raw=osdb_body_data_raw,
            osdb_body_data_src_url=osdb_body_data_src_url,
            osdb_output_type=osdb_output_type,
            osdb_response_format=osdb_response_format,
            request_options=request_options,
        )
        return _response.data

    def action_help(
        self, service_id: str, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionHelpResponse:
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
        ActionHelpResponse
            Action help text

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.osdb.action_help(
            service_id="serviceId",
            action_id="actionId",
        )
        """
        _response = self._raw_client.action_help(service_id, action_id, request_options=request_options)
        return _response.data

    def login(self, *, request_options: typing.Optional[RequestOptions] = None) -> LoginResponse:
        """
        Logs a user into the OSDB server, authenticating them by their WebID and returning an OSDB session ID in cookie osdb.sid

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            Confirmation of a successful OSDB login.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.osdb.login()
        """
        _response = self._raw_client.login(request_options=request_options)
        return _response.data

    def logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> LogoutResponse:
        """
        Logs a user out of the OSDB server, ending their OSDB session

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogoutResponse
            Confirmation of a successful OSDB logout.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.osdb.logout()
        """
        _response = self._raw_client.logout(request_options=request_options)
        return _response.data

    def list_services(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListServicesResponse:
        """
        Returns descriptions of all services registered with the OSDB server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListServicesResponse
            An array of service descriptions for all services registered with the OSDB server

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.osdb.list_services()
        """
        _response = self._raw_client.list_services(request_options=request_options)
        return _response.data

    def load_service(
        self,
        *,
        service_description_url: str,
        service_moniker: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoadServiceResponse:
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
        LoadServiceResponse
            loadService response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.osdb.load_service(
            service_description_url="http://ods-qa.openlinksw.com:8896/DAV/home/nobody/csv_extractor_svc.ods-qa.170109.ttl",
            service_moniker="csv_extractor",
        )
        """
        _response = self._raw_client.load_service(
            service_description_url=service_description_url,
            service_moniker=service_moniker,
            request_options=request_options,
        )
        return _response.data

    def describe_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DescribeServiceResponse:
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
        DescribeServiceResponse
            A single service description

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.osdb.describe_service(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.describe_service(service_id, request_options=request_options)
        return _response.data

    def unload_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UnloadServiceResponse:
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
        UnloadServiceResponse
            unloadService response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.osdb.unload_service(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.unload_service(service_id, request_options=request_options)
        return _response.data


class AsyncOsdbClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOsdbClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOsdbClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOsdbClient
        """
        return self._raw_client

    async def list_actions(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListActionsResponse:
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
        ListActionsResponse
            An array of action descriptions for the actions supported by the given service.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.osdb.list_actions(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_actions(service_id, request_options=request_options)
        return _response.data

    async def describe_action(
        self, service_id: str, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DescribeActionResponse:
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
        DescribeActionResponse
            A single action description

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.osdb.describe_action(
                service_id="serviceId",
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.describe_action(service_id, action_id, request_options=request_options)
        return _response.data

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
    ) -> ErrorModel:
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
        ErrorModel
            Error response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.osdb.execute_action(
                service_id="serviceId",
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_action(
            service_id,
            action_id,
            action_specific_property1=action_specific_property1,
            action_specific_property2=action_specific_property2,
            osdb_body_data_encoding=osdb_body_data_encoding,
            osdb_body_data_raw=osdb_body_data_raw,
            osdb_body_data_src_url=osdb_body_data_src_url,
            osdb_output_type=osdb_output_type,
            osdb_response_format=osdb_response_format,
            request_options=request_options,
        )
        return _response.data

    async def action_help(
        self, service_id: str, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionHelpResponse:
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
        ActionHelpResponse
            Action help text

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.osdb.action_help(
                service_id="serviceId",
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.action_help(service_id, action_id, request_options=request_options)
        return _response.data

    async def login(self, *, request_options: typing.Optional[RequestOptions] = None) -> LoginResponse:
        """
        Logs a user into the OSDB server, authenticating them by their WebID and returning an OSDB session ID in cookie osdb.sid

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            Confirmation of a successful OSDB login.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.osdb.login()


        asyncio.run(main())
        """
        _response = await self._raw_client.login(request_options=request_options)
        return _response.data

    async def logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> LogoutResponse:
        """
        Logs a user out of the OSDB server, ending their OSDB session

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogoutResponse
            Confirmation of a successful OSDB logout.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.osdb.logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.logout(request_options=request_options)
        return _response.data

    async def list_services(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListServicesResponse:
        """
        Returns descriptions of all services registered with the OSDB server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListServicesResponse
            An array of service descriptions for all services registered with the OSDB server

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.osdb.list_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_services(request_options=request_options)
        return _response.data

    async def load_service(
        self,
        *,
        service_description_url: str,
        service_moniker: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoadServiceResponse:
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
        LoadServiceResponse
            loadService response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.osdb.load_service(
                service_description_url="http://ods-qa.openlinksw.com:8896/DAV/home/nobody/csv_extractor_svc.ods-qa.170109.ttl",
                service_moniker="csv_extractor",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.load_service(
            service_description_url=service_description_url,
            service_moniker=service_moniker,
            request_options=request_options,
        )
        return _response.data

    async def describe_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DescribeServiceResponse:
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
        DescribeServiceResponse
            A single service description

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.osdb.describe_service(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.describe_service(service_id, request_options=request_options)
        return _response.data

    async def unload_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UnloadServiceResponse:
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
        UnloadServiceResponse
            unloadService response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.osdb.unload_service(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unload_service(service_id, request_options=request_options)
        return _response.data
