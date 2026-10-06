

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact_info import ArtifactInfo
from ..types.message_response import MessageResponse
from ..types.page_task_list_item import PageTaskListItem
from ..types.task_cancel_accepted import TaskCancelAccepted
from ..types.task_compile_result import TaskCompileResult
from ..types.task_created import TaskCreated
from ..types.task_progress import TaskProgress
from ..types.task_result import TaskResult
from ..types.task_status import TaskStatus
from .raw_client import AsyncRawTasksClient, RawTasksClient
from .types.generate_request_mode import GenerateRequestMode


OMIT = typing.cast(typing.Any, ...)


class TasksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTasksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTasksClient
        """
        return self._raw_client

    def list_my_tasks(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        mode: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageTaskListItem:
        """
        分页列出调用者自己的历史任务，支持状态 / 模式 / 主题过滤与排序。

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[str]
            按状态过滤，可逗号分隔（如 running,error）。

        mode : typing.Optional[str]
            按命题模式过滤。

        q : typing.Optional[str]
            按 topic 模糊搜索。

        order : typing.Optional[str]
            按创建时间排序：ASC / DESC。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageTaskListItem
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.list_my_tasks()
        """
        _response = self._raw_client.list_my_tasks(
            limit=limit, offset=offset, status=status, mode=mode, q=q, order=order, request_options=request_options
        )
        return _response.data

    def create_task(
        self,
        *,
        topic: typing.Optional[str] = OMIT,
        source_material: typing.Optional[str] = OMIT,
        difficulty: typing.Optional[str] = OMIT,
        total_score: typing.Optional[int] = OMIT,
        mode: typing.Optional[GenerateRequestMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskCreated:
        """
        提交一个异步生成任务，立即返回 ``task_id``；通过轮询获取进度与结果。

        Parameters
        ----------
        topic : typing.Optional[str]
            物理主题；主题生成模式必填，改编类模式可留空（由源材料推断）。

        source_material : typing.Optional[str]
            源材料文本：文献摘要、原题内容或思路描述（改编类模式使用）。

        difficulty : typing.Optional[str]
            难度等级描述。

        total_score : typing.Optional[int]
            题目总分（20-80，CPhO 决赛单题主流为 40）。

        mode : typing.Optional[GenerateRequestMode]
            命题模式；留空则按是否提供 source_material 自动推断。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCreated
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.create_task()
        """
        _response = self._raw_client.create_task(
            topic=topic,
            source_material=source_material,
            difficulty=difficulty,
            total_score=total_score,
            mode=mode,
            request_options=request_options,
        )
        return _response.data

    def create_task_upload(
        self,
        *,
        file: core.File,
        difficulty: typing.Optional[str] = OMIT,
        total_score: typing.Optional[int] = OMIT,
        mode: typing.Optional[str] = OMIT,
        topic: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskCreated:
        """
        上传源材料文件并提交改编任务。

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        difficulty : typing.Optional[str]

        total_score : typing.Optional[int]

        mode : typing.Optional[str]

        topic : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCreated
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.create_task_upload()
        """
        _response = self._raw_client.create_task_upload(
            file=file,
            difficulty=difficulty,
            total_score=total_score,
            mode=mode,
            topic=topic,
            request_options=request_options,
        )
        return _response.data

    def get_task_status(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TaskStatus:
        """
        返回任务状态及完成后的摘要（裁决、token 用量、产物清单等）。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskStatus
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.get_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_task_status(task_id, request_options=request_options)
        return _response.data

    def delete_task(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> MessageResponse:
        """
        删除任务元数据与磁盘产物。运行中的任务不会被中断，仅清理记录。

        Parameters
        ----------
        task_id : str

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
        client.tasks.delete_task(
            task_id="task_id",
        )
        """
        _response = self._raw_client.delete_task(task_id, request_options=request_options)
        return _response.data

    def get_task_progress(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskProgress:
        """
        返回任务的阶段事件时间线，含每个已完成阶段的结构化产出快照。

        可在轮询任务期间调用，用于展示当前所处节点与各阶段的格式化结果
        （非模型原始输出）。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskProgress
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.get_task_progress(
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_task_progress(task_id, request_options=request_options)
        return _response.data

    def list_task_artifacts(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactInfo]:
        """
        列出任务产物文件及其大小。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactInfo]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.list_task_artifacts(
            task_id="task_id",
        )
        """
        _response = self._raw_client.list_task_artifacts(task_id, request_options=request_options)
        return _response.data

    def download_artifacts_archive(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        把任务的全部产物打包为单个 zip 流式返回，便于「一键下载全部」。

        压缩包内文件名沿用产物的磁盘名（含 ``{task_id}_assets/`` 子目录结构）。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.download_artifacts_archive(
            task_id="task_id",
        )
        """
        _response = self._raw_client.download_artifacts_archive(task_id, request_options=request_options)
        return _response.data

    def download_artifact(
        self,
        task_id: str,
        name: str,
        *,
        disposition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        下载或内联预览指定产物文件（如 ``final_latex`` / ``log`` / ``assets/fig1.pdf``）。

        响应按文件类型设置 ``Content-Type``（如 ``.pdf → application/pdf``）。默认以
        ``attachment`` 触发下载；传 ``?disposition=inline`` 则以 ``inline`` 返回，便于
        在浏览器 / iframe 中直接预览 PDF。

        Parameters
        ----------
        task_id : str

        name : str

        disposition : typing.Optional[str]
            Content-Disposition 类型：attachment=下载（默认）；inline=浏览器内联预览（如 PDF）。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            产物二进制内容（MIME 按类型设置，并附 Content-Disposition 文件名）。

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.download_artifact(
            task_id="task_id",
            name="name",
        )
        """
        with self._raw_client.download_artifact(
            task_id, name, disposition=disposition, request_options=request_options
        ) as r:
            yield from r.data

    def get_task_result(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TaskResult:
        """
        内联返回最终 LaTeX、仲裁报告文本与编译状态，便于直接消费。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.get_task_result(
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_task_result(task_id, request_options=request_options)
        return _response.data

    def compile_task(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskCompileResult:
        """
        对已生成的 ``final_latex`` 与图片 TikZ 源**重新编译**为 PDF（不调用 LLM）。

        用于生成时 ``AUTO_COMPILE_LATEX=false`` 未产出 PDF、或需刷新 PDF 的场景。
        要求任务已处于终态且存在 ``final_latex`` 产物；同一任务的编译会串行化执行。

        - 运行 / 排队中的任务（非终态）→ 409；
        - 无 ``final_latex`` 产物 → 409；
        - 已有编译在进行中 → 409。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCompileResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.compile_task(
            task_id="task_id",
        )
        """
        _response = self._raw_client.compile_task(task_id, request_options=request_options)
        return _response.data

    def cancel_task(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskCancelAccepted:
        """
        协作式取消任务。

        - 队列中尚未启动的任务会被立即标记为 ``aborted``；
        - 运行中的任务标记为 ``aborting``，工作流在下一个阶段边界停止后落为 ``aborted``。

        已处于终态（``done`` / ``error`` / ``aborted`` / ``interrupted``）的任务返回 409。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCancelAccepted
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.cancel_task(
            task_id="task_id",
        )
        """
        _response = self._raw_client.cancel_task(task_id, request_options=request_options)
        return _response.data

    def retry_task(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TaskCreated:
        """
        基于原任务的输入克隆并重新入队，返回新的 ``task_id``。

        仅 ``error`` / ``aborted`` / ``interrupted`` 终态的任务可重试；其余状态返回 409。
        原任务记录保持不变，重跑生成的是一个全新的独立任务。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCreated
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tasks.retry_task(
            task_id="task_id",
        )
        """
        _response = self._raw_client.retry_task(task_id, request_options=request_options)
        return _response.data

    def stream_task_events(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[typing.Any]:
        """
        以 Server-Sent Events 增量推送阶段事件，减少轮询。

        发送两类事件：``phase``（阶段事件，含格式化产出，结构同 ``ProgressEvent``）与
        ``status``（任务进入终态时的最终状态）。连接建立时先下发一个 ``: connected``
        注释帧。客户端在不支持时可回退到轮询 ``/progress``。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[typing.Any]
            Server-Sent Events 流。帧格式：

            - `: connected` —— 建立连接时的注释帧（心跳/就绪标记，无 event）。
            - `event: phase` —— 阶段事件帧，`data` 为 JSON，结构同 `ProgressEvent` （字段：seq / phase / phase_label / occurrence_id / round / status / output / created_at）。
            - `event: status` —— 终止帧，`data` 为 `{"status": <终态>}`（任务进入 done / error / aborted / interrupted，或被删除时 `deleted`），随后服务端关闭流。

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.tasks.stream_task_events(
            task_id="task_id",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.stream_task_events(task_id, request_options=request_options) as r:
            yield from r.data


class AsyncTasksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTasksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTasksClient
        """
        return self._raw_client

    async def list_my_tasks(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        mode: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageTaskListItem:
        """
        分页列出调用者自己的历史任务，支持状态 / 模式 / 主题过滤与排序。

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[str]
            按状态过滤，可逗号分隔（如 running,error）。

        mode : typing.Optional[str]
            按命题模式过滤。

        q : typing.Optional[str]
            按 topic 模糊搜索。

        order : typing.Optional[str]
            按创建时间排序：ASC / DESC。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageTaskListItem
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
            await client.tasks.list_my_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_my_tasks(
            limit=limit, offset=offset, status=status, mode=mode, q=q, order=order, request_options=request_options
        )
        return _response.data

    async def create_task(
        self,
        *,
        topic: typing.Optional[str] = OMIT,
        source_material: typing.Optional[str] = OMIT,
        difficulty: typing.Optional[str] = OMIT,
        total_score: typing.Optional[int] = OMIT,
        mode: typing.Optional[GenerateRequestMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskCreated:
        """
        提交一个异步生成任务，立即返回 ``task_id``；通过轮询获取进度与结果。

        Parameters
        ----------
        topic : typing.Optional[str]
            物理主题；主题生成模式必填，改编类模式可留空（由源材料推断）。

        source_material : typing.Optional[str]
            源材料文本：文献摘要、原题内容或思路描述（改编类模式使用）。

        difficulty : typing.Optional[str]
            难度等级描述。

        total_score : typing.Optional[int]
            题目总分（20-80，CPhO 决赛单题主流为 40）。

        mode : typing.Optional[GenerateRequestMode]
            命题模式；留空则按是否提供 source_material 自动推断。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCreated
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
            await client.tasks.create_task()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_task(
            topic=topic,
            source_material=source_material,
            difficulty=difficulty,
            total_score=total_score,
            mode=mode,
            request_options=request_options,
        )
        return _response.data

    async def create_task_upload(
        self,
        *,
        file: core.File,
        difficulty: typing.Optional[str] = OMIT,
        total_score: typing.Optional[int] = OMIT,
        mode: typing.Optional[str] = OMIT,
        topic: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskCreated:
        """
        上传源材料文件并提交改编任务。

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        difficulty : typing.Optional[str]

        total_score : typing.Optional[int]

        mode : typing.Optional[str]

        topic : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCreated
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
            await client.tasks.create_task_upload()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_task_upload(
            file=file,
            difficulty=difficulty,
            total_score=total_score,
            mode=mode,
            topic=topic,
            request_options=request_options,
        )
        return _response.data

    async def get_task_status(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskStatus:
        """
        返回任务状态及完成后的摘要（裁决、token 用量、产物清单等）。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskStatus
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
            await client.tasks.get_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task_status(task_id, request_options=request_options)
        return _response.data

    async def delete_task(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageResponse:
        """
        删除任务元数据与磁盘产物。运行中的任务不会被中断，仅清理记录。

        Parameters
        ----------
        task_id : str

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
            await client.tasks.delete_task(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_task(task_id, request_options=request_options)
        return _response.data

    async def get_task_progress(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskProgress:
        """
        返回任务的阶段事件时间线，含每个已完成阶段的结构化产出快照。

        可在轮询任务期间调用，用于展示当前所处节点与各阶段的格式化结果
        （非模型原始输出）。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskProgress
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
            await client.tasks.get_task_progress(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task_progress(task_id, request_options=request_options)
        return _response.data

    async def list_task_artifacts(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactInfo]:
        """
        列出任务产物文件及其大小。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactInfo]
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
            await client.tasks.list_task_artifacts(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_task_artifacts(task_id, request_options=request_options)
        return _response.data

    async def download_artifacts_archive(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        把任务的全部产物打包为单个 zip 流式返回，便于「一键下载全部」。

        压缩包内文件名沿用产物的磁盘名（含 ``{task_id}_assets/`` 子目录结构）。

        Parameters
        ----------
        task_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tasks.download_artifacts_archive(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_artifacts_archive(task_id, request_options=request_options)
        return _response.data

    async def download_artifact(
        self,
        task_id: str,
        name: str,
        *,
        disposition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        下载或内联预览指定产物文件（如 ``final_latex`` / ``log`` / ``assets/fig1.pdf``）。

        响应按文件类型设置 ``Content-Type``（如 ``.pdf → application/pdf``）。默认以
        ``attachment`` 触发下载；传 ``?disposition=inline`` 则以 ``inline`` 返回，便于
        在浏览器 / iframe 中直接预览 PDF。

        Parameters
        ----------
        task_id : str

        name : str

        disposition : typing.Optional[str]
            Content-Disposition 类型：attachment=下载（默认）；inline=浏览器内联预览（如 PDF）。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            产物二进制内容（MIME 按类型设置，并附 Content-Disposition 文件名）。

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tasks.download_artifact(
                task_id="task_id",
                name="name",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_artifact(
            task_id, name, disposition=disposition, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_task_result(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskResult:
        """
        内联返回最终 LaTeX、仲裁报告文本与编译状态，便于直接消费。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskResult
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
            await client.tasks.get_task_result(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task_result(task_id, request_options=request_options)
        return _response.data

    async def compile_task(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskCompileResult:
        """
        对已生成的 ``final_latex`` 与图片 TikZ 源**重新编译**为 PDF（不调用 LLM）。

        用于生成时 ``AUTO_COMPILE_LATEX=false`` 未产出 PDF、或需刷新 PDF 的场景。
        要求任务已处于终态且存在 ``final_latex`` 产物；同一任务的编译会串行化执行。

        - 运行 / 排队中的任务（非终态）→ 409；
        - 无 ``final_latex`` 产物 → 409；
        - 已有编译在进行中 → 409。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCompileResult
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
            await client.tasks.compile_task(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compile_task(task_id, request_options=request_options)
        return _response.data

    async def cancel_task(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskCancelAccepted:
        """
        协作式取消任务。

        - 队列中尚未启动的任务会被立即标记为 ``aborted``；
        - 运行中的任务标记为 ``aborting``，工作流在下一个阶段边界停止后落为 ``aborted``。

        已处于终态（``done`` / ``error`` / ``aborted`` / ``interrupted``）的任务返回 409。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCancelAccepted
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
            await client.tasks.cancel_task(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_task(task_id, request_options=request_options)
        return _response.data

    async def retry_task(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TaskCreated:
        """
        基于原任务的输入克隆并重新入队，返回新的 ``task_id``。

        仅 ``error`` / ``aborted`` / ``interrupted`` 终态的任务可重试；其余状态返回 409。
        原任务记录保持不变，重跑生成的是一个全新的独立任务。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCreated
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
            await client.tasks.retry_task(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retry_task(task_id, request_options=request_options)
        return _response.data

    async def stream_task_events(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[typing.Any]:
        """
        以 Server-Sent Events 增量推送阶段事件，减少轮询。

        发送两类事件：``phase``（阶段事件，含格式化产出，结构同 ``ProgressEvent``）与
        ``status``（任务进入终态时的最终状态）。连接建立时先下发一个 ``: connected``
        注释帧。客户端在不支持时可回退到轮询 ``/progress``。

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[typing.Any]
            Server-Sent Events 流。帧格式：

            - `: connected` —— 建立连接时的注释帧（心跳/就绪标记，无 event）。
            - `event: phase` —— 阶段事件帧，`data` 为 JSON，结构同 `ProgressEvent` （字段：seq / phase / phase_label / occurrence_id / round / status / output / created_at）。
            - `event: status` —— 终止帧，`data` 为 `{"status": <终态>}`（任务进入 done / error / aborted / interrupted，或被删除时 `deleted`），随后服务端关闭流。

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.tasks.stream_task_events(
                task_id="task_id",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.stream_task_events(task_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
