

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pay_run import PayRun


class PayRuns(UniversalBaseModel):
    pay_runs: typing_extensions.Annotated[
        typing.Optional[typing.List[PayRun]], FieldMetadata(alias="PayRuns"), pydantic.Field(alias="PayRuns")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
