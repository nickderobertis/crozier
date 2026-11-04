

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.config_map import ConfigMap
from ..types.plugin import Plugin
from ..types.plugin_list import PluginList
from ..types.setting import Setting
from .types.install_plugin_request_source import InstallPluginRequestSource
from .types.upgrade_plugin_request_source import UpgradePluginRequestSource
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPluginV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_plugins(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PluginList]:
        """
        List plugins using query criteria and sort params

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword of plugin display name or description

        enabled : typing.Optional[bool]
            Whether the plugin is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PluginList]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/plugins",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "keyword": keyword,
                "enabled": enabled,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PluginList,
                    parse_obj_as(
                        type_=PluginList,
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

    def fetch_css_bundle(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Compatibility alias for the UI plugin CSS bundle.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/plugins/-/bundle.css",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def fetch_js_bundle(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Compatibility alias for the UI plugin JS bundle.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/plugins/-/bundle.js",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def install_plugin_from_uri(
        self, *, uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Plugin]:
        """
        Install a plugin from uri.

        Parameters
        ----------
        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Plugin]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/plugins/-/install-from-uri",
            method="POST",
            json={
                "uri": uri,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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

    def install_plugin(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        preset_name: typing.Optional[str] = OMIT,
        source: typing.Optional[InstallPluginRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Plugin]:
        """
        Install a plugin by uploading a Jar file.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        preset_name : typing.Optional[str]
            Plugin preset name. Halo finds the plugin from plugin presets.

        source : typing.Optional[InstallPluginRequestSource]
            Install source. Defaults to file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Plugin]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/plugins/install",
            method="POST",
            data={
                "presetName": preset_name,
                "source": source,
            },
            files={
                **({"file": file} if file is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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

    def fetch_plugin_json_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Fetch converted json config of plugin by configured configMapName.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose JSON config will be fetched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/json-config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def update_plugin_json_config(
        self,
        name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Update the config of plugin setting.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose JSON config will be updated.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/json-config",
            method="PUT",
            json=request,
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

    def change_plugin_running_state(
        self,
        name: str,
        *,
        enable: bool,
        async_: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Plugin]:
        """
        Change the running state of a plugin by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose running state will be changed.

        enable : bool
            Whether the plugin should be enabled.

        async_ : typing.Optional[bool]
            Whether to change the state asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Plugin]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/plugin-state",
            method="PUT",
            json={
                "async": async_,
                "enable": enable,
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
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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

    def reload_plugin(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Plugin]:
        """
        Reload a plugin by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of the plugin to reload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Plugin]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/reload",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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

    def reset_plugin_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConfigMap]:
        """
        Reset the configMap of plugin setting.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose setting config will be reset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigMap]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/reset-config",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigMap,
                    parse_obj_as(
                        type_=ConfigMap,
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

    def fetch_plugin_setting(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Setting]:
        """
        Fetch setting of plugin.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose setting will be fetched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Setting]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/setting",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Setting,
                    parse_obj_as(
                        type_=Setting,
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

    def upgrade_plugin(
        self,
        name: str,
        *,
        file: typing.Optional[core.File] = OMIT,
        preset_name: typing.Optional[str] = OMIT,
        source: typing.Optional[UpgradePluginRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Plugin]:
        """
        Upgrade a plugin by uploading a Jar file

        Parameters
        ----------
        name : str
            metadata.name of the plugin to upgrade.

        file : typing.Optional[core.File]
            See core.File for more documentation

        preset_name : typing.Optional[str]
            Plugin preset name. Halo finds the plugin from plugin presets.

        source : typing.Optional[UpgradePluginRequestSource]
            Install source. Defaults to file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Plugin]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/upgrade",
            method="POST",
            data={
                "presetName": preset_name,
                "source": source,
            },
            files={
                **({"file": file} if file is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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

    def upgrade_plugin_from_uri(
        self, name: str, *, uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Plugin]:
        """
        Upgrade a plugin from uri.

        Parameters
        ----------
        name : str
            metadata.name of the plugin to upgrade.

        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Plugin]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/upgrade-from-uri",
            method="POST",
            json={
                "uri": uri,
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
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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


class AsyncRawPluginV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_plugins(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PluginList]:
        """
        List plugins using query criteria and sort params

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword of plugin display name or description

        enabled : typing.Optional[bool]
            Whether the plugin is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PluginList]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/plugins",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "keyword": keyword,
                "enabled": enabled,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PluginList,
                    parse_obj_as(
                        type_=PluginList,
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

    async def fetch_css_bundle(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Compatibility alias for the UI plugin CSS bundle.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/plugins/-/bundle.css",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def fetch_js_bundle(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Compatibility alias for the UI plugin JS bundle.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/plugins/-/bundle.js",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def install_plugin_from_uri(
        self, *, uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Plugin]:
        """
        Install a plugin from uri.

        Parameters
        ----------
        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Plugin]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/plugins/-/install-from-uri",
            method="POST",
            json={
                "uri": uri,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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

    async def install_plugin(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        preset_name: typing.Optional[str] = OMIT,
        source: typing.Optional[InstallPluginRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Plugin]:
        """
        Install a plugin by uploading a Jar file.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        preset_name : typing.Optional[str]
            Plugin preset name. Halo finds the plugin from plugin presets.

        source : typing.Optional[InstallPluginRequestSource]
            Install source. Defaults to file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Plugin]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/plugins/install",
            method="POST",
            data={
                "presetName": preset_name,
                "source": source,
            },
            files={
                **({"file": file} if file is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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

    async def fetch_plugin_json_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Fetch converted json config of plugin by configured configMapName.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose JSON config will be fetched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/json-config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def update_plugin_json_config(
        self,
        name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Update the config of plugin setting.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose JSON config will be updated.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/json-config",
            method="PUT",
            json=request,
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

    async def change_plugin_running_state(
        self,
        name: str,
        *,
        enable: bool,
        async_: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Plugin]:
        """
        Change the running state of a plugin by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose running state will be changed.

        enable : bool
            Whether the plugin should be enabled.

        async_ : typing.Optional[bool]
            Whether to change the state asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Plugin]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/plugin-state",
            method="PUT",
            json={
                "async": async_,
                "enable": enable,
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
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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

    async def reload_plugin(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Plugin]:
        """
        Reload a plugin by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of the plugin to reload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Plugin]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/reload",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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

    async def reset_plugin_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConfigMap]:
        """
        Reset the configMap of plugin setting.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose setting config will be reset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigMap]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/reset-config",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigMap,
                    parse_obj_as(
                        type_=ConfigMap,
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

    async def fetch_plugin_setting(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Setting]:
        """
        Fetch setting of plugin.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose setting will be fetched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Setting]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/setting",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Setting,
                    parse_obj_as(
                        type_=Setting,
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

    async def upgrade_plugin(
        self,
        name: str,
        *,
        file: typing.Optional[core.File] = OMIT,
        preset_name: typing.Optional[str] = OMIT,
        source: typing.Optional[UpgradePluginRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Plugin]:
        """
        Upgrade a plugin by uploading a Jar file

        Parameters
        ----------
        name : str
            metadata.name of the plugin to upgrade.

        file : typing.Optional[core.File]
            See core.File for more documentation

        preset_name : typing.Optional[str]
            Plugin preset name. Halo finds the plugin from plugin presets.

        source : typing.Optional[UpgradePluginRequestSource]
            Install source. Defaults to file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Plugin]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/upgrade",
            method="POST",
            data={
                "presetName": preset_name,
                "source": source,
            },
            files={
                **({"file": file} if file is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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

    async def upgrade_plugin_from_uri(
        self, name: str, *, uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Plugin]:
        """
        Upgrade a plugin from uri.

        Parameters
        ----------
        name : str
            metadata.name of the plugin to upgrade.

        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Plugin]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/plugins/{encode_path_param(name)}/upgrade-from-uri",
            method="POST",
            json={
                "uri": uri,
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
                    Plugin,
                    parse_obj_as(
                        type_=Plugin,
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
