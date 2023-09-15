"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass

from .utils.retries import RetryConfig


SERVER_PROD = 'prod'
r"""Hosted API"""
SERVER_LOCAL = 'local'
r"""Development server"""
SERVERS = {
	SERVER_PROD: 'https://api.unstructured.io',
	SERVER_LOCAL: 'http://localhost:8000',
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: requests.Session
    security_client: requests.Session
    server_url: str = ''
    server: str = ''
    language: str = 'python'
    openapi_doc_version: str = '0.0.1'
    sdk_version: str = '0.1.3'
    gen_version: str = '2.115.2'
    retry_config: RetryConfig = None

    def get_server_details(self) -> tuple[str, dict[str, str]]:
        if self.server_url:
            return self.server_url.removesuffix('/'), {}
        if not self.server:
            self.server = SERVER_PROD

        return SERVERS[self.server], {}
