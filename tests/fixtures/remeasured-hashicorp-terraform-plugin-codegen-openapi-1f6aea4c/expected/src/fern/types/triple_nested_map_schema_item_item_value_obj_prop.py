

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TripleNestedMapSchemaItemItemValueObjProp(UniversalBaseModel):
    """
    Object inside a map!
    """

    number_prop: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number inside a map!
    """

    ignore_me2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ignore_me_2"),
        pydantic.Field(alias="ignore_me_2", description="This property will be ignored!"),
    ] = None
    """
    This property will be ignored!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
