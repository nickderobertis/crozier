

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetBaseSliceDesResponseItem(UniversalBaseModel):
    """
    A list of base slice descriptors
    """

    db_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="DB_ID"), pydantic.Field(alias="DB_ID")
    ] = None
    slice_des_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Slice_des_ID"), pydantic.Field(alias="Slice_des_ID")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
