import googleapiclient.discovery
from google.cloud import secretmanager

def access_secret(secret_name):
    client = secretmanager.SecretManagerServiceClient()
    project_id = "my-gcp-project"  # Reemplaza con tu Project ID

    secret_path = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=secret_path)
    
    return response.payload.data.decode("UTF-8")

def start_compute_instance(event, context):
    project = access_secret("PROJECT_ID")
    zone = access_secret("ZONE")
    instance_name = access_secret("INSTANCE_NAME")

    compute = googleapiclient.discovery.build("compute", "v1")

    print(f"🔹 Encendiendo la VM: {instance_name} en {project}/{zone}...")

    request = compute.instances().start(project=project, zone=zone, instance=instance_name)
    response = request.execute()

    print(f"✅ VM {instance_name} encendida: {response}")
