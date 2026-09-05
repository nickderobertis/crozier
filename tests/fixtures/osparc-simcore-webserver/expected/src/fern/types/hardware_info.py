

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HardwareInfo(UniversalBaseModel):
    aws_ec2instances: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="aws_ec2_instances"), pydantic.Field(alias="aws_ec2_instances")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
