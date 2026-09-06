

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_eval_parent_object_id_object_type import RunEvalParentObjectIdObjectType
from .run_eval_parent_object_id_row_ids import RunEvalParentObjectIdRowIds


class RunEvalParentObjectId(UniversalBaseModel):
    """
    Span parent properties
    """

    object_type: RunEvalParentObjectIdObjectType
    object_id: str = pydantic.Field()
    """
    The id of the container object you are logging to
    """

    row_ids: typing.Optional[RunEvalParentObjectIdRowIds] = pydantic.Field(default=None)
    """
    Identifiers for the row to to log a subspan under
    """

    propagated_event: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Include these properties in every span created under this parent
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
