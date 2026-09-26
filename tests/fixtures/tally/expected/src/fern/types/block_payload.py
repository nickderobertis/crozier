

import typing

from .calculated_fields_payload import CalculatedFieldsPayload
from .captcha_payload import CaptchaPayload
from .checkbox_payload import CheckboxPayload
from .conditional_logic_payload import ConditionalLogicPayload
from .divider_payload import DividerPayload
from .dropdown_option_payload import DropdownOptionPayload
from .embed_audio_payload import EmbedAudioPayload
from .embed_payload import EmbedPayload
from .embed_video_payload import EmbedVideoPayload
from .file_upload_payload import FileUploadPayload
from .form_title_payload import FormTitlePayload
from .heading1payload import Heading1Payload
from .heading2payload import Heading2Payload
from .heading3payload import Heading3Payload
from .hidden_fields_payload import HiddenFieldsPayload
from .image_payload import ImagePayload
from .input_date_payload import InputDatePayload
from .input_email_payload import InputEmailPayload
from .input_link_payload import InputLinkPayload
from .input_number_payload import InputNumberPayload
from .input_phone_number_payload import InputPhoneNumberPayload
from .input_text_payload import InputTextPayload
from .input_time_payload import InputTimePayload
from .label_payload import LabelPayload
from .linear_scale_payload import LinearScalePayload
from .matrix_column_payload import MatrixColumnPayload
from .matrix_payload import MatrixPayload
from .matrix_row_payload import MatrixRowPayload
from .multi_select_option_payload import MultiSelectOptionPayload
from .multiple_choice_option_payload import MultipleChoiceOptionPayload
from .page_break_payload import PageBreakPayload
from .payment_payload import PaymentPayload
from .question_payload import QuestionPayload
from .ranking_option_payload import RankingOptionPayload
from .rating_payload import RatingPayload
from .respondent_country_payload import RespondentCountryPayload
from .signature_payload import SignaturePayload
from .text_payload import TextPayload
from .textarea_payload import TextareaPayload
from .title_payload import TitlePayload
from .wallet_connect_payload import WalletConnectPayload

BlockPayload = typing.Union[
    FormTitlePayload,
    TextPayload,
    LabelPayload,
    TitlePayload,
    Heading1Payload,
    Heading2Payload,
    Heading3Payload,
    DividerPayload,
    PageBreakPayload,
    ImagePayload,
    EmbedPayload,
    EmbedVideoPayload,
    EmbedAudioPayload,
    QuestionPayload,
    MatrixPayload,
    InputTextPayload,
    InputNumberPayload,
    InputEmailPayload,
    InputLinkPayload,
    InputPhoneNumberPayload,
    InputDatePayload,
    InputTimePayload,
    TextareaPayload,
    FileUploadPayload,
    LinearScalePayload,
    RatingPayload,
    HiddenFieldsPayload,
    MultipleChoiceOptionPayload,
    CheckboxPayload,
    DropdownOptionPayload,
    RankingOptionPayload,
    MultiSelectOptionPayload,
    PaymentPayload,
    SignaturePayload,
    MatrixRowPayload,
    MatrixColumnPayload,
    WalletConnectPayload,
    ConditionalLogicPayload,
    CalculatedFieldsPayload,
    CaptchaPayload,
    RespondentCountryPayload,
]
