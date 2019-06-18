def write(operation):
    with open(log_path, "a") as f:
        f.writelines(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        f.writelines(",")
        f.writelines(operation)
        f.writelines("\n")
