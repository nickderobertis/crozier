

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .variable_declaration_notification import VariableDeclarationNotification
from .variables_notification_op import VariablesNotificationOp


class VariablesNotification(UniversalBaseModel):
    """
    Variable dataflow graph.

        Attributes:
            variables: Variable declarations and usage.
    """

    op: VariablesNotificationOp
    variables: typing.List[VariableDeclarationNotification]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
