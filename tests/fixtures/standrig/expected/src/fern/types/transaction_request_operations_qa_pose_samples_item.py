

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TransactionRequestOperationsQaPoseSamplesItem(UniversalBaseModel):
    pose_id: typing_extensions.Annotated[str, FieldMetadata(alias="poseId"), pydantic.Field(alias="poseId")]
    values: typing.Dict[str, float]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
