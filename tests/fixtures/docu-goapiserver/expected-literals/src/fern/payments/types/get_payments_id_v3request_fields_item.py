

import typing

GetPaymentsIdV3RequestFieldsItem = typing.Union[
    typing.Literal[
        "payment_id",
        "transaction_id",
        "school_id",
        "family_id",
        "family_name",
        "transaction_date",
        "amount",
        "fee_amount",
        "total_amount",
        "balance",
        "state",
        "receipt_number",
        "payment_mode",
        "payment_method_sub_kind",
        "description",
        "is_posted",
        "payd_online",
        "auto_billing",
        "created_at",
    ],
    typing.Any,
]
