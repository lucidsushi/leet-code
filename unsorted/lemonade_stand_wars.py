# send message / receive message

from trio import run, serve_tcp
from json import loads, dumps

async def server(stream):

    # what constitues a game tick?

    supplies_cost = {
        'lemons': 10,
        'sugar': 5
    }

    response = {
        'supplies': supplies_cost
    }

    def purchase(order_json):
        orders = {}
        for order in order_json['data']:
            orders[order] = supplies_cost[order] * order.get('amount')
        
        return orders

    request_payload = {
        'purchase': purchase
    }

    while True:
        data = await stream.receive_some(4096)
        if data:
            try:
                print(type(data))
                payload = loads(data.decode())
            except Exception:
                result = {'status': 'error'}
            else:
                result = {
                    'status': 'ok',
                    'payload': payload,
                    'response': request_payload.get(payload.get('action')(payload))
                }
            # {
            #     'action': 'purchase'
            #     'data': {
            #         'lemons': 5
            #     }
            # }
            await stream.send_all(dumps(result, indent=2).encode())

async def main():
    print('Awaiting connections…')
    await serve_tcp(server, 5000)

run(main)

# test with:
# $ netcat localhost 5000