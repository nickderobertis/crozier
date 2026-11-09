

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cause_of_action import CauseOfAction
from .cause_of_action_additional_data import CauseOfActionAdditionalData


class CaseCauseOfAction(UniversalBaseModel):
    cause_of_action: typing_extensions.Annotated[
        typing.Optional[CauseOfAction], FieldMetadata(alias="causeOfAction"), pydantic.Field(alias="causeOfAction")
    ] = None
    cause_of_action_additional_data_array: typing_extensions.Annotated[
        typing.List[CauseOfActionAdditionalData],
        FieldMetadata(alias="causeOfActionAdditionalDataArray"),
        pydantic.Field(alias="causeOfActionAdditionalDataArray"),
    ]
    object: str = pydantic.Field()
    """
    Name of the object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
