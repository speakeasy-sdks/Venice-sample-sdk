"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from speakeasybar import utils
from typing import Optional

class SubscribeToWebhooksRequestBodyWebhook(str, Enum):
    STOCK_UPDATE = 'stockUpdate'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SubscribeToWebhooksRequestBody:
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    webhook: Optional[SubscribeToWebhooksRequestBodyWebhook] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class SubscribeToWebhooksResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""An unknown error occurred interacting with the API."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

