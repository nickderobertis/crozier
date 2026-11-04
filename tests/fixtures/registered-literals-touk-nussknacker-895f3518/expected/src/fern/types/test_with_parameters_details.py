

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TestWithParametersDetails(UniversalBaseModel):
    source_parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="sourceParameters"),
        pydantic.Field(alias="sourceParameters"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
