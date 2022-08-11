from typing import Optional
from urllib.parse import urlsplit

from racetrack_client.client_config.client_config import ClientConfig


DEFAULT_LIFECYCLE_SCHEME = 'https'
DEFAULT_LIFECYCLE_PATH = '/lifecycle'


def resolve_lifecycle_url(client_config: ClientConfig, lifecycle_name: Optional[str]) -> str:
    """
    Get full URL of Lifecycle based on given short name.
    If aliased name is found, resolve it to full URL it's pointing to.
    If the name was not provided, return default URL.
    """
    short_url = _resolve_short_lifecycle_url(client_config, lifecycle_name)
    return _infer_full_lifecycle_url(short_url)


def _resolve_short_lifecycle_url(client_config: ClientConfig, lifecycle_name: Optional[str]) -> str:
    if not lifecycle_name:
        return client_config.lifecycle_url
    if lifecycle_name in client_config.lifecycle_url_aliases:
        return client_config.lifecycle_url_aliases[lifecycle_name]
    return lifecycle_name


def _infer_full_lifecycle_url(url: str) -> str:
    """Apply default protocol and path if not provided."""
    split = urlsplit(url)
    if split.netloc == '':
        split = split._replace(scheme='', netloc=split.scheme)
    if not split.scheme:
        url = f'{DEFAULT_LIFECYCLE_SCHEME}://{url}'
    split = urlsplit(url)  # parse again as path is recognized properly only with a scheme
    path = split.path if split.netloc else ''
    if not path:
        url = url + DEFAULT_LIFECYCLE_PATH
    return url
