def repair_mpeg_file(input_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    # Find Pack Header
    pack_header_index = data.find(b'\x00\x00\x01\xBA')
    if pack_header_index == -1:
        print("Pack Header not found.")
        return

    # Find Group of Pictures
    group_of_pictures_index = data.find(b'\x00\x00\x01\xB8', pack_header_index)
    if group_of_pictures_index == -1:
        print("Group of Pictures not found.")
        return

    # Delete data before Pack Header
    data = data[pack_header_index:]

    # Find next 00 00 01
    next_index = data.find(b'\x00\x00\x01', 1)

    # Insert System Header
    system_header = b'\x00\x00\x01\xBB'  # Sample system header, replace with valid one
    data = data[:next_index] + system_header + data[next_index:]

    # Insert Sequence Header before Group of Pictures
    sequence_header = b'\x00\x00\x01\xB3'  # Sample sequence header, replace with valid one
    data = data[:group_of_pictures_index] + sequence_header + data[group_of_pictures_index:]

    # Save repaired file
    output_file = 'Repaired/' + input_file.split('/')[-1]  # Assuming input_file is a full path
    with open(output_file, 'wb') as f:
        f.write(data)

    print("File repaired and saved as:", output_file)

# Prompt for input file
input_file = input("Enter the path of the damaged MPEG file: ")
repair_mpeg_file(input_file)
