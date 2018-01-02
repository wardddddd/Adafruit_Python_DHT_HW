[
    {
        "id": "2925123a.866e6e",
        "type": "inject",
        "z": "b3b479d.c1ed388",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "1",
        "crontab": "",
        "once": true,
        "x": 190,
        "y": 220,
        "wires": [
            [
                "2fff76a2.c3388a"
            ]
        ]
    },
    {
        "id": "2fff76a2.c3388a",
        "type": "function",
        "z": "b3b479d.c1ed388",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"V0NalioIfisUZAVo\"\n    };\nmsg.payload= \"Humidity,,73\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 380,
        "y": 220,
        "wires": [
            [
                "e8e2c912.e42f88"
            ]
        ]
    },
    {
        "id": "e8e2c912.e42f88",
        "type": "http request",
        "z": "b3b479d.c1ed388",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/D2FTGJIk/datapoints.csv",
        "tls": "",
        "x": 548,
        "y": 219,
        "wires": [
            [
                "fd1aeac1.289828",
                "dae1f850.c37c58"
            ]
        ]
    },
    {
        "id": "fd1aeac1.289828",
        "type": "debug",
        "z": "b3b479d.c1ed388",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 716,
        "y": 312,
        "wires": []
    },
    {
        "id": "dae1f850.c37c58",
        "type": "http response",
        "z": "b3b479d.c1ed388",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 772.640625,
        "y": 197.328125,
        "wires": []
    }
]
