from fastapi import APIRouter

router = APIRouter()

@router.get("/app-version/")
async def app_version():
    return {"Hello": "World"}

@router.get("/service-order-list/")
async def service_order_list():
    order1 = {
        'id': 1,
        'name': 'test',
        'allFaultAmount': '5',
        'openedFaultAmount': '5',
        'clientName': 'Lerya',
        'rootStorageName': 'РЦ 5'
    }
    return [order1]

@router.get("/filters/")
async def filters():
    return []


@router.get("/order-faults/")
async def filters(orderId):
    return [
        {
            'carName': 'Car1',
            'mainDevice': {
                'brand': 'Porshe',
                'serial_number': 'HRHENEYUWNG',
                'terminal_id': 'RI436HE'
            },
            'images': [
                'https://fullhdoboi.ru/wp-content/uploads/_ph/6/218989842.jpg',
                'https://fullhdoboi.ru/wp-content/uploads/_ph/6/218989842.jpg',
                'https://fullhdoboi.ru/wp-content/uploads/_ph/6/218989842.jpg',
                'https://fullhdoboi.ru/wp-content/uploads/_ph/6/218989842.jpg',
                'https://fullhdoboi.ru/wp-content/uploads/_ph/6/218989842.jpg',
            ]
        }
    ]
