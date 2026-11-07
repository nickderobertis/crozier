

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReferencedDocketNumber(UniversalBaseModel):
    """
    Object consisiting of each docket entry number and its corresponding API call.
    """

    docket_entries_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="docketEntriesAPI"),
        pydantic.Field(
            alias="docketEntriesAPI",
            description="Link to Docket Entries API with the current docket number. The response of this API will give all the primary documents and secondary documents that are associated to it.",
        ),
    ] = None
    """
    Link to Docket Entries API with the current docket number. The response of this API will give all the primary documents and secondary documents that are associated to it.
    """

    docket_number: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="docketNumber"),
        pydantic.Field(alias="docketNumber", description="Each referenced docket number"),
    ]
    """
    Each referenced docket number
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
