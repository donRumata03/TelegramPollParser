"""
This module is responsible for storing `Message`s and `VoteList`s in `parsed/` folder.
The messages are expected to be parsed from older to newer ones (message.id € [0, …]), so the database contains
a prefix of messages.

File names are "{id}_message.json" and "{id}_votes.json" for message and votes respectively.
For messages without polls or with polls with hidden info, the corresponding votes file is not created.
"""
import os

from serialization import telethon_to_json


def max_index_of_type(type):
    """ Returns the maximum index of a file of the given type in the database """
    file_names = os.listdir("parsed")
    file_names_of_type = [file_name for file_name in file_names if file_name.endswith(f"_{type}.json")]
    if len(file_names_of_type) == 0:
        return -1
    return max([int(file_name.split("_")[0]) for file_name in file_names_of_type])


def next_message_id_to_process():
    """ Returns the id of the next message to process — the first message id for which message file isn't created """
    file_names = os.listdir("parsed")
    # Last dumped message may miss its votes file, but if there are a lot of messages without polls,
    # it's better to skip them the previous ones
    max_message_id = max_index_of_type("message")
    max_votes_id = max_index_of_type("votes")

    return max(max_message_id - 1, max_votes_id) + 1


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
