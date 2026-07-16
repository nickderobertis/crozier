

import typing

from .console_data_exporter_config import ConsoleDataExporterConfig
from .custom_data_exporter_config import CustomDataExporterConfig
from .elastic_config import ElasticConfig
from .file_data_exporter_config import FileDataExporterConfig
from .kafka_config import KafkaConfig
from .mailer_console_exporter_config import MailerConsoleExporterConfig
from .mailer_generic_exporter_config import MailerGenericExporterConfig
from .mailer_mailgun_exporter_config import MailerMailgunExporterConfig
from .mailer_mailjet_exporter_config import MailerMailjetExporterConfig
from .mailer_sendgrid_exporter_config import MailerSendgridExporterConfig
from .pulsar_data_exporter_config import PulsarDataExporterConfig

DataExporterConfigConfig = typing.Union[
    ElasticConfig,
    KafkaConfig,
    PulsarDataExporterConfig,
    FileDataExporterConfig,
    MailerGenericExporterConfig,
    MailerConsoleExporterConfig,
    MailerMailgunExporterConfig,
    MailerMailjetExporterConfig,
    MailerSendgridExporterConfig,
    ConsoleDataExporterConfig,
    CustomDataExporterConfig,
]
