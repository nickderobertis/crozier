

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CheckAssetForWorkOrdersGetResponse(UniversalBaseModel):
    display_result: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayResult"),
        pydantic.Field(alias="displayResult", description="The list of work orders in html format"),
    ] = None
    """
    The list of work orders in html format
    """

    json_result: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jsonResult"),
        pydantic.Field(alias="jsonResult", description="The list of work orders in json format"),
    ] = None
    """
    The list of work orders in json format
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
