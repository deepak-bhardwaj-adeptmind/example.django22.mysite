import yaml

_path = "/Users/deepakkumar/Adeptmind/example.django22.mysite/scripts/jellyfish_domains.yaml"


def move_stores_to_jellyfish(_imap):
    _map = yaml.safe_load(open(_path))
    print("_map---", _map)
    print("_imap---", _imap)
    _map.update(eval(_imap))
    with open(_path, "w") as f:
        yaml.dump(_map, f)
