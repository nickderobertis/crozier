

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .run_multitask_strategy import RunMultitaskStrategy
from .run_status import RunStatus


class Run(UniversalBaseModel):
    run_id: str = pydantic.Field()
    """
    The ID of the run.
    """

    thread_id: str = pydantic.Field()
    """
    The ID of the thread.
    """

    assistant_id: str = pydantic.Field()
    """
    The assistant that was used for this run.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The time the run was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The last time the run was updated.
    """

    status: RunStatus = pydantic.Field()
    """
    The status of the run. One of 'pending', 'running', 'error', 'success', 'timeout', 'interrupted'.
    """

    metadata: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The run metadata.
    """

    kwargs_: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="kwargs"), pydantic.Field(alias="kwargs")
    ]
    multitask_strategy: RunMultitaskStrategy = pydantic.Field()
    """
    Strategy to handle concurrent runs on the same thread.
    """

    langsmith_session_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    LangSmith tracing session (project) name for this run, when tracing is enabled at creation time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
