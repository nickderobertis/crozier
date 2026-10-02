

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.get_api_playback_motion_response import GetApiPlaybackMotionResponse
from .types.get_api_playback_response import GetApiPlaybackResponse
from .types.post_api_bridge_pose_request import PostApiBridgePoseRequest
from .types.post_api_playback_control_request_command import PostApiPlaybackControlRequestCommand
from .types.post_api_playback_control_request_mode import PostApiPlaybackControlRequestMode
from .types.post_api_playback_control_response import PostApiPlaybackControlResponse
from .types.post_api_playback_motion_request import PostApiPlaybackMotionRequest
from .types.post_api_playback_motion_response import PostApiPlaybackMotionResponse
from .types.post_api_playback_parameters_response import PostApiPlaybackParametersResponse
from .types.post_api_playback_reload_response import PostApiPlaybackReloadResponse
from .types.qa_check_request_motion_sweep import QaCheckRequestMotionSweep
from .types.qa_check_request_pose_samples_item import QaCheckRequestPoseSamplesItem
from .types.transaction_request import TransactionRequest


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def get_api_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_health()
        """
        _response = self._raw_client.get_api_health(request_options=request_options)
        return _response.data

    def get_api_context(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_context()
        """
        _response = self._raw_client.get_api_context(request_options=request_options)
        return _response.data

    def get_api_parts(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_parts()
        """
        _response = self._raw_client.get_api_parts(request_options=request_options)
        return _response.data

    def get_api_deformers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_deformers()
        """
        _response = self._raw_client.get_api_deformers(request_options=request_options)
        return _response.data

    def get_api_params(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_params()
        """
        _response = self._raw_client.get_api_params(request_options=request_options)
        return _response.data

    def get_api_modeling(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_modeling()
        """
        _response = self._raw_client.get_api_modeling(request_options=request_options)
        return _response.data

    def get_api_modeling_audit(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_modeling_audit()
        """
        _response = self._raw_client.get_api_modeling_audit(request_options=request_options)
        return _response.data

    def get_api_modeling_techniques(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_modeling_techniques()
        """
        _response = self._raw_client.get_api_modeling_techniques(request_options=request_options)
        return _response.data

    def get_api_modeling_role_suggestions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_modeling_role_suggestions()
        """
        _response = self._raw_client.get_api_modeling_role_suggestions(request_options=request_options)
        return _response.data

    def get_api_modeling_artmesh_presets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_modeling_artmesh_presets()
        """
        _response = self._raw_client.get_api_modeling_artmesh_presets(request_options=request_options)
        return _response.data

    def get_api_rig_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_rig_summary()
        """
        _response = self._raw_client.get_api_rig_summary(request_options=request_options)
        return _response.data

    def get_api_rig_validate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_rig_validate()
        """
        _response = self._raw_client.get_api_rig_validate(request_options=request_options)
        return _response.data

    def get_api_rig_inspect(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_rig_inspect()
        """
        _response = self._raw_client.get_api_rig_inspect(request_options=request_options)
        return _response.data

    def get_api_reference(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_reference()
        """
        _response = self._raw_client.get_api_reference(request_options=request_options)
        return _response.data

    def get_api_qa_golden(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_qa_golden()
        """
        _response = self._raw_client.get_api_qa_golden(request_options=request_options)
        return _response.data

    def get_api_bundle(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_bundle()
        """
        _response = self._raw_client.get_api_bundle(request_options=request_options)
        return _response.data

    def get_api_schema(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_schema()
        """
        _response = self._raw_client.get_api_schema(request_options=request_options)
        return _response.data

    def get_api_changes(
        self, *, since: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        since : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_changes()
        """
        _response = self._raw_client.get_api_changes(since=since, request_options=request_options)
        return _response.data

    def get_api_parts_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_parts_id(
            id="id",
        )
        """
        _response = self._raw_client.get_api_parts_id(id, request_options=request_options)
        return _response.data

    def get_api_deformers_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_deformers_id(
            id="id",
        )
        """
        _response = self._raw_client.get_api_deformers_id(id, request_options=request_options)
        return _response.data

    def get_api_rig(
        self, *, include_assets: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        include_assets : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_rig()
        """
        _response = self._raw_client.get_api_rig(include_assets=include_assets, request_options=request_options)
        return _response.data

    def put_api_rig(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        include_assets: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Disabled by default (403 legacy_write_api_disabled). Prefer /api/modeling/transaction. Explicit --allow-legacy-writes enables the legacy bypass.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        include_assets : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.put_api_rig(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_api_rig(
            request=request, include_assets=include_assets, request_options=request_options
        )
        return _response.data

    def post_api_qa_check(
        self,
        *,
        poses: typing.Optional[typing.Sequence[str]] = OMIT,
        pose_samples: typing.Optional[typing.Sequence[QaCheckRequestPoseSamplesItem]] = OMIT,
        regions: typing.Optional[typing.Sequence[str]] = OMIT,
        width: typing.Optional[float] = OMIT,
        height: typing.Optional[float] = OMIT,
        physics: typing.Optional[bool] = OMIT,
        physics_time: typing.Optional[float] = OMIT,
        physics_steps: typing.Optional[float] = OMIT,
        min_coverage: typing.Optional[float] = OMIT,
        fail_on_edge_contact: typing.Optional[bool] = OMIT,
        expected_hashes: typing.Optional[typing.Dict[str, str]] = OMIT,
        check_triangle_distortion: typing.Optional[bool] = OMIT,
        max_triangle_stretch_ratio: typing.Optional[float] = OMIT,
        max_triangle_compression_ratio: typing.Optional[float] = OMIT,
        max_triangle_anisotropy: typing.Optional[float] = OMIT,
        motion_sweep: typing.Optional[QaCheckRequestMotionSweep] = OMIT,
        supersample: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        poses : typing.Optional[typing.Sequence[str]]

        pose_samples : typing.Optional[typing.Sequence[QaCheckRequestPoseSamplesItem]]

        regions : typing.Optional[typing.Sequence[str]]

        width : typing.Optional[float]

        height : typing.Optional[float]

        physics : typing.Optional[bool]

        physics_time : typing.Optional[float]

        physics_steps : typing.Optional[float]

        min_coverage : typing.Optional[float]

        fail_on_edge_contact : typing.Optional[bool]

        expected_hashes : typing.Optional[typing.Dict[str, str]]

        check_triangle_distortion : typing.Optional[bool]

        max_triangle_stretch_ratio : typing.Optional[float]

        max_triangle_compression_ratio : typing.Optional[float]

        max_triangle_anisotropy : typing.Optional[float]

        motion_sweep : typing.Optional[QaCheckRequestMotionSweep]

        supersample : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.post_api_qa_check()
        """
        _response = self._raw_client.post_api_qa_check(
            poses=poses,
            pose_samples=pose_samples,
            regions=regions,
            width=width,
            height=height,
            physics=physics,
            physics_time=physics_time,
            physics_steps=physics_steps,
            min_coverage=min_coverage,
            fail_on_edge_contact=fail_on_edge_contact,
            expected_hashes=expected_hashes,
            check_triangle_distortion=check_triangle_distortion,
            max_triangle_stretch_ratio=max_triangle_stretch_ratio,
            max_triangle_compression_ratio=max_triangle_compression_ratio,
            max_triangle_anisotropy=max_triangle_anisotropy,
            motion_sweep=motion_sweep,
            supersample=supersample,
            request_options=request_options,
        )
        return _response.data

    def post_api_modeling_transaction(
        self, *, request: TransactionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : TransactionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import (
            FernApi,
            TransactionRequestOperations,
            TransactionRequestOperationsOperationsItem,
            TransactionRequestOperationsOperationsItemAction_BlendShapeSet,
            TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Part,
            TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartTransform,
            TransactionRequestOperationsOperationsItemTarget,
            TransactionRequestOperationsQa,
        )

        client = FernApi()
        client.post_api_modeling_transaction(
            request=TransactionRequestOperations(
                expected_revision="expectedRevision",
                commit=True,
                operations=[
                    TransactionRequestOperationsOperationsItem(
                        id="id",
                        name="name",
                        target=TransactionRequestOperationsOperationsItemTarget(),
                        action=TransactionRequestOperationsOperationsItemAction_BlendShapeSet(
                            shape=TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Part(
                                transform=TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartTransform(),
                                id="id",
                                parameter="parameter",
                                neutral_input=1.1,
                                target_input=1.1,
                            ),
                        ),
                    )
                ],
                qa=TransactionRequestOperationsQa(),
            ),
        )
        """
        _response = self._raw_client.post_api_modeling_transaction(request=request, request_options=request_options)
        return _response.data

    def post_api_assets_externalize(
        self,
        *,
        rig: typing.Dict[str, typing.Any],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Disabled by default (403 legacy_write_api_disabled). Prefer /api/modeling/transaction. Explicit --allow-legacy-writes enables the legacy bypass.

        Parameters
        ----------
        rig : typing.Dict[str, typing.Any]

        dry_run : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.post_api_assets_externalize(
            rig={"key": "value"},
        )
        """
        _response = self._raw_client.post_api_assets_externalize(
            rig=rig, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    def get_api_screenshot(
        self,
        *,
        set_: typing.Optional[str] = None,
        detail: typing.Optional[str] = None,
        part_ids: typing.Optional[str] = None,
        physics: typing.Optional[str] = None,
        param_angle_x: typing.Optional[str] = None,
        param_angle_y: typing.Optional[str] = None,
        param_angle_z: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        set_ : typing.Optional[str]

        detail : typing.Optional[str]

        part_ids : typing.Optional[str]

        physics : typing.Optional[str]

        param_angle_x : typing.Optional[str]

        param_angle_y : typing.Optional[str]

        param_angle_z : typing.Optional[str]

        width : typing.Optional[str]

        height : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            PNG image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_screenshot()
        """
        with self._raw_client.get_api_screenshot(
            set_=set_,
            detail=detail,
            part_ids=part_ids,
            physics=physics,
            param_angle_x=param_angle_x,
            param_angle_y=param_angle_y,
            param_angle_z=param_angle_z,
            width=width,
            height=height,
            request_options=request_options,
        ) as r:
            yield from r.data

    def get_api_reference_sheet(
        self,
        *,
        set_: typing.Optional[str] = None,
        detail: typing.Optional[str] = None,
        part_ids: typing.Optional[str] = None,
        physics: typing.Optional[str] = None,
        param_angle_x: typing.Optional[str] = None,
        param_angle_y: typing.Optional[str] = None,
        param_angle_z: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        set_ : typing.Optional[str]

        detail : typing.Optional[str]

        part_ids : typing.Optional[str]

        physics : typing.Optional[str]

        param_angle_x : typing.Optional[str]

        param_angle_y : typing.Optional[str]

        param_angle_z : typing.Optional[str]

        width : typing.Optional[str]

        height : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            PNG image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_reference_sheet()
        """
        with self._raw_client.get_api_reference_sheet(
            set_=set_,
            detail=detail,
            part_ids=part_ids,
            physics=physics,
            param_angle_x=param_angle_x,
            param_angle_y=param_angle_y,
            param_angle_z=param_angle_z,
            width=width,
            height=height,
            request_options=request_options,
        ) as r:
            yield from r.data

    def post_api_qa_failure_image(
        self,
        *,
        pose_id: str,
        region: str,
        before_pose_id: typing.Optional[str] = OMIT,
        width: typing.Optional[float] = OMIT,
        height: typing.Optional[float] = OMIT,
        physics: typing.Optional[bool] = OMIT,
        values: typing.Optional[typing.Dict[str, float]] = OMIT,
        before_values: typing.Optional[typing.Dict[str, float]] = OMIT,
        physics_time: typing.Optional[float] = OMIT,
        physics_steps: typing.Optional[int] = OMIT,
        supersample: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        pose_id : str

        region : str

        before_pose_id : typing.Optional[str]

        width : typing.Optional[float]

        height : typing.Optional[float]

        physics : typing.Optional[bool]

        values : typing.Optional[typing.Dict[str, float]]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        before_values : typing.Optional[typing.Dict[str, float]]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        physics_time : typing.Optional[float]

        physics_steps : typing.Optional[int]

        supersample : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            PNG image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.post_api_qa_failure_image(
            pose_id="poseId",
            region="region",
        )
        """
        with self._raw_client.post_api_qa_failure_image(
            pose_id=pose_id,
            region=region,
            before_pose_id=before_pose_id,
            width=width,
            height=height,
            physics=physics,
            values=values,
            before_values=before_values,
            physics_time=physics_time,
            physics_steps=physics_steps,
            supersample=supersample,
            request_options=request_options,
        ) as r:
            yield from r.data

    def optional_bridge_connection_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.optional_bridge_connection_status()
        """
        _response = self._raw_client.optional_bridge_connection_status(request_options=request_options)
        return _response.data

    def optional_cubism_bridge_requires_idle_api110server(
        self, *, request: PostApiBridgePoseRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : PostApiBridgePoseRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            FernApi,
            PostApiBridgePoseRequest_SetParameterValues,
            PostApiBridgePoseRequestSetParameterValuesData,
            PostApiBridgePoseRequestSetParameterValuesDataParametersItem,
        )

        client = FernApi()
        client.optional_cubism_bridge_requires_idle_api110server(
            request=PostApiBridgePoseRequest_SetParameterValues(
                data=PostApiBridgePoseRequestSetParameterValuesData(
                    model_uid="ModelUID",
                    parameters=[
                        PostApiBridgePoseRequestSetParameterValuesDataParametersItem(
                            id="Id",
                            value=1.1,
                        )
                    ],
                ),
            ),
        )
        """
        _response = self._raw_client.optional_cubism_bridge_requires_idle_api110server(
            request=request, request_options=request_options
        )
        return _response.data

    def get_api_sample(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_sample()
        """
        _response = self._raw_client.get_api_sample(request_options=request_options)
        return _response.data

    def post_api_exports_bundle(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.post_api_exports_bundle(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_api_exports_bundle(request=request, request_options=request_options)
        return _response.data

    def get_api_playback_motion(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiPlaybackMotionResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiPlaybackMotionResponse
            Motion state; GET also returns the loaded native clip or null.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_playback_motion()
        """
        _response = self._raw_client.get_api_playback_motion(request_options=request_options)
        return _response.data

    def post_api_playback_motion(
        self, *, request: PostApiPlaybackMotionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostApiPlaybackMotionResponse:
        """
        Parameters
        ----------
        request : PostApiPlaybackMotionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiPlaybackMotionResponse
            Motion state; GET also returns the loaded native clip or null.

        Examples
        --------
        from fern import (
            FernApi,
            PostApiPlaybackMotionRequestClip,
            PostApiPlaybackMotionRequestClipClip,
            PostApiPlaybackMotionRequestClipClipTracksItem,
            PostApiPlaybackMotionRequestClipClipTracksItemKeysItem,
        )

        client = FernApi()
        client.post_api_playback_motion(
            request=PostApiPlaybackMotionRequestClip(
                action="load",
                clip=PostApiPlaybackMotionRequestClipClip(
                    format="standrig-motion",
                    version=1.1,
                    name="name",
                    duration=1.1,
                    tracks=[
                        PostApiPlaybackMotionRequestClipClipTracksItem(
                            parameter="parameter",
                            keys=[
                                PostApiPlaybackMotionRequestClipClipTracksItemKeysItem(
                                    time=1.1,
                                    value=1.1,
                                )
                            ],
                        )
                    ],
                ),
            ),
        )
        """
        _response = self._raw_client.post_api_playback_motion(request=request, request_options=request_options)
        return _response.data

    def get_api_playback_events(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            SSE latest playback state

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        response = client.get_api_playback_events()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.get_api_playback_events(request_options=request_options) as r:
            yield from r.data

    def get_api_playback(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetApiPlaybackResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiPlaybackResponse
            Transient playback state; not a render acknowledgment.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_playback()
        """
        _response = self._raw_client.get_api_playback(request_options=request_options)
        return _response.data

    def post_api_playback_parameters(
        self,
        *,
        source: str,
        sequence: int,
        values: typing.Dict[str, float],
        expected_session_id: typing.Optional[str] = OMIT,
        expected_model_version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiPlaybackParametersResponse:
        """
        Parameters
        ----------
        source : str

        sequence : int
            Strictly increasing per source. Use a new source ID for a new input session.

        values : typing.Dict[str, float]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        expected_session_id : typing.Optional[str]
            Reject when the service session differs.

        expected_model_version : typing.Optional[int]
            Reject when the loaded model version differs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiPlaybackParametersResponse
            Transient playback state; not a render acknowledgment.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.post_api_playback_parameters(
            source="source",
            sequence=1,
            values={"key": 1.1},
        )
        """
        _response = self._raw_client.post_api_playback_parameters(
            source=source,
            sequence=sequence,
            values=values,
            expected_session_id=expected_session_id,
            expected_model_version=expected_model_version,
            request_options=request_options,
        )
        return _response.data

    def post_api_playback_control(
        self,
        *,
        command: PostApiPlaybackControlRequestCommand,
        mode: typing.Optional[PostApiPlaybackControlRequestMode] = OMIT,
        x: typing.Optional[float] = OMIT,
        y: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiPlaybackControlResponse:
        """
        Parameters
        ----------
        command : PostApiPlaybackControlRequestCommand

        mode : typing.Optional[PostApiPlaybackControlRequestMode]

        x : typing.Optional[float]

        y : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiPlaybackControlResponse
            Transient playback state; not a render acknowledgment.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.post_api_playback_control(
            command="play",
        )
        """
        _response = self._raw_client.post_api_playback_control(
            command=command, mode=mode, x=x, y=y, request_options=request_options
        )
        return _response.data

    def post_api_playback_reload(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> PostApiPlaybackReloadResponse:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiPlaybackReloadResponse
            Transient playback state; not a render acknowledgment.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.post_api_playback_reload(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_api_playback_reload(request=request, request_options=request_options)
        return _response.data

    def get_api_checkpoints(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_api_checkpoints()
        """
        _response = self._raw_client.get_api_checkpoints(request_options=request_options)
        return _response.data

    def post_api_checkpoints(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.post_api_checkpoints(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_api_checkpoints(request=request, request_options=request_options)
        return _response.data

    def post_api_checkpoints_restore(
        self, *, id: str, expected_revision: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        expected_revision : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.post_api_checkpoints_restore(
            id="id",
            expected_revision="expectedRevision",
        )
        """
        _response = self._raw_client.post_api_checkpoints_restore(
            id=id, expected_revision=expected_revision, request_options=request_options
        )
        return _response.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def get_api_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_health(request_options=request_options)
        return _response.data

    async def get_api_context(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_context()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_context(request_options=request_options)
        return _response.data

    async def get_api_parts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_parts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_parts(request_options=request_options)
        return _response.data

    async def get_api_deformers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_deformers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_deformers(request_options=request_options)
        return _response.data

    async def get_api_params(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_params()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_params(request_options=request_options)
        return _response.data

    async def get_api_modeling(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_modeling()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_modeling(request_options=request_options)
        return _response.data

    async def get_api_modeling_audit(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_modeling_audit()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_modeling_audit(request_options=request_options)
        return _response.data

    async def get_api_modeling_techniques(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_modeling_techniques()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_modeling_techniques(request_options=request_options)
        return _response.data

    async def get_api_modeling_role_suggestions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_modeling_role_suggestions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_modeling_role_suggestions(request_options=request_options)
        return _response.data

    async def get_api_modeling_artmesh_presets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_modeling_artmesh_presets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_modeling_artmesh_presets(request_options=request_options)
        return _response.data

    async def get_api_rig_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_rig_summary()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_rig_summary(request_options=request_options)
        return _response.data

    async def get_api_rig_validate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_rig_validate()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_rig_validate(request_options=request_options)
        return _response.data

    async def get_api_rig_inspect(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_rig_inspect()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_rig_inspect(request_options=request_options)
        return _response.data

    async def get_api_reference(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_reference()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_reference(request_options=request_options)
        return _response.data

    async def get_api_qa_golden(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_qa_golden()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_qa_golden(request_options=request_options)
        return _response.data

    async def get_api_bundle(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_bundle()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_bundle(request_options=request_options)
        return _response.data

    async def get_api_schema(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_schema()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_schema(request_options=request_options)
        return _response.data

    async def get_api_changes(
        self, *, since: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        since : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_changes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_changes(since=since, request_options=request_options)
        return _response.data

    async def get_api_parts_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_parts_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_parts_id(id, request_options=request_options)
        return _response.data

    async def get_api_deformers_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_deformers_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_deformers_id(id, request_options=request_options)
        return _response.data

    async def get_api_rig(
        self, *, include_assets: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        include_assets : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_rig()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_rig(include_assets=include_assets, request_options=request_options)
        return _response.data

    async def put_api_rig(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        include_assets: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Disabled by default (403 legacy_write_api_disabled). Prefer /api/modeling/transaction. Explicit --allow-legacy-writes enables the legacy bypass.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        include_assets : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.put_api_rig(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_rig(
            request=request, include_assets=include_assets, request_options=request_options
        )
        return _response.data

    async def post_api_qa_check(
        self,
        *,
        poses: typing.Optional[typing.Sequence[str]] = OMIT,
        pose_samples: typing.Optional[typing.Sequence[QaCheckRequestPoseSamplesItem]] = OMIT,
        regions: typing.Optional[typing.Sequence[str]] = OMIT,
        width: typing.Optional[float] = OMIT,
        height: typing.Optional[float] = OMIT,
        physics: typing.Optional[bool] = OMIT,
        physics_time: typing.Optional[float] = OMIT,
        physics_steps: typing.Optional[float] = OMIT,
        min_coverage: typing.Optional[float] = OMIT,
        fail_on_edge_contact: typing.Optional[bool] = OMIT,
        expected_hashes: typing.Optional[typing.Dict[str, str]] = OMIT,
        check_triangle_distortion: typing.Optional[bool] = OMIT,
        max_triangle_stretch_ratio: typing.Optional[float] = OMIT,
        max_triangle_compression_ratio: typing.Optional[float] = OMIT,
        max_triangle_anisotropy: typing.Optional[float] = OMIT,
        motion_sweep: typing.Optional[QaCheckRequestMotionSweep] = OMIT,
        supersample: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        poses : typing.Optional[typing.Sequence[str]]

        pose_samples : typing.Optional[typing.Sequence[QaCheckRequestPoseSamplesItem]]

        regions : typing.Optional[typing.Sequence[str]]

        width : typing.Optional[float]

        height : typing.Optional[float]

        physics : typing.Optional[bool]

        physics_time : typing.Optional[float]

        physics_steps : typing.Optional[float]

        min_coverage : typing.Optional[float]

        fail_on_edge_contact : typing.Optional[bool]

        expected_hashes : typing.Optional[typing.Dict[str, str]]

        check_triangle_distortion : typing.Optional[bool]

        max_triangle_stretch_ratio : typing.Optional[float]

        max_triangle_compression_ratio : typing.Optional[float]

        max_triangle_anisotropy : typing.Optional[float]

        motion_sweep : typing.Optional[QaCheckRequestMotionSweep]

        supersample : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_qa_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_qa_check(
            poses=poses,
            pose_samples=pose_samples,
            regions=regions,
            width=width,
            height=height,
            physics=physics,
            physics_time=physics_time,
            physics_steps=physics_steps,
            min_coverage=min_coverage,
            fail_on_edge_contact=fail_on_edge_contact,
            expected_hashes=expected_hashes,
            check_triangle_distortion=check_triangle_distortion,
            max_triangle_stretch_ratio=max_triangle_stretch_ratio,
            max_triangle_compression_ratio=max_triangle_compression_ratio,
            max_triangle_anisotropy=max_triangle_anisotropy,
            motion_sweep=motion_sweep,
            supersample=supersample,
            request_options=request_options,
        )
        return _response.data

    async def post_api_modeling_transaction(
        self, *, request: TransactionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : TransactionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            TransactionRequestOperations,
            TransactionRequestOperationsOperationsItem,
            TransactionRequestOperationsOperationsItemAction_BlendShapeSet,
            TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Part,
            TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartTransform,
            TransactionRequestOperationsOperationsItemTarget,
            TransactionRequestOperationsQa,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_modeling_transaction(
                request=TransactionRequestOperations(
                    expected_revision="expectedRevision",
                    commit=True,
                    operations=[
                        TransactionRequestOperationsOperationsItem(
                            id="id",
                            name="name",
                            target=TransactionRequestOperationsOperationsItemTarget(),
                            action=TransactionRequestOperationsOperationsItemAction_BlendShapeSet(
                                shape=TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Part(
                                    transform=TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartTransform(),
                                    id="id",
                                    parameter="parameter",
                                    neutral_input=1.1,
                                    target_input=1.1,
                                ),
                            ),
                        )
                    ],
                    qa=TransactionRequestOperationsQa(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_modeling_transaction(
            request=request, request_options=request_options
        )
        return _response.data

    async def post_api_assets_externalize(
        self,
        *,
        rig: typing.Dict[str, typing.Any],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Disabled by default (403 legacy_write_api_disabled). Prefer /api/modeling/transaction. Explicit --allow-legacy-writes enables the legacy bypass.

        Parameters
        ----------
        rig : typing.Dict[str, typing.Any]

        dry_run : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_assets_externalize(
                rig={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_assets_externalize(
            rig=rig, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def get_api_screenshot(
        self,
        *,
        set_: typing.Optional[str] = None,
        detail: typing.Optional[str] = None,
        part_ids: typing.Optional[str] = None,
        physics: typing.Optional[str] = None,
        param_angle_x: typing.Optional[str] = None,
        param_angle_y: typing.Optional[str] = None,
        param_angle_z: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        set_ : typing.Optional[str]

        detail : typing.Optional[str]

        part_ids : typing.Optional[str]

        physics : typing.Optional[str]

        param_angle_x : typing.Optional[str]

        param_angle_y : typing.Optional[str]

        param_angle_z : typing.Optional[str]

        width : typing.Optional[str]

        height : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            PNG image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_screenshot()


        asyncio.run(main())
        """
        async with self._raw_client.get_api_screenshot(
            set_=set_,
            detail=detail,
            part_ids=part_ids,
            physics=physics,
            param_angle_x=param_angle_x,
            param_angle_y=param_angle_y,
            param_angle_z=param_angle_z,
            width=width,
            height=height,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_api_reference_sheet(
        self,
        *,
        set_: typing.Optional[str] = None,
        detail: typing.Optional[str] = None,
        part_ids: typing.Optional[str] = None,
        physics: typing.Optional[str] = None,
        param_angle_x: typing.Optional[str] = None,
        param_angle_y: typing.Optional[str] = None,
        param_angle_z: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        set_ : typing.Optional[str]

        detail : typing.Optional[str]

        part_ids : typing.Optional[str]

        physics : typing.Optional[str]

        param_angle_x : typing.Optional[str]

        param_angle_y : typing.Optional[str]

        param_angle_z : typing.Optional[str]

        width : typing.Optional[str]

        height : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            PNG image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_reference_sheet()


        asyncio.run(main())
        """
        async with self._raw_client.get_api_reference_sheet(
            set_=set_,
            detail=detail,
            part_ids=part_ids,
            physics=physics,
            param_angle_x=param_angle_x,
            param_angle_y=param_angle_y,
            param_angle_z=param_angle_z,
            width=width,
            height=height,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def post_api_qa_failure_image(
        self,
        *,
        pose_id: str,
        region: str,
        before_pose_id: typing.Optional[str] = OMIT,
        width: typing.Optional[float] = OMIT,
        height: typing.Optional[float] = OMIT,
        physics: typing.Optional[bool] = OMIT,
        values: typing.Optional[typing.Dict[str, float]] = OMIT,
        before_values: typing.Optional[typing.Dict[str, float]] = OMIT,
        physics_time: typing.Optional[float] = OMIT,
        physics_steps: typing.Optional[int] = OMIT,
        supersample: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        pose_id : str

        region : str

        before_pose_id : typing.Optional[str]

        width : typing.Optional[float]

        height : typing.Optional[float]

        physics : typing.Optional[bool]

        values : typing.Optional[typing.Dict[str, float]]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        before_values : typing.Optional[typing.Dict[str, float]]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        physics_time : typing.Optional[float]

        physics_steps : typing.Optional[int]

        supersample : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            PNG image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_qa_failure_image(
                pose_id="poseId",
                region="region",
            )


        asyncio.run(main())
        """
        async with self._raw_client.post_api_qa_failure_image(
            pose_id=pose_id,
            region=region,
            before_pose_id=before_pose_id,
            width=width,
            height=height,
            physics=physics,
            values=values,
            before_values=before_values,
            physics_time=physics_time,
            physics_steps=physics_steps,
            supersample=supersample,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def optional_bridge_connection_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.optional_bridge_connection_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.optional_bridge_connection_status(request_options=request_options)
        return _response.data

    async def optional_cubism_bridge_requires_idle_api110server(
        self, *, request: PostApiBridgePoseRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : PostApiBridgePoseRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PostApiBridgePoseRequest_SetParameterValues,
            PostApiBridgePoseRequestSetParameterValuesData,
            PostApiBridgePoseRequestSetParameterValuesDataParametersItem,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.optional_cubism_bridge_requires_idle_api110server(
                request=PostApiBridgePoseRequest_SetParameterValues(
                    data=PostApiBridgePoseRequestSetParameterValuesData(
                        model_uid="ModelUID",
                        parameters=[
                            PostApiBridgePoseRequestSetParameterValuesDataParametersItem(
                                id="Id",
                                value=1.1,
                            )
                        ],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.optional_cubism_bridge_requires_idle_api110server(
            request=request, request_options=request_options
        )
        return _response.data

    async def get_api_sample(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_sample()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_sample(request_options=request_options)
        return _response.data

    async def post_api_exports_bundle(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_exports_bundle(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_exports_bundle(request=request, request_options=request_options)
        return _response.data

    async def get_api_playback_motion(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiPlaybackMotionResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiPlaybackMotionResponse
            Motion state; GET also returns the loaded native clip or null.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_playback_motion()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_playback_motion(request_options=request_options)
        return _response.data

    async def post_api_playback_motion(
        self, *, request: PostApiPlaybackMotionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostApiPlaybackMotionResponse:
        """
        Parameters
        ----------
        request : PostApiPlaybackMotionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiPlaybackMotionResponse
            Motion state; GET also returns the loaded native clip or null.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PostApiPlaybackMotionRequestClip,
            PostApiPlaybackMotionRequestClipClip,
            PostApiPlaybackMotionRequestClipClipTracksItem,
            PostApiPlaybackMotionRequestClipClipTracksItemKeysItem,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_playback_motion(
                request=PostApiPlaybackMotionRequestClip(
                    action="load",
                    clip=PostApiPlaybackMotionRequestClipClip(
                        format="standrig-motion",
                        version=1.1,
                        name="name",
                        duration=1.1,
                        tracks=[
                            PostApiPlaybackMotionRequestClipClipTracksItem(
                                parameter="parameter",
                                keys=[
                                    PostApiPlaybackMotionRequestClipClipTracksItemKeysItem(
                                        time=1.1,
                                        value=1.1,
                                    )
                                ],
                            )
                        ],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_playback_motion(request=request, request_options=request_options)
        return _response.data

    async def get_api_playback_events(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            SSE latest playback state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            response = await client.get_api_playback_events()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.get_api_playback_events(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_api_playback(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiPlaybackResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiPlaybackResponse
            Transient playback state; not a render acknowledgment.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_playback()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_playback(request_options=request_options)
        return _response.data

    async def post_api_playback_parameters(
        self,
        *,
        source: str,
        sequence: int,
        values: typing.Dict[str, float],
        expected_session_id: typing.Optional[str] = OMIT,
        expected_model_version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiPlaybackParametersResponse:
        """
        Parameters
        ----------
        source : str

        sequence : int
            Strictly increasing per source. Use a new source ID for a new input session.

        values : typing.Dict[str, float]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        expected_session_id : typing.Optional[str]
            Reject when the service session differs.

        expected_model_version : typing.Optional[int]
            Reject when the loaded model version differs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiPlaybackParametersResponse
            Transient playback state; not a render acknowledgment.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_playback_parameters(
                source="source",
                sequence=1,
                values={"key": 1.1},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_playback_parameters(
            source=source,
            sequence=sequence,
            values=values,
            expected_session_id=expected_session_id,
            expected_model_version=expected_model_version,
            request_options=request_options,
        )
        return _response.data

    async def post_api_playback_control(
        self,
        *,
        command: PostApiPlaybackControlRequestCommand,
        mode: typing.Optional[PostApiPlaybackControlRequestMode] = OMIT,
        x: typing.Optional[float] = OMIT,
        y: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiPlaybackControlResponse:
        """
        Parameters
        ----------
        command : PostApiPlaybackControlRequestCommand

        mode : typing.Optional[PostApiPlaybackControlRequestMode]

        x : typing.Optional[float]

        y : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiPlaybackControlResponse
            Transient playback state; not a render acknowledgment.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_playback_control(
                command="play",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_playback_control(
            command=command, mode=mode, x=x, y=y, request_options=request_options
        )
        return _response.data

    async def post_api_playback_reload(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> PostApiPlaybackReloadResponse:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiPlaybackReloadResponse
            Transient playback state; not a render acknowledgment.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_playback_reload(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_playback_reload(request=request, request_options=request_options)
        return _response.data

    async def get_api_checkpoints(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_api_checkpoints()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_checkpoints(request_options=request_options)
        return _response.data

    async def post_api_checkpoints(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_checkpoints(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_checkpoints(request=request, request_options=request_options)
        return _response.data

    async def post_api_checkpoints_restore(
        self, *, id: str, expected_revision: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        expected_revision : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON result. Inspect ok, errors and commit/QA fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.post_api_checkpoints_restore(
                id="id",
                expected_revision="expectedRevision",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_checkpoints_restore(
            id=id, expected_revision=expected_revision, request_options=request_options
        )
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
