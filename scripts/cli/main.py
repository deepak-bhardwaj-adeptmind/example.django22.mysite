import click

from scripts.move_stores_to_jellyfish import move_stores_to_jellyfish


@click.group()
def script():
    """
    Get information on inventory
    """
    pass


@script.command()
@click.option("-ua", "--url_to_ag_id", required=True)
def migrate_to_jellyfish(url_to_ag_id):
    """
    Run direct inventory for a specific store
    """
    print("url_to_ag_id----", url_to_ag_id)
    move_stores_to_jellyfish(url_to_ag_id)


if __name__ == "__main__":
    script()
