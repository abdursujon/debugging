"""
Traffic light simulation of two street namely oxford road and market_street
ns: north south
ew: east-west
"""

oxford_road = {"ns": "green", "ns_y": "yellow", "ew": "red"}
market_street = {"ns": "red", "ns_y": "yellow", "ew": "green"}
vanilla_road = {"ns": "green", "ns_y": "green", "ew": "green"}


def switch_lights(stop_light):
    for key in stop_light.keys():
        if stop_light[key] == "green":
            stop_light[key] = "yellow"
        elif stop_light[key] == "yellow":
            stop_light[key] = "red"
        elif stop_light[key] == "red":
            stop_light[key] = "green"
    assert "red" in stop_light.values(), "Fatal error, neither light is red! " + str(
        stop_light
    )
    assert "green" in stop_light.values(), (
        "Caution, neither light is green, expect a lot of traffic! " + str(stop_light)
    )
    assert "yellow" in stop_light.values(), (
        "Caution, neither light turns yellow, pedestrian might be run into by vehicle! "
        + str(stop_light)
    )


switch_lights(oxford_road)
switch_lights(market_street)
switch_lights(vanilla_road)
