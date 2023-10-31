import click

from scripts.move_stores_to_jellyfish import move_stores_to_jellyfish


@click.group()
def script():
    """
    Get information on inventory
    """
    pass


# @script.command()
# @click.option("-e", "--env", default="local", help="environment to use")
# @k8s_option
# def register(env: str, k8: bool):
#     """
#     Register direct inventory flows with Prefect
#     """
#     for project, store_data in get_project_to_store_id_inventory_map().items():
#         for store_id in store_data:
#             tags = [
#                 TagValues.k8s,
#                 TagValues.mall,
#                 TagValues.direct_inventory,
#                 TagValues.high_priority,
#                 get_validate_client_tag(project),
#             ]
#             infra_overrides = {}
#             if store_id in BIG_STORES:
#                 tags.append(TagValues.big_store)
#                 infra_overrides = Kubernetes.get_high_memory_overrides()
# 
#             deployment_name = f"direct-inventory-update-{project}-{store_id}"
#             deployment_builder = DeploymentBuilder(
#                 flow=direct_inventory_update,
#                 deployment_name=deployment_name,
#                 parameters={"project": project, "store_id": store_id},
#                 tags=tags,
#                 schedule=(CronSchedule(cron="0 */4 * * *", timezone="Canada/Eastern")),
#                 work_queue_name=WorkQueues.mall_kube_jobs,
#             )
# 
#             is_kube = env == "kube" or k8
# 
#             if is_kube:
#                 apply_deployment(deployment_builder.kubernetes(infra_overrides=infra_overrides))
#             else:
#                 apply_deployment(deployment_builder.local())


@script.command()
@click.option("-ua", "--url_to_ag_id", required=True)
def migrate_to_jellyfish(url_to_ag_id):
    """
    Run direct inventory for a specific store
    """
    print("url_to_ag_id----", url_to_ag_id)
    # move_stores_to_jellyfish(url_to_ag_id)


if __name__ == "__main__":
    script()
