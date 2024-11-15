import os
import shutil
import time
import hashlib

def calculate_md5(file_path):
    """Calculate MD5 checksum for a given file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def synchronize_folders(source, replica, log_file):
    """Synchronize the replica folder to match the source folder."""
    if not os.path.exists(source):
        os.makedirs(source)
        log_action(log_file, f"Created source directory: {source}")

    if not os.path.exists(replica):
        os.makedirs(replica)
        log_action(log_file, f"Created replica directory: {replica}")

    # Copy and update files from source to replica
    for root, dirs, files in os.walk(source):
        relative_path = os.path.relpath(root, source)
        replica_path = os.path.join(replica, relative_path)

        if not os.path.exists(replica_path):
            os.makedirs(replica_path)
            log_action(log_file, f"Created directory: {replica_path}")

        for file_name in files:
            source_file = os.path.join(root, file_name)
            
            # Add _replica suffix to the filename
            file_name_without_ext, file_ext = os.path.splitext(file_name)
            file_name_replica = f"{file_name_without_ext}_replica{file_ext}"
            
            replica_file = os.path.join(replica_path, file_name_replica)

            if not os.path.exists(replica_file) or calculate_md5(source_file) != calculate_md5(replica_file):
                shutil.copy2(source_file, replica_file)
                log_action(log_file, f"Copied/Updated file: {source_file} to {replica_file}")

    # Remove files and directories that are not in the source
    for root, dirs, files in os.walk(replica):
        relative_path = os.path.relpath(root, replica)
        source_path = os.path.join(source, relative_path)

        if not os.path.exists(source_path):
            shutil.rmtree(root)
            log_action(log_file, f"Removed directory: {root}")
            continue

        for file_name in files:
            # Check for the original name pattern with the _replica suffix
            file_name_without_ext, file_ext = os.path.splitext(file_name)
            if not file_name_without_ext.endswith("_replica"):
                continue  # Skip files without the _replica suffix

            original_file_name = f"{file_name_without_ext[:-8]}{file_ext}"  # Remove _replica suffix
            source_file = os.path.join(source_path, original_file_name)
            replica_file = os.path.join(root, file_name)

            if not os.path.exists(source_file):
                os.remove(replica_file)
                log_action(log_file, f"Removed file: {replica_file}")

def log_action(log_file, message):
    """Log an action to both the log file and console."""
    with open(log_file, "a") as log:
        log.write(f"{message}\n")
    print(message)

def main():
    # Set up the paths for the folder structure
    source = os.path.join(os.getcwd(), "source")
    replica = os.path.join(os.getcwd(), "replica")
    log_file = os.path.join(os.getcwd(), "log.txt")
    interval = 10  # Synchronization interval in seconds

    # Run the synchronization periodically
    while True:
        synchronize_folders(source, replica, log_file)
        time.sleep(interval)

if __name__ == "__main__":
    main()
