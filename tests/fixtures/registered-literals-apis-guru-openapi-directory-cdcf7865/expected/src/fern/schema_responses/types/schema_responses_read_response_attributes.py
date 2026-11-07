

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schema_responses_read_response_attributes_reviews_state import SchemaResponsesReadResponseAttributesReviewsState


class SchemaResponsesReadResponseAttributes(UniversalBaseModel):
    """
    The properties of the Schema Response.
    """

    date_created: typing.Optional[int] = pydantic.Field(default=None)
    """
    The date the Schema Response was created
    """

    date_modified: typing.Optional[int] = pydantic.Field(default=None)
    """
    The date the Schema Response was most recently changed.
    """

    date_submitted: typing.Optional[int] = pydantic.Field(default=None)
    """
    The date the Schema Response was submitted for approval.
    """

    is_original_response: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A bool that represents whether the Schema Response is the original one that was made when the registration was created.
    """

    is_pending_current_user_approval: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A bool that represents whether the Schema Response needs the current user to approve the state transition.
    """

    reviews_state: typing.Optional[SchemaResponsesReadResponseAttributesReviewsState] = pydantic.Field(default=None)
    """
    A string that represents Schema Response state. `initial` is the state of a Schema Response on a newly registered Registration, to edit a Schema Response you must create a Schema Response Action that triggers a new submission.
    """

    revision_justification: typing.Optional[str] = pydantic.Field(default=None)
    """
    A user provided string representing the reason a new Schema Response was needed.
    """

    revision_responses: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A dictionary object representing responses to to the revision where the key is the block key for that the response. For example in the registration response `{"q1": "Answer 1"}` the block key is `q1`..
    """

    updated_response_keys: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    A list of strings which the response keys for Registration Response Blocks that were updated from the previous schema.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
