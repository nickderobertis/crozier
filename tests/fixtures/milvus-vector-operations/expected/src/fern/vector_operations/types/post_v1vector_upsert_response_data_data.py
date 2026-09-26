

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostV1VectorUpsertResponseDataData(UniversalBaseModel):
    """
    Response payload.
    """

    upsert_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="upsertCount"),
        pydantic.Field(alias="upsertCount", description="The number of upserted entities."),
    ] = None
    """
    The number of upserted entities.
    """

    upsert_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="upsertIds"),
        pydantic.Field(alias="upsertIds", description="An array of the IDs of inserted entities."),
    ] = None
    """
    An array of the IDs of inserted entities.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
