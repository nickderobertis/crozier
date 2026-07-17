

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ActorCatalogWithUpdatedAt(UniversalBaseModel):
    """
    A source actor catalog with the timestamp it was mostly recently updated
    """

    catalog: typing.Optional[typing.Dict[str, typing.Any]] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
