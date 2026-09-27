

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PutMockserverDiffResponse(UniversalBaseModel):
    diff_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="diffCount"), pydantic.Field(alias="diffCount")
    ] = None
    identical: typing.Optional[bool] = None
    diffs: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
