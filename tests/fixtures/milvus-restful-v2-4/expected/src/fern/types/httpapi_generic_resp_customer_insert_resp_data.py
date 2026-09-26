

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HttpapiGenericRespCustomerInsertRespData(UniversalBaseModel):
    insert_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="insertCount"),
        pydantic.Field(alias="insertCount", description="The number of inserted entities."),
    ] = None
    """
    The number of inserted entities.
    """

    insert_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="insertIds"),
        pydantic.Field(alias="insertIds", description="An array of the IDs of inserted entities."),
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
