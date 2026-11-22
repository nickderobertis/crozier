

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RegionTarget(UniversalBaseModel):
    region: str = pydantic.Field()
    """
    The region the clone is placed in.
    """

    share_with: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="shareWith"), pydantic.Field(alias="shareWith")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
