import yaml

with open("config/packages/house_modes.yaml", "r") as stream:
    try:
        house_modes = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

modes = ['morning', 'daytime', 'evening', 'late_evening', 'early_night', 'late_night']
for mode in modes:
    print('----')
    for house_mode_config in house_modes['automation']:
        if 'use_blueprint' in house_mode_config:
            inputs = house_mode_config['use_blueprint']['input']
            house_mode = inputs['target_house_mode']
            if house_mode.startswith(mode):
                print(house_mode.ljust(30) + ': ' + inputs['upstairs_hallway_scene'])