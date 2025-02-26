import os
import googleapiclient.discovery


def stop_compute_instance(event, context):
    project = os.getenv("PROJECT_ID")
    zone = os.getenv("ZONE")
    instance_name = os.getenv("INSTANCE_NAME")

    compute = googleapiclient.discovery.build("compute", "v1")

    print(f"🔹 Apagando la VM: {instance_name} en {project}/{zone}...")

    request = compute.instances().stop(project=project, zone=zone, instance=instance_name)
    response = request.execute()

    print(f"✅ VM {instance_name} apagada: {response}")