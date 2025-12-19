def parse_channel_messages(filename):
    messages = {}
    current_channel = None
    buffer = []

    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip()

            # new channel header
            if line.startswith("#") and line.endswith(":"):
                # save previous
                if current_channel:
                    messages[current_channel] = "\n".join(buffer).strip()

                # start new
                current_channel = line[1:-1]  # remove # and :
                buffer = []

            else:
                buffer.append(line)

        # save last
        if current_channel:
            messages[current_channel] = "\n".join(buffer).strip()

    return messages