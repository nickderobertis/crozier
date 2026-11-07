

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.task_directive_object import TaskDirectiveObject
from ...types.taskforce_object import TaskforceObject


class GetV1TmsPendingStarterTaskforcesResponseMqprofiles(UniversalBaseModel):
    taskforce: typing.Optional[TaskforceObject] = None
    task_directive: typing.Optional[TaskDirectiveObject] = None
    mqprofiles: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    MQ profiles relevant to this taskforce. See https://observation-management-service.github.io/ewms-docs/apis/_generated/mqs-objects.html#mqprofileobject.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
