

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NullTypeDirect(UniversalBaseModel):
    """
    Model with a property whose type is the bare 'null' type (OAS 3.1). The generator should treat this as a nullable Object.
    """

    id: typing.Optional[int] = None
    always_null: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="alwaysNull"),
        pydantic.Field(
            alias="alwaysNull",
            description="This property can only ever be null.  In OAS 3.1 you express that with `type: null`.  The C# generator must map this to a nullable Object.",
        ),
    ] = None
    """
    This property can only ever be null.  In OAS 3.1 you express that with `type: null`.  The C# generator must map this to a nullable Object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
