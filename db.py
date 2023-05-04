"""
This module is responsible for storing `Message`s and `VoteList`s in `parsed/` folder.
The messages are expected to be parsed from older to newer ones (message.id € [0, …]), so the database contains
a prefix of messages.

File names are "{id}_message.json" and "{id}_votes.json" for message and votes respectively.
For messages without polls or with polls with hidden info, the corresponding votes file is not created.
"""
import os

from serialization import telethon_to_json


def next_message_id_to_process():
    """ Returns the id of the next message to process — the first message id for which message file isn't created """
    file_names = os.listdir("parsed")
    message_ids_of_polls = [int(file_name.split("_")[0]) for file_name in file_names if
                            file_name.endswith("_message.json")]
    if len(message_ids_of_polls) == 0:
        return 0
    return max(message_ids_of_polls) + 1


def store_message(message):
    """ Stores the message in a file """
    with open(f"parsed/{message.id}_message.json", "w", encoding="utf-8") as file:
        file.write(telethon_to_json(message))


def store_votes(message, votes):
    """ Stores the votes in a file """
    with open(f"parsed/{message.id}_votes.json", "w", encoding="utf-8") as file:
        file.write(telethon_to_json(votes))


if __name__ == '__main__':
    print(next_message_id_to_process())
