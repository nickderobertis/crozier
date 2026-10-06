

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent_binding_info import AgentBindingInfo
from ..types.app_settings_info import AppSettingsInfo
from ..types.llm_options import LlmOptions
from ..types.message_response import MessageResponse
from ..types.model_config_info import ModelConfigInfo
from ..types.page_model_config_info import PageModelConfigInfo
from ..types.page_provider_info import PageProviderInfo
from ..types.provider_info import ProviderInfo
from ..types.provider_kinds_response import ProviderKindsResponse
from .raw_client import AsyncRawLlmSettingsClient, RawLlmSettingsClient
from .types.app_settings_update_latex_compiler_backend import AppSettingsUpdateLatexCompilerBackend


OMIT = typing.cast(typing.Any, ...)


class LlmSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLlmSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLlmSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLlmSettingsClient
        """
        return self._raw_client

    def list_provider_kinds(self, *, request_options: typing.Optional[RequestOptions] = None) -> ProviderKindsResponse:
        """
        返回服务商注册中心已注册的 kind 列表，供「新建服务商」表单的下拉框使用，
        新增 provider 后前端零改动。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderKindsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.list_provider_kinds()
        """
        _response = self._raw_client.list_provider_kinds(request_options=request_options)
        return _response.data

    def get_llm_options(self, *, request_options: typing.Optional[RequestOptions] = None) -> LlmOptions:
        """
        聚合返回服务商类型、Agent 角色与应用设置项元信息，使管理端表单完全由
        后端描述驱动（新增设置项 / 角色 / provider 无需改前端）。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LlmOptions
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.get_llm_options()
        """
        _response = self._raw_client.get_llm_options(request_options=request_options)
        return _response.data

    def list_providers(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageProviderInfo:
        """
        分页列出服务商（api_key 脱敏）。

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageProviderInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.list_providers()
        """
        _response = self._raw_client.list_providers(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def create_provider(
        self,
        *,
        name: str,
        kind: str,
        api_key: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        max_retries: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderInfo:
        """
        创建服务商凭据；``name`` 必须唯一。

        Parameters
        ----------
        name : str
            服务商配置名称（唯一）。

        kind : str
            服务商类型，需匹配已注册 client provider。

        api_key : typing.Optional[str]
            API Key（入库存储，响应中掩码）。

        base_url : typing.Optional[str]
            API Base URL（openai_compatible 必填；openrouter 可留空）。

        timeout : typing.Optional[int]
            请求超时（秒）。

        max_retries : typing.Optional[int]
            SDK 自动重试次数。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.create_provider(
            name="default",
            kind="openrouter",
        )
        """
        _response = self._raw_client.create_provider(
            name=name,
            kind=kind,
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            request_options=request_options,
        )
        return _response.data

    def get_provider(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderInfo:
        """
        Parameters
        ----------
        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.get_provider(
            provider_id="provider_id",
        )
        """
        _response = self._raw_client.get_provider(provider_id, request_options=request_options)
        return _response.data

    def delete_provider(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageResponse:
        """
        删除服务商；若仍被模型配置引用则拒绝。

        Parameters
        ----------
        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.delete_provider(
            provider_id="provider_id",
        )
        """
        _response = self._raw_client.delete_provider(provider_id, request_options=request_options)
        return _response.data

    def update_provider(
        self,
        provider_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        kind: typing.Optional[str] = OMIT,
        api_key: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        max_retries: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderInfo:
        """
        更新服务商；仅传入的字段会被修改（``api_key`` 留空表示保持不变）。

        Parameters
        ----------
        provider_id : str

        name : typing.Optional[str]

        kind : typing.Optional[str]

        api_key : typing.Optional[str]
            新 API Key；留空表示不修改。

        base_url : typing.Optional[str]

        timeout : typing.Optional[int]

        max_retries : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.update_provider(
            provider_id="provider_id",
        )
        """
        _response = self._raw_client.update_provider(
            provider_id,
            name=name,
            kind=kind,
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            request_options=request_options,
        )
        return _response.data

    def list_model_configs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageModelConfigInfo:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageModelConfigInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.list_model_configs()
        """
        _response = self._raw_client.list_model_configs(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def create_model_config(
        self,
        *,
        name: str,
        provider_id: str,
        model: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        streaming: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelConfigInfo:
        """
        创建模型配置；``name`` 唯一，``provider_id`` 必须存在。

        Parameters
        ----------
        name : str
            模型配置名称（唯一）。

        provider_id : str
            引用的服务商 ID。

        model : typing.Optional[str]
            模型标识（如 google/gemini-2.5-pro）。

        temperature : typing.Optional[float]
            采样温度。

        max_tokens : typing.Optional[int]
            单次生成最大 token 数。

        streaming : typing.Optional[bool]
            是否使用流式响应。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelConfigInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.create_model_config(
            name="big-default",
            provider_id="provider_id",
        )
        """
        _response = self._raw_client.create_model_config(
            name=name,
            provider_id=provider_id,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            streaming=streaming,
            request_options=request_options,
        )
        return _response.data

    def get_model_config(
        self, model_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelConfigInfo:
        """
        Parameters
        ----------
        model_config_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelConfigInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.get_model_config(
            model_config_id="model_config_id",
        )
        """
        _response = self._raw_client.get_model_config(model_config_id, request_options=request_options)
        return _response.data

    def delete_model_config(
        self, model_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageResponse:
        """
        删除模型配置；若仍被 Agent 绑定引用则拒绝。

        Parameters
        ----------
        model_config_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.delete_model_config(
            model_config_id="model_config_id",
        )
        """
        _response = self._raw_client.delete_model_config(model_config_id, request_options=request_options)
        return _response.data

    def update_model_config(
        self,
        model_config_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        provider_id: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        streaming: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelConfigInfo:
        """
        Parameters
        ----------
        model_config_id : str

        name : typing.Optional[str]

        provider_id : typing.Optional[str]

        model : typing.Optional[str]

        temperature : typing.Optional[float]

        max_tokens : typing.Optional[int]

        streaming : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelConfigInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.update_model_config(
            model_config_id="model_config_id",
        )
        """
        _response = self._raw_client.update_model_config(
            model_config_id,
            name=name,
            provider_id=provider_id,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            streaming=streaming,
            request_options=request_options,
        )
        return _response.data

    def list_bindings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AgentBindingInfo]:
        """
        列出全部权威 Agent 角色及其当前绑定的模型配置。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentBindingInfo]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.list_bindings()
        """
        _response = self._raw_client.list_bindings(request_options=request_options)
        return _response.data

    def set_binding(
        self, role: str, *, model_config_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentBindingInfo:
        """
        把指定 Agent 角色绑定到某个模型配置。

        Parameters
        ----------
        role : str

        model_config_id : str
            要绑定的模型配置 ID。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentBindingInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.set_binding(
            role="role",
            model_config_id="model_config_id",
        )
        """
        _response = self._raw_client.set_binding(role, model_config_id=model_config_id, request_options=request_options)
        return _response.data

    def get_app_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> AppSettingsInfo:
        """
        返回当前运行期应用设置（重试次数、自动编译开关、SSE 参数等）。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppSettingsInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.get_app_settings()
        """
        _response = self._raw_client.get_app_settings(request_options=request_options)
        return _response.data

    def update_app_settings(
        self,
        *,
        max_retry_count: typing.Optional[int] = OMIT,
        source_material_max_chars: typing.Optional[int] = OMIT,
        auto_compile_figures: typing.Optional[bool] = OMIT,
        auto_compile_latex: typing.Optional[bool] = OMIT,
        latex_compile_timeout: typing.Optional[int] = OMIT,
        latex_compiler_backend: typing.Optional[AppSettingsUpdateLatexCompilerBackend] = OMIT,
        latex_service_base_url: typing.Optional[str] = OMIT,
        latex_service_api_key: typing.Optional[str] = OMIT,
        latex_service_poll_interval: typing.Optional[float] = OMIT,
        latex_service_max_wait: typing.Optional[float] = OMIT,
        sse_poll_interval: typing.Optional[float] = OMIT,
        sse_max_duration: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppSettingsInfo:
        """
        更新运行期应用设置；仅传入的字段会被修改。

        Parameters
        ----------
        max_retry_count : typing.Optional[int]
            单阶段最大重试次数。

        source_material_max_chars : typing.Optional[int]
            源材料进入上下文的最大字符数。

        auto_compile_figures : typing.Optional[bool]
            是否自动编译图片 TikZ。

        auto_compile_latex : typing.Optional[bool]
            是否自动编译最终 LaTeX。

        latex_compile_timeout : typing.Optional[int]
            单次 LaTeX / TikZ 编译子进程超时（秒）。

        latex_compiler_backend : typing.Optional[AppSettingsUpdateLatexCompilerBackend]
            LaTeX 编译后端：local（本机 subprocess）或 remote（独立编译服务）。

        latex_service_base_url : typing.Optional[str]
            远程编译服务根 URL（backend=remote 时必填）。

        latex_service_api_key : typing.Optional[str]
            远程编译服务 API Key（经 Authorization: Bearer 发送）。

        latex_service_poll_interval : typing.Optional[float]
            远程编译作业状态轮询间隔（秒）。

        latex_service_max_wait : typing.Optional[float]
            远程编译作业等待终态的客户端总截止（秒）。

        sse_poll_interval : typing.Optional[float]
            SSE 进度推送轮询间隔（秒）。

        sse_max_duration : typing.Optional[float]
            SSE 连接最长存活时间（秒）。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppSettingsInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.llm_settings.update_app_settings()
        """
        _response = self._raw_client.update_app_settings(
            max_retry_count=max_retry_count,
            source_material_max_chars=source_material_max_chars,
            auto_compile_figures=auto_compile_figures,
            auto_compile_latex=auto_compile_latex,
            latex_compile_timeout=latex_compile_timeout,
            latex_compiler_backend=latex_compiler_backend,
            latex_service_base_url=latex_service_base_url,
            latex_service_api_key=latex_service_api_key,
            latex_service_poll_interval=latex_service_poll_interval,
            latex_service_max_wait=latex_service_max_wait,
            sse_poll_interval=sse_poll_interval,
            sse_max_duration=sse_max_duration,
            request_options=request_options,
        )
        return _response.data


class AsyncLlmSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLlmSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLlmSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLlmSettingsClient
        """
        return self._raw_client

    async def list_provider_kinds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderKindsResponse:
        """
        返回服务商注册中心已注册的 kind 列表，供「新建服务商」表单的下拉框使用，
        新增 provider 后前端零改动。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderKindsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.list_provider_kinds()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_provider_kinds(request_options=request_options)
        return _response.data

    async def get_llm_options(self, *, request_options: typing.Optional[RequestOptions] = None) -> LlmOptions:
        """
        聚合返回服务商类型、Agent 角色与应用设置项元信息，使管理端表单完全由
        后端描述驱动（新增设置项 / 角色 / provider 无需改前端）。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LlmOptions
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.get_llm_options()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_llm_options(request_options=request_options)
        return _response.data

    async def list_providers(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageProviderInfo:
        """
        分页列出服务商（api_key 脱敏）。

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageProviderInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.list_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_providers(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    async def create_provider(
        self,
        *,
        name: str,
        kind: str,
        api_key: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        max_retries: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderInfo:
        """
        创建服务商凭据；``name`` 必须唯一。

        Parameters
        ----------
        name : str
            服务商配置名称（唯一）。

        kind : str
            服务商类型，需匹配已注册 client provider。

        api_key : typing.Optional[str]
            API Key（入库存储，响应中掩码）。

        base_url : typing.Optional[str]
            API Base URL（openai_compatible 必填；openrouter 可留空）。

        timeout : typing.Optional[int]
            请求超时（秒）。

        max_retries : typing.Optional[int]
            SDK 自动重试次数。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.create_provider(
                name="default",
                kind="openrouter",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_provider(
            name=name,
            kind=kind,
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            request_options=request_options,
        )
        return _response.data

    async def get_provider(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderInfo:
        """
        Parameters
        ----------
        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.get_provider(
                provider_id="provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_provider(provider_id, request_options=request_options)
        return _response.data

    async def delete_provider(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageResponse:
        """
        删除服务商；若仍被模型配置引用则拒绝。

        Parameters
        ----------
        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.delete_provider(
                provider_id="provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_provider(provider_id, request_options=request_options)
        return _response.data

    async def update_provider(
        self,
        provider_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        kind: typing.Optional[str] = OMIT,
        api_key: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        max_retries: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderInfo:
        """
        更新服务商；仅传入的字段会被修改（``api_key`` 留空表示保持不变）。

        Parameters
        ----------
        provider_id : str

        name : typing.Optional[str]

        kind : typing.Optional[str]

        api_key : typing.Optional[str]
            新 API Key；留空表示不修改。

        base_url : typing.Optional[str]

        timeout : typing.Optional[int]

        max_retries : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.update_provider(
                provider_id="provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_provider(
            provider_id,
            name=name,
            kind=kind,
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            request_options=request_options,
        )
        return _response.data

    async def list_model_configs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageModelConfigInfo:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageModelConfigInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.list_model_configs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_model_configs(
            limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def create_model_config(
        self,
        *,
        name: str,
        provider_id: str,
        model: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        streaming: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelConfigInfo:
        """
        创建模型配置；``name`` 唯一，``provider_id`` 必须存在。

        Parameters
        ----------
        name : str
            模型配置名称（唯一）。

        provider_id : str
            引用的服务商 ID。

        model : typing.Optional[str]
            模型标识（如 google/gemini-2.5-pro）。

        temperature : typing.Optional[float]
            采样温度。

        max_tokens : typing.Optional[int]
            单次生成最大 token 数。

        streaming : typing.Optional[bool]
            是否使用流式响应。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelConfigInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.create_model_config(
                name="big-default",
                provider_id="provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_model_config(
            name=name,
            provider_id=provider_id,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            streaming=streaming,
            request_options=request_options,
        )
        return _response.data

    async def get_model_config(
        self, model_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelConfigInfo:
        """
        Parameters
        ----------
        model_config_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelConfigInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.get_model_config(
                model_config_id="model_config_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_model_config(model_config_id, request_options=request_options)
        return _response.data

    async def delete_model_config(
        self, model_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageResponse:
        """
        删除模型配置；若仍被 Agent 绑定引用则拒绝。

        Parameters
        ----------
        model_config_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.delete_model_config(
                model_config_id="model_config_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_model_config(model_config_id, request_options=request_options)
        return _response.data

    async def update_model_config(
        self,
        model_config_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        provider_id: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        streaming: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelConfigInfo:
        """
        Parameters
        ----------
        model_config_id : str

        name : typing.Optional[str]

        provider_id : typing.Optional[str]

        model : typing.Optional[str]

        temperature : typing.Optional[float]

        max_tokens : typing.Optional[int]

        streaming : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelConfigInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.update_model_config(
                model_config_id="model_config_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_model_config(
            model_config_id,
            name=name,
            provider_id=provider_id,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            streaming=streaming,
            request_options=request_options,
        )
        return _response.data

    async def list_bindings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AgentBindingInfo]:
        """
        列出全部权威 Agent 角色及其当前绑定的模型配置。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentBindingInfo]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.list_bindings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_bindings(request_options=request_options)
        return _response.data

    async def set_binding(
        self, role: str, *, model_config_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentBindingInfo:
        """
        把指定 Agent 角色绑定到某个模型配置。

        Parameters
        ----------
        role : str

        model_config_id : str
            要绑定的模型配置 ID。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentBindingInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.set_binding(
                role="role",
                model_config_id="model_config_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_binding(
            role, model_config_id=model_config_id, request_options=request_options
        )
        return _response.data

    async def get_app_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> AppSettingsInfo:
        """
        返回当前运行期应用设置（重试次数、自动编译开关、SSE 参数等）。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppSettingsInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.get_app_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_app_settings(request_options=request_options)
        return _response.data

    async def update_app_settings(
        self,
        *,
        max_retry_count: typing.Optional[int] = OMIT,
        source_material_max_chars: typing.Optional[int] = OMIT,
        auto_compile_figures: typing.Optional[bool] = OMIT,
        auto_compile_latex: typing.Optional[bool] = OMIT,
        latex_compile_timeout: typing.Optional[int] = OMIT,
        latex_compiler_backend: typing.Optional[AppSettingsUpdateLatexCompilerBackend] = OMIT,
        latex_service_base_url: typing.Optional[str] = OMIT,
        latex_service_api_key: typing.Optional[str] = OMIT,
        latex_service_poll_interval: typing.Optional[float] = OMIT,
        latex_service_max_wait: typing.Optional[float] = OMIT,
        sse_poll_interval: typing.Optional[float] = OMIT,
        sse_max_duration: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppSettingsInfo:
        """
        更新运行期应用设置；仅传入的字段会被修改。

        Parameters
        ----------
        max_retry_count : typing.Optional[int]
            单阶段最大重试次数。

        source_material_max_chars : typing.Optional[int]
            源材料进入上下文的最大字符数。

        auto_compile_figures : typing.Optional[bool]
            是否自动编译图片 TikZ。

        auto_compile_latex : typing.Optional[bool]
            是否自动编译最终 LaTeX。

        latex_compile_timeout : typing.Optional[int]
            单次 LaTeX / TikZ 编译子进程超时（秒）。

        latex_compiler_backend : typing.Optional[AppSettingsUpdateLatexCompilerBackend]
            LaTeX 编译后端：local（本机 subprocess）或 remote（独立编译服务）。

        latex_service_base_url : typing.Optional[str]
            远程编译服务根 URL（backend=remote 时必填）。

        latex_service_api_key : typing.Optional[str]
            远程编译服务 API Key（经 Authorization: Bearer 发送）。

        latex_service_poll_interval : typing.Optional[float]
            远程编译作业状态轮询间隔（秒）。

        latex_service_max_wait : typing.Optional[float]
            远程编译作业等待终态的客户端总截止（秒）。

        sse_poll_interval : typing.Optional[float]
            SSE 进度推送轮询间隔（秒）。

        sse_max_duration : typing.Optional[float]
            SSE 连接最长存活时间（秒）。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppSettingsInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.llm_settings.update_app_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_app_settings(
            max_retry_count=max_retry_count,
            source_material_max_chars=source_material_max_chars,
            auto_compile_figures=auto_compile_figures,
            auto_compile_latex=auto_compile_latex,
            latex_compile_timeout=latex_compile_timeout,
            latex_compiler_backend=latex_compiler_backend,
            latex_service_base_url=latex_service_base_url,
            latex_service_api_key=latex_service_api_key,
            latex_service_poll_interval=latex_service_poll_interval,
            latex_service_max_wait=latex_service_max_wait,
            sse_poll_interval=sse_poll_interval,
            sse_max_duration=sse_max_duration,
            request_options=request_options,
        )
        return _response.data
