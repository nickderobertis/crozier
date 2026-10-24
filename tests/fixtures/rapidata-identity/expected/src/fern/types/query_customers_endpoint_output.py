

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QueryCustomersEndpointOutput(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique identifier of the customer.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address of the customer.
    """

    organization_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="organizationName"),
        pydantic.Field(
            alias="organizationName", description="The name of the organization this customer belongs to, if any."
        ),
    ] = None
    """
    The name of the organization this customer belongs to, if any.
    """

    organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="organizationId"),
        pydantic.Field(
            alias="organizationId", description="The identifier of the organization this customer belongs to, if any."
        ),
    ] = None
    """
    The identifier of the organization this customer belongs to, if any.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
