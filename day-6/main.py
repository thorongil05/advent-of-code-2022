with open('./day-6/input.txt') as f:
    input_sequence_raw = f.read()
    
START_OF_PACKET_MARKER_LEN = 4
START_OF_MESSAGE_MARKER_LEN = 14

def detect_marker(input_sequence_raw: str, marker_len: int):
    start_of_packet_marker_list = []
    for i, letter in enumerate(input_sequence_raw):
        start_of_packet_marker_list.append(letter)
        if len(set(start_of_packet_marker_list[-marker_len:])) == marker_len:
            return start_of_packet_marker_list

processed_characters_packet_marker = len(detect_marker(input_sequence_raw, START_OF_PACKET_MARKER_LEN))
processed_characters_message_marker = len(detect_marker(input_sequence_raw, START_OF_MESSAGE_MARKER_LEN))

print(f'Number of characters to be processed to find the packet marker: {processed_characters_packet_marker}')
print(f'Number of characters to be processed to find the message marker: {processed_characters_message_marker}')