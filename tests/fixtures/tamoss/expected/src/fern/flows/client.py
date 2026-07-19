

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.content_format import ContentFormat
from ..types.deletion_request import DeletionRequest
from ..types.flow import Flow
from ..types.flow_collection import FlowCollection
from ..types.mime_type import MimeType
from ..types.tags import Tags
from ..types.timerange import Timerange
from ..types.url_tag_list import UrlTagList
from ..types.uuid_ import Uuid
from .raw_client import AsyncRawFlowsClient, RawFlowsClient


OMIT = typing.cast(typing.Any, ...)


class FlowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFlowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFlowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFlowsClient
        """
        return self._raw_client

    def get_flows(
        self,
        *,
        source_id: typing.Optional[Uuid] = None,
        timerange: typing.Optional[Timerange] = None,
        include_timerange: typing.Optional[bool] = None,
        format: typing.Optional[ContentFormat] = None,
        codec: typing.Optional[MimeType] = None,
        label: typing.Optional[str] = None,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        frame_width: typing.Optional[int] = None,
        frame_height: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Flow]:
        """
        List the Flows registered in the TAMS service instance.

        Parameters
        ----------
        source_id : typing.Optional[Uuid]
            Filter on Source identifier.

        timerange : typing.Optional[Timerange]
            Filter on Flows that overlap the given timerange. An empty timerange returns Flows with no content.

        include_timerange : typing.Optional[bool]
            Third-party compatibility extension. Include each listed Flow's computed content timerange in the response.

        format : typing.Optional[ContentFormat]
            Filter on Flow format.

        codec : typing.Optional[MimeType]
            Filter on Flow codec.

        label : typing.Optional[str]
            Filter on Flows that have the given label.

        tag_name : typing.Optional[UrlTagList]
            Filter on flows that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on Flows that have a tag named {name} regardless of value.
            {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        frame_width : typing.Optional[int]
            Filter on video Flows that have the given frame width.

        frame_height : typing.Optional[int]
            Filter on video Flows that have the given frame height.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Flow]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.get_flows()
        """
        _response = self._raw_client.get_flows(
            source_id=source_id,
            timerange=timerange,
            include_timerange=include_timerange,
            format=format,
            codec=codec,
            label=label,
            tag_name=tag_name,
            tag_exists_name=tag_exists_name,
            frame_width=frame_width,
            frame_height=frame_height,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def head_flows(
        self,
        *,
        source_id: typing.Optional[Uuid] = None,
        timerange: typing.Optional[Timerange] = None,
        include_timerange: typing.Optional[bool] = None,
        format: typing.Optional[ContentFormat] = None,
        codec: typing.Optional[MimeType] = None,
        label: typing.Optional[str] = None,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        frame_width: typing.Optional[int] = None,
        frame_height: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return Flows path headers

        Parameters
        ----------
        source_id : typing.Optional[Uuid]
            Filter on Source identifier.

        timerange : typing.Optional[Timerange]
            Filter on Flows that overlap the given timerange.

        include_timerange : typing.Optional[bool]
            Third-party compatibility extension. Include each listed Flow's computed content timerange in the response.

        format : typing.Optional[ContentFormat]
            Filter on Flow format.

        codec : typing.Optional[MimeType]
            Filter on Flow codec.

        label : typing.Optional[str]
            Filter on Flows that have the given label.

        tag_name : typing.Optional[UrlTagList]
            Filter on flows that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on Flows that have a tag named {name} regardless of value.
            {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        frame_width : typing.Optional[int]
            Filter on video Flows that have the given frame width.

        frame_height : typing.Optional[int]
            Filter on video Flows that have the given frame height.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.head_flows()
        """
        _response = self._raw_client.head_flows(
            source_id=source_id,
            timerange=timerange,
            include_timerange=include_timerange,
            format=format,
            codec=codec,
            label=label,
            tag_name=tag_name,
            tag_exists_name=tag_exists_name,
            frame_width=frame_width,
            frame_height=frame_height,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.headers

    def get_flows_flow_id(
        self,
        flow_id: Uuid,
        *,
        include_timerange: typing.Optional[bool] = None,
        timerange: typing.Optional[Timerange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Flow:
        """
        Returns Flow metadata.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        include_timerange : typing.Optional[bool]
            Include `timerange` in the response.

        timerange : typing.Optional[Timerange]
            Limit `timerange` of the response to the time range over which Segments partially or wholly overlap with the provided timerange.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Flow


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.get_flows_flow_id(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.get_flows_flow_id(
            flow_id, include_timerange=include_timerange, timerange=timerange, request_options=request_options
        )
        return _response.data

    def put_flows_flow_id(
        self, flow_id: Uuid, *, request: Flow, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Flow]:
        """
        Create or replace the Flow metadata.

        Clients should aim to populate as many of the Flow metadata fields as possible and practical. The fewer parameters that are set, the higher the likelihood that reading clients will have to retrieve the media to determine technical metadata to e.g. configure decoders.

        Some parameters may be ignored/overridden by service implementations. This is to enable the Flow json-blob to be re-used with no/minimal editing in various use cases. Such parameters are called out in their description.

        Service implementations SHOULD verify that Flow metadata is compatible with the associated Source.
        Service implementations MAY accept modification/addition of parameters, and reflect such changes in the Source, where it will not bring any Flows of the Source into conflict.
        Where metadata would result in any Flow of the Source coming into conflict, the request SHOULD be rejected with a 400 response.
        Examples of conflicting metadata include `format` not matching, or the `role` in `source_collection` and `flow_collection` not matching.
        It may also be possible for service implementations to detect some instances where multiple Flows should not be considered of the same Source, such as audio Flows with different numbers of tracks.
        Further guidance on when Flows/Sources may be considered the same/different may be found in the [Practical Guidance for Media](https://specs.amwa.tv/ms-04/releases/v1.0.0/docs/3.0._Practical_Guidance_for_Media.html) section of AMWA MS-04.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : Flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Flow]
            The Flow has been created.

        Examples
        --------
        from fern import FernApi, FlowVideo, FlowVideoEssenceParameters, FlowVideoFormat

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.put_flows_flow_id(
            flow_id="flowId",
            request=FlowVideo(
                id="id",
                source_id="source_id",
                format=FlowVideoFormat.URN_X_NMOS_FORMAT_VIDEO,
                essence_parameters=FlowVideoEssenceParameters(
                    frame_width=1,
                    frame_height=1,
                ),
            ),
        )
        """
        _response = self._raw_client.put_flows_flow_id(flow_id, request=request, request_options=request_options)
        return _response.data

    def delete_flows_flow_id(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[DeletionRequest]:
        """
        Deletes the Flow and associated Segments.
        If Flow Segment deletion takes too long then this request will return 202 Accepted and the `Location` header will point to a Flow Delete Request to monitor deletion progress

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[DeletionRequest]
            This request has taken longer than the configured timeout, and will continue asynchronously

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.delete_flows_flow_id(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.delete_flows_flow_id(flow_id, request_options=request_options)
        return _response.data

    def head_flows_flow_id(
        self,
        flow_id: Uuid,
        *,
        include_timerange: typing.Optional[bool] = None,
        timerange: typing.Optional[Timerange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return Flow path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        include_timerange : typing.Optional[bool]
            Include `timerange` in the response.

        timerange : typing.Optional[Timerange]
            Limit `timerange` of the response to the time range over which Segments partially or wholly overlap with the provided timerange.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.head_flows_flow_id(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.head_flows_flow_id(
            flow_id, include_timerange=include_timerange, timerange=timerange, request_options=request_options
        )
        return _response.headers

    def get_flows_flow_id_tags(self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> Tags:
        """
        Returns the Flow tags.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tags


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.get_flows_flow_id_tags(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.get_flows_flow_id_tags(flow_id, request_options=request_options)
        return _response.data

    def head_flows_flow_id_tags(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow tags path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.head_flows_flow_id_tags(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.head_flows_flow_id_tags(flow_id, request_options=request_options)
        return _response.headers

    def get_flows_flow_id_tags_name(
        self, flow_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Return the tag value associated with the tag name.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.get_flows_flow_id_tags_name(
            flow_id="flowId",
            name="name",
        )
        """
        _response = self._raw_client.get_flows_flow_id_tags_name(flow_id, name, request_options=request_options)
        return _response.data

    def put_flows_flow_id_tags_name(
        self, flow_id: Uuid, name: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the tag.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.put_flows_flow_id_tags_name(
            flow_id="flowId",
            name="name",
            request='"proxy"\n',
        )
        """
        _response = self._raw_client.put_flows_flow_id_tags_name(
            flow_id, name, request=request, request_options=request_options
        )
        return _response.data

    def delete_flows_flow_id_tags_name(
        self, flow_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the tag.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.delete_flows_flow_id_tags_name(
            flow_id="flowId",
            name="name",
        )
        """
        _response = self._raw_client.delete_flows_flow_id_tags_name(flow_id, name, request_options=request_options)
        return _response.data

    def head_flows_flow_id_tags_name(
        self, flow_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow tag path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.head_flows_flow_id_tags_name(
            flow_id="flowId",
            name="name",
        )
        """
        _response = self._raw_client.head_flows_flow_id_tags_name(flow_id, name, request_options=request_options)
        return _response.headers

    def get_flows_flow_id_description(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the Flow description property. This should be a human-readable description that may be showed in detailed views of Flows. The description should be longer and more detailed than `label`.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.get_flows_flow_id_description(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.get_flows_flow_id_description(flow_id, request_options=request_options)
        return _response.data

    def put_flows_flow_id_description(
        self, flow_id: Uuid, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the description property. This should be a human-readable description that may be showed in detailed views of Flows. The description should be longer and more detailed than `label`.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.put_flows_flow_id_description(
            flow_id="flowId",
            request='"Big Buck Bunny video-only capture"\n',
        )
        """
        _response = self._raw_client.put_flows_flow_id_description(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_flows_flow_id_description(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the description property.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.delete_flows_flow_id_description(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.delete_flows_flow_id_description(flow_id, request_options=request_options)
        return _response.data

    def head_flows_flow_id_description(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow description path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.head_flows_flow_id_description(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.head_flows_flow_id_description(flow_id, request_options=request_options)
        return _response.headers

    def get_flows_flow_id_label(self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns the Flow label property. This should be a very short, human-readable label that may be displayed in listings of Flows.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.get_flows_flow_id_label(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.get_flows_flow_id_label(flow_id, request_options=request_options)
        return _response.data

    def put_flows_flow_id_label(
        self, flow_id: Uuid, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the label property. This should be a very short, human-readable label that may be displayed in listings of Flows.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.put_flows_flow_id_label(
            flow_id="flowId",
            request='"Big Buck Bunny Movie"\n',
        )
        """
        _response = self._raw_client.put_flows_flow_id_label(flow_id, request=request, request_options=request_options)
        return _response.data

    def delete_flows_flow_id_label(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the label property.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.delete_flows_flow_id_label(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.delete_flows_flow_id_label(flow_id, request_options=request_options)
        return _response.data

    def head_flows_flow_id_label(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow label path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.head_flows_flow_id_label(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.head_flows_flow_id_label(flow_id, request_options=request_options)
        return _response.headers

    def get_flows_flow_id_read_only(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Returns the Flow read_only property. If set to 'true', service implementations SHOULD reject client requests to update Flow metadata (other than the read_only property), and Flow Segments. Service implementations should also reject requests to the [`/flows/{flowId}/storage`](#/operations/POST_flows-flowId-storage) endpoint for the Flow, and requests to delete the Flow.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.get_flows_flow_id_read_only(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.get_flows_flow_id_read_only(flow_id, request_options=request_options)
        return _response.data

    def put_flows_flow_id_read_only(
        self, flow_id: Uuid, *, request: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Set the read-only property. If set to 'true', service implementations SHOULD reject client requests to update Flow metadata (other than the read_only property), and Flow Segments. Service implementations should also reject requests to the [`/flows/{flowId}/storage`](#/operations/POST_flows-flowId-storage) endpoint for the Flow, and requests to delete the Flow.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.put_flows_flow_id_read_only(
            flow_id="flowId",
            request=True,
        )
        """
        _response = self._raw_client.put_flows_flow_id_read_only(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    def head_flows_flow_id_read_only(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow read_only path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.head_flows_flow_id_read_only(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.head_flows_flow_id_read_only(flow_id, request_options=request_options)
        return _response.headers

    def get_flows_flow_id_flow_collection(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FlowCollection:
        """
        Returns the Flow collection property. A list of Flows that are collected together by this Flow.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FlowCollection


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.get_flows_flow_id_flow_collection(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.get_flows_flow_id_flow_collection(flow_id, request_options=request_options)
        return _response.data

    def put_flows_flow_id_flow_collection(
        self, flow_id: Uuid, *, request: FlowCollection, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the Flow collection property. A list of Flows that are collected together by this Flow.

        Service implementations SHOULD verify that Flow metadata is compatible with the associated Source.
        Service implementations MAY accept modification/addition of parameters, and reflect such changes in the Source, where it will not bring any Flows of the Source into conflict.
        Where metadata would result in any Flow of the Source coming into conflict, the request SHOULD be rejected with a 400 response.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : FlowCollection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, FlowCollectionItem

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.put_flows_flow_id_flow_collection(
            flow_id="flowId",
            request=[
                FlowCollectionItem(
                    id="id",
                    role="role",
                )
            ],
        )
        """
        _response = self._raw_client.put_flows_flow_id_flow_collection(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_flows_flow_id_flow_collection(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the Flow collection property.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.delete_flows_flow_id_flow_collection(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.delete_flows_flow_id_flow_collection(flow_id, request_options=request_options)
        return _response.data

    def head_flows_flow_id_flow_collection(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Returns the Flow collection path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.head_flows_flow_id_flow_collection(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.head_flows_flow_id_flow_collection(flow_id, request_options=request_options)
        return _response.headers

    def get_flows_flow_id_max_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Returns the Flow max bit rate property.

        The maximum bit rate of the Flow Segments in 1000 bits/second.
        A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.get_flows_flow_id_max_bit_rate(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.get_flows_flow_id_max_bit_rate(flow_id, request_options=request_options)
        return _response.data

    def put_flows_flow_id_max_bit_rate(
        self, flow_id: Uuid, *, request: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the max bit rate property.

        The maximum bit rate of the Flow Segments in 1000 bits/second.
        A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.put_flows_flow_id_max_bit_rate(
            flow_id="flowId",
            request=5000,
        )
        """
        _response = self._raw_client.put_flows_flow_id_max_bit_rate(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_flows_flow_id_max_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the Flow max bit rate property.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.delete_flows_flow_id_max_bit_rate(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.delete_flows_flow_id_max_bit_rate(flow_id, request_options=request_options)
        return _response.data

    def head_flows_flow_id_max_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Returns the Flow max bit rate path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.head_flows_flow_id_max_bit_rate(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.head_flows_flow_id_max_bit_rate(flow_id, request_options=request_options)
        return _response.headers

    def get_flows_flow_id_avg_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Returns the Flow average bit rate property.

        The average bit rate of the Flow Segments in 1000 bits/second.
        A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.get_flows_flow_id_avg_bit_rate(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.get_flows_flow_id_avg_bit_rate(flow_id, request_options=request_options)
        return _response.data

    def put_flows_flow_id_avg_bit_rate(
        self, flow_id: Uuid, *, request: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the average bit rate property.

        The average bit rate of the Flow Segments in 1000 bits/second.
        A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.put_flows_flow_id_avg_bit_rate(
            flow_id="flowId",
            request=3246,
        )
        """
        _response = self._raw_client.put_flows_flow_id_avg_bit_rate(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_flows_flow_id_avg_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the Flow average bit rate property.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.delete_flows_flow_id_avg_bit_rate(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.delete_flows_flow_id_avg_bit_rate(flow_id, request_options=request_options)
        return _response.data

    def head_flows_flow_id_avg_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Returns the Flow average bit rate path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flows.head_flows_flow_id_avg_bit_rate(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.head_flows_flow_id_avg_bit_rate(flow_id, request_options=request_options)
        return _response.headers


class AsyncFlowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFlowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFlowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFlowsClient
        """
        return self._raw_client

    async def get_flows(
        self,
        *,
        source_id: typing.Optional[Uuid] = None,
        timerange: typing.Optional[Timerange] = None,
        include_timerange: typing.Optional[bool] = None,
        format: typing.Optional[ContentFormat] = None,
        codec: typing.Optional[MimeType] = None,
        label: typing.Optional[str] = None,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        frame_width: typing.Optional[int] = None,
        frame_height: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Flow]:
        """
        List the Flows registered in the TAMS service instance.

        Parameters
        ----------
        source_id : typing.Optional[Uuid]
            Filter on Source identifier.

        timerange : typing.Optional[Timerange]
            Filter on Flows that overlap the given timerange. An empty timerange returns Flows with no content.

        include_timerange : typing.Optional[bool]
            Third-party compatibility extension. Include each listed Flow's computed content timerange in the response.

        format : typing.Optional[ContentFormat]
            Filter on Flow format.

        codec : typing.Optional[MimeType]
            Filter on Flow codec.

        label : typing.Optional[str]
            Filter on Flows that have the given label.

        tag_name : typing.Optional[UrlTagList]
            Filter on flows that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on Flows that have a tag named {name} regardless of value.
            {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        frame_width : typing.Optional[int]
            Filter on video Flows that have the given frame width.

        frame_height : typing.Optional[int]
            Filter on video Flows that have the given frame height.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Flow]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.get_flows()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows(
            source_id=source_id,
            timerange=timerange,
            include_timerange=include_timerange,
            format=format,
            codec=codec,
            label=label,
            tag_name=tag_name,
            tag_exists_name=tag_exists_name,
            frame_width=frame_width,
            frame_height=frame_height,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def head_flows(
        self,
        *,
        source_id: typing.Optional[Uuid] = None,
        timerange: typing.Optional[Timerange] = None,
        include_timerange: typing.Optional[bool] = None,
        format: typing.Optional[ContentFormat] = None,
        codec: typing.Optional[MimeType] = None,
        label: typing.Optional[str] = None,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        frame_width: typing.Optional[int] = None,
        frame_height: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return Flows path headers

        Parameters
        ----------
        source_id : typing.Optional[Uuid]
            Filter on Source identifier.

        timerange : typing.Optional[Timerange]
            Filter on Flows that overlap the given timerange.

        include_timerange : typing.Optional[bool]
            Third-party compatibility extension. Include each listed Flow's computed content timerange in the response.

        format : typing.Optional[ContentFormat]
            Filter on Flow format.

        codec : typing.Optional[MimeType]
            Filter on Flow codec.

        label : typing.Optional[str]
            Filter on Flows that have the given label.

        tag_name : typing.Optional[UrlTagList]
            Filter on flows that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on Flows that have a tag named {name} regardless of value.
            {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        frame_width : typing.Optional[int]
            Filter on video Flows that have the given frame width.

        frame_height : typing.Optional[int]
            Filter on video Flows that have the given frame height.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.head_flows()


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows(
            source_id=source_id,
            timerange=timerange,
            include_timerange=include_timerange,
            format=format,
            codec=codec,
            label=label,
            tag_name=tag_name,
            tag_exists_name=tag_exists_name,
            frame_width=frame_width,
            frame_height=frame_height,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.headers

    async def get_flows_flow_id(
        self,
        flow_id: Uuid,
        *,
        include_timerange: typing.Optional[bool] = None,
        timerange: typing.Optional[Timerange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Flow:
        """
        Returns Flow metadata.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        include_timerange : typing.Optional[bool]
            Include `timerange` in the response.

        timerange : typing.Optional[Timerange]
            Limit `timerange` of the response to the time range over which Segments partially or wholly overlap with the provided timerange.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Flow


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.get_flows_flow_id(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows_flow_id(
            flow_id, include_timerange=include_timerange, timerange=timerange, request_options=request_options
        )
        return _response.data

    async def put_flows_flow_id(
        self, flow_id: Uuid, *, request: Flow, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Flow]:
        """
        Create or replace the Flow metadata.

        Clients should aim to populate as many of the Flow metadata fields as possible and practical. The fewer parameters that are set, the higher the likelihood that reading clients will have to retrieve the media to determine technical metadata to e.g. configure decoders.

        Some parameters may be ignored/overridden by service implementations. This is to enable the Flow json-blob to be re-used with no/minimal editing in various use cases. Such parameters are called out in their description.

        Service implementations SHOULD verify that Flow metadata is compatible with the associated Source.
        Service implementations MAY accept modification/addition of parameters, and reflect such changes in the Source, where it will not bring any Flows of the Source into conflict.
        Where metadata would result in any Flow of the Source coming into conflict, the request SHOULD be rejected with a 400 response.
        Examples of conflicting metadata include `format` not matching, or the `role` in `source_collection` and `flow_collection` not matching.
        It may also be possible for service implementations to detect some instances where multiple Flows should not be considered of the same Source, such as audio Flows with different numbers of tracks.
        Further guidance on when Flows/Sources may be considered the same/different may be found in the [Practical Guidance for Media](https://specs.amwa.tv/ms-04/releases/v1.0.0/docs/3.0._Practical_Guidance_for_Media.html) section of AMWA MS-04.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : Flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Flow]
            The Flow has been created.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            FlowVideo,
            FlowVideoEssenceParameters,
            FlowVideoFormat,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.put_flows_flow_id(
                flow_id="flowId",
                request=FlowVideo(
                    id="id",
                    source_id="source_id",
                    format=FlowVideoFormat.URN_X_NMOS_FORMAT_VIDEO,
                    essence_parameters=FlowVideoEssenceParameters(
                        frame_width=1,
                        frame_height=1,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_flows_flow_id(flow_id, request=request, request_options=request_options)
        return _response.data

    async def delete_flows_flow_id(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[DeletionRequest]:
        """
        Deletes the Flow and associated Segments.
        If Flow Segment deletion takes too long then this request will return 202 Accepted and the `Location` header will point to a Flow Delete Request to monitor deletion progress

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[DeletionRequest]
            This request has taken longer than the configured timeout, and will continue asynchronously

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.delete_flows_flow_id(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_flows_flow_id(flow_id, request_options=request_options)
        return _response.data

    async def head_flows_flow_id(
        self,
        flow_id: Uuid,
        *,
        include_timerange: typing.Optional[bool] = None,
        timerange: typing.Optional[Timerange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return Flow path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        include_timerange : typing.Optional[bool]
            Include `timerange` in the response.

        timerange : typing.Optional[Timerange]
            Limit `timerange` of the response to the time range over which Segments partially or wholly overlap with the provided timerange.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.head_flows_flow_id(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows_flow_id(
            flow_id, include_timerange=include_timerange, timerange=timerange, request_options=request_options
        )
        return _response.headers

    async def get_flows_flow_id_tags(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tags:
        """
        Returns the Flow tags.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tags


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.get_flows_flow_id_tags(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows_flow_id_tags(flow_id, request_options=request_options)
        return _response.data

    async def head_flows_flow_id_tags(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow tags path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.head_flows_flow_id_tags(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows_flow_id_tags(flow_id, request_options=request_options)
        return _response.headers

    async def get_flows_flow_id_tags_name(
        self, flow_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Return the tag value associated with the tag name.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.get_flows_flow_id_tags_name(
                flow_id="flowId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows_flow_id_tags_name(flow_id, name, request_options=request_options)
        return _response.data

    async def put_flows_flow_id_tags_name(
        self, flow_id: Uuid, name: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the tag.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.put_flows_flow_id_tags_name(
                flow_id="flowId",
                name="name",
                request='"proxy"\n',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_flows_flow_id_tags_name(
            flow_id, name, request=request, request_options=request_options
        )
        return _response.data

    async def delete_flows_flow_id_tags_name(
        self, flow_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the tag.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.delete_flows_flow_id_tags_name(
                flow_id="flowId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_flows_flow_id_tags_name(
            flow_id, name, request_options=request_options
        )
        return _response.data

    async def head_flows_flow_id_tags_name(
        self, flow_id: Uuid, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow tag path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        name : str
            The tag name. {name} MUST be URL encoded where special characters are present.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.head_flows_flow_id_tags_name(
                flow_id="flowId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows_flow_id_tags_name(flow_id, name, request_options=request_options)
        return _response.headers

    async def get_flows_flow_id_description(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the Flow description property. This should be a human-readable description that may be showed in detailed views of Flows. The description should be longer and more detailed than `label`.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.get_flows_flow_id_description(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows_flow_id_description(flow_id, request_options=request_options)
        return _response.data

    async def put_flows_flow_id_description(
        self, flow_id: Uuid, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the description property. This should be a human-readable description that may be showed in detailed views of Flows. The description should be longer and more detailed than `label`.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.put_flows_flow_id_description(
                flow_id="flowId",
                request='"Big Buck Bunny video-only capture"\n',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_flows_flow_id_description(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_flows_flow_id_description(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the description property.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.delete_flows_flow_id_description(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_flows_flow_id_description(flow_id, request_options=request_options)
        return _response.data

    async def head_flows_flow_id_description(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow description path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.head_flows_flow_id_description(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows_flow_id_description(flow_id, request_options=request_options)
        return _response.headers

    async def get_flows_flow_id_label(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the Flow label property. This should be a very short, human-readable label that may be displayed in listings of Flows.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.get_flows_flow_id_label(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows_flow_id_label(flow_id, request_options=request_options)
        return _response.data

    async def put_flows_flow_id_label(
        self, flow_id: Uuid, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the label property. This should be a very short, human-readable label that may be displayed in listings of Flows.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.put_flows_flow_id_label(
                flow_id="flowId",
                request='"Big Buck Bunny Movie"\n',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_flows_flow_id_label(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_flows_flow_id_label(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the label property.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.delete_flows_flow_id_label(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_flows_flow_id_label(flow_id, request_options=request_options)
        return _response.data

    async def head_flows_flow_id_label(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow label path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.head_flows_flow_id_label(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows_flow_id_label(flow_id, request_options=request_options)
        return _response.headers

    async def get_flows_flow_id_read_only(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Returns the Flow read_only property. If set to 'true', service implementations SHOULD reject client requests to update Flow metadata (other than the read_only property), and Flow Segments. Service implementations should also reject requests to the [`/flows/{flowId}/storage`](#/operations/POST_flows-flowId-storage) endpoint for the Flow, and requests to delete the Flow.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.get_flows_flow_id_read_only(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows_flow_id_read_only(flow_id, request_options=request_options)
        return _response.data

    async def put_flows_flow_id_read_only(
        self, flow_id: Uuid, *, request: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Set the read-only property. If set to 'true', service implementations SHOULD reject client requests to update Flow metadata (other than the read_only property), and Flow Segments. Service implementations should also reject requests to the [`/flows/{flowId}/storage`](#/operations/POST_flows-flowId-storage) endpoint for the Flow, and requests to delete the Flow.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.put_flows_flow_id_read_only(
                flow_id="flowId",
                request=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_flows_flow_id_read_only(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    async def head_flows_flow_id_read_only(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return Flow read_only path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.head_flows_flow_id_read_only(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows_flow_id_read_only(flow_id, request_options=request_options)
        return _response.headers

    async def get_flows_flow_id_flow_collection(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FlowCollection:
        """
        Returns the Flow collection property. A list of Flows that are collected together by this Flow.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FlowCollection


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.get_flows_flow_id_flow_collection(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows_flow_id_flow_collection(flow_id, request_options=request_options)
        return _response.data

    async def put_flows_flow_id_flow_collection(
        self, flow_id: Uuid, *, request: FlowCollection, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the Flow collection property. A list of Flows that are collected together by this Flow.

        Service implementations SHOULD verify that Flow metadata is compatible with the associated Source.
        Service implementations MAY accept modification/addition of parameters, and reflect such changes in the Source, where it will not bring any Flows of the Source into conflict.
        Where metadata would result in any Flow of the Source coming into conflict, the request SHOULD be rejected with a 400 response.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : FlowCollection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FlowCollectionItem

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.put_flows_flow_id_flow_collection(
                flow_id="flowId",
                request=[
                    FlowCollectionItem(
                        id="id",
                        role="role",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_flows_flow_id_flow_collection(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_flows_flow_id_flow_collection(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the Flow collection property.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.delete_flows_flow_id_flow_collection(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_flows_flow_id_flow_collection(
            flow_id, request_options=request_options
        )
        return _response.data

    async def head_flows_flow_id_flow_collection(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Returns the Flow collection path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.head_flows_flow_id_flow_collection(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows_flow_id_flow_collection(flow_id, request_options=request_options)
        return _response.headers

    async def get_flows_flow_id_max_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Returns the Flow max bit rate property.

        The maximum bit rate of the Flow Segments in 1000 bits/second.
        A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.get_flows_flow_id_max_bit_rate(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows_flow_id_max_bit_rate(flow_id, request_options=request_options)
        return _response.data

    async def put_flows_flow_id_max_bit_rate(
        self, flow_id: Uuid, *, request: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the max bit rate property.

        The maximum bit rate of the Flow Segments in 1000 bits/second.
        A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.put_flows_flow_id_max_bit_rate(
                flow_id="flowId",
                request=5000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_flows_flow_id_max_bit_rate(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_flows_flow_id_max_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the Flow max bit rate property.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.delete_flows_flow_id_max_bit_rate(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_flows_flow_id_max_bit_rate(flow_id, request_options=request_options)
        return _response.data

    async def head_flows_flow_id_max_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Returns the Flow max bit rate path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.head_flows_flow_id_max_bit_rate(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows_flow_id_max_bit_rate(flow_id, request_options=request_options)
        return _response.headers

    async def get_flows_flow_id_avg_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Returns the Flow average bit rate property.

        The average bit rate of the Flow Segments in 1000 bits/second.
        A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.get_flows_flow_id_avg_bit_rate(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows_flow_id_avg_bit_rate(flow_id, request_options=request_options)
        return _response.data

    async def put_flows_flow_id_avg_bit_rate(
        self, flow_id: Uuid, *, request: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create or update the average bit rate property.

        The average bit rate of the Flow Segments in 1000 bits/second.
        A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.put_flows_flow_id_avg_bit_rate(
                flow_id="flowId",
                request=3246,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_flows_flow_id_avg_bit_rate(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_flows_flow_id_avg_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the Flow average bit rate property.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.delete_flows_flow_id_avg_bit_rate(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_flows_flow_id_avg_bit_rate(flow_id, request_options=request_options)
        return _response.data

    async def head_flows_flow_id_avg_bit_rate(
        self, flow_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Returns the Flow average bit rate path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flows.head_flows_flow_id_avg_bit_rate(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows_flow_id_avg_bit_rate(flow_id, request_options=request_options)
        return _response.headers
