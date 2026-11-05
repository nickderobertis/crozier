

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .any_value import AnyValue
from .metric import Metric


class Meta(UniversalBaseModel):
    metrics: typing.Optional[typing.List[Metric]] = None
    puid: typing.Optional[str] = None
    request_path: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="requestPath"), pydantic.Field(alias="requestPath")
    ] = None
    routing: typing.Optional[typing.Dict[str, int]] = None
    tags: typing.Optional[typing.Dict[str, AnyValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
