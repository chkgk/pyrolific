from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.subscription_detail import SubscriptionDetail
from ...models.subscription_update_detail import SubscriptionUpdateDetail
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    *,
    client: Client,
    json_body: SubscriptionUpdateDetail,
    
) -> Dict[str, Any]:
    url = "{}/api/v1/hooks/subscriptions/{subscription_id}/".format(client.base_url, subscription_id=subscription_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SubscriptionDetail]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SubscriptionDetail.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SubscriptionDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    *,
    client: Client,
    json_body: SubscriptionUpdateDetail,
    
) -> Response[SubscriptionDetail]:
    """Update a subscription

     This allows you to update a subscription. For example you can temporarily disable a subscription if
    you wish.

    Args:
        subscription_id (str):
        
        json_body (SubscriptionUpdateDetail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionDetail]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
        json_body=json_body,
        
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: Client,
    json_body: SubscriptionUpdateDetail,
    
) -> Optional[SubscriptionDetail]:
    """Update a subscription

     This allows you to update a subscription. For example you can temporarily disable a subscription if
    you wish.

    Args:
        subscription_id (str):
        
        json_body (SubscriptionUpdateDetail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionDetail
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        json_body=json_body,
        
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: Client,
    json_body: SubscriptionUpdateDetail,
    
) -> Response[SubscriptionDetail]:
    """Update a subscription

     This allows you to update a subscription. For example you can temporarily disable a subscription if
    you wish.

    Args:
        subscription_id (str):
        
        json_body (SubscriptionUpdateDetail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionDetail]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
        json_body=json_body,
        
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: Client,
    json_body: SubscriptionUpdateDetail,
    
) -> Optional[SubscriptionDetail]:
    """Update a subscription

     This allows you to update a subscription. For example you can temporarily disable a subscription if
    you wish.

    Args:
        subscription_id (str):
        
        json_body (SubscriptionUpdateDetail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionDetail
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            json_body=json_body,
            
        )
    ).parsed
