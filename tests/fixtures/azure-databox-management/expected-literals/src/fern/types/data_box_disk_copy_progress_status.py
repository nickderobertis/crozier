

import typing

DataBoxDiskCopyProgressStatus = typing.Union[
    typing.Literal[
        "NotStarted",
        "InProgress",
        "Completed",
        "CompletedWithErrors",
        "Failed",
        "NotReturned",
        "HardwareError",
        "DeviceFormatted",
        "DeviceMetadataModified",
        "StorageAccountNotAccessible",
        "UnsupportedData",
    ],
    typing.Any,
]
