

import typing

FieldQuestionType = typing.Union[
    typing.Literal[
        "INPUT_TEXT",
        "INPUT_NUMBER",
        "INPUT_EMAIL",
        "INPUT_LINK",
        "INPUT_PHONE_NUMBER",
        "INPUT_DATE",
        "INPUT_TIME",
        "TEXTAREA",
        "RATING",
        "LINEAR_SCALE",
        "CHECKBOX",
        "MULTIPLE_CHOICE_OPTION",
        "DROPDOWN_OPTION",
        "RANKING_OPTION",
        "MULTI_SELECT_OPTION",
        "HIDDEN_FIELDS",
        "CALCULATED_FIELDS",
    ],
    typing.Any,
]
