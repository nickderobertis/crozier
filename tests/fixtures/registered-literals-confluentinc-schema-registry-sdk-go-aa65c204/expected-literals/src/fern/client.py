

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.atlas_business_metadata_def import AtlasBusinessMetadataDef
from .types.atlas_entity import AtlasEntity
from .types.atlas_entity_with_ext_info import AtlasEntityWithExtInfo
from .types.business_metadata import BusinessMetadata
from .types.business_metadata_def_response import BusinessMetadataDefResponse
from .types.business_metadata_response import BusinessMetadataResponse
from .types.compatibility_check_response import CompatibilityCheckResponse
from .types.config import Config
from .types.config_update_request import ConfigUpdateRequest
from .types.create_exporter_response import CreateExporterResponse
from .types.dek import Dek
from .types.delete_dek_version_request_algorithm import DeleteDekVersionRequestAlgorithm
from .types.delete_dek_versions_request_algorithm import DeleteDekVersionsRequestAlgorithm
from .types.delete_mode_response import DeleteModeResponse
from .types.delete_subject_config_response import DeleteSubjectConfigResponse
from .types.delete_subject_mode_response import DeleteSubjectModeResponse
from .types.delete_top_level_config_response import DeleteTopLevelConfigResponse
from .types.exporter_info import ExporterInfo
from .types.exporter_status import ExporterStatus
from .types.get_dek_by_version_request_algorithm import GetDekByVersionRequestAlgorithm
from .types.get_dek_request_algorithm import GetDekRequestAlgorithm
from .types.get_dek_versions_request_algorithm import GetDekVersionsRequestAlgorithm
from .types.get_response_value import GetResponseValue
from .types.kek import Kek
from .types.mode import Mode
from .types.mode_update_request import ModeUpdateRequest
from .types.register_schema_response import RegisterSchemaResponse
from .types.schema import Schema
from .types.schema_string import SchemaString
from .types.search_result import SearchResult
from .types.search_using_attribute_request_sort_order import SearchUsingAttributeRequestSortOrder
from .types.search_using_attribute_request_time_range_type import SearchUsingAttributeRequestTimeRangeType
from .types.search_using_basic_request_sort_order import SearchUsingBasicRequestSortOrder
from .types.search_using_basic_request_time_range_type import SearchUsingBasicRequestTimeRangeType
from .types.server_cluster_id import ServerClusterId
from .types.subject_version import SubjectVersion
from .types.tag import Tag
from .types.tag_def import TagDef
from .types.tag_def_response import TagDefResponse
from .types.tag_response import TagResponse
from .types.undelete_dek_version_request_algorithm import UndeleteDekVersionRequestAlgorithm
from .types.undelete_dek_versions_request_algorithm import UndeleteDekVersionsRequestAlgorithm
from .types.update_exporter_response import UpdateExporterResponse


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

    def get_dek_subjects(
        self,
        name: str,
        *,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of dek subjects

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_dek_subjects(
            name="name",
        )
        """
        _response = self._raw_client.get_dek_subjects(name, deleted=deleted, request_options=request_options)
        return _response.data

    def create_dek(
        self,
        name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dek:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dek
            The create response
        """
        _response = self._raw_client.create_dek(name, request=request, request_options=request_options)
        return _response.data

    def get_kek_names(
        self, *, deleted: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of kek names

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_kek_names()
        """
        _response = self._raw_client.get_kek_names(deleted=deleted, request_options=request_options)
        return _response.data

    def create_kek(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Kek:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Kek
            The create response
        """
        _response = self._raw_client.create_kek(request=request, request_options=request_options)
        return _response.data

    def get_kek(
        self,
        name: str,
        *,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Kek:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Kek
            The kek info

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_kek(
            name="name",
        )
        """
        _response = self._raw_client.get_kek(name, deleted=deleted, request_options=request_options)
        return _response.data

    def put_kek(
        self,
        name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Kek:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Kek
            The update response
        """
        _response = self._raw_client.put_kek(name, request=request, request_options=request_options)
        return _response.data

    def delete_kek(
        self,
        name: str,
        *,
        permanent: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        permanent : typing.Optional[bool]
            Whether to perform a permanent delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_kek(
            name="name",
        )
        """
        _response = self._raw_client.delete_kek(name, permanent=permanent, request_options=request_options)
        return _response.data

    def get_dek(
        self,
        name: str,
        subject: str,
        *,
        algorithm: typing.Optional[GetDekRequestAlgorithm] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dek:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        algorithm : typing.Optional[GetDekRequestAlgorithm]
            Algorithm of the dek

        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dek
            The dek info

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_dek(
            name="name",
            subject="subject",
        )
        """
        _response = self._raw_client.get_dek(
            name, subject, algorithm=algorithm, deleted=deleted, request_options=request_options
        )
        return _response.data

    def delete_dek_versions(
        self,
        name: str,
        subject: str,
        *,
        algorithm: typing.Optional[DeleteDekVersionsRequestAlgorithm] = None,
        permanent: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        algorithm : typing.Optional[DeleteDekVersionsRequestAlgorithm]
            Algorithm of the dek

        permanent : typing.Optional[bool]
            Whether to perform a permanent delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_dek_versions(
            name="name",
            subject="subject",
        )
        """
        _response = self._raw_client.delete_dek_versions(
            name, subject, algorithm=algorithm, permanent=permanent, request_options=request_options
        )
        return _response.data

    def get_dek_by_version(
        self,
        name: str,
        subject: str,
        version: str,
        *,
        algorithm: typing.Optional[GetDekByVersionRequestAlgorithm] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dek:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        version : str
            Version of the dek

        algorithm : typing.Optional[GetDekByVersionRequestAlgorithm]
            Algorithm of the dek

        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dek
            The dek info

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_dek_by_version(
            name="name",
            subject="subject",
            version="version",
        )
        """
        _response = self._raw_client.get_dek_by_version(
            name, subject, version, algorithm=algorithm, deleted=deleted, request_options=request_options
        )
        return _response.data

    def delete_dek_version(
        self,
        name: str,
        subject: str,
        version: str,
        *,
        algorithm: typing.Optional[DeleteDekVersionRequestAlgorithm] = None,
        permanent: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        version : str
            Version of the dek

        algorithm : typing.Optional[DeleteDekVersionRequestAlgorithm]
            Algorithm of the dek

        permanent : typing.Optional[bool]
            Whether to perform a permanent delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_dek_version(
            name="name",
            subject="subject",
            version="version",
        )
        """
        _response = self._raw_client.delete_dek_version(
            name, subject, version, algorithm=algorithm, permanent=permanent, request_options=request_options
        )
        return _response.data

    def get_dek_versions(
        self,
        name: str,
        subject: str,
        *,
        algorithm: typing.Optional[GetDekVersionsRequestAlgorithm] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[int]:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        algorithm : typing.Optional[GetDekVersionsRequestAlgorithm]
            Algorithm of the dek

        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            List of version numbers for dek

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_dek_versions(
            name="name",
            subject="subject",
        )
        """
        _response = self._raw_client.get_dek_versions(
            name, subject, algorithm=algorithm, deleted=deleted, request_options=request_options
        )
        return _response.data

    def undelete_dek_version(
        self,
        name: str,
        subject: str,
        version: str,
        *,
        algorithm: typing.Optional[UndeleteDekVersionRequestAlgorithm] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        version : str
            Version of the dek

        algorithm : typing.Optional[UndeleteDekVersionRequestAlgorithm]
            Algorithm of the dek

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.undelete_dek_version(
            name="name",
            subject="subject",
            version="version",
        )
        """
        _response = self._raw_client.undelete_dek_version(
            name, subject, version, algorithm=algorithm, request_options=request_options
        )
        return _response.data

    def undelete_dek_versions(
        self,
        name: str,
        subject: str,
        *,
        algorithm: typing.Optional[UndeleteDekVersionsRequestAlgorithm] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        algorithm : typing.Optional[UndeleteDekVersionsRequestAlgorithm]
            Algorithm of the dek

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.undelete_dek_versions(
            name="name",
            subject="subject",
        )
        """
        _response = self._raw_client.undelete_dek_versions(
            name, subject, algorithm=algorithm, request_options=request_options
        )
        return _response.data

    def undelete_kek(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.undelete_kek(
            name="name",
        )
        """
        _response = self._raw_client.undelete_kek(name, request_options=request_options)
        return _response.data

    def create_business_metadata(
        self, *, request: typing.Sequence[BusinessMetadata], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BusinessMetadataResponse]:
        """
        Bulk API to create multiple business metadata.

        Parameters
        ----------
        request : typing.Sequence[BusinessMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataResponse]
            The business metadata. Errored business metadata will have an additional error property.

        Examples
        --------
        from fern import BusinessMetadata, FernApi

        client = FernApi()
        client.create_business_metadata(
            request=[
                BusinessMetadata(
                    type_name="typeName",
                    attributes={"key": "{}"},
                    entity_type="entityType",
                    entity_name="entityName",
                )
            ],
        )
        """
        _response = self._raw_client.create_business_metadata(request=request, request_options=request_options)
        return _response.data

    def update_business_metadata(
        self, *, request: typing.Sequence[BusinessMetadata], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BusinessMetadataResponse]:
        """
        Bulk API to update multiple business metadata.

        Parameters
        ----------
        request : typing.Sequence[BusinessMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataResponse]
            The business metadata. Errored business metadata will have an additional error property.

        Examples
        --------
        from fern import BusinessMetadata, FernApi

        client = FernApi()
        client.update_business_metadata(
            request=[
                BusinessMetadata(
                    type_name="typeName",
                    attributes={"key": "{}"},
                    entity_type="entityType",
                    entity_name="entityName",
                )
            ],
        )
        """
        _response = self._raw_client.update_business_metadata(request=request, request_options=request_options)
        return _response.data

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, GetResponseValue]:
        """
        The Root resource is a no-op.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, GetResponseValue]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get()
        """
        _response = self._raw_client.get(request_options=request_options)
        return _response.data

    def post(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.post()
        """
        _response = self._raw_client.post(request_options=request_options)
        return _response.data

    def test_compatibility_for_subject(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        verbose: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompatibilityCheckResponse:
        """
        the compatibility level applied for the check is the configured compatibility level for the subject (http:get:: /config/(string: subject)). If this subject's compatibility level was never changed, then the global compatibility level applies (http:get:: /config).

        Parameters
        ----------
        subject : str
            Subject of the schema version against which compatibility is to be tested

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        verbose : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompatibilityCheckResponse
            successful operation
        """
        _response = self._raw_client.test_compatibility_for_subject(
            subject, request=request, verbose=verbose, request_options=request_options
        )
        return _response.data

    def test_compatibility_by_subject_name(
        self,
        subject: str,
        version: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        verbose: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompatibilityCheckResponse:
        """
        the compatibility level applied for the check is the configured compatibility level for the subject (http:get:: /config/(string: subject)). If this subject's compatibility level was never changed, then the global compatibility level applies (http:get:: /config).

        Parameters
        ----------
        subject : str
            Subject of the schema version against which compatibility is to be tested

        version : str
            Version of the subject's schema against which compatibility is to be tested. Valid values for versionId are between [1,2^31-1] or the string "latest"."latest" checks compatibility of the input schema with the last registered schema under the specified subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        verbose : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompatibilityCheckResponse
            successful operation
        """
        _response = self._raw_client.test_compatibility_by_subject_name(
            subject, version, request=request, verbose=verbose, request_options=request_options
        )
        return _response.data

    def get_top_level_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> Config:
        """
        Retrieves the global compatibility level.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            The global compatibility level.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_top_level_config()
        """
        _response = self._raw_client.get_top_level_config(request_options=request_options)
        return _response.data

    def update_top_level_config(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConfigUpdateRequest:
        """
        Updates the global compatibility level. On success, echoes the original request back to the client.

        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigUpdateRequest
            The original request.
        """
        _response = self._raw_client.update_top_level_config(request=request, request_options=request_options)
        return _response.data

    def delete_top_level_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTopLevelConfigResponse:
        """
        Deletes the global compatibility level config and reverts to the default.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTopLevelConfigResponse
            Operation succeeded. Returns old global compatibility level.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_top_level_config()
        """
        _response = self._raw_client.delete_top_level_config(request_options=request_options)
        return _response.data

    def get_subject_level_config(
        self,
        subject: str,
        *,
        default_to_global: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Config:
        """
        Parameters
        ----------
        subject : str

        default_to_global : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_subject_level_config(
            subject="subject",
        )
        """
        _response = self._raw_client.get_subject_level_config(
            subject, default_to_global=default_to_global, request_options=request_options
        )
        return _response.data

    def update_subject_level_config(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConfigUpdateRequest:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigUpdateRequest
            successful operation
        """
        _response = self._raw_client.update_subject_level_config(
            subject, request=request, request_options=request_options
        )
        return _response.data

    def delete_subject_config(
        self, subject: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSubjectConfigResponse:
        """
        Parameters
        ----------
        subject : str
            the name of the subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSubjectConfigResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_subject_config(
            subject="subject",
        )
        """
        _response = self._raw_client.delete_subject_config(subject, request_options=request_options)
        return _response.data

    def list_contexts(
        self, *, context_prefix: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        context_prefix : typing.Optional[str]
            prefix to filter contexts

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_contexts()
        """
        _response = self._raw_client.list_contexts(context_prefix=context_prefix, request_options=request_options)
        return _response.data

    def get_top_level_mode(self, *, request_options: typing.Optional[RequestOptions] = None) -> Mode:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Mode
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_top_level_mode()
        """
        _response = self._raw_client.get_top_level_mode(request_options=request_options)
        return _response.data

    def update_top_level_mode(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModeUpdateRequest:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModeUpdateRequest
            successful operation
        """
        _response = self._raw_client.update_top_level_mode(request=request, request_options=request_options)
        return _response.data

    def delete_mode(
        self, *, recursive: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteModeResponse:
        """
        Parameters
        ----------
        recursive : typing.Optional[bool]
            recursive delete mode across all subjects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteModeResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_mode()
        """
        _response = self._raw_client.delete_mode(recursive=recursive, request_options=request_options)
        return _response.data

    def get_mode(
        self,
        subject: str,
        *,
        default_to_global: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Mode:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        default_to_global : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Mode
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_mode(
            subject="subject",
        )
        """
        _response = self._raw_client.get_mode(
            subject, default_to_global=default_to_global, request_options=request_options
        )
        return _response.data

    def update_mode(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModeUpdateRequest:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModeUpdateRequest
            successful operation
        """
        _response = self._raw_client.update_mode(subject, request=request, request_options=request_options)
        return _response.data

    def delete_subject_mode(
        self,
        subject: str,
        *,
        recursive: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteSubjectModeResponse:
        """
        Parameters
        ----------
        subject : str
            the name of the subject

        recursive : typing.Optional[bool]
            recursive delete mode for all subjects under the context if subject parameter is a context

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSubjectModeResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_subject_mode(
            subject="subject",
        )
        """
        _response = self._raw_client.delete_subject_mode(subject, recursive=recursive, request_options=request_options)
        return _response.data

    def get_schemas(
        self,
        *,
        subject_prefix: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        latest_only: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Parameters
        ----------
        subject_prefix : typing.Optional[str]

        deleted : typing.Optional[bool]

        latest_only : typing.Optional[bool]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_schemas()
        """
        _response = self._raw_client.get_schemas(
            subject_prefix=subject_prefix,
            deleted=deleted,
            latest_only=latest_only,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def get_schema(
        self,
        id: int,
        *,
        subject: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        fetch_max_id: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchemaString:
        """
        Parameters
        ----------
        id : int
            Globally unique identifier of the schema

        subject : typing.Optional[str]

        format : typing.Optional[str]

        fetch_max_id : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaString
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_schema(
            id=1,
        )
        """
        _response = self._raw_client.get_schema(
            id, subject=subject, format=format, fetch_max_id=fetch_max_id, request_options=request_options
        )
        return _response.data

    def get_subjects(
        self,
        id: int,
        *,
        subject: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        id : int
            Globally unique identifier of the schema

        subject : typing.Optional[str]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_subjects(
            id=1,
        )
        """
        _response = self._raw_client.get_subjects(id, subject=subject, deleted=deleted, request_options=request_options)
        return _response.data

    def get_versions(
        self,
        id: int,
        *,
        subject: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SubjectVersion]:
        """
        Parameters
        ----------
        id : int
            Globally unique identifier of the schema

        subject : typing.Optional[str]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SubjectVersion]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_versions(
            id=1,
        )
        """
        _response = self._raw_client.get_versions(id, subject=subject, deleted=deleted, request_options=request_options)
        return _response.data

    def get_schema_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_schema_types()
        """
        _response = self._raw_client.get_schema_types(request_options=request_options)
        return _response.data

    def list(
        self,
        *,
        subject_prefix: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        deleted_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        subject_prefix : typing.Optional[str]

        deleted : typing.Optional[bool]

        deleted_only : typing.Optional[bool]
            Whether to return deleted subjects only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list()
        """
        _response = self._raw_client.list(
            subject_prefix=subject_prefix, deleted=deleted, deleted_only=deleted_only, request_options=request_options
        )
        return _response.data

    def look_up_schema_under_subject(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        format: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subject : str
            Subject under which the schema will be registered

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        format : typing.Optional[str]
            Desired output format, dependent on schema type

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = self._raw_client.look_up_schema_under_subject(
            subject, request=request, format=format, deleted=deleted, request_options=request_options
        )
        return _response.data

    def delete_subject(
        self,
        subject: str,
        *,
        permanent: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[int]:
        """
        Parameters
        ----------
        subject : str
            the name of the subject

        permanent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_subject(
            subject="subject",
        )
        """
        _response = self._raw_client.delete_subject(subject, permanent=permanent, request_options=request_options)
        return _response.data

    def list_versions(
        self,
        subject: str,
        *,
        deleted: typing.Optional[bool] = None,
        deleted_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[int]:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        deleted : typing.Optional[bool]

        deleted_only : typing.Optional[bool]
            Whether to return deleted schemas only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_versions(
            subject="subject",
        )
        """
        _response = self._raw_client.list_versions(
            subject, deleted=deleted, deleted_only=deleted_only, request_options=request_options
        )
        return _response.data

    def register(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        normalize: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegisterSchemaResponse:
        """
        Register a new schema under the specified subject. If successfully registered, this returns the unique identifier of this schema in the registry. The returned identifier should be used to retrieve this schema from the schemas resource and is different from the schema's version which is associated with the subject. If the same schema is registered under a different subject, the same identifier will be returned. However, the version of the schema may be different under different subjects.
        A schema should be compatible with the previously registered schema or schemas (if there are any) as per the configured compatibility level. The configured compatibility level can be obtained by issuing a GET http:get:: /config/(string: subject). If that returns null, then GET http:get:: /config
        When there are multiple instances of Schema Registry running in the same cluster, the schema registration request will be forwarded to one of the instances designated as the primary. If the primary is not available, the client will get an error code indicating that the forwarding has failed.

        Parameters
        ----------
        subject : str
            Name of the subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        normalize : typing.Optional[bool]
            Whether to register the normalized schema

        format : typing.Optional[str]
            Desired output format, dependent on schema type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterSchemaResponse
            successful operation
        """
        _response = self._raw_client.register(
            subject, request=request, normalize=normalize, format=format, request_options=request_options
        )
        return _response.data

    def get_schema_by_version(
        self,
        subject: str,
        version: str,
        *,
        format: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Schema:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        version : str
            Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.

        format : typing.Optional[str]
            Desired output format, dependent on schema type

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schema
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_schema_by_version(
            subject="subject",
            version="version",
        )
        """
        _response = self._raw_client.get_schema_by_version(
            subject, version, format=format, deleted=deleted, request_options=request_options
        )
        return _response.data

    def delete_schema_version(
        self,
        subject: str,
        version: str,
        *,
        permanent: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        version : str
            Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.

        permanent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_schema_version(
            subject="subject",
            version="version",
        )
        """
        _response = self._raw_client.delete_schema_version(
            subject, version, permanent=permanent, request_options=request_options
        )
        return _response.data

    def get_referenced_by(
        self, subject: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        version : str
            Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_referenced_by(
            subject="subject",
            version="version",
        )
        """
        _response = self._raw_client.get_referenced_by(subject, version, request_options=request_options)
        return _response.data

    def get_schema_only(
        self,
        subject: str,
        version: str,
        *,
        format: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        version : str
            Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.

        format : typing.Optional[str]
            Desired output format, dependent on schema type

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_schema_only(
            subject="subject",
            version="version",
        )
        """
        _response = self._raw_client.get_schema_only(
            subject, version, format=format, deleted=deleted, request_options=request_options
        )
        return _response.data

    def get_cluster_id(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServerClusterId:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServerClusterId
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_cluster_id()
        """
        _response = self._raw_client.get_cluster_id(request_options=request_options)
        return _response.data

    def get_exporters(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_exporters()
        """
        _response = self._raw_client.get_exporters(request_options=request_options)
        return _response.data

    def create_exporter(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateExporterResponse:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateExporterResponse
            successful operation
        """
        _response = self._raw_client.create_exporter(request=request, request_options=request_options)
        return _response.data

    def get_exporter_info(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ExporterInfo:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExporterInfo
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_exporter_info(
            name="name",
        )
        """
        _response = self._raw_client.get_exporter_info(name, request_options=request_options)
        return _response.data

    def put_exporter(
        self,
        name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateExporterResponse:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExporterResponse
            successful operation
        """
        _response = self._raw_client.put_exporter(name, request=request, request_options=request_options)
        return _response.data

    def delete_exporter(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_exporter(
            name="name",
        )
        """
        _response = self._raw_client.delete_exporter(name, request_options=request_options)
        return _response.data

    def get_exporter_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_exporter_config(
            name="name",
        )
        """
        _response = self._raw_client.get_exporter_config(name, request_options=request_options)
        return _response.data

    def put_exporter_config(
        self,
        name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateExporterResponse:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExporterResponse
            successful operation
        """
        _response = self._raw_client.put_exporter_config(name, request=request, request_options=request_options)
        return _response.data

    def get_exporter_cluster_link_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_exporter_cluster_link_config(
            name="name",
        )
        """
        _response = self._raw_client.get_exporter_cluster_link_config(name, request_options=request_options)
        return _response.data

    def pause_exporter(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateExporterResponse:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExporterResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.pause_exporter(
            name="name",
        )
        """
        _response = self._raw_client.pause_exporter(name, request_options=request_options)
        return _response.data

    def reset_exporter(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateExporterResponse:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExporterResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reset_exporter(
            name="name",
        )
        """
        _response = self._raw_client.reset_exporter(name, request_options=request_options)
        return _response.data

    def resume_exporter(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateExporterResponse:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExporterResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.resume_exporter(
            name="name",
        )
        """
        _response = self._raw_client.resume_exporter(name, request_options=request_options)
        return _response.data

    def get_exporter_status(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExporterStatus:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExporterStatus
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_exporter_status(
            name="name",
        )
        """
        _response = self._raw_client.get_exporter_status(name, request_options=request_options)
        return _response.data

    def create_tags(
        self, *, request: typing.Sequence[Tag], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagResponse]:
        """
        Bulk API to create multiple tags.

        Parameters
        ----------
        request : typing.Sequence[Tag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagResponse]
            The tags. Errored tags will have an additional error property.

        Examples
        --------
        from fern import FernApi, Tag, TimeBoundary

        client = FernApi()
        client.create_tags(
            request=[
                Tag(
                    type_name="typeName",
                    attributes={"key": {"key": "value"}},
                    entity_guid="entityGuid",
                    entity_status="ACTIVE",
                    propagate=True,
                    validity_periods=[
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        ),
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        ),
                    ],
                    remove_propagations_on_entity_delete=True,
                    entity_type="entityType",
                    entity_name="entityName",
                )
            ],
        )
        """
        _response = self._raw_client.create_tags(request=request, request_options=request_options)
        return _response.data

    def update_tags(
        self, *, request: typing.Sequence[Tag], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagResponse]:
        """
        Bulk API to update multiple tags.

        Parameters
        ----------
        request : typing.Sequence[Tag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagResponse]
            The tags. Errored tags will have an additional error property.

        Examples
        --------
        from fern import FernApi, Tag, TimeBoundary

        client = FernApi()
        client.update_tags(
            request=[
                Tag(
                    type_name="typeName",
                    attributes={"key": {"key": "value"}},
                    entity_guid="entityGuid",
                    entity_status="ACTIVE",
                    propagate=True,
                    validity_periods=[
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        ),
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        ),
                    ],
                    remove_propagations_on_entity_delete=True,
                    entity_type="entityType",
                    entity_name="entityName",
                )
            ],
        )
        """
        _response = self._raw_client.update_tags(request=request, request_options=request_options)
        return _response.data

    def delete_business_metadata(
        self,
        type_name: str,
        qualified_name: str,
        bm_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a business metadata on an entity.

        Parameters
        ----------
        type_name : str
            The type of the entity

        qualified_name : str
            The qualified name of the entity

        bm_name : str
            The name of the business metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_business_metadata(
            type_name="typeName",
            qualified_name="qualifiedName",
            bm_name="bmName",
        )
        """
        _response = self._raw_client.delete_business_metadata(
            type_name, qualified_name, bm_name, request_options=request_options
        )
        return _response.data

    def delete_tag(
        self,
        type_name: str,
        qualified_name: str,
        tag_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a tag on an entity.

        Parameters
        ----------
        type_name : str
            The type of the entity

        qualified_name : str
            The qualified name of the entity

        tag_name : str
            The name of the tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_tag(
            type_name="typeName",
            qualified_name="qualifiedName",
            tag_name="tagName",
        )
        """
        _response = self._raw_client.delete_tag(type_name, qualified_name, tag_name, request_options=request_options)
        return _response.data

    def get_business_metadata(
        self, type_name: str, qualified_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BusinessMetadataResponse]:
        """
        Gets the list of business metadata for a given entity represented by a qualified name.

        Parameters
        ----------
        type_name : str
            The type of the entity

        qualified_name : str
            The qualified name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataResponse]
            The business metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_business_metadata(
            type_name="typeName",
            qualified_name="qualifiedName",
        )
        """
        _response = self._raw_client.get_business_metadata(type_name, qualified_name, request_options=request_options)
        return _response.data

    def get_by_unique_attributes(
        self,
        type_name: str,
        qualified_name: str,
        *,
        min_ext_info: typing.Optional[bool] = None,
        ignore_relationships: typing.Optional[bool] = None,
        include_internal_prefix: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtlasEntityWithExtInfo:
        """
        Fetch complete definition of an entity given its type and unique attribute.

        Parameters
        ----------
        type_name : str
            The type of the entity

        qualified_name : str
            The qualified name of the entity

        min_ext_info : typing.Optional[bool]
            Whether to only populate header and schema attributes

        ignore_relationships : typing.Optional[bool]
            Whether to ignore relationships

        include_internal_prefix : typing.Optional[str]
            If not null, include internal attributes that start with this prefix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtlasEntityWithExtInfo
            The entity

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_by_unique_attributes(
            type_name="typeName",
            qualified_name="qualifiedName",
        )
        """
        _response = self._raw_client.get_by_unique_attributes(
            type_name,
            qualified_name,
            min_ext_info=min_ext_info,
            ignore_relationships=ignore_relationships,
            include_internal_prefix=include_internal_prefix,
            request_options=request_options,
        )
        return _response.data

    def delete_by_unique_attributes(
        self, type_name: str, qualified_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        type_name : str

        qualified_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_by_unique_attributes(
            type_name="typeName",
            qualified_name="qualifiedName",
        )
        """
        _response = self._raw_client.delete_by_unique_attributes(
            type_name, qualified_name, request_options=request_options
        )
        return _response.data

    def get_tags(
        self, type_name: str, qualified_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagResponse]:
        """
        Gets the list of classifications for a given entity represented by a qualifed name.

        Parameters
        ----------
        type_name : str
            The type of the entity

        qualified_name : str
            The qualified name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagResponse]
            The tags

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_tags(
            type_name="typeName",
            qualified_name="qualifiedName",
        )
        """
        _response = self._raw_client.get_tags(type_name, qualified_name, request_options=request_options)
        return _response.data

    def create_or_update(
        self,
        *,
        referred_entities: typing.Optional[typing.Dict[str, AtlasEntity]] = OMIT,
        entity: typing.Optional[AtlasEntity] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        referred_entities : typing.Optional[typing.Dict[str, AtlasEntity]]

        entity : typing.Optional[AtlasEntity]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            default response

        Examples
        --------
        from fern import (
            AtlasClassification,
            AtlasEntity,
            AtlasTermAssignmentHeader,
            FernApi,
            TimeBoundary,
        )

        client = FernApi()
        client.create_or_update(
            referred_entities={
                "key": AtlasEntity(
                    type_name="typeName",
                    attributes={"key": "{}"},
                    guid="guid",
                    home_id="homeId",
                    is_proxy=True,
                    is_incomplete=True,
                    provenance_type=0,
                    status="ACTIVE",
                    created_by="createdBy",
                    updated_by="updatedBy",
                    create_time=1000000,
                    update_time=1000000,
                    version=6,
                    relationship_attributes={"key": "{}"},
                    classifications=[
                        AtlasClassification(
                            type_name="typeName",
                            attributes={"key": {"key": "value"}},
                            entity_guid="entityGuid",
                            entity_status="ACTIVE",
                            propagate=True,
                            validity_periods=[
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                            ],
                            remove_propagations_on_entity_delete=True,
                        ),
                        AtlasClassification(
                            type_name="typeName",
                            attributes={"key": {"key": "value"}},
                            entity_guid="entityGuid",
                            entity_status="ACTIVE",
                            propagate=True,
                            validity_periods=[
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                            ],
                            remove_propagations_on_entity_delete=True,
                        ),
                    ],
                    meanings=[
                        AtlasTermAssignmentHeader(
                            term_guid="termGuid",
                            relation_guid="relationGuid",
                            description="description",
                            display_text="displayText",
                            expression="expression",
                            created_by="createdBy",
                            steward="steward",
                            source="source",
                            confidence=1,
                            status="DISCOVERED",
                        ),
                        AtlasTermAssignmentHeader(
                            term_guid="termGuid",
                            relation_guid="relationGuid",
                            description="description",
                            display_text="displayText",
                            expression="expression",
                            created_by="createdBy",
                            steward="steward",
                            source="source",
                            confidence=1,
                            status="DISCOVERED",
                        ),
                    ],
                    custom_attributes={"key": "customAttributes"},
                    business_attributes={"key": {"key": "{}"}},
                    labels=["labels", "labels"],
                    pending_tasks=["pendingTasks", "pendingTasks"],
                    proxy=True,
                )
            },
            entity=AtlasEntity(
                type_name="typeName",
                attributes={"key": "{}"},
                guid="guid",
                home_id="homeId",
                is_proxy=True,
                is_incomplete=True,
                provenance_type=0,
                status="ACTIVE",
                created_by="createdBy",
                updated_by="updatedBy",
                create_time=1000000,
                update_time=1000000,
                version=6,
                relationship_attributes={"key": "{}"},
                classifications=[
                    AtlasClassification(
                        type_name="typeName",
                        attributes={"key": {"key": "value"}},
                        entity_guid="entityGuid",
                        entity_status="ACTIVE",
                        propagate=True,
                        validity_periods=[
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                        ],
                        remove_propagations_on_entity_delete=True,
                    ),
                    AtlasClassification(
                        type_name="typeName",
                        attributes={"key": {"key": "value"}},
                        entity_guid="entityGuid",
                        entity_status="ACTIVE",
                        propagate=True,
                        validity_periods=[
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                        ],
                        remove_propagations_on_entity_delete=True,
                    ),
                ],
                meanings=[
                    AtlasTermAssignmentHeader(
                        term_guid="termGuid",
                        relation_guid="relationGuid",
                        description="description",
                        display_text="displayText",
                        expression="expression",
                        created_by="createdBy",
                        steward="steward",
                        source="source",
                        confidence=1,
                        status="DISCOVERED",
                    ),
                    AtlasTermAssignmentHeader(
                        term_guid="termGuid",
                        relation_guid="relationGuid",
                        description="description",
                        display_text="displayText",
                        expression="expression",
                        created_by="createdBy",
                        steward="steward",
                        source="source",
                        confidence=1,
                        status="DISCOVERED",
                    ),
                ],
                custom_attributes={"key": "customAttributes"},
                business_attributes={"key": {"key": "{}"}},
                labels=["labels", "labels"],
                pending_tasks=["pendingTasks", "pendingTasks"],
                proxy=True,
            ),
        )
        """
        _response = self._raw_client.create_or_update(
            referred_entities=referred_entities, entity=entity, request_options=request_options
        )
        return _response.data

    def partial_update_by_unique_attributes(
        self,
        *,
        referred_entities: typing.Optional[typing.Dict[str, AtlasEntity]] = OMIT,
        entity: typing.Optional[AtlasEntity] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        referred_entities : typing.Optional[typing.Dict[str, AtlasEntity]]

        entity : typing.Optional[AtlasEntity]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            default response

        Examples
        --------
        from fern import (
            AtlasClassification,
            AtlasEntity,
            AtlasTermAssignmentHeader,
            FernApi,
            TimeBoundary,
        )

        client = FernApi()
        client.partial_update_by_unique_attributes(
            referred_entities={
                "key": AtlasEntity(
                    type_name="typeName",
                    attributes={"key": "{}"},
                    guid="guid",
                    home_id="homeId",
                    is_proxy=True,
                    is_incomplete=True,
                    provenance_type=0,
                    status="ACTIVE",
                    created_by="createdBy",
                    updated_by="updatedBy",
                    create_time=1000000,
                    update_time=1000000,
                    version=6,
                    relationship_attributes={"key": "{}"},
                    classifications=[
                        AtlasClassification(
                            type_name="typeName",
                            attributes={"key": {"key": "value"}},
                            entity_guid="entityGuid",
                            entity_status="ACTIVE",
                            propagate=True,
                            validity_periods=[
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                            ],
                            remove_propagations_on_entity_delete=True,
                        ),
                        AtlasClassification(
                            type_name="typeName",
                            attributes={"key": {"key": "value"}},
                            entity_guid="entityGuid",
                            entity_status="ACTIVE",
                            propagate=True,
                            validity_periods=[
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                            ],
                            remove_propagations_on_entity_delete=True,
                        ),
                    ],
                    meanings=[
                        AtlasTermAssignmentHeader(
                            term_guid="termGuid",
                            relation_guid="relationGuid",
                            description="description",
                            display_text="displayText",
                            expression="expression",
                            created_by="createdBy",
                            steward="steward",
                            source="source",
                            confidence=1,
                            status="DISCOVERED",
                        ),
                        AtlasTermAssignmentHeader(
                            term_guid="termGuid",
                            relation_guid="relationGuid",
                            description="description",
                            display_text="displayText",
                            expression="expression",
                            created_by="createdBy",
                            steward="steward",
                            source="source",
                            confidence=1,
                            status="DISCOVERED",
                        ),
                    ],
                    custom_attributes={"key": "customAttributes"},
                    business_attributes={"key": {"key": "{}"}},
                    labels=["labels", "labels"],
                    pending_tasks=["pendingTasks", "pendingTasks"],
                    proxy=True,
                )
            },
            entity=AtlasEntity(
                type_name="typeName",
                attributes={"key": "{}"},
                guid="guid",
                home_id="homeId",
                is_proxy=True,
                is_incomplete=True,
                provenance_type=0,
                status="ACTIVE",
                created_by="createdBy",
                updated_by="updatedBy",
                create_time=1000000,
                update_time=1000000,
                version=6,
                relationship_attributes={"key": "{}"},
                classifications=[
                    AtlasClassification(
                        type_name="typeName",
                        attributes={"key": {"key": "value"}},
                        entity_guid="entityGuid",
                        entity_status="ACTIVE",
                        propagate=True,
                        validity_periods=[
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                        ],
                        remove_propagations_on_entity_delete=True,
                    ),
                    AtlasClassification(
                        type_name="typeName",
                        attributes={"key": {"key": "value"}},
                        entity_guid="entityGuid",
                        entity_status="ACTIVE",
                        propagate=True,
                        validity_periods=[
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                        ],
                        remove_propagations_on_entity_delete=True,
                    ),
                ],
                meanings=[
                    AtlasTermAssignmentHeader(
                        term_guid="termGuid",
                        relation_guid="relationGuid",
                        description="description",
                        display_text="displayText",
                        expression="expression",
                        created_by="createdBy",
                        steward="steward",
                        source="source",
                        confidence=1,
                        status="DISCOVERED",
                    ),
                    AtlasTermAssignmentHeader(
                        term_guid="termGuid",
                        relation_guid="relationGuid",
                        description="description",
                        display_text="displayText",
                        expression="expression",
                        created_by="createdBy",
                        steward="steward",
                        source="source",
                        confidence=1,
                        status="DISCOVERED",
                    ),
                ],
                custom_attributes={"key": "customAttributes"},
                business_attributes={"key": {"key": "{}"}},
                labels=["labels", "labels"],
                pending_tasks=["pendingTasks", "pendingTasks"],
                proxy=True,
            ),
        )
        """
        _response = self._raw_client.partial_update_by_unique_attributes(
            referred_entities=referred_entities, entity=entity, request_options=request_options
        )
        return _response.data

    def search_using_attribute(
        self,
        *,
        type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        types: typing.Optional[str] = None,
        attr: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        attrs: typing.Optional[str] = None,
        attr_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        attr_value_prefix: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        time_range_type: typing.Optional[SearchUsingAttributeRequestTimeRangeType] = None,
        time_range_attr: typing.Optional[str] = None,
        time_range_start: typing.Optional[int] = None,
        time_range_end: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[SearchUsingAttributeRequestSortOrder] = None,
        deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResult:
        """
        Retrieve data for the specified attribute search query.

        Parameters
        ----------
        type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the result to only entities of specified types

        types : typing.Optional[str]

        attr : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One of more additional attributes to return in the response

        attrs : typing.Optional[str]

        attr_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The attribute to search

        attr_value_prefix : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The prefix for the attribute value to search

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the result to only entities tagged with the given tag

        time_range_type : typing.Optional[SearchUsingAttributeRequestTimeRangeType]
            The type of time range search, default is CUSTOM

        time_range_attr : typing.Optional[str]
            The attribute for a time range search

        time_range_start : typing.Optional[int]
            The start for a custom time range search in ms since the epoch

        time_range_end : typing.Optional[int]
            The end for a custom time range search in ms since the epoch

        sort_by : typing.Optional[str]
            An attribute to sort by

        sort_order : typing.Optional[SearchUsingAttributeRequestSortOrder]
            Sort order, either ASCENDING (default) or DESCENDING

        deleted : typing.Optional[bool]
            Whether to include deleted entities

        limit : typing.Optional[int]
            Limit the result set to only include the specified number of entries

        offset : typing.Optional[int]
            Start offset of the result set (useful for pagination)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResult
            On successful search query with some results, might return an empty list if execution succeeded without any results

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.search_using_attribute()
        """
        _response = self._raw_client.search_using_attribute(
            type=type,
            types=types,
            attr=attr,
            attrs=attrs,
            attr_name=attr_name,
            attr_value_prefix=attr_value_prefix,
            tag=tag,
            time_range_type=time_range_type,
            time_range_attr=time_range_attr,
            time_range_start=time_range_start,
            time_range_end=time_range_end,
            sort_by=sort_by,
            sort_order=sort_order,
            deleted=deleted,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def search_using_basic(
        self,
        *,
        query: typing.Optional[str] = None,
        type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        types: typing.Optional[str] = None,
        attr: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        attrs: typing.Optional[str] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        time_range_type: typing.Optional[SearchUsingBasicRequestTimeRangeType] = None,
        time_range_attr: typing.Optional[str] = None,
        time_range_start: typing.Optional[int] = None,
        time_range_end: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[SearchUsingBasicRequestSortOrder] = None,
        deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResult:
        """
        Retrieve data for the specified fulltext query.

        Parameters
        ----------
        query : typing.Optional[str]
            The full-text query

        type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the result to only entities of specified types

        types : typing.Optional[str]

        attr : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One of more additional attributes to return in the response

        attrs : typing.Optional[str]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the result to only entities with the given tag

        time_range_type : typing.Optional[SearchUsingBasicRequestTimeRangeType]
            The type of time range search, default is CUSTOM

        time_range_attr : typing.Optional[str]
            The attribute for a time range search

        time_range_start : typing.Optional[int]
            The start for a custom time range search in ms since the epoch

        time_range_end : typing.Optional[int]
            The end for a custom time range search in ms since the epoch

        sort_by : typing.Optional[str]
            An attribute to sort by

        sort_order : typing.Optional[SearchUsingBasicRequestSortOrder]
            Sort order, either ASCENDING (default) or DESCENDING

        deleted : typing.Optional[bool]
            Whether to include deleted entities

        limit : typing.Optional[int]
            Limit the result set to only include the specified number of entries

        offset : typing.Optional[int]
            Start offset of the result set (useful for pagination)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResult
            On successful fulltext query with some results, might return an empty list if execution succeeded without any results

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.search_using_basic()
        """
        _response = self._raw_client.search_using_basic(
            query=query,
            type=type,
            types=types,
            attr=attr,
            attrs=attrs,
            tag=tag,
            time_range_type=time_range_type,
            time_range_attr=time_range_attr,
            time_range_start=time_range_start,
            time_range_end=time_range_end,
            sort_by=sort_by,
            sort_order=sort_order,
            deleted=deleted,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def get_all_business_metadata_defs(
        self, *, prefix: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BusinessMetadataDefResponse]:
        """
        Bulk retrieval API for retrieving business metadata definitions.

        Parameters
        ----------
        prefix : typing.Optional[str]
            The prefix of a business metadata definition name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataDefResponse]
            The business metadata definitions

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_all_business_metadata_defs()
        """
        _response = self._raw_client.get_all_business_metadata_defs(prefix=prefix, request_options=request_options)
        return _response.data

    def create_business_metadata_defs(
        self,
        *,
        request: typing.Sequence[AtlasBusinessMetadataDef],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BusinessMetadataDefResponse]:
        """
        Bulk create API for business metadata definitions.

        Parameters
        ----------
        request : typing.Sequence[AtlasBusinessMetadataDef]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataDefResponse]
            The business metadata definitions. Errored business metadata definitions will have an additional error property.

        Examples
        --------
        import datetime

        from fern import (
            AtlasAttributeDef,
            AtlasBusinessMetadataDef,
            AtlasConstraintDef,
            FernApi,
        )

        client = FernApi()
        client.create_business_metadata_defs(
            request=[
                AtlasBusinessMetadataDef(
                    category="PRIMITIVE",
                    guid="guid",
                    created_by="createdBy",
                    updated_by="updatedBy",
                    create_time=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    update_time=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    version=0,
                    name="name",
                    description="description",
                    type_version="typeVersion",
                    service_type="serviceType",
                    options={"key": "options"},
                    attribute_defs=[
                        AtlasAttributeDef(
                            name="name",
                            type_name="typeName",
                            is_optional=True,
                            cardinality="SINGLE",
                            values_min_count=6,
                            values_max_count=1,
                            is_unique=True,
                            is_indexable=True,
                            include_in_notification=True,
                            default_value="defaultValue",
                            description="description",
                            search_weight=5,
                            index_type="DEFAULT",
                            constraints=[
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                            ],
                            options={"key": "options"},
                            display_name="displayName",
                        ),
                        AtlasAttributeDef(
                            name="name",
                            type_name="typeName",
                            is_optional=True,
                            cardinality="SINGLE",
                            values_min_count=6,
                            values_max_count=1,
                            is_unique=True,
                            is_indexable=True,
                            include_in_notification=True,
                            default_value="defaultValue",
                            description="description",
                            search_weight=5,
                            index_type="DEFAULT",
                            constraints=[
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                            ],
                            options={"key": "options"},
                            display_name="displayName",
                        ),
                    ],
                )
            ],
        )
        """
        _response = self._raw_client.create_business_metadata_defs(request=request, request_options=request_options)
        return _response.data

    def update_business_metadata_defs(
        self,
        *,
        request: typing.Sequence[AtlasBusinessMetadataDef],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BusinessMetadataDefResponse]:
        """
        Bulk update API for business metadata definitions.

        Parameters
        ----------
        request : typing.Sequence[AtlasBusinessMetadataDef]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataDefResponse]
            The business metadata definitions. Errored business metadata definitions will have an additional error property.

        Examples
        --------
        import datetime

        from fern import (
            AtlasAttributeDef,
            AtlasBusinessMetadataDef,
            AtlasConstraintDef,
            FernApi,
        )

        client = FernApi()
        client.update_business_metadata_defs(
            request=[
                AtlasBusinessMetadataDef(
                    category="PRIMITIVE",
                    guid="guid",
                    created_by="createdBy",
                    updated_by="updatedBy",
                    create_time=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    update_time=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    version=0,
                    name="name",
                    description="description",
                    type_version="typeVersion",
                    service_type="serviceType",
                    options={"key": "options"},
                    attribute_defs=[
                        AtlasAttributeDef(
                            name="name",
                            type_name="typeName",
                            is_optional=True,
                            cardinality="SINGLE",
                            values_min_count=6,
                            values_max_count=1,
                            is_unique=True,
                            is_indexable=True,
                            include_in_notification=True,
                            default_value="defaultValue",
                            description="description",
                            search_weight=5,
                            index_type="DEFAULT",
                            constraints=[
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                            ],
                            options={"key": "options"},
                            display_name="displayName",
                        ),
                        AtlasAttributeDef(
                            name="name",
                            type_name="typeName",
                            is_optional=True,
                            cardinality="SINGLE",
                            values_min_count=6,
                            values_max_count=1,
                            is_unique=True,
                            is_indexable=True,
                            include_in_notification=True,
                            default_value="defaultValue",
                            description="description",
                            search_weight=5,
                            index_type="DEFAULT",
                            constraints=[
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                            ],
                            options={"key": "options"},
                            display_name="displayName",
                        ),
                    ],
                )
            ],
        )
        """
        _response = self._raw_client.update_business_metadata_defs(request=request, request_options=request_options)
        return _response.data

    def get_all_tag_defs(
        self, *, prefix: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagDefResponse]:
        """
        Bulk retrieval API for retrieving tag definitions.

        Parameters
        ----------
        prefix : typing.Optional[str]
            The prefix of a tag definition name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagDefResponse]
            The tag definitions

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_all_tag_defs()
        """
        _response = self._raw_client.get_all_tag_defs(prefix=prefix, request_options=request_options)
        return _response.data

    def create_tag_defs(
        self, *, request: typing.Sequence[TagDef], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagDefResponse]:
        """
        Bulk create API for tag definitions.

        Parameters
        ----------
        request : typing.Sequence[TagDef]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagDefResponse]
            The tag definitions. Errored tag definitions will have an additional error property.

        Examples
        --------
        from fern import AtlasAttributeDef, AtlasConstraintDef, FernApi, TagDef

        client = FernApi()
        client.create_tag_defs(
            request=[
                TagDef(
                    category="PRIMITIVE",
                    guid="guid",
                    created_by="createdBy",
                    updated_by="updatedBy",
                    create_time=1000000,
                    update_time=1000000,
                    version=0,
                    name="name",
                    description="description",
                    type_version="typeVersion",
                    service_type="serviceType",
                    options={"key": "options"},
                    attribute_defs=[
                        AtlasAttributeDef(
                            name="name",
                            type_name="typeName",
                            is_optional=True,
                            cardinality="SINGLE",
                            values_min_count=6,
                            values_max_count=1,
                            is_unique=True,
                            is_indexable=True,
                            include_in_notification=True,
                            default_value="defaultValue",
                            description="description",
                            search_weight=5,
                            index_type="DEFAULT",
                            constraints=[
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                            ],
                            options={"key": "options"},
                            display_name="displayName",
                        ),
                        AtlasAttributeDef(
                            name="name",
                            type_name="typeName",
                            is_optional=True,
                            cardinality="SINGLE",
                            values_min_count=6,
                            values_max_count=1,
                            is_unique=True,
                            is_indexable=True,
                            include_in_notification=True,
                            default_value="defaultValue",
                            description="description",
                            search_weight=5,
                            index_type="DEFAULT",
                            constraints=[
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                            ],
                            options={"key": "options"},
                            display_name="displayName",
                        ),
                    ],
                    super_types=["superTypes", "superTypes"],
                    entity_types=["entityTypes", "entityTypes"],
                    sub_types=["subTypes", "subTypes"],
                )
            ],
        )
        """
        _response = self._raw_client.create_tag_defs(request=request, request_options=request_options)
        return _response.data

    def update_tag_defs(
        self, *, request: typing.Sequence[TagDef], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagDefResponse]:
        """
        Bulk update API for tag definitions.

        Parameters
        ----------
        request : typing.Sequence[TagDef]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagDefResponse]
            The tag definitions. Errored tag definitions will have an additional error property.

        Examples
        --------
        from fern import AtlasAttributeDef, AtlasConstraintDef, FernApi, TagDef

        client = FernApi()
        client.update_tag_defs(
            request=[
                TagDef(
                    category="PRIMITIVE",
                    guid="guid",
                    created_by="createdBy",
                    updated_by="updatedBy",
                    create_time=1000000,
                    update_time=1000000,
                    version=0,
                    name="name",
                    description="description",
                    type_version="typeVersion",
                    service_type="serviceType",
                    options={"key": "options"},
                    attribute_defs=[
                        AtlasAttributeDef(
                            name="name",
                            type_name="typeName",
                            is_optional=True,
                            cardinality="SINGLE",
                            values_min_count=6,
                            values_max_count=1,
                            is_unique=True,
                            is_indexable=True,
                            include_in_notification=True,
                            default_value="defaultValue",
                            description="description",
                            search_weight=5,
                            index_type="DEFAULT",
                            constraints=[
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                            ],
                            options={"key": "options"},
                            display_name="displayName",
                        ),
                        AtlasAttributeDef(
                            name="name",
                            type_name="typeName",
                            is_optional=True,
                            cardinality="SINGLE",
                            values_min_count=6,
                            values_max_count=1,
                            is_unique=True,
                            is_indexable=True,
                            include_in_notification=True,
                            default_value="defaultValue",
                            description="description",
                            search_weight=5,
                            index_type="DEFAULT",
                            constraints=[
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                                AtlasConstraintDef(
                                    type="type",
                                    params={"key": {"key": "value"}},
                                ),
                            ],
                            options={"key": "options"},
                            display_name="displayName",
                        ),
                    ],
                    super_types=["superTypes", "superTypes"],
                    entity_types=["entityTypes", "entityTypes"],
                    sub_types=["subTypes", "subTypes"],
                )
            ],
        )
        """
        _response = self._raw_client.update_tag_defs(request=request, request_options=request_options)
        return _response.data

    def get_business_metadata_def_by_name(
        self, bm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AtlasBusinessMetadataDef:
        """
        Get the business metadata definition with the given name.

        Parameters
        ----------
        bm_name : str
            The name of the business metadata definition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtlasBusinessMetadataDef
            The business metadata definition

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_business_metadata_def_by_name(
            bm_name="bmName",
        )
        """
        _response = self._raw_client.get_business_metadata_def_by_name(bm_name, request_options=request_options)
        return _response.data

    def delete_business_metadata_def(
        self, bm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete API for business metadata definition identified by its name.

        Parameters
        ----------
        bm_name : str
            The name of the business metadata definition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_business_metadata_def(
            bm_name="bmName",
        )
        """
        _response = self._raw_client.delete_business_metadata_def(bm_name, request_options=request_options)
        return _response.data

    def get_tag_def_by_name(self, tag_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> TagDef:
        """
        Get the tag definition with the given name.

        Parameters
        ----------
        tag_name : str
            The name of the tag definiton

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagDef
            The tag definition

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_tag_def_by_name(
            tag_name="tagName",
        )
        """
        _response = self._raw_client.get_tag_def_by_name(tag_name, request_options=request_options)
        return _response.data

    def delete_tag_def(self, tag_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete API for tag definition identified by its name.

        Parameters
        ----------
        tag_name : str
            The name of the tag definition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_tag_def(
            tag_name="tagName",
        )
        """
        _response = self._raw_client.delete_tag_def(tag_name, request_options=request_options)
        return _response.data

    def put_asyncapi_parse(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get number of times the cli tool is used to import and parse the spec file

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
        client.put_asyncapi_parse()
        """
        _response = self._raw_client.put_asyncapi_parse(request_options=request_options)
        return _response.data

    def put_asyncapi(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get number of times the cli tool is used to export/produce the spec file

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
        client.put_asyncapi()
        """
        _response = self._raw_client.put_asyncapi(request_options=request_options)
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

    async def get_dek_subjects(
        self,
        name: str,
        *,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of dek subjects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_dek_subjects(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dek_subjects(name, deleted=deleted, request_options=request_options)
        return _response.data

    async def create_dek(
        self,
        name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dek:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dek
            The create response
        """
        _response = await self._raw_client.create_dek(name, request=request, request_options=request_options)
        return _response.data

    async def get_kek_names(
        self, *, deleted: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of kek names

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_kek_names()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_kek_names(deleted=deleted, request_options=request_options)
        return _response.data

    async def create_kek(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Kek:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Kek
            The create response
        """
        _response = await self._raw_client.create_kek(request=request, request_options=request_options)
        return _response.data

    async def get_kek(
        self,
        name: str,
        *,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Kek:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Kek
            The kek info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_kek(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_kek(name, deleted=deleted, request_options=request_options)
        return _response.data

    async def put_kek(
        self,
        name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Kek:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Kek
            The update response
        """
        _response = await self._raw_client.put_kek(name, request=request, request_options=request_options)
        return _response.data

    async def delete_kek(
        self,
        name: str,
        *,
        permanent: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        permanent : typing.Optional[bool]
            Whether to perform a permanent delete

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
            await client.delete_kek(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_kek(name, permanent=permanent, request_options=request_options)
        return _response.data

    async def get_dek(
        self,
        name: str,
        subject: str,
        *,
        algorithm: typing.Optional[GetDekRequestAlgorithm] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dek:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        algorithm : typing.Optional[GetDekRequestAlgorithm]
            Algorithm of the dek

        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dek
            The dek info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_dek(
                name="name",
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dek(
            name, subject, algorithm=algorithm, deleted=deleted, request_options=request_options
        )
        return _response.data

    async def delete_dek_versions(
        self,
        name: str,
        subject: str,
        *,
        algorithm: typing.Optional[DeleteDekVersionsRequestAlgorithm] = None,
        permanent: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        algorithm : typing.Optional[DeleteDekVersionsRequestAlgorithm]
            Algorithm of the dek

        permanent : typing.Optional[bool]
            Whether to perform a permanent delete

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
            await client.delete_dek_versions(
                name="name",
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_dek_versions(
            name, subject, algorithm=algorithm, permanent=permanent, request_options=request_options
        )
        return _response.data

    async def get_dek_by_version(
        self,
        name: str,
        subject: str,
        version: str,
        *,
        algorithm: typing.Optional[GetDekByVersionRequestAlgorithm] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dek:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        version : str
            Version of the dek

        algorithm : typing.Optional[GetDekByVersionRequestAlgorithm]
            Algorithm of the dek

        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dek
            The dek info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_dek_by_version(
                name="name",
                subject="subject",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dek_by_version(
            name, subject, version, algorithm=algorithm, deleted=deleted, request_options=request_options
        )
        return _response.data

    async def delete_dek_version(
        self,
        name: str,
        subject: str,
        version: str,
        *,
        algorithm: typing.Optional[DeleteDekVersionRequestAlgorithm] = None,
        permanent: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        version : str
            Version of the dek

        algorithm : typing.Optional[DeleteDekVersionRequestAlgorithm]
            Algorithm of the dek

        permanent : typing.Optional[bool]
            Whether to perform a permanent delete

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
            await client.delete_dek_version(
                name="name",
                subject="subject",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_dek_version(
            name, subject, version, algorithm=algorithm, permanent=permanent, request_options=request_options
        )
        return _response.data

    async def get_dek_versions(
        self,
        name: str,
        subject: str,
        *,
        algorithm: typing.Optional[GetDekVersionsRequestAlgorithm] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[int]:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        algorithm : typing.Optional[GetDekVersionsRequestAlgorithm]
            Algorithm of the dek

        deleted : typing.Optional[bool]
            Whether to include deleted keys

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            List of version numbers for dek

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_dek_versions(
                name="name",
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dek_versions(
            name, subject, algorithm=algorithm, deleted=deleted, request_options=request_options
        )
        return _response.data

    async def undelete_dek_version(
        self,
        name: str,
        subject: str,
        version: str,
        *,
        algorithm: typing.Optional[UndeleteDekVersionRequestAlgorithm] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        version : str
            Version of the dek

        algorithm : typing.Optional[UndeleteDekVersionRequestAlgorithm]
            Algorithm of the dek

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
            await client.undelete_dek_version(
                name="name",
                subject="subject",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.undelete_dek_version(
            name, subject, version, algorithm=algorithm, request_options=request_options
        )
        return _response.data

    async def undelete_dek_versions(
        self,
        name: str,
        subject: str,
        *,
        algorithm: typing.Optional[UndeleteDekVersionsRequestAlgorithm] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

        subject : str
            Subject of the dek

        algorithm : typing.Optional[UndeleteDekVersionsRequestAlgorithm]
            Algorithm of the dek

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
            await client.undelete_dek_versions(
                name="name",
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.undelete_dek_versions(
            name, subject, algorithm=algorithm, request_options=request_options
        )
        return _response.data

    async def undelete_kek(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the kek

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
            await client.undelete_kek(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.undelete_kek(name, request_options=request_options)
        return _response.data

    async def create_business_metadata(
        self, *, request: typing.Sequence[BusinessMetadata], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BusinessMetadataResponse]:
        """
        Bulk API to create multiple business metadata.

        Parameters
        ----------
        request : typing.Sequence[BusinessMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataResponse]
            The business metadata. Errored business metadata will have an additional error property.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BusinessMetadata

        client = AsyncFernApi()


        async def main() -> None:
            await client.create_business_metadata(
                request=[
                    BusinessMetadata(
                        type_name="typeName",
                        attributes={"key": "{}"},
                        entity_type="entityType",
                        entity_name="entityName",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_business_metadata(request=request, request_options=request_options)
        return _response.data

    async def update_business_metadata(
        self, *, request: typing.Sequence[BusinessMetadata], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BusinessMetadataResponse]:
        """
        Bulk API to update multiple business metadata.

        Parameters
        ----------
        request : typing.Sequence[BusinessMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataResponse]
            The business metadata. Errored business metadata will have an additional error property.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BusinessMetadata

        client = AsyncFernApi()


        async def main() -> None:
            await client.update_business_metadata(
                request=[
                    BusinessMetadata(
                        type_name="typeName",
                        attributes={"key": "{}"},
                        entity_type="entityType",
                        entity_name="entityName",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_business_metadata(request=request, request_options=request_options)
        return _response.data

    async def get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, GetResponseValue]:
        """
        The Root resource is a no-op.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, GetResponseValue]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(request_options=request_options)
        return _response.data

    async def post(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.post()


        asyncio.run(main())
        """
        _response = await self._raw_client.post(request_options=request_options)
        return _response.data

    async def test_compatibility_for_subject(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        verbose: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompatibilityCheckResponse:
        """
        the compatibility level applied for the check is the configured compatibility level for the subject (http:get:: /config/(string: subject)). If this subject's compatibility level was never changed, then the global compatibility level applies (http:get:: /config).

        Parameters
        ----------
        subject : str
            Subject of the schema version against which compatibility is to be tested

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        verbose : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompatibilityCheckResponse
            successful operation
        """
        _response = await self._raw_client.test_compatibility_for_subject(
            subject, request=request, verbose=verbose, request_options=request_options
        )
        return _response.data

    async def test_compatibility_by_subject_name(
        self,
        subject: str,
        version: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        verbose: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompatibilityCheckResponse:
        """
        the compatibility level applied for the check is the configured compatibility level for the subject (http:get:: /config/(string: subject)). If this subject's compatibility level was never changed, then the global compatibility level applies (http:get:: /config).

        Parameters
        ----------
        subject : str
            Subject of the schema version against which compatibility is to be tested

        version : str
            Version of the subject's schema against which compatibility is to be tested. Valid values for versionId are between [1,2^31-1] or the string "latest"."latest" checks compatibility of the input schema with the last registered schema under the specified subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        verbose : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompatibilityCheckResponse
            successful operation
        """
        _response = await self._raw_client.test_compatibility_by_subject_name(
            subject, version, request=request, verbose=verbose, request_options=request_options
        )
        return _response.data

    async def get_top_level_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> Config:
        """
        Retrieves the global compatibility level.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            The global compatibility level.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_top_level_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_top_level_config(request_options=request_options)
        return _response.data

    async def update_top_level_config(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConfigUpdateRequest:
        """
        Updates the global compatibility level. On success, echoes the original request back to the client.

        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigUpdateRequest
            The original request.
        """
        _response = await self._raw_client.update_top_level_config(request=request, request_options=request_options)
        return _response.data

    async def delete_top_level_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTopLevelConfigResponse:
        """
        Deletes the global compatibility level config and reverts to the default.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTopLevelConfigResponse
            Operation succeeded. Returns old global compatibility level.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.delete_top_level_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_top_level_config(request_options=request_options)
        return _response.data

    async def get_subject_level_config(
        self,
        subject: str,
        *,
        default_to_global: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Config:
        """
        Parameters
        ----------
        subject : str

        default_to_global : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_subject_level_config(
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subject_level_config(
            subject, default_to_global=default_to_global, request_options=request_options
        )
        return _response.data

    async def update_subject_level_config(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConfigUpdateRequest:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigUpdateRequest
            successful operation
        """
        _response = await self._raw_client.update_subject_level_config(
            subject, request=request, request_options=request_options
        )
        return _response.data

    async def delete_subject_config(
        self, subject: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSubjectConfigResponse:
        """
        Parameters
        ----------
        subject : str
            the name of the subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSubjectConfigResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.delete_subject_config(
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_subject_config(subject, request_options=request_options)
        return _response.data

    async def list_contexts(
        self, *, context_prefix: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        context_prefix : typing.Optional[str]
            prefix to filter contexts

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_contexts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_contexts(context_prefix=context_prefix, request_options=request_options)
        return _response.data

    async def get_top_level_mode(self, *, request_options: typing.Optional[RequestOptions] = None) -> Mode:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Mode
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_top_level_mode()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_top_level_mode(request_options=request_options)
        return _response.data

    async def update_top_level_mode(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModeUpdateRequest:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModeUpdateRequest
            successful operation
        """
        _response = await self._raw_client.update_top_level_mode(request=request, request_options=request_options)
        return _response.data

    async def delete_mode(
        self, *, recursive: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteModeResponse:
        """
        Parameters
        ----------
        recursive : typing.Optional[bool]
            recursive delete mode across all subjects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteModeResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.delete_mode()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_mode(recursive=recursive, request_options=request_options)
        return _response.data

    async def get_mode(
        self,
        subject: str,
        *,
        default_to_global: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Mode:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        default_to_global : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Mode
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_mode(
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mode(
            subject, default_to_global=default_to_global, request_options=request_options
        )
        return _response.data

    async def update_mode(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModeUpdateRequest:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModeUpdateRequest
            successful operation
        """
        _response = await self._raw_client.update_mode(subject, request=request, request_options=request_options)
        return _response.data

    async def delete_subject_mode(
        self,
        subject: str,
        *,
        recursive: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteSubjectModeResponse:
        """
        Parameters
        ----------
        subject : str
            the name of the subject

        recursive : typing.Optional[bool]
            recursive delete mode for all subjects under the context if subject parameter is a context

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSubjectModeResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.delete_subject_mode(
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_subject_mode(
            subject, recursive=recursive, request_options=request_options
        )
        return _response.data

    async def get_schemas(
        self,
        *,
        subject_prefix: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        latest_only: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Parameters
        ----------
        subject_prefix : typing.Optional[str]

        deleted : typing.Optional[bool]

        latest_only : typing.Optional[bool]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_schemas()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schemas(
            subject_prefix=subject_prefix,
            deleted=deleted,
            latest_only=latest_only,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def get_schema(
        self,
        id: int,
        *,
        subject: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        fetch_max_id: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchemaString:
        """
        Parameters
        ----------
        id : int
            Globally unique identifier of the schema

        subject : typing.Optional[str]

        format : typing.Optional[str]

        fetch_max_id : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaString
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_schema(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schema(
            id, subject=subject, format=format, fetch_max_id=fetch_max_id, request_options=request_options
        )
        return _response.data

    async def get_subjects(
        self,
        id: int,
        *,
        subject: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        id : int
            Globally unique identifier of the schema

        subject : typing.Optional[str]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_subjects(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subjects(
            id, subject=subject, deleted=deleted, request_options=request_options
        )
        return _response.data

    async def get_versions(
        self,
        id: int,
        *,
        subject: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SubjectVersion]:
        """
        Parameters
        ----------
        id : int
            Globally unique identifier of the schema

        subject : typing.Optional[str]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SubjectVersion]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_versions(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_versions(
            id, subject=subject, deleted=deleted, request_options=request_options
        )
        return _response.data

    async def get_schema_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_schema_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schema_types(request_options=request_options)
        return _response.data

    async def list(
        self,
        *,
        subject_prefix: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        deleted_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        subject_prefix : typing.Optional[str]

        deleted : typing.Optional[bool]

        deleted_only : typing.Optional[bool]
            Whether to return deleted subjects only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            subject_prefix=subject_prefix, deleted=deleted, deleted_only=deleted_only, request_options=request_options
        )
        return _response.data

    async def look_up_schema_under_subject(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        format: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subject : str
            Subject under which the schema will be registered

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        format : typing.Optional[str]
            Desired output format, dependent on schema type

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = await self._raw_client.look_up_schema_under_subject(
            subject, request=request, format=format, deleted=deleted, request_options=request_options
        )
        return _response.data

    async def delete_subject(
        self,
        subject: str,
        *,
        permanent: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[int]:
        """
        Parameters
        ----------
        subject : str
            the name of the subject

        permanent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.delete_subject(
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_subject(subject, permanent=permanent, request_options=request_options)
        return _response.data

    async def list_versions(
        self,
        subject: str,
        *,
        deleted: typing.Optional[bool] = None,
        deleted_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[int]:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        deleted : typing.Optional[bool]

        deleted_only : typing.Optional[bool]
            Whether to return deleted schemas only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_versions(
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_versions(
            subject, deleted=deleted, deleted_only=deleted_only, request_options=request_options
        )
        return _response.data

    async def register(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        normalize: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegisterSchemaResponse:
        """
        Register a new schema under the specified subject. If successfully registered, this returns the unique identifier of this schema in the registry. The returned identifier should be used to retrieve this schema from the schemas resource and is different from the schema's version which is associated with the subject. If the same schema is registered under a different subject, the same identifier will be returned. However, the version of the schema may be different under different subjects.
        A schema should be compatible with the previously registered schema or schemas (if there are any) as per the configured compatibility level. The configured compatibility level can be obtained by issuing a GET http:get:: /config/(string: subject). If that returns null, then GET http:get:: /config
        When there are multiple instances of Schema Registry running in the same cluster, the schema registration request will be forwarded to one of the instances designated as the primary. If the primary is not available, the client will get an error code indicating that the forwarding has failed.

        Parameters
        ----------
        subject : str
            Name of the subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        normalize : typing.Optional[bool]
            Whether to register the normalized schema

        format : typing.Optional[str]
            Desired output format, dependent on schema type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterSchemaResponse
            successful operation
        """
        _response = await self._raw_client.register(
            subject, request=request, normalize=normalize, format=format, request_options=request_options
        )
        return _response.data

    async def get_schema_by_version(
        self,
        subject: str,
        version: str,
        *,
        format: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Schema:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        version : str
            Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.

        format : typing.Optional[str]
            Desired output format, dependent on schema type

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schema
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_schema_by_version(
                subject="subject",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schema_by_version(
            subject, version, format=format, deleted=deleted, request_options=request_options
        )
        return _response.data

    async def delete_schema_version(
        self,
        subject: str,
        version: str,
        *,
        permanent: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        version : str
            Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.

        permanent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.delete_schema_version(
                subject="subject",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_schema_version(
            subject, version, permanent=permanent, request_options=request_options
        )
        return _response.data

    async def get_referenced_by(
        self, subject: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        version : str
            Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_referenced_by(
                subject="subject",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_referenced_by(subject, version, request_options=request_options)
        return _response.data

    async def get_schema_only(
        self,
        subject: str,
        version: str,
        *,
        format: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        subject : str
            Name of the Subject

        version : str
            Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.

        format : typing.Optional[str]
            Desired output format, dependent on schema type

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_schema_only(
                subject="subject",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schema_only(
            subject, version, format=format, deleted=deleted, request_options=request_options
        )
        return _response.data

    async def get_cluster_id(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServerClusterId:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServerClusterId
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_cluster_id()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cluster_id(request_options=request_options)
        return _response.data

    async def get_exporters(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_exporters()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_exporters(request_options=request_options)
        return _response.data

    async def create_exporter(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateExporterResponse:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateExporterResponse
            successful operation
        """
        _response = await self._raw_client.create_exporter(request=request, request_options=request_options)
        return _response.data

    async def get_exporter_info(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExporterInfo:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExporterInfo
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_exporter_info(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_exporter_info(name, request_options=request_options)
        return _response.data

    async def put_exporter(
        self,
        name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateExporterResponse:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExporterResponse
            successful operation
        """
        _response = await self._raw_client.put_exporter(name, request=request, request_options=request_options)
        return _response.data

    async def delete_exporter(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

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
            await client.delete_exporter(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_exporter(name, request_options=request_options)
        return _response.data

    async def get_exporter_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_exporter_config(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_exporter_config(name, request_options=request_options)
        return _response.data

    async def put_exporter_config(
        self,
        name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateExporterResponse:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExporterResponse
            successful operation
        """
        _response = await self._raw_client.put_exporter_config(name, request=request, request_options=request_options)
        return _response.data

    async def get_exporter_cluster_link_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_exporter_cluster_link_config(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_exporter_cluster_link_config(name, request_options=request_options)
        return _response.data

    async def pause_exporter(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateExporterResponse:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExporterResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.pause_exporter(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pause_exporter(name, request_options=request_options)
        return _response.data

    async def reset_exporter(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateExporterResponse:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExporterResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reset_exporter(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_exporter(name, request_options=request_options)
        return _response.data

    async def resume_exporter(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateExporterResponse:
        """
        Parameters
        ----------
        name : str
            Name of the exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExporterResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.resume_exporter(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resume_exporter(name, request_options=request_options)
        return _response.data

    async def get_exporter_status(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExporterStatus:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExporterStatus
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_exporter_status(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_exporter_status(name, request_options=request_options)
        return _response.data

    async def create_tags(
        self, *, request: typing.Sequence[Tag], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagResponse]:
        """
        Bulk API to create multiple tags.

        Parameters
        ----------
        request : typing.Sequence[Tag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagResponse]
            The tags. Errored tags will have an additional error property.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Tag, TimeBoundary

        client = AsyncFernApi()


        async def main() -> None:
            await client.create_tags(
                request=[
                    Tag(
                        type_name="typeName",
                        attributes={"key": {"key": "value"}},
                        entity_guid="entityGuid",
                        entity_status="ACTIVE",
                        propagate=True,
                        validity_periods=[
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                        ],
                        remove_propagations_on_entity_delete=True,
                        entity_type="entityType",
                        entity_name="entityName",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tags(request=request, request_options=request_options)
        return _response.data

    async def update_tags(
        self, *, request: typing.Sequence[Tag], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagResponse]:
        """
        Bulk API to update multiple tags.

        Parameters
        ----------
        request : typing.Sequence[Tag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagResponse]
            The tags. Errored tags will have an additional error property.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Tag, TimeBoundary

        client = AsyncFernApi()


        async def main() -> None:
            await client.update_tags(
                request=[
                    Tag(
                        type_name="typeName",
                        attributes={"key": {"key": "value"}},
                        entity_guid="entityGuid",
                        entity_status="ACTIVE",
                        propagate=True,
                        validity_periods=[
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                            TimeBoundary(
                                start_time="startTime",
                                end_time="endTime",
                                time_zone="timeZone",
                            ),
                        ],
                        remove_propagations_on_entity_delete=True,
                        entity_type="entityType",
                        entity_name="entityName",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_tags(request=request, request_options=request_options)
        return _response.data

    async def delete_business_metadata(
        self,
        type_name: str,
        qualified_name: str,
        bm_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a business metadata on an entity.

        Parameters
        ----------
        type_name : str
            The type of the entity

        qualified_name : str
            The qualified name of the entity

        bm_name : str
            The name of the business metadata

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
            await client.delete_business_metadata(
                type_name="typeName",
                qualified_name="qualifiedName",
                bm_name="bmName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_business_metadata(
            type_name, qualified_name, bm_name, request_options=request_options
        )
        return _response.data

    async def delete_tag(
        self,
        type_name: str,
        qualified_name: str,
        tag_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a tag on an entity.

        Parameters
        ----------
        type_name : str
            The type of the entity

        qualified_name : str
            The qualified name of the entity

        tag_name : str
            The name of the tag

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
            await client.delete_tag(
                type_name="typeName",
                qualified_name="qualifiedName",
                tag_name="tagName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_tag(
            type_name, qualified_name, tag_name, request_options=request_options
        )
        return _response.data

    async def get_business_metadata(
        self, type_name: str, qualified_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BusinessMetadataResponse]:
        """
        Gets the list of business metadata for a given entity represented by a qualified name.

        Parameters
        ----------
        type_name : str
            The type of the entity

        qualified_name : str
            The qualified name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataResponse]
            The business metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_business_metadata(
                type_name="typeName",
                qualified_name="qualifiedName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_business_metadata(
            type_name, qualified_name, request_options=request_options
        )
        return _response.data

    async def get_by_unique_attributes(
        self,
        type_name: str,
        qualified_name: str,
        *,
        min_ext_info: typing.Optional[bool] = None,
        ignore_relationships: typing.Optional[bool] = None,
        include_internal_prefix: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtlasEntityWithExtInfo:
        """
        Fetch complete definition of an entity given its type and unique attribute.

        Parameters
        ----------
        type_name : str
            The type of the entity

        qualified_name : str
            The qualified name of the entity

        min_ext_info : typing.Optional[bool]
            Whether to only populate header and schema attributes

        ignore_relationships : typing.Optional[bool]
            Whether to ignore relationships

        include_internal_prefix : typing.Optional[str]
            If not null, include internal attributes that start with this prefix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtlasEntityWithExtInfo
            The entity

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_by_unique_attributes(
                type_name="typeName",
                qualified_name="qualifiedName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_unique_attributes(
            type_name,
            qualified_name,
            min_ext_info=min_ext_info,
            ignore_relationships=ignore_relationships,
            include_internal_prefix=include_internal_prefix,
            request_options=request_options,
        )
        return _response.data

    async def delete_by_unique_attributes(
        self, type_name: str, qualified_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        type_name : str

        qualified_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.delete_by_unique_attributes(
                type_name="typeName",
                qualified_name="qualifiedName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_by_unique_attributes(
            type_name, qualified_name, request_options=request_options
        )
        return _response.data

    async def get_tags(
        self, type_name: str, qualified_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagResponse]:
        """
        Gets the list of classifications for a given entity represented by a qualifed name.

        Parameters
        ----------
        type_name : str
            The type of the entity

        qualified_name : str
            The qualified name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagResponse]
            The tags

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_tags(
                type_name="typeName",
                qualified_name="qualifiedName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tags(type_name, qualified_name, request_options=request_options)
        return _response.data

    async def create_or_update(
        self,
        *,
        referred_entities: typing.Optional[typing.Dict[str, AtlasEntity]] = OMIT,
        entity: typing.Optional[AtlasEntity] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        referred_entities : typing.Optional[typing.Dict[str, AtlasEntity]]

        entity : typing.Optional[AtlasEntity]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            default response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            AtlasClassification,
            AtlasEntity,
            AtlasTermAssignmentHeader,
            TimeBoundary,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.create_or_update(
                referred_entities={
                    "key": AtlasEntity(
                        type_name="typeName",
                        attributes={"key": "{}"},
                        guid="guid",
                        home_id="homeId",
                        is_proxy=True,
                        is_incomplete=True,
                        provenance_type=0,
                        status="ACTIVE",
                        created_by="createdBy",
                        updated_by="updatedBy",
                        create_time=1000000,
                        update_time=1000000,
                        version=6,
                        relationship_attributes={"key": "{}"},
                        classifications=[
                            AtlasClassification(
                                type_name="typeName",
                                attributes={"key": {"key": "value"}},
                                entity_guid="entityGuid",
                                entity_status="ACTIVE",
                                propagate=True,
                                validity_periods=[
                                    TimeBoundary(
                                        start_time="startTime",
                                        end_time="endTime",
                                        time_zone="timeZone",
                                    ),
                                    TimeBoundary(
                                        start_time="startTime",
                                        end_time="endTime",
                                        time_zone="timeZone",
                                    ),
                                ],
                                remove_propagations_on_entity_delete=True,
                            ),
                            AtlasClassification(
                                type_name="typeName",
                                attributes={"key": {"key": "value"}},
                                entity_guid="entityGuid",
                                entity_status="ACTIVE",
                                propagate=True,
                                validity_periods=[
                                    TimeBoundary(
                                        start_time="startTime",
                                        end_time="endTime",
                                        time_zone="timeZone",
                                    ),
                                    TimeBoundary(
                                        start_time="startTime",
                                        end_time="endTime",
                                        time_zone="timeZone",
                                    ),
                                ],
                                remove_propagations_on_entity_delete=True,
                            ),
                        ],
                        meanings=[
                            AtlasTermAssignmentHeader(
                                term_guid="termGuid",
                                relation_guid="relationGuid",
                                description="description",
                                display_text="displayText",
                                expression="expression",
                                created_by="createdBy",
                                steward="steward",
                                source="source",
                                confidence=1,
                                status="DISCOVERED",
                            ),
                            AtlasTermAssignmentHeader(
                                term_guid="termGuid",
                                relation_guid="relationGuid",
                                description="description",
                                display_text="displayText",
                                expression="expression",
                                created_by="createdBy",
                                steward="steward",
                                source="source",
                                confidence=1,
                                status="DISCOVERED",
                            ),
                        ],
                        custom_attributes={"key": "customAttributes"},
                        business_attributes={"key": {"key": "{}"}},
                        labels=["labels", "labels"],
                        pending_tasks=["pendingTasks", "pendingTasks"],
                        proxy=True,
                    )
                },
                entity=AtlasEntity(
                    type_name="typeName",
                    attributes={"key": "{}"},
                    guid="guid",
                    home_id="homeId",
                    is_proxy=True,
                    is_incomplete=True,
                    provenance_type=0,
                    status="ACTIVE",
                    created_by="createdBy",
                    updated_by="updatedBy",
                    create_time=1000000,
                    update_time=1000000,
                    version=6,
                    relationship_attributes={"key": "{}"},
                    classifications=[
                        AtlasClassification(
                            type_name="typeName",
                            attributes={"key": {"key": "value"}},
                            entity_guid="entityGuid",
                            entity_status="ACTIVE",
                            propagate=True,
                            validity_periods=[
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                            ],
                            remove_propagations_on_entity_delete=True,
                        ),
                        AtlasClassification(
                            type_name="typeName",
                            attributes={"key": {"key": "value"}},
                            entity_guid="entityGuid",
                            entity_status="ACTIVE",
                            propagate=True,
                            validity_periods=[
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                            ],
                            remove_propagations_on_entity_delete=True,
                        ),
                    ],
                    meanings=[
                        AtlasTermAssignmentHeader(
                            term_guid="termGuid",
                            relation_guid="relationGuid",
                            description="description",
                            display_text="displayText",
                            expression="expression",
                            created_by="createdBy",
                            steward="steward",
                            source="source",
                            confidence=1,
                            status="DISCOVERED",
                        ),
                        AtlasTermAssignmentHeader(
                            term_guid="termGuid",
                            relation_guid="relationGuid",
                            description="description",
                            display_text="displayText",
                            expression="expression",
                            created_by="createdBy",
                            steward="steward",
                            source="source",
                            confidence=1,
                            status="DISCOVERED",
                        ),
                    ],
                    custom_attributes={"key": "customAttributes"},
                    business_attributes={"key": {"key": "{}"}},
                    labels=["labels", "labels"],
                    pending_tasks=["pendingTasks", "pendingTasks"],
                    proxy=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update(
            referred_entities=referred_entities, entity=entity, request_options=request_options
        )
        return _response.data

    async def partial_update_by_unique_attributes(
        self,
        *,
        referred_entities: typing.Optional[typing.Dict[str, AtlasEntity]] = OMIT,
        entity: typing.Optional[AtlasEntity] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        referred_entities : typing.Optional[typing.Dict[str, AtlasEntity]]

        entity : typing.Optional[AtlasEntity]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            default response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            AtlasClassification,
            AtlasEntity,
            AtlasTermAssignmentHeader,
            TimeBoundary,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.partial_update_by_unique_attributes(
                referred_entities={
                    "key": AtlasEntity(
                        type_name="typeName",
                        attributes={"key": "{}"},
                        guid="guid",
                        home_id="homeId",
                        is_proxy=True,
                        is_incomplete=True,
                        provenance_type=0,
                        status="ACTIVE",
                        created_by="createdBy",
                        updated_by="updatedBy",
                        create_time=1000000,
                        update_time=1000000,
                        version=6,
                        relationship_attributes={"key": "{}"},
                        classifications=[
                            AtlasClassification(
                                type_name="typeName",
                                attributes={"key": {"key": "value"}},
                                entity_guid="entityGuid",
                                entity_status="ACTIVE",
                                propagate=True,
                                validity_periods=[
                                    TimeBoundary(
                                        start_time="startTime",
                                        end_time="endTime",
                                        time_zone="timeZone",
                                    ),
                                    TimeBoundary(
                                        start_time="startTime",
                                        end_time="endTime",
                                        time_zone="timeZone",
                                    ),
                                ],
                                remove_propagations_on_entity_delete=True,
                            ),
                            AtlasClassification(
                                type_name="typeName",
                                attributes={"key": {"key": "value"}},
                                entity_guid="entityGuid",
                                entity_status="ACTIVE",
                                propagate=True,
                                validity_periods=[
                                    TimeBoundary(
                                        start_time="startTime",
                                        end_time="endTime",
                                        time_zone="timeZone",
                                    ),
                                    TimeBoundary(
                                        start_time="startTime",
                                        end_time="endTime",
                                        time_zone="timeZone",
                                    ),
                                ],
                                remove_propagations_on_entity_delete=True,
                            ),
                        ],
                        meanings=[
                            AtlasTermAssignmentHeader(
                                term_guid="termGuid",
                                relation_guid="relationGuid",
                                description="description",
                                display_text="displayText",
                                expression="expression",
                                created_by="createdBy",
                                steward="steward",
                                source="source",
                                confidence=1,
                                status="DISCOVERED",
                            ),
                            AtlasTermAssignmentHeader(
                                term_guid="termGuid",
                                relation_guid="relationGuid",
                                description="description",
                                display_text="displayText",
                                expression="expression",
                                created_by="createdBy",
                                steward="steward",
                                source="source",
                                confidence=1,
                                status="DISCOVERED",
                            ),
                        ],
                        custom_attributes={"key": "customAttributes"},
                        business_attributes={"key": {"key": "{}"}},
                        labels=["labels", "labels"],
                        pending_tasks=["pendingTasks", "pendingTasks"],
                        proxy=True,
                    )
                },
                entity=AtlasEntity(
                    type_name="typeName",
                    attributes={"key": "{}"},
                    guid="guid",
                    home_id="homeId",
                    is_proxy=True,
                    is_incomplete=True,
                    provenance_type=0,
                    status="ACTIVE",
                    created_by="createdBy",
                    updated_by="updatedBy",
                    create_time=1000000,
                    update_time=1000000,
                    version=6,
                    relationship_attributes={"key": "{}"},
                    classifications=[
                        AtlasClassification(
                            type_name="typeName",
                            attributes={"key": {"key": "value"}},
                            entity_guid="entityGuid",
                            entity_status="ACTIVE",
                            propagate=True,
                            validity_periods=[
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                            ],
                            remove_propagations_on_entity_delete=True,
                        ),
                        AtlasClassification(
                            type_name="typeName",
                            attributes={"key": {"key": "value"}},
                            entity_guid="entityGuid",
                            entity_status="ACTIVE",
                            propagate=True,
                            validity_periods=[
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                                TimeBoundary(
                                    start_time="startTime",
                                    end_time="endTime",
                                    time_zone="timeZone",
                                ),
                            ],
                            remove_propagations_on_entity_delete=True,
                        ),
                    ],
                    meanings=[
                        AtlasTermAssignmentHeader(
                            term_guid="termGuid",
                            relation_guid="relationGuid",
                            description="description",
                            display_text="displayText",
                            expression="expression",
                            created_by="createdBy",
                            steward="steward",
                            source="source",
                            confidence=1,
                            status="DISCOVERED",
                        ),
                        AtlasTermAssignmentHeader(
                            term_guid="termGuid",
                            relation_guid="relationGuid",
                            description="description",
                            display_text="displayText",
                            expression="expression",
                            created_by="createdBy",
                            steward="steward",
                            source="source",
                            confidence=1,
                            status="DISCOVERED",
                        ),
                    ],
                    custom_attributes={"key": "customAttributes"},
                    business_attributes={"key": {"key": "{}"}},
                    labels=["labels", "labels"],
                    pending_tasks=["pendingTasks", "pendingTasks"],
                    proxy=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partial_update_by_unique_attributes(
            referred_entities=referred_entities, entity=entity, request_options=request_options
        )
        return _response.data

    async def search_using_attribute(
        self,
        *,
        type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        types: typing.Optional[str] = None,
        attr: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        attrs: typing.Optional[str] = None,
        attr_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        attr_value_prefix: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        time_range_type: typing.Optional[SearchUsingAttributeRequestTimeRangeType] = None,
        time_range_attr: typing.Optional[str] = None,
        time_range_start: typing.Optional[int] = None,
        time_range_end: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[SearchUsingAttributeRequestSortOrder] = None,
        deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResult:
        """
        Retrieve data for the specified attribute search query.

        Parameters
        ----------
        type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the result to only entities of specified types

        types : typing.Optional[str]

        attr : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One of more additional attributes to return in the response

        attrs : typing.Optional[str]

        attr_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The attribute to search

        attr_value_prefix : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The prefix for the attribute value to search

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the result to only entities tagged with the given tag

        time_range_type : typing.Optional[SearchUsingAttributeRequestTimeRangeType]
            The type of time range search, default is CUSTOM

        time_range_attr : typing.Optional[str]
            The attribute for a time range search

        time_range_start : typing.Optional[int]
            The start for a custom time range search in ms since the epoch

        time_range_end : typing.Optional[int]
            The end for a custom time range search in ms since the epoch

        sort_by : typing.Optional[str]
            An attribute to sort by

        sort_order : typing.Optional[SearchUsingAttributeRequestSortOrder]
            Sort order, either ASCENDING (default) or DESCENDING

        deleted : typing.Optional[bool]
            Whether to include deleted entities

        limit : typing.Optional[int]
            Limit the result set to only include the specified number of entries

        offset : typing.Optional[int]
            Start offset of the result set (useful for pagination)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResult
            On successful search query with some results, might return an empty list if execution succeeded without any results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.search_using_attribute()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_using_attribute(
            type=type,
            types=types,
            attr=attr,
            attrs=attrs,
            attr_name=attr_name,
            attr_value_prefix=attr_value_prefix,
            tag=tag,
            time_range_type=time_range_type,
            time_range_attr=time_range_attr,
            time_range_start=time_range_start,
            time_range_end=time_range_end,
            sort_by=sort_by,
            sort_order=sort_order,
            deleted=deleted,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def search_using_basic(
        self,
        *,
        query: typing.Optional[str] = None,
        type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        types: typing.Optional[str] = None,
        attr: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        attrs: typing.Optional[str] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        time_range_type: typing.Optional[SearchUsingBasicRequestTimeRangeType] = None,
        time_range_attr: typing.Optional[str] = None,
        time_range_start: typing.Optional[int] = None,
        time_range_end: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[SearchUsingBasicRequestSortOrder] = None,
        deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResult:
        """
        Retrieve data for the specified fulltext query.

        Parameters
        ----------
        query : typing.Optional[str]
            The full-text query

        type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the result to only entities of specified types

        types : typing.Optional[str]

        attr : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One of more additional attributes to return in the response

        attrs : typing.Optional[str]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the result to only entities with the given tag

        time_range_type : typing.Optional[SearchUsingBasicRequestTimeRangeType]
            The type of time range search, default is CUSTOM

        time_range_attr : typing.Optional[str]
            The attribute for a time range search

        time_range_start : typing.Optional[int]
            The start for a custom time range search in ms since the epoch

        time_range_end : typing.Optional[int]
            The end for a custom time range search in ms since the epoch

        sort_by : typing.Optional[str]
            An attribute to sort by

        sort_order : typing.Optional[SearchUsingBasicRequestSortOrder]
            Sort order, either ASCENDING (default) or DESCENDING

        deleted : typing.Optional[bool]
            Whether to include deleted entities

        limit : typing.Optional[int]
            Limit the result set to only include the specified number of entries

        offset : typing.Optional[int]
            Start offset of the result set (useful for pagination)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResult
            On successful fulltext query with some results, might return an empty list if execution succeeded without any results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.search_using_basic()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_using_basic(
            query=query,
            type=type,
            types=types,
            attr=attr,
            attrs=attrs,
            tag=tag,
            time_range_type=time_range_type,
            time_range_attr=time_range_attr,
            time_range_start=time_range_start,
            time_range_end=time_range_end,
            sort_by=sort_by,
            sort_order=sort_order,
            deleted=deleted,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def get_all_business_metadata_defs(
        self, *, prefix: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BusinessMetadataDefResponse]:
        """
        Bulk retrieval API for retrieving business metadata definitions.

        Parameters
        ----------
        prefix : typing.Optional[str]
            The prefix of a business metadata definition name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataDefResponse]
            The business metadata definitions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_all_business_metadata_defs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_business_metadata_defs(
            prefix=prefix, request_options=request_options
        )
        return _response.data

    async def create_business_metadata_defs(
        self,
        *,
        request: typing.Sequence[AtlasBusinessMetadataDef],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BusinessMetadataDefResponse]:
        """
        Bulk create API for business metadata definitions.

        Parameters
        ----------
        request : typing.Sequence[AtlasBusinessMetadataDef]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataDefResponse]
            The business metadata definitions. Errored business metadata definitions will have an additional error property.

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            AtlasAttributeDef,
            AtlasBusinessMetadataDef,
            AtlasConstraintDef,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.create_business_metadata_defs(
                request=[
                    AtlasBusinessMetadataDef(
                        category="PRIMITIVE",
                        guid="guid",
                        created_by="createdBy",
                        updated_by="updatedBy",
                        create_time=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        update_time=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        version=0,
                        name="name",
                        description="description",
                        type_version="typeVersion",
                        service_type="serviceType",
                        options={"key": "options"},
                        attribute_defs=[
                            AtlasAttributeDef(
                                name="name",
                                type_name="typeName",
                                is_optional=True,
                                cardinality="SINGLE",
                                values_min_count=6,
                                values_max_count=1,
                                is_unique=True,
                                is_indexable=True,
                                include_in_notification=True,
                                default_value="defaultValue",
                                description="description",
                                search_weight=5,
                                index_type="DEFAULT",
                                constraints=[
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                ],
                                options={"key": "options"},
                                display_name="displayName",
                            ),
                            AtlasAttributeDef(
                                name="name",
                                type_name="typeName",
                                is_optional=True,
                                cardinality="SINGLE",
                                values_min_count=6,
                                values_max_count=1,
                                is_unique=True,
                                is_indexable=True,
                                include_in_notification=True,
                                default_value="defaultValue",
                                description="description",
                                search_weight=5,
                                index_type="DEFAULT",
                                constraints=[
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                ],
                                options={"key": "options"},
                                display_name="displayName",
                            ),
                        ],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_business_metadata_defs(
            request=request, request_options=request_options
        )
        return _response.data

    async def update_business_metadata_defs(
        self,
        *,
        request: typing.Sequence[AtlasBusinessMetadataDef],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BusinessMetadataDefResponse]:
        """
        Bulk update API for business metadata definitions.

        Parameters
        ----------
        request : typing.Sequence[AtlasBusinessMetadataDef]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BusinessMetadataDefResponse]
            The business metadata definitions. Errored business metadata definitions will have an additional error property.

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            AtlasAttributeDef,
            AtlasBusinessMetadataDef,
            AtlasConstraintDef,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.update_business_metadata_defs(
                request=[
                    AtlasBusinessMetadataDef(
                        category="PRIMITIVE",
                        guid="guid",
                        created_by="createdBy",
                        updated_by="updatedBy",
                        create_time=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        update_time=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        version=0,
                        name="name",
                        description="description",
                        type_version="typeVersion",
                        service_type="serviceType",
                        options={"key": "options"},
                        attribute_defs=[
                            AtlasAttributeDef(
                                name="name",
                                type_name="typeName",
                                is_optional=True,
                                cardinality="SINGLE",
                                values_min_count=6,
                                values_max_count=1,
                                is_unique=True,
                                is_indexable=True,
                                include_in_notification=True,
                                default_value="defaultValue",
                                description="description",
                                search_weight=5,
                                index_type="DEFAULT",
                                constraints=[
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                ],
                                options={"key": "options"},
                                display_name="displayName",
                            ),
                            AtlasAttributeDef(
                                name="name",
                                type_name="typeName",
                                is_optional=True,
                                cardinality="SINGLE",
                                values_min_count=6,
                                values_max_count=1,
                                is_unique=True,
                                is_indexable=True,
                                include_in_notification=True,
                                default_value="defaultValue",
                                description="description",
                                search_weight=5,
                                index_type="DEFAULT",
                                constraints=[
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                ],
                                options={"key": "options"},
                                display_name="displayName",
                            ),
                        ],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_business_metadata_defs(
            request=request, request_options=request_options
        )
        return _response.data

    async def get_all_tag_defs(
        self, *, prefix: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagDefResponse]:
        """
        Bulk retrieval API for retrieving tag definitions.

        Parameters
        ----------
        prefix : typing.Optional[str]
            The prefix of a tag definition name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagDefResponse]
            The tag definitions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_all_tag_defs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_tag_defs(prefix=prefix, request_options=request_options)
        return _response.data

    async def create_tag_defs(
        self, *, request: typing.Sequence[TagDef], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagDefResponse]:
        """
        Bulk create API for tag definitions.

        Parameters
        ----------
        request : typing.Sequence[TagDef]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagDefResponse]
            The tag definitions. Errored tag definitions will have an additional error property.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AtlasAttributeDef, AtlasConstraintDef, TagDef

        client = AsyncFernApi()


        async def main() -> None:
            await client.create_tag_defs(
                request=[
                    TagDef(
                        category="PRIMITIVE",
                        guid="guid",
                        created_by="createdBy",
                        updated_by="updatedBy",
                        create_time=1000000,
                        update_time=1000000,
                        version=0,
                        name="name",
                        description="description",
                        type_version="typeVersion",
                        service_type="serviceType",
                        options={"key": "options"},
                        attribute_defs=[
                            AtlasAttributeDef(
                                name="name",
                                type_name="typeName",
                                is_optional=True,
                                cardinality="SINGLE",
                                values_min_count=6,
                                values_max_count=1,
                                is_unique=True,
                                is_indexable=True,
                                include_in_notification=True,
                                default_value="defaultValue",
                                description="description",
                                search_weight=5,
                                index_type="DEFAULT",
                                constraints=[
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                ],
                                options={"key": "options"},
                                display_name="displayName",
                            ),
                            AtlasAttributeDef(
                                name="name",
                                type_name="typeName",
                                is_optional=True,
                                cardinality="SINGLE",
                                values_min_count=6,
                                values_max_count=1,
                                is_unique=True,
                                is_indexable=True,
                                include_in_notification=True,
                                default_value="defaultValue",
                                description="description",
                                search_weight=5,
                                index_type="DEFAULT",
                                constraints=[
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                ],
                                options={"key": "options"},
                                display_name="displayName",
                            ),
                        ],
                        super_types=["superTypes", "superTypes"],
                        entity_types=["entityTypes", "entityTypes"],
                        sub_types=["subTypes", "subTypes"],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tag_defs(request=request, request_options=request_options)
        return _response.data

    async def update_tag_defs(
        self, *, request: typing.Sequence[TagDef], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TagDefResponse]:
        """
        Bulk update API for tag definitions.

        Parameters
        ----------
        request : typing.Sequence[TagDef]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagDefResponse]
            The tag definitions. Errored tag definitions will have an additional error property.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AtlasAttributeDef, AtlasConstraintDef, TagDef

        client = AsyncFernApi()


        async def main() -> None:
            await client.update_tag_defs(
                request=[
                    TagDef(
                        category="PRIMITIVE",
                        guid="guid",
                        created_by="createdBy",
                        updated_by="updatedBy",
                        create_time=1000000,
                        update_time=1000000,
                        version=0,
                        name="name",
                        description="description",
                        type_version="typeVersion",
                        service_type="serviceType",
                        options={"key": "options"},
                        attribute_defs=[
                            AtlasAttributeDef(
                                name="name",
                                type_name="typeName",
                                is_optional=True,
                                cardinality="SINGLE",
                                values_min_count=6,
                                values_max_count=1,
                                is_unique=True,
                                is_indexable=True,
                                include_in_notification=True,
                                default_value="defaultValue",
                                description="description",
                                search_weight=5,
                                index_type="DEFAULT",
                                constraints=[
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                ],
                                options={"key": "options"},
                                display_name="displayName",
                            ),
                            AtlasAttributeDef(
                                name="name",
                                type_name="typeName",
                                is_optional=True,
                                cardinality="SINGLE",
                                values_min_count=6,
                                values_max_count=1,
                                is_unique=True,
                                is_indexable=True,
                                include_in_notification=True,
                                default_value="defaultValue",
                                description="description",
                                search_weight=5,
                                index_type="DEFAULT",
                                constraints=[
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                    AtlasConstraintDef(
                                        type="type",
                                        params={"key": {"key": "value"}},
                                    ),
                                ],
                                options={"key": "options"},
                                display_name="displayName",
                            ),
                        ],
                        super_types=["superTypes", "superTypes"],
                        entity_types=["entityTypes", "entityTypes"],
                        sub_types=["subTypes", "subTypes"],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_tag_defs(request=request, request_options=request_options)
        return _response.data

    async def get_business_metadata_def_by_name(
        self, bm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AtlasBusinessMetadataDef:
        """
        Get the business metadata definition with the given name.

        Parameters
        ----------
        bm_name : str
            The name of the business metadata definition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtlasBusinessMetadataDef
            The business metadata definition

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_business_metadata_def_by_name(
                bm_name="bmName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_business_metadata_def_by_name(bm_name, request_options=request_options)
        return _response.data

    async def delete_business_metadata_def(
        self, bm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete API for business metadata definition identified by its name.

        Parameters
        ----------
        bm_name : str
            The name of the business metadata definition

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
            await client.delete_business_metadata_def(
                bm_name="bmName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_business_metadata_def(bm_name, request_options=request_options)
        return _response.data

    async def get_tag_def_by_name(
        self, tag_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TagDef:
        """
        Get the tag definition with the given name.

        Parameters
        ----------
        tag_name : str
            The name of the tag definiton

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagDef
            The tag definition

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_tag_def_by_name(
                tag_name="tagName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tag_def_by_name(tag_name, request_options=request_options)
        return _response.data

    async def delete_tag_def(self, tag_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete API for tag definition identified by its name.

        Parameters
        ----------
        tag_name : str
            The name of the tag definition

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
            await client.delete_tag_def(
                tag_name="tagName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_tag_def(tag_name, request_options=request_options)
        return _response.data

    async def put_asyncapi_parse(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get number of times the cli tool is used to import and parse the spec file

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
            await client.put_asyncapi_parse()


        asyncio.run(main())
        """
        _response = await self._raw_client.put_asyncapi_parse(request_options=request_options)
        return _response.data

    async def put_asyncapi(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get number of times the cli tool is used to export/produce the spec file

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
            await client.put_asyncapi()


        asyncio.run(main())
        """
        _response = await self._raw_client.put_asyncapi(request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
