

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.workflow import Workflow
from .raw_client import AsyncRawWorkflowcontrollerClient, RawWorkflowcontrollerClient


OMIT = typing.cast(typing.Any, ...)


class WorkflowcontrollerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkflowcontrollerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkflowcontrollerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkflowcontrollerClient
        """
        return self._raw_client

    def startworkflow(
        self,
        id: str,
        *,
        input: typing.Dict[str, typing.Any],
        workflow_version: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """


        | Permissions |
        | ------- |
        | ExecuteWorkflow   |
        | 5   |

        Parameters
        ----------
        id : str

        input : typing.Dict[str, typing.Any]

        workflow_version : typing.Optional[float]

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
        )
        client.workflowcontroller.startworkflow(
            id="id",
            input={"key": "value"},
        )
        """
        _response = self._raw_client.startworkflow(
            id, input=input, workflow_version=workflow_version, request_options=request_options
        )
        return _response.data

    def deleteversionbyid(
        self, id: str, version: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        | Permissions |
        | ------- |
        | DeleteWorkflow   |
        | 4   |

        Parameters
        ----------
        id : str

        version : float

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
        )
        client.workflowcontroller.deleteversionbyid(
            id="id",
            version=1.1,
        )
        """
        _response = self._raw_client.deleteversionbyid(id, version, request_options=request_options)
        return _response.data

    def count(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        | Permissions |
        | ------- |
        | ViewWorkflow   |
        | 1   |

        Parameters
        ----------
        id : str

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
        )
        client.workflowcontroller.count(
            id="id",
        )
        """
        _response = self._raw_client.count(id, request_options=request_options)
        return _response.data

    def deletebyid(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        | Permissions |
        | ------- |
        | DeleteWorkflow   |
        | 4   |

        Parameters
        ----------
        id : str

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
        )
        client.workflowcontroller.deletebyid(
            id="id",
        )
        """
        _response = self._raw_client.deletebyid(id, request_options=request_options)
        return _response.data

    def updatebyid(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        bpmn_file: typing.Optional[str] = OMIT,
        input_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """


        | Permissions |
        | ------- |
        | UpdateWorkflow   |
        | 3   |

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        bpmn_file : typing.Optional[str]

        input_schema : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

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
        )
        client.workflowcontroller.updatebyid(
            id="id",
        )
        """
        _response = self._raw_client.updatebyid(
            id,
            name=name,
            bpmn_file=bpmn_file,
            input_schema=input_schema,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def find(
        self, *, filter: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Workflow]:
        """


        | Permissions |
        | ------- |
        | ViewWorkflow   |
        | 1   |

        Parameters
        ----------
        filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Workflow]
            Array of Workflow model instances

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workflowcontroller.find()
        """
        _response = self._raw_client.find(filter=filter, request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        name: str,
        bpmn_file: str,
        input_schema: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Workflow:
        """


        | Permissions |
        | ------- |
        | CreateWorkflow   |
        | 2   |

        Parameters
        ----------
        name : str

        bpmn_file : str

        input_schema : typing.Dict[str, typing.Any]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Workflow
            Workflow model instance

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workflowcontroller.create(
            name="name",
            bpmn_file="bpmnFile",
            input_schema={"key": "value"},
        )
        """
        _response = self._raw_client.create(
            name=name,
            bpmn_file=bpmn_file,
            input_schema=input_schema,
            description=description,
            request_options=request_options,
        )
        return _response.data


class AsyncWorkflowcontrollerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkflowcontrollerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkflowcontrollerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkflowcontrollerClient
        """
        return self._raw_client

    async def startworkflow(
        self,
        id: str,
        *,
        input: typing.Dict[str, typing.Any],
        workflow_version: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """


        | Permissions |
        | ------- |
        | ExecuteWorkflow   |
        | 5   |

        Parameters
        ----------
        id : str

        input : typing.Dict[str, typing.Any]

        workflow_version : typing.Optional[float]

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
        )


        async def main() -> None:
            await client.workflowcontroller.startworkflow(
                id="id",
                input={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.startworkflow(
            id, input=input, workflow_version=workflow_version, request_options=request_options
        )
        return _response.data

    async def deleteversionbyid(
        self, id: str, version: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        | Permissions |
        | ------- |
        | DeleteWorkflow   |
        | 4   |

        Parameters
        ----------
        id : str

        version : float

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
        )


        async def main() -> None:
            await client.workflowcontroller.deleteversionbyid(
                id="id",
                version=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteversionbyid(id, version, request_options=request_options)
        return _response.data

    async def count(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        | Permissions |
        | ------- |
        | ViewWorkflow   |
        | 1   |

        Parameters
        ----------
        id : str

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
        )


        async def main() -> None:
            await client.workflowcontroller.count(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.count(id, request_options=request_options)
        return _response.data

    async def deletebyid(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        | Permissions |
        | ------- |
        | DeleteWorkflow   |
        | 4   |

        Parameters
        ----------
        id : str

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
        )


        async def main() -> None:
            await client.workflowcontroller.deletebyid(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletebyid(id, request_options=request_options)
        return _response.data

    async def updatebyid(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        bpmn_file: typing.Optional[str] = OMIT,
        input_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """


        | Permissions |
        | ------- |
        | UpdateWorkflow   |
        | 3   |

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        bpmn_file : typing.Optional[str]

        input_schema : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

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
        )


        async def main() -> None:
            await client.workflowcontroller.updatebyid(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatebyid(
            id,
            name=name,
            bpmn_file=bpmn_file,
            input_schema=input_schema,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def find(
        self, *, filter: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Workflow]:
        """


        | Permissions |
        | ------- |
        | ViewWorkflow   |
        | 1   |

        Parameters
        ----------
        filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Workflow]
            Array of Workflow model instances

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workflowcontroller.find()


        asyncio.run(main())
        """
        _response = await self._raw_client.find(filter=filter, request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        name: str,
        bpmn_file: str,
        input_schema: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Workflow:
        """


        | Permissions |
        | ------- |
        | CreateWorkflow   |
        | 2   |

        Parameters
        ----------
        name : str

        bpmn_file : str

        input_schema : typing.Dict[str, typing.Any]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Workflow
            Workflow model instance

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workflowcontroller.create(
                name="name",
                bpmn_file="bpmnFile",
                input_schema={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            name=name,
            bpmn_file=bpmn_file,
            input_schema=input_schema,
            description=description,
            request_options=request_options,
        )
        return _response.data
