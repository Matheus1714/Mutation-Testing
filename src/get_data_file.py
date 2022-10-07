def get_data_file(file_path):
    with open(file_path, 'r') as f:
        mi = []
        dmi = []
        for line in f:
            p = line.split()
            mi_str, dmi_str = p
            mi.append(float(mi_str))
            dmi.append(float(dmi_str))
    return mi, dmi
