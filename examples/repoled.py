[
    {
        "id": "55b327ce.cf7f08",
        "type": "change",
        "z": "a1573d38.2a66d",
        "name": "change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 435,
        "y": 215,
        "wires": [
            [
                "acb33fc.5854bc",
                "f890af17.80fdd"
            ]
        ]
    },
    {
        "id": "91d4de10.d551b",
        "type": "change",
        "z": "a1573d38.2a66d",
        "name": "change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 413,
        "y": 276,
        "wires": [
            [
                "acb33fc.5854bc",
                "f890af17.80fdd"
            ]
        ]
    },
    {
        "id": "f90aa738.672858",
        "type": "switch",
        "z": "a1573d38.2a66d",
        "name": "if button is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "num"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 230,
        "y": 260,
        "wires": [
            [
                "55b327ce.cf7f08"
            ],
            [
                "91d4de10.d551b"
            ]
        ]
    },
    {
        "id": "acb33fc.5854bc",
        "type": "debug",
        "z": "a1573d38.2a66d",
        "name": "",
        "active": false,
        "console": "false",
        "complete": "payload",
        "x": 726,
        "y": 321,
        "wires": []
    },
    {
        "id": "b8d6e2e1.a9177",
        "type": "rpi-gpio in",
        "z": "a1573d38.2a66d",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 70,
        "y": 280,
        "wires": [
            [
                "f90aa738.672858"
            ]
        ]
    },
    {
        "id": "f890af17.80fdd",
        "type": "rpi-gpio out",
        "z": "a1573d38.2a66d",
        "name": "LED",
        "pin": "11",
        "set": true,
        "level": "1",
        "freq": "",
        "out": "out",
        "x": 710,
        "y": 200,
        "wires": []
    }
]
