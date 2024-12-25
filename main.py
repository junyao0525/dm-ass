import subprocess
import yaml


def update_conda_environment(env_file="environment.yml"):
    try:
        print(f"Updating environment using {env_file}...")
        subprocess.check_call(["conda", "env", "update", "--file", env_file, "--prune"])
        print("Environment updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during update: {e}")
        raise


# Call the function to update the environment
update_conda_environment()