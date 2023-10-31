import yaml

_path = "/Users/deepakkumar/Adeptmind/example.django22.mysite/scripts/jellyfish_domains.yaml"


def move_stores_to_jellyfish(_imap):
    _map = yaml.safe_load(_path)
    output = _map | _imap
    _map.update(_imap)
    with open(_path, "w") as f:
        yaml.dump(output, f)
