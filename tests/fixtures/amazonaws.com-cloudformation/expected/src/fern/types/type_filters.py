

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .type_filters_category import TypeFiltersCategory


class TypeFilters(UniversalBaseModel):
    """
    Filter criteria to use in determining which extensions to return.
    """

    category: typing_extensions.Annotated[
        typing.Optional[TypeFiltersCategory],
        FieldMetadata(alias="Category"),
        pydantic.Field(
            alias="Category",
            description="<p>The category of extensions to return.</p> <ul> <li> <p> <code>REGISTERED</code>: Private extensions that have been registered for this account and region.</p> </li> <li> <p> <code>ACTIVATED</code>: Public extensions that have been activated for this account and region.</p> </li> <li> <p> <code>THIRD_PARTY</code>: Extensions available for use from publishers other than Amazon. This includes:</p> <ul> <li> <p>Private extensions registered in the account.</p> </li> <li> <p>Public extensions from publishers other than Amazon, whether activated or not.</p> </li> </ul> </li> <li> <p> <code>AWS_TYPES</code>: Extensions available for use from Amazon.</p> </li> </ul>",
        ),
    ] = None
    """
    <p>The category of extensions to return.</p> <ul> <li> <p> <code>REGISTERED</code>: Private extensions that have been registered for this account and region.</p> </li> <li> <p> <code>ACTIVATED</code>: Public extensions that have been activated for this account and region.</p> </li> <li> <p> <code>THIRD_PARTY</code>: Extensions available for use from publishers other than Amazon. This includes:</p> <ul> <li> <p>Private extensions registered in the account.</p> </li> <li> <p>Public extensions from publishers other than Amazon, whether activated or not.</p> </li> </ul> </li> <li> <p> <code>AWS_TYPES</code>: Extensions available for use from Amazon.</p> </li> </ul>
    """

    publisher_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublisherId"),
        pydantic.Field(
            alias="PublisherId",
            description="<p>The id of the publisher of the extension.</p> <p>Extensions published by Amazon aren't assigned a publisher ID. Use the <code>AWS_TYPES</code> category to specify a list of types published by Amazon.</p>",
        ),
    ] = None
    """
    <p>The id of the publisher of the extension.</p> <p>Extensions published by Amazon aren't assigned a publisher ID. Use the <code>AWS_TYPES</code> category to specify a list of types published by Amazon.</p>
    """

    type_name_prefix: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeNamePrefix"),
        pydantic.Field(alias="TypeNamePrefix", description="A prefix to use as a filter for results."),
    ] = None
    """
    A prefix to use as a filter for results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
