from functools import cache

def read_mapping(f):
    mapping = {}

    f.readline()

    while " " in (line := f.readline()):
        dest, source, r = [int(x) for x in line.strip().split()]
        mapping[source] = (dest, r)

    return mapping


def get_dest(mapping, source):
    for s, (d, r) in mapping.items():
        if s <= source <= s + r:
            return d + (source - s)

    return source

locations = []

with open("input.txt") as f:
    seeds = [int(x) for x in f.readline().strip().split(": ")[1].split()]
    f.readline()

    seed_to_soil = read_mapping(f)
    soil_to_fert = read_mapping(f)
    fert_to_water = read_mapping(f)
    water_to_light = read_mapping(f)
    light_to_temp = read_mapping(f)
    temp_to_humidity = read_mapping(f)
    humidity_to_location = read_mapping(f)

    @cache
    def get_loc(idx):
        return get_dest(
                    humidity_to_location,
                    get_dest(
                        temp_to_humidity,
                        get_dest(
                            light_to_temp,
                            get_dest(
                                water_to_light,
                                get_dest(
                                    fert_to_water,
                                    get_dest(
                                        soil_to_fert,
                                        get_dest(
                                            seed_to_soil,
                                            idx
                                        )
                                    )
                                )
                            )
                        )
                    )
                )


    for i in range(0, len(seeds), 2):
        print(f"{i} / {len(seeds)}")
        for j in range(seeds[i], seeds[i] + seeds[i + 1] + 1):
            locations.append(get_loc(j))


print(min(locations))
