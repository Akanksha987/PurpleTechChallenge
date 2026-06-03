ZONES = {
    "SKINCARE": [
        (100, 100),
        (400, 100),
        (400, 300),
        (100, 300)
    ],

    "BILLING": [
        (500, 100),
        (700, 100),
        (700, 300),
        (500, 300)
    ]
}


def get_zone(x, y):

    skincare = ZONES["SKINCARE"]

    if (
        skincare[0][0] <= x <= skincare[1][0]
        and
        skincare[0][1] <= y <= skincare[2][1]
    ):
        return "SKINCARE"

    billing = ZONES["BILLING"]

    if (
        billing[0][0] <= x <= billing[1][0]
        and
        billing[0][1] <= y <= billing[2][1]
    ):
        return "BILLING"

    return None