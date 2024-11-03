def dpt_to_array(file_path):

    try:
        with open(file_path, "r") as f:

            file_name = file_path.split("/")[-1]
            file_extension = file_name.split(".")[-1]

            if file_extension != "dpt":
                raise ValueError(f"\n--> The file \'{file_name}\' is not a \'.dpt\' file. <--")
            else:
                data = f.readlines()
            f.close()

    except FileNotFoundError:
        raise FileNotFoundError(f"The provided file path \'{file_path}\' does not point to a valid file")
    
    res = []

    for i in data:
        point = i.split(",")
        try:
            wavenumber = float(point[0])
        except ValueError:
            raise ValueError(f"{file_name} contains incorrect data.\nFound {point[0]} in line {data.index(i)}")

        try:
            ab = float(point[1].strip())
        except ValueError:
            raise ValueError(f"{file_name} contains incorrect data.\nFound {point[0]} in line {data.index(i)}")

        res.append((wavenumber, ab))

    return res
