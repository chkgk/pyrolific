from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_secret import CreateSecret
from ...models.secret_detail import SecretDetail
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CreateSecret
) -> Dict[str, Any]:
    url = "{}/api/v1/hooks/secrets/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SecretDetail]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SecretDetail.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SecretDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateSecret,
    
) -> Response[SecretDetail]:
    """Create/replace a secret

     Generate a secret for verifying the request signature header of the subscription payload. If a
    secret already exists, this call will delete the old secret and create a new one.

    Args:
        
        json_body (CreateSecret):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretDetail]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CreateSecret,
    
) -> Optional[SecretDetail]:
    """Create/replace a secret

     Generate a secret for verifying the request signature header of the subscription payload. If a
    secret already exists, this call will delete the old secret and create a new one.

    Args:
        
        json_body (CreateSecret):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretDetail
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateSecret,
    
) -> Response[SecretDetail]:
    """Create/replace a secret

     Generate a secret for verifying the request signature header of the subscription payload. If a
    secret already exists, this call will delete the old secret and create a new one.

    Args:
        
        json_body (CreateSecret):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretDetail]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CreateSecret,
    
) -> Optional[SecretDetail]:
    """Create/replace a secret

     Generate a secret for verifying the request signature header of the subscription payload. If a
    secret already exists, this call will delete the old secret and create a new one.

    Args:
        
        json_body (CreateSecret):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            
        )
    ).parsed
