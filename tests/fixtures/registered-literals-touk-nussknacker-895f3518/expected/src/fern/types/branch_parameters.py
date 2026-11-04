

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .parameter import Parameter


class BranchParameters(UniversalBaseModel):
    branch_id: typing_extensions.Annotated[str, FieldMetadata(alias="branchId"), pydantic.Field(alias="branchId")]
    parameters: typing.Optional[typing.List[Parameter]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
