

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .function_type_enum_nullish import FunctionTypeEnumNullish
from .prompt_data_nullish import PromptDataNullish
from .prompt_log_id import PromptLogId


class Prompt(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the prompt
    """

    xact_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="_xact_id"),
        pydantic.Field(
            alias="_xact_id",
            description="The transaction id of an event is unique to the network operation that processed the event insertion. Transaction ids are monotonically increasing over time and can be used to retrieve a versioned snapshot of the prompt (see the `version` parameter)",
        ),
    ]
    """
    The transaction id of an event is unique to the network operation that processed the event insertion. Transaction ids are monotonically increasing over time and can be used to retrieve a versioned snapshot of the prompt (see the `version` parameter)
    """

    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the prompt belongs under
    """

    log_id: PromptLogId = pydantic.Field()
    """
    A literal 'p' which identifies the object as a project prompt
    """

    org_id: str = pydantic.Field()
    """
    Unique identifier for the organization
    """

    name: str = pydantic.Field()
    """
    Name of the prompt
    """

    slug: str = pydantic.Field()
    """
    Unique identifier for the prompt
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the prompt
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of prompt creation
    """

    prompt_data: typing.Optional[PromptDataNullish] = None
    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of tags for the prompt
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    User-controlled metadata about the prompt
    """

    function_type: typing.Optional[FunctionTypeEnumNullish] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
