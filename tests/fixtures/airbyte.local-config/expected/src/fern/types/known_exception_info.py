

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class KnownExceptionInfo(UniversalBaseModel):
    exception_class_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="exceptionClassName")
    ] = None
    exception_stack: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="exceptionStack")
    ] = None
    message: str
    root_cause_exception_class_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rootCauseExceptionClassName")
    ] = None
    root_cause_exception_stack: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="rootCauseExceptionStack")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
