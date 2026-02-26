def ping_pong(sounds):
    sounds = sounds.split("-")

    bad_pings = bad_pongs = 0
    last_bad_shot = None

    for i in range(1, len(sounds)):
        if sounds[i] not in ("ping", "pong"):
            if sounds[i - 1] == "ping":
                bad_pings += 1
                last_bad_shot = "ping"
            elif sounds[i - 1] == "pong":
                bad_pongs += 1
                last_bad_shot = "pong"

    pings = sounds.count("ping") - bad_pings
    pongs = sounds.count("pong") - bad_pongs

    if pings > pongs:
        return "ping"
    if pongs > pings:
        return "pong"

    return "pong" if last_bad_shot == "ping" else "ping"


def main():
    r = ping_pong("ping-pong-ding-pong-ping-donk-ping-thud")
    print(r)


if __name__ == "__main__":
    main()


"""

def ping_pong(sounds):
    shots = sounds.split("-")
    bad_pings = bad_pongs = 0
    last_bad_shot = None

    for prev, curr in zip(shots, shots[1:]):
        if curr not in ("ping", "pong"):
            if prev == "ping":
                bad_pings += 1
                last_bad_shot = "ping"
            elif prev == "pong":
                bad_pongs += 1
                last_bad_shot = "pong"

    pings = shots.count("ping") - bad_pings
    pongs = shots.count("pong") - bad_pongs

    if pings > pongs: return "ping"
    if pongs > pings: return "pong"
    return "pong" if last_bad_shot == "ping" else "ping"

"""
