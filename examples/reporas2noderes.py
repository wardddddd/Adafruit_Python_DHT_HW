[
    {
        "id": "5325db9d.4d89d4",
        "type": "http request",
        "z": "7be881c5.af82f",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/D2FTGJIk/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 570,
        "y": 180,
        "wires": [
            [
                "d81423d.4b7e6e",
                "6ee07025.dd092"
            ]
        ]
    },
    {
        "id": "a48aae75.cb47f",
        "type": "inject",
        "z": "7be881c5.af82f",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 110,
        "y": 180,
        "wires": [
            [
                "2a253cb8.087484"
            ]
        ]
    },
    {
        "id": "2a253cb8.087484",
        "type": "function",
        "z": "7be881c5.af82f",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"V0NalioIfisUZAVo\"\n    };\n\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 180,
        "wires": [
            [
                "5325db9d.4d89d4"
            ]
        ]
    },
    {
        "id": "d81423d.4b7e6e",
        "type": "http response",
        "z": "7be881c5.af82f",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 770,
        "y": 160,
        "wires": []
    },
    {
        "id": "6ee07025.dd092",
        "type": "debug",
        "z": "7be881c5.af82f",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 795.8828125,
        "y": 279.37890625,
        "wires": []
    }
]
