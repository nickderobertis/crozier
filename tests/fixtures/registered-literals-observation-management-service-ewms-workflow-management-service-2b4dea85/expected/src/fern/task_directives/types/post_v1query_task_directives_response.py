

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.query_next_after import QueryNextAfter
from ...types.task_directive_object import TaskDirectiveObject


class PostV1QueryTaskDirectivesResponse(UniversalBaseModel):
    task_directives: typing.List[TaskDirectiveObject] = pydantic.Field()
    """
    A list of task directive objects. Entries may not be unique if query included a 'projection'.
    """

    next_after: typing.Optional[QueryNextAfter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
