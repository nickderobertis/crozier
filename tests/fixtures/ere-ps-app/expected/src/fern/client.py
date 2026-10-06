

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .card_resource.client import AsyncCardResourceClient, CardResourceClient
    from .document_resource.client import AsyncDocumentResourceClient, DocumentResourceClient
    from .e_rezept_workflow_resource.client import AsyncERezeptWorkflowResourceClient, ERezeptWorkflowResourceClient
    from .pharmacy_resource.client import AsyncPharmacyResourceClient, PharmacyResourceClient
    from .prescription_bundle_validator_resource.client import (
        AsyncPrescriptionBundleValidatorResourceClient,
        PrescriptionBundleValidatorResourceClient,
    )
    from .preview_resource.client import AsyncPreviewResourceClient, PreviewResourceClient
    from .status_resource.client import AsyncStatusResourceClient, StatusResourceClient
    from .user_configurations_resource.client import (
        AsyncUserConfigurationsResourceClient,
        UserConfigurationsResourceClient,
    )
    from .xml_prescription_resource.client import AsyncXmlPrescriptionResourceClient, XmlPrescriptionResourceClient
    from .xslt_resource.client import AsyncXsltResourceClient, XsltResourceClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

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

    client = FernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
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
        self._card_resource: typing.Optional[CardResourceClient] = None
        self._user_configurations_resource: typing.Optional[UserConfigurationsResourceClient] = None
        self._document_resource: typing.Optional[DocumentResourceClient] = None
        self._xslt_resource: typing.Optional[XsltResourceClient] = None
        self._pharmacy_resource: typing.Optional[PharmacyResourceClient] = None
        self._preview_resource: typing.Optional[PreviewResourceClient] = None
        self._status_resource: typing.Optional[StatusResourceClient] = None
        self._prescription_bundle_validator_resource: typing.Optional[PrescriptionBundleValidatorResourceClient] = None
        self._e_rezept_workflow_resource: typing.Optional[ERezeptWorkflowResourceClient] = None
        self._xml_prescription_resource: typing.Optional[XmlPrescriptionResourceClient] = None

    @property
    def card_resource(self):
        if self._card_resource is None:
            from .card_resource.client import CardResourceClient

            self._card_resource = CardResourceClient(client_wrapper=self._client_wrapper)
        return self._card_resource

    @property
    def user_configurations_resource(self):
        if self._user_configurations_resource is None:
            from .user_configurations_resource.client import UserConfigurationsResourceClient

            self._user_configurations_resource = UserConfigurationsResourceClient(client_wrapper=self._client_wrapper)
        return self._user_configurations_resource

    @property
    def document_resource(self):
        if self._document_resource is None:
            from .document_resource.client import DocumentResourceClient

            self._document_resource = DocumentResourceClient(client_wrapper=self._client_wrapper)
        return self._document_resource

    @property
    def xslt_resource(self):
        if self._xslt_resource is None:
            from .xslt_resource.client import XsltResourceClient

            self._xslt_resource = XsltResourceClient(client_wrapper=self._client_wrapper)
        return self._xslt_resource

    @property
    def pharmacy_resource(self):
        if self._pharmacy_resource is None:
            from .pharmacy_resource.client import PharmacyResourceClient

            self._pharmacy_resource = PharmacyResourceClient(client_wrapper=self._client_wrapper)
        return self._pharmacy_resource

    @property
    def preview_resource(self):
        if self._preview_resource is None:
            from .preview_resource.client import PreviewResourceClient

            self._preview_resource = PreviewResourceClient(client_wrapper=self._client_wrapper)
        return self._preview_resource

    @property
    def status_resource(self):
        if self._status_resource is None:
            from .status_resource.client import StatusResourceClient

            self._status_resource = StatusResourceClient(client_wrapper=self._client_wrapper)
        return self._status_resource

    @property
    def prescription_bundle_validator_resource(self):
        if self._prescription_bundle_validator_resource is None:
            from .prescription_bundle_validator_resource.client import (
                PrescriptionBundleValidatorResourceClient,
            )

            self._prescription_bundle_validator_resource = PrescriptionBundleValidatorResourceClient(
                client_wrapper=self._client_wrapper
            )
        return self._prescription_bundle_validator_resource

    @property
    def e_rezept_workflow_resource(self):
        if self._e_rezept_workflow_resource is None:
            from .e_rezept_workflow_resource.client import ERezeptWorkflowResourceClient

            self._e_rezept_workflow_resource = ERezeptWorkflowResourceClient(client_wrapper=self._client_wrapper)
        return self._e_rezept_workflow_resource

    @property
    def xml_prescription_resource(self):
        if self._xml_prescription_resource is None:
            from .xml_prescription_resource.client import XmlPrescriptionResourceClient

            self._xml_prescription_resource = XmlPrescriptionResourceClient(client_wrapper=self._client_wrapper)
        return self._xml_prescription_resource


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
    base_url : str
        The base url to use for requests from the client.

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

    client = AsyncFernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
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
        self._card_resource: typing.Optional[AsyncCardResourceClient] = None
        self._user_configurations_resource: typing.Optional[AsyncUserConfigurationsResourceClient] = None
        self._document_resource: typing.Optional[AsyncDocumentResourceClient] = None
        self._xslt_resource: typing.Optional[AsyncXsltResourceClient] = None
        self._pharmacy_resource: typing.Optional[AsyncPharmacyResourceClient] = None
        self._preview_resource: typing.Optional[AsyncPreviewResourceClient] = None
        self._status_resource: typing.Optional[AsyncStatusResourceClient] = None
        self._prescription_bundle_validator_resource: typing.Optional[
            AsyncPrescriptionBundleValidatorResourceClient
        ] = None
        self._e_rezept_workflow_resource: typing.Optional[AsyncERezeptWorkflowResourceClient] = None
        self._xml_prescription_resource: typing.Optional[AsyncXmlPrescriptionResourceClient] = None

    @property
    def card_resource(self):
        if self._card_resource is None:
            from .card_resource.client import AsyncCardResourceClient

            self._card_resource = AsyncCardResourceClient(client_wrapper=self._client_wrapper)
        return self._card_resource

    @property
    def user_configurations_resource(self):
        if self._user_configurations_resource is None:
            from .user_configurations_resource.client import AsyncUserConfigurationsResourceClient

            self._user_configurations_resource = AsyncUserConfigurationsResourceClient(
                client_wrapper=self._client_wrapper
            )
        return self._user_configurations_resource

    @property
    def document_resource(self):
        if self._document_resource is None:
            from .document_resource.client import AsyncDocumentResourceClient

            self._document_resource = AsyncDocumentResourceClient(client_wrapper=self._client_wrapper)
        return self._document_resource

    @property
    def xslt_resource(self):
        if self._xslt_resource is None:
            from .xslt_resource.client import AsyncXsltResourceClient

            self._xslt_resource = AsyncXsltResourceClient(client_wrapper=self._client_wrapper)
        return self._xslt_resource

    @property
    def pharmacy_resource(self):
        if self._pharmacy_resource is None:
            from .pharmacy_resource.client import AsyncPharmacyResourceClient

            self._pharmacy_resource = AsyncPharmacyResourceClient(client_wrapper=self._client_wrapper)
        return self._pharmacy_resource

    @property
    def preview_resource(self):
        if self._preview_resource is None:
            from .preview_resource.client import AsyncPreviewResourceClient

            self._preview_resource = AsyncPreviewResourceClient(client_wrapper=self._client_wrapper)
        return self._preview_resource

    @property
    def status_resource(self):
        if self._status_resource is None:
            from .status_resource.client import AsyncStatusResourceClient

            self._status_resource = AsyncStatusResourceClient(client_wrapper=self._client_wrapper)
        return self._status_resource

    @property
    def prescription_bundle_validator_resource(self):
        if self._prescription_bundle_validator_resource is None:
            from .prescription_bundle_validator_resource.client import (
                AsyncPrescriptionBundleValidatorResourceClient,
            )

            self._prescription_bundle_validator_resource = AsyncPrescriptionBundleValidatorResourceClient(
                client_wrapper=self._client_wrapper
            )
        return self._prescription_bundle_validator_resource

    @property
    def e_rezept_workflow_resource(self):
        if self._e_rezept_workflow_resource is None:
            from .e_rezept_workflow_resource.client import AsyncERezeptWorkflowResourceClient

            self._e_rezept_workflow_resource = AsyncERezeptWorkflowResourceClient(client_wrapper=self._client_wrapper)
        return self._e_rezept_workflow_resource

    @property
    def xml_prescription_resource(self):
        if self._xml_prescription_resource is None:
            from .xml_prescription_resource.client import AsyncXmlPrescriptionResourceClient

            self._xml_prescription_resource = AsyncXmlPrescriptionResourceClient(client_wrapper=self._client_wrapper)
        return self._xml_prescription_resource
