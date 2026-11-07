

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .enricher_mock_validation_error import EnricherMockValidationError
from .map_int_non_empty_list_assertion_validation_error import MapIntNonEmptyListAssertionValidationError


class NodeTestCaseValidationErrors(UniversalBaseModel):
    enricher_mock_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[EnricherMockValidationError]],
        FieldMetadata(alias="enricherMockErrors"),
        pydantic.Field(alias="enricherMockErrors"),
    ] = None
    assertions_errors: typing_extensions.Annotated[
        typing.Optional[MapIntNonEmptyListAssertionValidationError],
        FieldMetadata(alias="assertionsErrors"),
        pydantic.Field(alias="assertionsErrors"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
