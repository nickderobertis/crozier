

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RejectedTransitionCriterionDto(UniversalBaseModel):
    transition_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="transitionName"),
        pydantic.Field(alias="transitionName", description="The name of the transition"),
    ]
    """
    The name of the transition
    """

    criterion: str = pydantic.Field()
    """
    The name of the criterion
    """

    reason: str = pydantic.Field()
    """
    The reason why the criterion returned false
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
