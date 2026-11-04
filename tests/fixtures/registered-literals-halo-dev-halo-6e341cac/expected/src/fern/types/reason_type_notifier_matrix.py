

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notifier_info import NotifierInfo
from .reason_type_info import ReasonTypeInfo


class ReasonTypeNotifierMatrix(UniversalBaseModel):
    """
    Matrix describing which notifiers are enabled for each reason type.
    """

    notifiers: typing.List[NotifierInfo] = pydantic.Field()
    """
    Notification notifiers available to the user.
    """

    reason_types: typing_extensions.Annotated[
        typing.List[ReasonTypeInfo],
        FieldMetadata(alias="reasonTypes"),
        pydantic.Field(alias="reasonTypes", description="Reason types available to the user."),
    ]
    """
    Reason types available to the user.
    """

    state_matrix: typing_extensions.Annotated[
        typing.List[typing.List[bool]],
        FieldMetadata(alias="stateMatrix"),
        pydantic.Field(alias="stateMatrix", description="Enabled-state matrix indexed by reason type and notifier."),
    ]
    """
    Enabled-state matrix indexed by reason type and notifier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
